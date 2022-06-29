from cgitb import reset
import logging

import hou
from hou import OperationFailed

from ox.constants import parm_template_types

ox_logger = logging.getLogger("ox_logger")


class ParmTemplate:
    def __init__(self, node):
        self.node: hou.Node = node
        self.parm_template_group = self.node.parmTemplateGroup()  # type: hou.Node.parmTemplateGroup


    def __save_template_group(self, supress_error=True):
        try:
            self.node.setParmTemplateGroup(parm_template_group=self.parm_template_group)
            self.parm_template_group = self.node.parmTemplateGroup()
        except OperationFailed as e:
            if supress_error:
                print(e)
            else:
                raise e

    def remove_parm_template_by_name(self, parm_name):
        result = self.parm_template_group.remove(parm_name)
        ox_logger.debug(f'Remove "{parm_name}" parm template result: {result}')
        self.__save_template_group()

    def __add_parm_template_to_node_folder(self, folder_label, parm_template):
        self.__create_folder_if_not_exist(folder_label=folder_label)
        folder = self.parm_template_group.findFolder(folder_label)
        self.parm_template_group.appendToFolder(folder, parm_template)
        self.__save_template_group()

    def __create_folder_if_not_exist(self, folder_label):
        folder_name = folder_label.replace(" ", "_").lower()
        folder_templates = self.get_parm_templates_of_folder_type()
        folder_labels = [i.label() for i in folder_templates]
        if folder_label not in folder_labels:
            self.add_folder(folder_label=folder_label, folder_name=folder_name, as_first=True)

    def __add_parm_template(self, parm_template, as_first=False, insert_after_parm=None):
        if as_first:
            first_pt = self.__get_parm_templates()[0]
            self.parm_template_group.insertBefore(first_pt, parm_template)
        elif insert_after_parm:
            print(f'Node: {self.node}')
            parm_to_follow = self.node.parm(insert_after_parm)
            ptf_pt = parm_to_follow.parmTemplate()
            print(f"Adding parm insert after: {parm_to_follow.name()}")
            self.parm_template_group.insertAfter(ptf_pt, parm_template)
        else:
            self.parm_template_group.append(parm_template)
        self.__save_template_group()

    def __get_entries(self):
        return self.parm_template_group.entries()

    def __get_parm_templates(self):
        parm_templates = self.parm_template_group.parmTemplates()
        ox_logger.debug(f'{self.node.name()} parmTemplates: {parm_templates}')
        return parm_templates

    def get_parm_templates_of_folder_type(self):
        parm_templates = self.__get_parm_templates()
        folder_parm_templates = [i for i in parm_templates if i.type().name() == parm_template_types.FOLDER]
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
        self.__add_parm_template(parm_template=folder_template, as_first=as_first)
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
        parm_templates = self.__get_parm_templates()
        for pt in parm_templates:
            self.parm_template_group.remove(pt)
            self.__save_template_group()

    def add_int_parameter(self, name, label, num_components=1, folder_label=None, return_as_path=False, insert_after_parm=None, **kwargs):
        new_parm_template = hou.IntParmTemplate(name=name, label=label, num_components=num_components, **kwargs)
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template, insert_after_parm=insert_after_parm)
        return_parm = self.node.parm(name)
        if return_as_path:
            return return_parm.path()
        return return_parm

    def add_float_parameter(
        self, name, label, num_components=1, min_f=0.0, max_f=10.0, min_is_strict=False, max_is_strict=False, folder_label=None, **kwargs
    ):
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
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_toggle_parameter(self, name, label, folder_label=None, **kwargs):
        new_parm_template = hou.ToggleParmTemplate(name=name, label=label, **kwargs)
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_button_parameter(
        self, name, label, folder_label=None, join_with_next=False, script_callback=None, script_callback_language=hou.scriptLanguage.Python, **kwargs
    ):
        new_parm_template = hou.ButtonParmTemplate(
            name=name,
            label=label,
            join_with_next=join_with_next,
            script_callback=script_callback,
            script_callback_language=script_callback_language,
            **kwargs,
        )
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_string_parameter(
        self,
        name,
        label,
        num_components=1,
        folder_label=None,
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
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_menu_parameter(self, name, label, menu_items, menu_labels=(), folder_label=None, **kwargs):
        new_parm_template = hou.MenuParmTemplate(name=name, label=label, menu_items=menu_items, menu_labels=menu_labels, **kwargs)
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_ramp_parameter(self, name, label, ramp_parm_type=hou.rampParmType.Float, folder_label=None, **kwargs):
        new_parm_template = hou.RampParmTemplate(name=name, label=label, ramp_parm_type=ramp_parm_type, **kwargs)
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_separator_parameter(self, name, folder_label=None, **kwargs):
        new_parm_template = hou.SeparatorParmTemplate(name=name, **kwargs)
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template)
        return self.node.parm(name)

    def add_operator_path_parameter(self, name, label=None, num_components=1, folder_label=None, insert_after_parm=None, **kwargs):
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
        if folder_label:
            self.__add_parm_template_to_node_folder(folder_label=folder_label, parm_template=new_parm_template)
        else:
            self.__add_parm_template(parm_template=new_parm_template, insert_after_parm=insert_after_parm)
        return self.node.parm(name)
