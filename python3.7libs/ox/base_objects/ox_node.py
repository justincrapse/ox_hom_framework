import re
import logging
from typing import List

import hou

from ox.base_objects.parm_templates import ParmTemplate
from ox.utils.node_color_lookup import color_lookup_dict
from ox.utils import session_utils
from ox.constants.ox_conf import sesh_vars, logging_levels

ox_logger = logging.getLogger("ox_logger")


class OXNode(ParmTemplate):  # mixins
    # these are for child class lookups:
    parm_lookup_dict = {}

    def __init__(self, node=None):
        super().__init__(node=node)
        self.name = node.name()
        self.node = node  # type: hou.Node
        self.path = node.path()
        self.type = node.type().name()
        if self.type in color_lookup_dict:
            self.set_color(color_lookup_dict[self.type])

    def __setattr__(self, name, value):
        skip_list = ["node"]
        clean_key = self.clean_parm_key(raw_key=name)
        if clean_key in self.parm_lookup_dict and clean_key not in skip_list and hasattr(self, name):
            hou_parm_string = self.parm_lookup_dict[clean_key]
            parm = self.node.parm(hou_parm_string)
            parm.deleteAllKeyframes()
            parm.set(value)
        else:
            super().__setattr__(name, value)

    @staticmethod
    def clean_parm_key(raw_key):
        del_list = ["parm_"]
        clean_key = re.sub(r"{}".format("|".join(del_list)), "", raw_key)
        return clean_key

    def delete_node(self):
        result = self.node.destroy()
        ox_logger.debug(f'Result for delete node "{self.name}": {result}')

    def delete_child_node(self, child_name):
        child_hou_node = self.get_child_by_name(child_name=child_name)
        if child_hou_node:
            child_hou_node.destroy()

    def delete_all_children(self):
        for child_node in self.get_children_hou_nodes():
            child_node.destroy()

    def delete_all_items(self):
        all_items = self.node.allItems()
        self.node.deleteItems(all_items)

    def get_input_labels(self):
        labels = self.node.inputLabels()
        return list(labels)

    def get_label_index(self, label):
        labels = self.get_input_labels()
        try:
            index = labels.index(label)
            return index
        except ValueError as e:
            ValueError(f"Label: {label}. Was not found in node: {self.path}")

    def create_node(self, node_type_name, node_name=None):
        new_node = self.node.createNode(node_type_name, node_name)
        return new_node

    def create_node_if_not_exist(self, ox_node_class, node_name=None):
        node_type_name = ox_node_class.node_type
        child_node = self.get_child_by_name(child_name=node_name)
        if not child_node:
            child_node = self.create_node(node_type_name=node_type_name, node_name=node_name)
        return ox_node_class(node=child_node)

    def connect_from(self, ox_node, input_index=0, out_index=0, input_label=None):
        """use input_label over input_index whenever possible"""
        other_hou_node = ox_node.node
        if input_label:
            input_index = self.get_label_index(label=input_label)
        self.node.setInput(input_index=input_index, item_to_become_input=other_hou_node, output_index=out_index)

    def get_child_by_name(self, child_name):
        for child in self.get_children_hou_nodes():
            if child.name() == child_name:
                return child

    def has_child_with_name(self, child_name):
        return bool(self.get_child_by_name(child_name=child_name))

    def get_children_paths_by_partial_name(self, substring):
        path_list = []
        for node in self.get_children_hou_nodes():
            if substring in node.name():
                path_list.append(node.path())
        return path_list

    def get_children_hou_nodes_by_partial_name(self, substring):
        node_list = []
        for node in self.get_children_hou_nodes():
            if substring in node.name():
                node_list.append(node)
        return node_list

    def get_children_hou_nodes(self) -> List[hou.Node]:
        children_node_list = self.node.children()
        return children_node_list

    def get_child_by_node_type(self, node_type):
        for child in self.get_children_hou_nodes():
            if child.type().name() == node_type:
                return child

    def set_color(self, color):
        self.node.setColor(color)

    def set_name(self, new_name):
        self.node.setName(new_name)

    def get_prim_values(self, field):
        value_list = [i.attribValue(field) for i in self.node.geometry().prims()]
        return value_list

    def get_planes(self):
        planes = self.node.planes()
        return planes

    def get_displayed_child_node(
        self,
    ):
        for node in self.get_children_hou_nodes():
            if node.isDisplayFlagSet():
                return node

    def layout_children(self):
        self.node.layoutChildren()

    def move_node_relative_to(self, relative_node, x=0, y=-1, unit_multiplier=2):
        relative_position_vector = relative_node.node.position()
        r_x = relative_position_vector[0]
        r_y = relative_position_vector[1]
        vector = hou.Vector2(r_x + x * unit_multiplier, r_y + y * unit_multiplier)
        self.node.setPosition(vector)

    def unlock_node(self):
        self.node.allowEditingOfContents()

    def get_folder_labels(self):
        templates = self.get_parm_templates_of_folder_type()
        labels = [i.label() for i in templates]
        return labels

    def set_display_flag(self, on=True, include_render_flag=True):
        self.node.setDisplayFlag(on=on)
        if include_render_flag:
            self.node.setRenderFlag(on=on)

    def set_render_flag(self, on=True):
        self.node.setRenderFlag(on=on)

    def set_bypass_flag(self, on):
        self.node.bypass(on=on)

    def get_prim_groups(self):
        group_list = [i.name() for i in self.node.geometry().primGroups()]
        return group_list

    def load_preset(self, preset_name):
        LOAD_USER_PRESETS = session_utils.get_session_variable(sesh_vars.LOAD_USER_PRESETS)
        if LOAD_USER_PRESETS:
            script = f"oppresetload {self.path} {preset_name}"
            result = hou.hscript(script)
            if "Invalid preset name" not in result[1]:
                ox_logger.info(f'Successfully Loaded Preset Name "{preset_name}" for node type {self.type}')
            else:
                ox_logger.debug(f'Preset Name "{preset_name}" Not Found for node type {self.type}. Result: {result}')
        else:
            ox_logger.debug(f"LOAD_USER_PRESETS is False: {LOAD_USER_PRESETS}")

    def save_preset(self, node_path, preset_name, preset_path):
        script = f'oppresetsave {node_path} "{preset_name}" {preset_path}'
        result = hou.hscript(script)
        if result[1]:
            ox_logger.info(f"there was a result message: {result}")
        ox_logger.info(f"Saved preset {preset_name} to node {node_path} to folder: {preset_path} Result: {result}")

    def delete_preset(self, node_path, preset_name, preset_path=None):
        if preset_path:
            script = f'oppresetrm {node_path} "{preset_name}" {preset_path}'
        else:
            script = f'oppresetrm {node_path} "{preset_name}"'
        result = hou.hscript(script)
        if result[1]:
            ox_logger.info(f"there was a result message: {result}")
        ox_logger.info(f"Deleted preset {preset_name} on node {node_path} on folder: {preset_path} Result: {result}")

    def select_node(self, on=True):
        self.node.setSelected(on=on)

    def rename_node(self, new_name):
        result = self.node.setName(name=new_name)
        self.name = new_name
        ox_logger.debug(f'rename node result: {result}')

    ##################################################################################################################################################
    # parm methods
    def get_parms(self) -> List[hou.Parm]:
        parameters = self.node.parms()
        return parameters

    def get_parms_by_name_substring(self, substring, ends_with=False):
        parameters = self.get_parms()
        if not ends_with:
            parm_sublist = [i for i in parameters if substring in i.name()]
        else:
            parm_sublist = [i for i in parameters if i.name().endswith(substring)]
        return parm_sublist

    def get_parm_labels(self):
        parameters = self.get_parms()
        parm_label_list = [i.label() for i in parameters]
        return parm_label_list

    def get_parm_names(self):
        parameters = self.get_parms()
        parm_name_list = [i.name() for i in parameters]
        return parm_name_list

    def get_parm_names_by_substring(self, substring):
        parm_names = self.get_parm_names()
        parm_sublist = [i for i in parm_names if substring in i]
        return parm_sublist

    def parms_to_dict(self, parm_list: List[hou.Parm], substring=None):
        parm_list = self.get_parms_by_name_substring(substring=substring) if substring else self.get_parms()
        parm_dict = {i.name(): i.eval() for i in parm_list}
        return parm_dict
        
    ##################################################################################################################################################
