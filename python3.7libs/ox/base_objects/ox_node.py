import re

import hou

from ox.base_objects.parm_templates import ParmTemplate
from ox.utils.node_color_lookup import color_lookup_dict


class OXNode(ParmTemplate):  # mixin
    # these are for child class lookups:
    parm_lookup_dict = {}

    def __init__(self, node=None):
        super().__init__(node=node)
        self.node = node
        self.path = node.path()
        self.type = node.type().name()
        if self.type in color_lookup_dict:
            self.set_color(color_lookup_dict[self.type])

    def __setattr__(self, name, value):
        skip_list = ['node']
        clean_key = self.clean_parm_key(raw_key=name)
        if clean_key in self.parm_lookup_dict and clean_key not in skip_list and hasattr(self, name):
            hou_parm_string = self.parm_lookup_dict[clean_key]
            parm = self.node.parm(hou_parm_string)
            parm.set(value)
        else:
            super().__setattr__(name, value)

    @staticmethod
    def clean_parm_key(raw_key):
        del_list = ['parm_']
        clean_key = re.sub(r"{}".format('|'.join(del_list)), '', raw_key)
        return clean_key

    def create_node(self, node_type_name, node_name=None):
        new_node = self.node.createNode(node_type_name, node_name)
        return new_node

    def connect_from(self, ox_node, input_index=0, out_index=0):
        other_hou_node = ox_node.node
        self.node.setInput(input_index=input_index, item_to_become_input=other_hou_node, output_index=out_index)

    def get_child_by_name(self, child_name):
        for child in self.node.children():
            if child.name() == child_name:
                return child

    def get_children_paths_by_partial_name(self, substring):
        path_list = []
        for node in self.node.children():
            if substring in node.name():
                path_list.append(node.path())
        return path_list

    def set_color(self, color):
        self.node.setColor(color)

    def get_prim_values(self, field):
        value_list = [i.attribValue(field) for i in self.node.geometry().prims()]
        return value_list

    def get_displayed_child_node(self, ):
        for node in self.node.children():
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
        labels = self.get_entry_labels()
        return labels

    def set_display_flag(self, on=True, include_render_flag=True):
        self.node.setDisplayFlag(on=on)
        if include_render_flag:
            self.node.setRenderFlag(on=on)

    def get_prim_groups(self):
        group_list = [i.name() for i in self.node.geometry().primGroups()]
        return group_list
