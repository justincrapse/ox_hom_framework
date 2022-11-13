"""
This is a mix-in class. Meaning: While all this could be written for the OXNode class, we break it out into this other module so that we can easily
group related code which makes it easier to maintain. 
"""


import logging

import hou
from hou import OperationFailed

from ox.constants import parm_template_types

ox_logger = logging.getLogger("ox_logger")


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

    def __create_folder_if_not_exist(self, folder_label, folder_name=None):
        folder_name = folder_name if folder_name else folder_label.replace(" ", "_").lower()
        folder_templates = self.get_parm_templates_by_type(template_type=parm_template_types.FOLDER)
        folder_labels = [i.label() for i in folder_templates]
        if folder_label not in folder_labels:
            self.add_folder(folder_label=folder_label, folder_name=folder_name, as_first=True)

    def __get_entries(self):
        return self.parm_template_group.entries()

    def __get_parm_templates(self):
        parm_templates = self.parm_template_group.parmTemplates()
        ox_logger.debug(f'Getting all parm templates for "{self.node.name()}" parmTemplates: {parm_templates}')
        return parm_templates

    def add_parm_template(
        self,
        parm_template,
        folder_label=None,
        as_first=False,
        insert_after_parm=None,
        insert_before_parm=None,
        return_type=None,
    ) -> hou.Parm:
        """if folder_label is specified, as_first, insert_after_parm, and insert_before_parm are not relavant as those will dictate which
        folder a parm template is added to."""
        parm_template: hou.ParmTemplate
        if folder_label:
            ox_logger.debug(f"Appending parm to folder: {folder_label}")
            self.__create_folder_if_not_exist(folder_label=folder_label)
            folder = self.parm_template_group.findFolder(folder_label)
            self.parm_template_group.appendToFolder(folder, parm_template)
        elif as_first:
            ox_logger.debug("Inserting parm template as first entry")
            first_pt = self.__get_parm_templates()[0]
            self.parm_template_group.insertBefore(first_pt, parm_template)
        elif insert_after_parm:
            parm_to_follow = insert_after_parm if isinstance(insert_after_parm, hou.Parm) else self.node.parm(insert_after_parm)
            if not parm_to_follow:
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
        self._save_template_group()
        ox_logger.info(f'Added new parm template to "{self.node.name()}" node: {parm_template.name()}')
        if return_type == "color":
            return_parm_tuple = (
                self.node.parm(f"{parm_template.name()}r"),
                self.node.parm(f"{parm_template.name()}g"),
                self.node.parm(f"{parm_template.name()}b"),
            )
            return return_parm_tuple
        new_parm = self.node.parm(parm_template.name())
        if not new_parm:
            ox_logger.error(f"No new parm created for parm_template: {parm_template}.")
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
    ):
        """
        This method will delete the parm method if it already exists and can reapply that value to the newly created parm
        """
        existing_parm: hou.Parm = self.node.parm(parm_template.name())
        if existing_parm:
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
        if existing_parm:
            new_parm.set(original_value)
        return new_parm

    def add_parm_template_to_sub_folder():
        pass

    def remove_parm_template_by_name(self, parm_name, save_template_group=True):
        result = self.parm_template_group.remove(parm_name)
        ox_logger.debug(f'Remove "{parm_name}" parm template result: {result}')
        if save_template_group:
            self._save_template_group()

    def remove_folder_by_label(self, label):
        folder_name = self.get_folder_name_by_label(label=label)
        self.remove_parm_template_by_name(parm_name=folder_name)

    def get_folder_parm_templates_by_label(self, folder_label):
        parm_template_list = self.parm_template_group.parmTemplates()
        pt: hou.ParmTemplate
        for pt in parm_template_list:
            if pt.label() == folder_label:
                folder_parm_templates = pt.parmTemplates()
                return folder_parm_templates
        ox_logger.info(f"\nNo matching folder label for {folder_label} for method get_folder_parm_templates_by_label")

    def remove_subfolder_by_labels(self, parent_folder_label, folder_label):
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

    def get_sub_folder_parm_value_dict_by_folder_labels(self, parent_folder_label, folder_label):
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
        folder_parm_templates = self.get_parm_templates_by_type(template_type=parm_template_types.FOLDER)
        for folder_pt in folder_parm_templates:
            if folder_pt.label() == label:
                return folder_pt.name()

    def get_parm_templates_by_type(self, template_type):
        """template types can be found in ox.constants.parm_template_types"""
        parm_templates = self.__get_parm_templates()
        folder_parm_templates = [i for i in parm_templates if i.type().name() == template_type]
        return folder_parm_templates

    def get_folder_parm_labels(self, folder_label, return_parm_labels=False):
        folder_template = self.get_folder_template(folder_label=folder_label)
        parms = folder_template.parmTemplates()
        if return_parm_labels:
            return [i.label() for i in parms]
        return parms

    def get_folder_template(self, folder_label):
        folder_template = self.get_parm_template_by_label(label=folder_label)
        return folder_template

    def get_parm_template_by_label(self, label):
        for template in self.__get_parm_templates():
            if template.label() == label:
                return template

    def get_parm_template_names_by_substring(self, substring):
        match_list = [i for i in self.__get_parm_templates() if substring in i.name()]
        return match_list

    def get_entry_labels(self):
        labels = [i.label() for i in self.__get_entries()]
        return labels

    def add_folder(self, folder_label, folder_name, as_first=False):
        folder_template = hou.FolderParmTemplate(folder_name, folder_label)
        self.add_parm_template(parm_template=folder_template, as_first=as_first)
        self._save_template_group()
        return folder_label

    def delete_folder(self, folder_label):
        parm_templates = self.__get_parm_templates()
        for pt in parm_templates:
            if pt.label() == folder_label:
                self.parm_template_group.remove(pt)
                self._save_template_group()
                break

    def delete_all_folders(self):
        """TODO: Looks like this is just deleting all parm templates. Need to review and provide good docstring"""
        parm_templates = self.__get_parm_templates()
        for pt in parm_templates:
            self.parm_template_group.remove(pt)
            self._save_template_group()

    ##################################################################################################################################################
    # creating parm templates

    def create_int_parm_template(
        self, name, label=None, num_components=1, min=0, max=10, help=None, is_label_hidden=False, join_with_next=False, **kwargs
    ):
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.IntParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
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
        min=0.0,
        max=10.0,
        min_is_strict=False,
        max_is_strict=False,
        is_label_hidden=False,
        join_with_next=False,
        **kwargs,
    ):
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.FloatParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
            min=min,
            max=max,
            min_is_strict=min_is_strict,
            max_is_strict=max_is_strict,
            is_label_hidden=is_label_hidden,
            join_with_next=join_with_next,
            **kwargs,
        )
        return new_parm_template

    def create_toggle_parm_template(self, name, label=None, is_label_hidden=False, join_with_next=False, **kwargs):
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.ToggleParmTemplate(name=name, label=label, is_label_hidden=is_label_hidden, join_with_next=join_with_next, **kwargs)
        return new_parm_template

    def create_button_parm_template(
        self, name, label, join_with_next=False, script_callback=None, script_callback_language=hou.scriptLanguage.Python, **kwargs
    ):
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

    def create_menu_parm_template(self, name, menu_items, label=None, menu_labels=(), is_label_hidden=False, join_with_next=False, **kwargs):
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
        new_parm_template = hou.RampParmTemplate(name=name, label=label, ramp_parm_type=ramp_parm_type, **kwargs)
        return new_parm_template

    def create_separator_parm_template(self, name, **kwargs):
        new_parm_template = hou.SeparatorParmTemplate(name=name, **kwargs)
        return new_parm_template

    def create_operator_parm_template(self, name, label=None, num_components=1, is_label_hidden=False, join_with_next=False, **kwargs):
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
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.FolderParmTemplate(name=name, label=label)
        return new_parm_template

    def create_vex_snippet_parm_template(self, name, label=None, **kwargs) -> hou.StringParmTemplate:
        """
        This is pretty much just the attribute wrangle vex parameter .asCode()
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

    ##################################################################################################################################################
    # creating special parm templates
    def create_color_tuple_parm_template(self, name, label=None, default_value=([1, 1, 1]), is_label_hidden=False, join_with_next=False):
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
