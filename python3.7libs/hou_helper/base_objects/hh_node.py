import re

import hou


from hou_helper.base_objects.parm_templates import ParmTemplate


class HHNode:
    # these are for child class lookups:
    parm_lookup_dict = {}

    def __init__(self, node=None):
        self.node = node
        self.parm_template = ParmTemplate(node=self.node)
        self.path = node.path()

    def __setattr__(self, name, value):
        skip_list = ['node']
        clean_key = self.clean_parm_key(raw_key=name)
        # print(f'accessing setattr with {name, value}')
        if clean_key in self.parm_lookup_dict and clean_key not in skip_list and hasattr(self, name):
            print(f'in setattr with: {clean_key}, {value}')
            hou_parm_string = self.parm_lookup_dict[clean_key]
            parm = self.node.parm(hou_parm_string)
            parm.set(value)
        else:
            super().__setattr__(name, value)

    @staticmethod
    def clean_parm_key(raw_key):
        del_list = ['parm_', '_menu']
        # clean_re = rf"{'|'.join(del_list)}"
        clean_key = re.sub(rf"{'|'.join(del_list)}", '', raw_key)
        return clean_key

    def create_node(self, node_type_name, node_name=None):
        # f'creating node on {self.node}: type:{node_type_name}, name:{node_name}'
        new_node = self.node.createNode(node_type_name, node_name)
        return new_node

    def connect_from(self, hh_node, input_index=0, out_index=0):
        other_hou_node = hh_node.node
        # print(f'connecting from {self.node.name()} to {other_hou_nade.name()} in: {input_index}, out: {out_index}')
        self.node.setInput(input_index=input_index, item_to_become_input=other_hou_node, output_index=out_index)

    def get_child_by_name(self, child_name):
        for child in self.node.children():
            if child.name() == child_name:
                return child

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

