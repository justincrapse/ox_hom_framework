"""
WARNING:
this class' attribute access and namespace is particularly arranged. All access to attributes will be checked to see if it is a parameter existing
in the child class (that represents a houdini node.) Avoid adding attributes to this class. The few that are here are added to a "skip_list" so that
they are not evaluated in the same manner. If there is overlap with this skip list and a parameter attribute that you want to change, a message
will let the coder know that there is an overlap and that this particular attribute will have to be set using the hou module.
"""
from collections import defaultdict
import re
import logging
from typing import List
from unittest.loader import VALID_MODULE_NAME

import hou

from ox.base_objects.parm_templates import ParmTemplate
from ox.utils.node_color_lookup import color_lookup_dict
from ox.utils import session_utils
from ox.constants.ox_conf import sesh_vars
from ox.constants import parm_template_types

ox_logger = logging.getLogger("ox_logger")


class OXNode(ParmTemplate):  # mixins
    # these are for child class lookups (that inherit from OXNode):
    parm_lookup_dict = {}

    def __init__(self, node=None):
        super().__init__(node=node)
        self.name: str = node.name()
        self.node: hou.Node = node
        self.path: str = node.path()
        self.type: str = node.type().name()

        # not sure how to handle this, but will leave for R2 review. This loads in user-defined node colors by node type.
        if self.type in color_lookup_dict:
            self.set_color(color_lookup_dict[self.type])

    def __setattr__(self, name, value):
        """
        What this special method does is overrides the nature of ox_some_node.parm_some_parm = some_new_value. Instead of just setting the
        instance value, which would do nothing in Houdini, this gets the actual parameter and sets it to some_new_value
        """
        skip_list = ["node", "name", "path", "type"]
        clean_key = self.clean_parm_key(raw_key=name)
        if clean_key in self.parm_lookup_dict and clean_key not in skip_list and hasattr(self, name):
            hou_parm_string = self.parm_lookup_dict[clean_key]
            parm = self.node.parm(hou_parm_string)
            parm.deleteAllKeyframes()  # TODO: don't remember why this is here and it probably needs to change or add an accurate comment
            parm.set(value)
        else:
            super().__setattr__(name, value)

    @staticmethod
    def clean_parm_key(raw_key):
        """Cleans the parm attribute name to match the key in the child ox node class parm_lookup_dict so that it can get the actual name of the
        parameter before it was modified to be a python-valid attribute name"""
        del_list = ["parm_"]
        clean_key = re.sub(r"{}".format("|".join(del_list)), "", raw_key)  # TODO: This is kind of odd and should have had a comment.
        return clean_key

    ##################################################################################################################################################
    # node opperations
    def delete_node(self):
        result = self.node.destroy()
        ox_logger.debug(f'Result for delete node "{self.name}": {result}')

    def delete_child_node_by_name(self, child_name, expect_child_node=True):
        child_hou_node = self.get_child_by_name(child_name=child_name)
        if child_hou_node:
            child_hou_node.destroy()
        elif expect_child_node:
            raise ValueError(f'Expected child node with name "{child_name}"')

    def delete_all_children(self):
        """delete all children nodes. Keep in mind this might not delete everything within a node network. See "delete_all_items" method for that"""
        for child_node in self.get_children_nodes():
            child_node.destroy()

    def delete_all_items(self):
        all_items = self.node.allItems()
        self.node.deleteItems(all_items)

    def get_input_labels(self):
        labels = self.node.inputLabels()
        return list(labels)

    def get_input_label_index(self, label):
        labels = self.get_input_labels()
        try:
            index = labels.index(label)
            return index
        except ValueError:
            raise ValueError(f"Label: {label}. Was not found in node: {self.path}")

    def create_node(self, node_type_name, node_name=None) -> hou.Node:
        new_node = self.node.createNode(node_type_name, node_name)
        return new_node

    def create_node_if_not_exists(self, ox_node_class, node_name=None):
        node_type_name = ox_node_class.node_type
        child_node = self.get_child_by_name(child_name=node_name)
        if not child_node:
            child_node = self.create_node(node_type_name=node_type_name, node_name=node_name)
        return child_node

    def create_ox_node_if_not_exists(self, ox_node_class, node_name=None):
        """shortcut method that will go ahead and create an ox node"""
        child_node = self.create_node_if_not_exists(ox_node_class=ox_node_class, node_name=node_name)
        return ox_node_class(node=child_node)

    def connect_from(self, ox_node, input_index=0, out_index=0, input_label=None):
        """use input_label over input_index whenever possible"""
        other_hou_node = ox_node.node
        if input_label:
            input_index = self.get_input_label_index(label=input_label)
        self.node.setInput(input_index=input_index, item_to_become_input=other_hou_node, output_index=out_index)

    def get_child_by_name(self, child_name):
        for child in self.get_children_nodes():
            if child.name() == child_name:
                return child

    def has_child_with_name(self, child_name):
        return bool(self.get_child_by_name(child_name=child_name))

    def get_children_paths_by_partial_name(self, substring):
        path_list = []
        for node in self.get_children_nodes():
            if substring in node.name():
                path_list.append(node.path())
        return path_list

    def get_children_nodes_by_partial_name(self, substring):
        node_list = []
        for node in self.get_children_nodes():
            if substring in node.name():
                node_list.append(node)
        return node_list

    def get_children_nodes(self) -> List[hou.Node]:
        children_node_list = self.node.children()
        return children_node_list

    def get_child_nodes_by_type(self, node_type, expect_match=True):
        matching_nodes = [i for i in self.get_children_nodes() if i.type().name() == node_type]
        if not matching_nodes and expect_match:
            raise ValueError(f'Expected child node of type "{node_type}" but no matches were found')
        return matching_nodes

    def get_child_by_node_type(self, node_type, expect_match=True, only_one_match=True):
        matching_nodes = self.get_child_nodes_by_type(node_type=node_type, expect_match=expect_match)
        if matching_nodes and len(matching_nodes) > 1 and only_one_match:
            return ValueError(f"Expected only one match for child node type {node_type} but found many: {matching_nodes}")
        if matching_nodes and len(matching_nodes) == 1:
            return matching_nodes[0]

    def set_color(self, color):
        """
        Can pass in a tuple for RGB values or a hou.Color object. 
        """
        color = color if isinstance(color, hou.Color) else hou.Color(color)
        self.node.setColor(color)

    def set_name(self, new_name):
        self.node.setName(new_name)

    def get_prim_values(self, field):
        value_list = [i.attribValue(field) for i in self.node.geometry().prims()]
        return value_list

    def get_planes(self):
        planes = self.node.planes()
        return planes

    def get_displayed_child_node(self):
        for node in self.get_children_nodes():
            if node.isDisplayFlagSet():
                return node

    def layout_children(self):
        self.node.layoutChildren()

    def move_node_relative_to(self, ox_node, x=0, y=-1, unit_multiplier=2):
        """a handy method that will move this node relative to another node. The default moves the node below the relative node"""
        relative_position_vector = ox_node.node.position()
        r_x = relative_position_vector[0]
        r_y = relative_position_vector[1]
        vector = hou.Vector2(r_x + x * unit_multiplier, r_y + y * unit_multiplier)
        self.node.setPosition(vector)

    def unlock_node(self):
        self.node.allowEditingOfContents()

    def get_folder_labels(self):
        templates = self.get_parm_templates_by_type(template_type=parm_template_types.FOLDER)
        labels = [i.label() for i in templates]
        return labels

    def set_display_flag(self, on=True):
        self.node.setDisplayFlag(on=on)

    def set_render_flag(self, on=True):
        self.node.setRenderFlag(on=on)

    def set_display_and_render_flags(self, on=True):
        self.set_display_flag(on=on)
        self.set_render_flag(on=on)

    def set_bypass_flag(self, on):
        self.node.bypass(on=on)

    def get_prim_groups(self):
        group_list = [i.name() for i in self.node.geometry().primGroups()]
        return group_list

    def load_preset(self, preset_name=None):
        """if no preset name specified, just use the node name. This is a good default for many use cases"""
        preset_name = preset_name if preset_name else self.name
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
        """uses default preset path when preset_path not specified"""
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
        ox_logger.info(f'renaming node from "{self.name}" to "{new_name}"')
        result = self.node.setName(name=new_name)
        self.name = new_name
        ox_logger.debug(f"rename node result: {result}")

    def get_input_count(self):
        input_count = len(self.node.inputConnections())
        return input_count

    ##################################################################################################################################################
    # parm methods
    def get_parms(self) -> List[hou.Parm]:
        parameters = self.node.parms()
        return parameters

    def get_parms_by_name_substring(self, substring, ends_with=False, starts_with=False):
        parameters = self.get_parms()
        if ends_with:
            parm_sublist = [i for i in parameters if i.name().endswith(substring)]
        elif starts_with:
            parm_sublist = [i for i in parameters if i.name().startswith(substring)]
        else:
            parm_sublist = [i for i in parameters if substring in i.name()]
        return parm_sublist

    def get_parms_by_regex(self, regex_str):
        parameters = self.get_parms()   
        parm_sublist = [i for i in parameters if re.match(regex_str, i.name())]
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

    def get_parms_as_dict(self, parm_list: List[hou.Parm], substring=None):
        """
        returns all parameters as a dictionary with the parm name as key and parm value as the value.
        If a substring is specified, this will only match parameter names with that substring
        """
        parm_list = self.get_parms_by_name_substring(substring=substring) if substring else self.get_parms()
        parm_dict = {i.name(): i.eval() for i in parm_list}
        return parm_dict

    def get_children_parms_dict(self):
        """
        handy method that gets all children nodes and parameters as a dict to reaply later or to another node. 
        """
        child_parms_dict = defaultdict(dict)
        for i in self.get_children_nodes():
            ox_logger.debug(f'coppying parms for child node {i.name()}')
            for parm in i.parms():
                parm_value = parm.eval()
                parm_name = parm.name()
                node_name = i.name()
                child_parms_dict[node_name][parm_name] = parm_value
        return child_parms_dict

    def apply_children_parms_dict(self, children_parms_dict):
        for key, value in children_parms_dict.items():
            ox_logger.debug(f'Getting child node by key: ({key}) to apply children parms to')
            key_node: hou.Node = self.get_child_by_name(key)
            for parm_key, parm_value in value.items():
                try: 
                    parm: hou.Parm = key_node.parm(parm_key)
                except AttributeError:
                    ox_logger.warn(f'No parm "{parm_key}" found for node {key_node} to apply value to. Skipping')
                    continue
                ox_logger.debug(f'Node: {key_node} - Setting parm "{parm_key}" to value: {parm_value}')
                parm.set(parm_value)

    ##################################################################################################################################################
