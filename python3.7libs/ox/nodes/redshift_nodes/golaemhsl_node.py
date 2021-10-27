from ox.base_objects.ox_node import HHNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class GolaemhslNode(HHNode):
    node_type = 'redshift::GolaemHSL'
    parm_lookup_dict = {'incolorr': 'inColorr', 'incolorg': 'inColorg', 'incolorb': 'inColorb', 'h': 'h', 's': 's', 'l': 'l'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_incolorr = Parameter(parm=self.node.parm('inColorr'))
        self.parm_incolorg = Parameter(parm=self.node.parm('inColorg'))
        self.parm_incolorb = Parameter(parm=self.node.parm('inColorb'))
        self.parm_h = Parameter(parm=self.node.parm('h'))
        self.parm_s = Parameter(parm=self.node.parm('s'))
        self.parm_l = Parameter(parm=self.node.parm('l'))

        
        # parm menu vars:


        # input vars:
        self.input_incolor = 0
        self.input_h = 1
        self.input_s = 2
        self.input_l = 3


# parm menu classes:

