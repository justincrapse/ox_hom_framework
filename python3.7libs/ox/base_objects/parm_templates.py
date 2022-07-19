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

    def __save_template_group(self, supress_error=True):
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

    def add_parm_template(self, parm_template, folder_label=None, as_first=False, insert_after_parm=None, insert_before_parm=None):
        """if folder_label is specified, as_first, insert_after_parm, and insert_before_parm are not relavant as those will dictate which
        folder a parm template is added to."""
        if folder_label:
            self.__create_folder_if_not_exist(folder_label=folder_label)
            folder = self.parm_template_group.findFolder(folder_label)
            self.parm_template_group.appendToFolder(folder, parm_template)
        elif as_first:
            first_pt = self.__get_parm_templates()[0]
            self.parm_template_group.insertBefore(first_pt, parm_template)
        elif insert_after_parm:
            parm_to_follow = self.node.parm(insert_after_parm)
            ptf_pt = parm_to_follow.parmTemplate()
            ox_logger.debug(f"Adding parm insert after: {parm_to_follow.name()}")
            self.parm_template_group.insertAfter(ptf_pt, parm_template)
        elif insert_before_parm:
            parm_to_preceed = self.node.parm(insert_after_parm)
            ptf_pt = parm_to_preceed.parmTemplate()
            ox_logger.debug(f"Adding parm insert before: {parm_to_preceed.name()}")
            self.parm_template_group.insertBefore(ptf_pt, parm_template)
        else:
            self.parm_template_group.append(parm_template)
        self.__save_template_group()

    def remove_parm_template_by_name(self, parm_name):
        result = self.parm_template_group.remove(parm_name)
        ox_logger.debug(f'Remove "{parm_name}" parm template result: {result}')
        self.__save_template_group()

    def remove_folder_by_label(self, label):
        folder_name = self.get_folder_name_by_label(label=label)
        self.remove_parm_template_by_name(parm_name=folder_name)

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
        self.__save_template_group()
        return folder_label

    def delete_folder(self, folder_label):
        parm_templates = self.__get_parm_templates()
        for pt in parm_templates:
            if pt.label() == folder_label:
                self.parm_template_group.remove(pt)
                self.__save_template_group()
                break

    def delete_all_folders(self):
        """TODO: Looks like this is just deleting all parm templates. Need to review and provide good docstring"""
        parm_templates = self.__get_parm_templates()
        for pt in parm_templates:
            self.parm_template_group.remove(pt)
            self.__save_template_group()

    ##################################################################################################################################################
    # creating parm templates

    def create_int_parm_template(self, name, label, num_components=1, **kwargs):
        new_parm_template = hou.IntParmTemplate(name=name, label=label, num_components=num_components, **kwargs)
        return new_parm_template

    def create_float_parm_template(self, name, label, num_components=1, min_f=0.0, max_f=10.0, min_is_strict=False, max_is_strict=False, **kwargs):
        new_parm_template = hou.FloatParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
            min=min_f,
            max=max_f,
            min_is_strict=min_is_strict,
            max_is_strict=max_is_strict,
            **kwargs,
        )
        return new_parm_template

    def create_toggle_parm_template(self, name, label, **kwargs):
        new_parm_template = hou.ToggleParmTemplate(name=name, label=label, **kwargs)
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
        label,
        num_components=1,
        multiline=False,
        join_with_next=False,
        script_callback=None,
        script_callback_language=hou.scriptLanguage.Python,
        tags=None,
        **kwargs,
    ):
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
            **kwargs,
        )
        return new_parm_template

    def create_menu_parm_template(self, name, label, menu_items, menu_labels=(), **kwargs):
        new_parm_template = hou.MenuParmTemplate(name=name, label=label, menu_items=menu_items, menu_labels=menu_labels, **kwargs)
        return new_parm_template

    def create_ramp_parm_template(self, name, label, ramp_parm_type=hou.rampParmType.Float, **kwargs):
        new_parm_template = hou.RampParmTemplate(name=name, label=label, ramp_parm_type=ramp_parm_type, **kwargs)
        return new_parm_template

    def add_separator_parameter(self, name, **kwargs):
        new_parm_template = hou.SeparatorParmTemplate(name=name, **kwargs)
        return new_parm_template

    def add_operator_path_parameter(self, name, label=None, num_components=1, **kwargs):
        label = label if label else name.replace(" ", "_")
        new_parm_template = hou.StringParmTemplate(
            name=name,
            label=label,
            num_components=num_components,
            naming_scheme=hou.parmNamingScheme.Base1,
            string_type=hou.stringParmType.NodeReference,
            menu_type=hou.menuType.Normal,
            **kwargs,
        )
        return new_parm_template
