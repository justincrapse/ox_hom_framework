import re


class HHNode:
    # these are for child class lookups:
    parm_lookup_dict = {}

    def __init__(self, node=None):
        self.node = node

    def clean_parm_key(self, raw_key):
        del_list = ['parm_', '_menu']
        clean_re = rf"{'|'.join(del_list)}"
        clean_key = re.sub(rf"{'|'.join(del_list)}", '', raw_key)
        return clean_key

    def create_node(self, node_type_name, node_name=None):
        print(f'creating node on {self.node}: type:{node_type_name}, name:{node_name}')
        new_node = self.node.createNode(node_type_name, node_name)
        return new_node

    def connect_from(self, other_hh_node, input_index=0, out_index=0):
        other_hh_node_list = [other_hh_node] if not isinstance(other_hh_node, list) else other_hh_node
        for other_node in other_hh_node_list:
            other_node = other_hh_node.node
            self.node.setInput(input_index=input_index, item_to_become_input=other_node, output_index=out_index)

    def __setattr__(self, name, value):
        skip_list = ['node']
        clean_key = self.clean_parm_key(raw_key=name)
        print(f'accessing setattr with {name, value}')
        if clean_key in self.parm_lookup_dict and clean_key not in skip_list and hasattr(self, name):
            print(f'in setattr with: {clean_key}, {value}')
            hou_parm_string = self.parm_lookup_dict[clean_key]
            parm = self.node.parm(hou_parm_string)
            parm.set(value)
        else:
            super().__setattr__(name, value)



        

