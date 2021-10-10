from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class SwitchNode(HHNode):
    node_type = 'switch'
    parm_lookup_dict = {'input': 'input'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_input = Parameter(parm=self.node.parm('input'))

        
        # parm menu vars:


        # input vars:
        self.input_input_1 = 0
        self.input_input_2 = 1
        self.input_input_3 = 2
        self.input_input_4 = 3
        self.input_input_5 = 4


# parm menu classes:

