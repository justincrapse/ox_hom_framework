"""
This is a mix-in class. Meaning: While all this could be written for the OXNode class, we break it out into this other module so that we can easily
group related code which makes it easier to maintain. 
"""

import logging
from typing import List
import functools
import time

import hou

from hou import OperationFailed
from ox.constants import parm_template_types

ox_logger = logging.getLogger("ox_logger")

time_list = []
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds: {func.__name__}")
        # time_list.append()
        return value

    return wrapper_timer

class ParmTemplate:
    def __init__(self, node):
        self.node: hou.Node = node
        self.parm_template_group: hou.Node.parmTemplateGroup = self.node.parmTemplateGroup()

    def _save_template_group(self, supress_error=True):
        # TODO: supress_error needs an explanation!
        try:
            self.node.setParmTemplateGroup(parm_template_group=self.parm_template_group)
            self.parm_template_group = self.node.parmTemplateGroup()
        except OperationFailed as e:
            if supress_error:
                ox_logger.info(f"Supressed Error:{e}")
            else:
                raise e

    def _get_updated_parm_template_group(self):
        ptg: hou.Node.parmTemplateGroup = self.node.parmTemplateGroup()
        return ptg

    def __create_folder_if_not_exist(self, folder_label, folder_name=None):
        folder_name = folder_name if folder_name else folder_label.replace(" ", "_").lower()
        folder_templates = self.get_parm_templates_by_type(template_type=parm_template_types.FOLDER)
        folder_labels = [i.label() for i in folder_templates]
        if folder_label not in folder_labels:
            self.add_folder(folder_label=folder_label, folder_name=folder_name, as_first=True)

    def __get_entries(self):
        return self.parm_template_group.entries()

    def __get_parm_templates(self):
        parm_templates = self.node.parmTemplateGroup().parmTemplates()
        ox_logger.debug(f'Getting all parm templates for "{self.node.name()}" parmTemplates: {parm_templates}')
        return parm_templates

    def join_with_next(self, parm, join_with_next=True):
        orig_pt = parm.parmTemplate()
        pt: hou.ParmTemplate = parm.parmTemplate()
        pt.setJoinWithNext(join_with_next)
        ptg: hou.ParmTemplateGroup = self.parm_template_group
        ptg.replace(orig_pt, pt)
        self._save_template_group()

    def add_parm_template(
        self,
        parm_template,
        folder_label=None,
        as_first=False,
        insert_after_parm=None,
        insert_before_parm=None,
        return_type=None,
        supress_logger=False,
        save_ptg=True,
    ) -> hou.Parm:
        """
        Adds a parm template to a node. if folder_label is specified, as_first, insert_after_parm, and insert_before_parm are not relavant as those
        will dictate which folder a parm template is added to.

        :param folder_label: When specified, the parm_template will be added to the folder by label string.
        :param as_first: Will insert this parameter as the first in the node.
        :param insert_after_parm: This can be a parm object or the name of a parm after which you insert the new parm template
        :param insert_before_parm: same as insert_after_parm but before.
        :param return_type: Return types may vary depending on the type of parm template. Add logic as neccisary. Options:
            * 'color'  # for color parm templates
        :param supress_logger: For specific expected error logging that may intentionally be supressed

        """
        parm_template: hou.ParmTemplate
        if folder_label:
            ox_logger.debug(f"Appending parm to folder: {folder_label}")
            # this causes issues with subfolders
            # self.__create_folder_if_not_exist(folder_label=folder_label)
            folder = self.parm_template_group.findFolder(folder_label)
            ox_logger.debug(f"Found folder: {folder_label}")
            self.parm_template_group.appendToFolder(folder, parm_template)
        elif as_first:
            ox_logger.debug("Inserting parm template as first entry")
            first_pt = self.__get_parm_templates()[0]
            self.parm_template_group.insertBefore(first_pt, parm_template)
        elif insert_after_parm:
            parm_to_follow = insert_after_parm if isinstance(insert_after_parm, hou.Parm) else self.node.parm(insert_after_parm)
            if not parm_to_follow:
                if not supress_logger:
                    ox_logger.error(f'No parm_to_follow found for parm "{insert_after_parm}"')
            ptf_pt = parm_to_follow.parmTemplate()
            ox_logger.debug(f"Adding parm insert after: {parm_to_follow.name()}")
            self.parm_template_group.insertAfter(ptf_pt, parm_template)
        elif insert_before_parm:
            parm_to_preceed = self.node.parm(insert_after_parm)
            ptf_pt = parm_to_preceed.parmTemplate()
            ox_logger.debug(f"Adding parm insert before: {parm_to_preceed.name()}")
            self.parm_template_group.insertBefore(ptf_pt, parm_template)
        else:
            ox_logger.debug("No matching strategy. Appending parm template to end")
            self.parm_template_group.append(parm_template)
        self._save_template_group(supress_error=False)
        ox_logger.debug(f'Added new parm template to "{self.node.name()}" node: {parm_template.name()}')
        if return_type == "color":
            # return_parm_tuple = (
            #     self.node.parm(f"{parm_template.name()}r"),
            #     self.node.parm(f"{parm_template.name()}g"),
            #     self.node.parm(f"{parm_template.name()}b"),
            # )
            return self.node.parmTuple(parm_template.name())
        new_parm = self.node.parm(parm_template.name())
        if not new_parm:
            if not supress_logger:
                ox_logger.error(f"No new parm created for parm_template: {parm_template}. If a new parm was created, it may need a different return_type value")
        return new_parm

    def add_parm_template_with_override(
        self,
        parm_template,
        folder_label=None,
        as_first=False,
        insert_after_parm=None,
        insert_before_parm=None,
        return_type=None,
        keep_original_value=True,
    ) -> hou.Parm:
        """This method will delete the parm method if it already exists and can reapply the previous value to the newly created parm"""
        existing_parm: hou.Parm = self.node.parm(parm_template.name())
        ox_logger.debug(f"existing parm for {parm_template.name()}: {existing_parm}")
        if existing_parm and keep_original_value:
            original_value = existing_parm.eval()
            self.remove_parm_template_by_name(parm_name=parm_template.name())
        new_parm = self.add_parm_template(
            parm_template=parm_template,
            folder_label=folder_label,
            as_first=as_first,
            insert_after_parm=insert_after_parm,
            insert_before_parm=insert_before_parm,
            return_type=return_type,
        )
        if existing_parm and keep_original_value:
            new_parm.set(original_value)
        return new_parm

    def add_parm_template_if_not_exist(self, parm_template: hou.ParmTemplate, supress_logger=True, folder_label=None, insert_before_parm=None, **kwargs):
        """Only adds the parm template if it does not already exist."""
        existing_parm: hou.Parm = self.node.parm(parm_template.name())
        if existing_parm:
            return existing_parm
        else:
            # we cannot determine if sepparm "seperation parameters" exist becasue they will not be returned by the above code. So we can skip errors here for that type:
            try:
                return self.add_parm_template(
                    parm_template=parm_template, supress_logger=supress_logger, folder_label=folder_label, insert_before_parm=insert_before_parm, **kwargs
                )
            except hou.OperationFailed as e:
                if "already exists" in str(e):
                    return existing_parm

    def add_parm_template_to_sub_folder():
        """TODO: Need to implement this."""
        pass

    def remove_parm_template_by_name(self, parm_name, save_template_group=True):
        """
        removes a parm template by name

        :param save_template_group: This parameter lets you hold off on saving the template group, which may behave better when removing many parms
        """
        try:
            result = self.parm_template_group.remove(parm_name)
            ox_logger.info(f'Remove "{parm_name}" parm template result: {result}')
        except hou.OperationFailed:
            ox_logger.info(f'Remove failed for  "{parm_name}" parm template result: {result}')
            return
        if save_template_group:
            self._save_template_group()

    def remove_folder_by_label(self, label):
        """Removes a folder given the label string"""
        folder_name = self.get_folder_name_by_label(label=label)
        self.remove_parm_template_by_name(parm_name=folder_name)

    def get_folder_parm_templates_by_label(self, folder_label):
        """Returns the folder parm templates given the folder label string"""
        parm_template_list = self.parm_template_group.parmTemplates()
        pt: hou.ParmTemplate
        for pt in parm_template_list:
            if pt.label() == folder_label:
                folder_parm_templates = pt.parmTemplates()
                return folder_parm_templates
        ox_logger.info(f"\nNo matching folder label for {folder_label} for method get_folder_parm_templates_by_label")

    def remove_subfolder_by_labels(self, parent_folder_label, folder_label):
        """Removes a subfolder by parent and subfolder labels"""
        parent_folder_parm_templates = self.get_folder_parm_templates_by_label(folder_label=parent_folder_label)
        ox_logger.info(f"\nParent Folder Parm Templates: {parent_folder_parm_templates}")
        pt: hou.ParmTemplate
        folder_parm_name = None
        for pt in parent_folder_parm_templates:
            ox_logger.info(f"pt.label(): {pt.label()} folder_label_to_match: {folder_label}")
            if pt.label() == folder_label:
                folder_parm_name = pt.name()
                break
        if folder_parm_name:
            self.parm_template_group.remove(folder_parm_name)
            self._save_template_group()
        else:
            ox_logger.info(f"No matching folder label for parent {parent_folder_label} and child {folder_label}")

    def get_sub_folder_parm_value_dict_by_folder_labels(self, parent_folder_label, folder_label) -> dict:
        """Returns a dictionary of parm names and values for the subfolder"""
        parent_folder_parm_templates = self.get_folder_parm_templates_by_label(folder_label=parent_folder_label)
        ox_logger.info(f"\nParent Folder Parm Templates: {parent_folder_parm_templates}")
        pt: hou.ParmTemplate
        folder_parm_templates = None
        for pt in parent_folder_parm_templates:
            if pt.label() == folder_label:
                folder_parm_templates = pt.parmTemplates()
        if folder_parm_templates:
            parm_value_dict = {i.name(): self.node.parm(i.name()).eval() for i in folder_parm_templates}
            return parm_value_dict
        else:
            ox_logger.info(f"No matching folder label for parent {parent_folder_label} and child {folder_label}")

    def get_folder_name_by_label(self, label):
        """
        Returns the folder name by label. Note that folder names are auto-generated and may be unexpected values that don't line up the way you think
        they would
        """
        folder_parm_templates = self.get_parm_templates_by_type(template_type=parm_template_types.FOLDER)
        for folder_pt in folder_parm_templates:
            if folder_pt.label() == label:
                return folder_pt.name()

    def get_parm_templates_by_type(self, template_type):
        """Returns list of parm templates by type. template types can be found in ox.constants.parm_template_types"""
        parm_templates = self.__get_parm_templates()
        folder_parm_templates = [i for i in parm_templates if i.type().name() == template_type]
        return folder_parm_templates

    def get_folder_parm_labels(self, folder_label):
        """Returns the parm labels of a folder"""
        folder_template = self.get_folder_template(folder_label=folder_label)
        parms = folder_template.parmTemplates()
        parm_labels = [i.label() for i in parms]
        return parm_labels

    def get_folder_parms_by_label(self, folder_label) -> List[hou.Parm]:
        """Returns parms of a folder"""
        folder_template = self.get_folder_template(folder_label=folder_label)
        parms = folder_template.parmTemplates()
        return parms

    def get_folder_template(self, folder_label):
        """Returns as folder's template by folder label"""
        folder_template = self.get_parm_template_by_label(label=folder_label)
        return folder_template

    def get_parm_template_by_label(self, label):
        """Returns a parm template by label"""
        for template in self.__get_parm_templates():
            if template.label() == label:
                return template

    def get_parm_template_names_by_substring(self, substring):
        """Returns parm template names matched by specified substring"""
        match_list = [i for i in self.__get_parm_templates() if substring in i.name()]
        return match_list

    def get_entry_labels(self):
        """Retruns a list of entry labels. TODO: explain what an entry is"""
        labels = [i.label() for i in self.__get_entries()]
        return labels

    def add_folder(self, folder_label, folder_name, folder_type=hou.folderType.Tabs, as_first=False, insert_after_parm=None, folder_label_to_add_to=None):
        """Adds a folder to a node.
        Folder types (hou.folderType.[Tabs | Simple | Collapsible | RadioButtons | MultiparmBlock | ScrollingMultiparmBlock | TabbedMultiparmBlock | ImportBlock])
        """
        folder_template = hou.FolderParmTemplate(folder_name, folder_label, folder_type=folder_type)
        self.add_parm_template(parm_template=folder_template, as_first=as_first, insert_after_parm=insert_after_parm, folder_label=folder_label_to_add_to)
        self._save_template_group()
        return folder_label

    def delete_folder(self, folder_label):
        """Deletes a top-level folder"""
        parm_templates = self.__get_parm_templates()
        for pt in parm_templates:
            if pt.label() == folder_label:
                self.parm_template_group.remove(pt)
                self._save_template_group()
                break

    # def delete_all_folders(self):
    #     """TODO: Looks like this is just deleting all parm templates. Need to review and provide good docstring"""
    #     parm_templates = self.__get_parm_templates()
    #     for pt in parm_templates:
    #         self.parm_template_group.remove(pt)
    #         self._save_template_group()

    ##################################################################################################################################################
    # creating parm templates

    def create_int_parm_template(
        self,
        name,
        label=None,
        num_components=1,
        default_value=(),
        min=0,
        max=10,
        help=None,
        is_label_hidden=False,
        join_with_next=False,
        **kwargs,
    ):
        """Creates an integer parameter template"""
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.IntParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
            default_value=default_value,
            min=min,
            max=max,
            help=help,
            is_label_hidden=is_label_hidden,
            join_with_next=join_with_next,
            **kwargs,
        )
        return new_parm_template

    def create_float_parm_template(
        self,
        name,
        label=None,
        num_components=1,
        default_value=(),
        min=0.0,
        max=10.0,
        min_is_strict=False,
        max_is_strict=False,
        is_label_hidden=False,
        join_with_next=False,
        **kwargs,
    ):
        """Creates a float parameter template"""
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.FloatParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
            default_value=default_value,
            min=min,
            max=max,
            min_is_strict=min_is_strict,
            max_is_strict=max_is_strict,
            is_label_hidden=is_label_hidden,
            join_with_next=join_with_next,
            **kwargs,
        )
        return new_parm_template

    def create_toggle_parm_template(
        self,
        name,
        label=None,
        default_value=False,
        is_label_hidden=False,
        join_with_next=False,
        **kwargs,
    ):
        """Creates a toggle parameter template"""
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.ToggleParmTemplate(
            name=name,
            label=label,
            default_value=default_value,
            is_label_hidden=is_label_hidden,
            join_with_next=join_with_next,
            **kwargs,
        )
        return new_parm_template

    def create_button_parm_template(
        self,
        name,
        label,
        join_with_next=False,
        script_callback=None,
        script_callback_language=hou.scriptLanguage.Python,
        **kwargs,
    ):
        """Creates a button parameter template"""
        new_parm_template = hou.ButtonParmTemplate(
            name=name,
            label=label,
            join_with_next=join_with_next,
            script_callback=script_callback,
            script_callback_language=script_callback_language,
            **kwargs,
        )
        return new_parm_template

    def create_string_parm_template(
        self,
        name,
        label=None,
        num_components=1,
        multiline=False,
        join_with_next=False,
        script_callback=None,
        script_callback_language=hou.scriptLanguage.Python,
        tags=None,
        is_label_hidden=False,
        default_value=(),
        **kwargs,
    ):
        """Creates a string parameter template"""
        label = label if label else name.replace(" ", "_")
        default_value = default_value if isinstance(default_value, tuple) else (default_value,)
        tags = tags if tags else {}
        if multiline:
            tags["editor"] = "1"
        new_parm_template = hou.StringParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
            join_with_next=join_with_next,
            script_callback=script_callback,
            script_callback_language=script_callback_language,
            tags=tags,
            is_label_hidden=is_label_hidden,
            default_value=default_value,
            **kwargs,
        )
        return new_parm_template

    def create_menu_parm_template(
        self,
        name,
        menu_items,
        label=None,
        menu_labels=(),
        is_label_hidden=False,
        join_with_next=False,
        **kwargs,
    ):
        """Creates a menu parameter template"""
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.MenuParmTemplate(
            name=name,
            label=label,
            menu_items=menu_items,
            menu_labels=menu_labels,
            is_label_hidden=is_label_hidden,
            join_with_next=join_with_next,
            **kwargs,
        )
        return new_parm_template

    def create_ramp_parm_template(self, name, label, ramp_parm_type=hou.rampParmType.Float, **kwargs):
        """Creates a ramp parameter template"""
        new_parm_template = hou.RampParmTemplate(name=name, label=label, ramp_parm_type=ramp_parm_type, **kwargs)
        return new_parm_template

    def create_separator_parm_template(self, name, **kwargs):
        """Creates a separator parameter template"""
        new_parm_template = hou.SeparatorParmTemplate(name=name, **kwargs)
        return new_parm_template

    def create_operator_parm_template(
        self,
        name,
        label=None,
        num_components=1,
        is_label_hidden=False,
        join_with_next=False,
        **kwargs,
    ):
        """Creates an operator parameter template"""
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.StringParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
            naming_scheme=hou.parmNamingScheme.Base1,
            string_type=hou.stringParmType.NodeReference,
            menu_type=hou.menuType.Normal,
            is_label_hidden=is_label_hidden,
            join_with_next=join_with_next,
            **kwargs,
        )
        return new_parm_template

    def create_folder_parm_template(self, name, label=None) -> hou.FolderParmTemplate:
        """Creates a folder parameter template"""
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.FolderParmTemplate(name=name, label=label)
        return new_parm_template

    ##################################################################################################################################################
    # creating special parm templates
    def create_color_tuple_parm_template(
        self,
        name,
        label=None,
        default_value=([1, 1, 1]),
        is_label_hidden=False,
        join_with_next=False,
    ):
        """creates a color tuple parameter template"""
        new_parm_template = self.create_float_parm_template(
            name=name,
            label=label,
            num_components=3,
            default_value=default_value,
            min=0,
            max=1,
            min_is_strict=False,
            look=hou.parmLook.ColorSquare,
            naming_scheme=hou.parmNamingScheme.RGBA,
            is_label_hidden=is_label_hidden,
            join_with_next=join_with_next,
        )
        return new_parm_template

    def create_vex_snippet_parm_template(self, name, label=None, **kwargs) -> hou.StringParmTemplate:
        """
        This is pretty much just the attribute wrangle vex parameter .asCode()
        I have not been able to get this to work properly. TODO: figure out how to implement this correctly
        """
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.StringParmTemplate(
            name=name,
            label=label,
            num_components=1,
            default_value=([""]),
            naming_scheme=hou.parmNamingScheme.Base1,
            string_type=hou.stringParmType.Regular,
            menu_items=([]),
            menu_labels=([]),
            icon_names=([]),
            item_generator_script="import vexpressionmenu\\n\\nreturn vexpressionmenu.buildSnippetMenu('attribwrangle/snippet')",
            item_generator_script_language=hou.scriptLanguage.Python,
            menu_type=hou.menuType.StringReplace,
            **kwargs,
        )
        new_parm_template.setTags(
            {
                "autoscope": "0000000000000000",
                "editor": "1",
                "editorlang": "VEX",
                "editorlines": "8-30",
                "script_action": """import vexpressionmenu

node = kwargs['node']
parmname = 'snippet'

vexpressionmenu.createSpareParmsFromChCalls(node, parmname)""",
                "script_action_help": "Creates spare parameters for each unique call of ch() ",
                "script_action_icon": "BUTTONS_create_parm_from_ch",
            }
        )
        return new_parm_template
