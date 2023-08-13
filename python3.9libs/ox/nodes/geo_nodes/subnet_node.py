from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SubnetNode(OXNode):
    node_type = 'subnet'
    parm_lookup_dict = {'label1': 'label1', 'label2': 'label2', 'label3': 'label3', 'label4': 'label4'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_label1 = Parameter(parm=self.node.parm('label1'))
        self.parm_label2 = Parameter(parm=self.node.parm('label2'))
        self.parm_label3 = Parameter(parm=self.node.parm('label3'))
        self.parm_label4 = Parameter(parm=self.node.parm('label4'))

        
        # parm menu vars:


        # input vars:
        self.input_sub_network_input__1 = 'Sub-Network Input #1'
        self.input_sub_network_input__2 = 'Sub-Network Input #2'
        self.input_sub_network_input__3 = 'Sub-Network Input #3'
        self.input_sub_network_input__4 = 'Sub-Network Input #4'


# parm menu classes:

