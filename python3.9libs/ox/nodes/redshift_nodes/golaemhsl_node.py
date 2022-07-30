from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class GolaemhslNode(OXNode):
    node_type = 'redshift::GolaemHSL'
    parm_lookup_dict = {'incolorr': 'inColorr', 'incolorg': 'inColorg', 'incolorb': 'inColorb', 'h': 'h', 's': 's', 'l': 'l', 'shader_skipdefvalparms': 'shader_skipdefvalparms'}

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
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))

        
        # parm menu vars:


        # input vars:
        self.input_incolor = 'inColor'
        self.input_h = 'h'
        self.input_s = 's'
        self.input_l = 'l'


# parm menu classes:

