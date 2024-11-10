from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ConvertnormalNode(OXNode):
    node_type = 'convertnormal'
    parm_lookup_dict = {'conversion': 'conversion', 'normalize': 'normalize', 'offsetx': 'offsetx', 'offsety': 'offsety', 'offsetz': 'offsetz', 'scalex': 'scalex', 'scaley': 'scaley', 'scalez': 'scalez'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_normalize = Parameter(parm=self.node.parm('normalize'))
        self.parm_offsetx = Parameter(parm=self.node.parm('offsetx'))
        self.parm_offsety = Parameter(parm=self.node.parm('offsety'))
        self.parm_offsetz = Parameter(parm=self.node.parm('offsetz'))
        self.parm_scalex = Parameter(parm=self.node.parm('scalex'))
        self.parm_scaley = Parameter(parm=self.node.parm('scaley'))
        self.parm_scalez = Parameter(parm=self.node.parm('scalez'))

        
        # parm menu vars:
        self.parm_conversion = ConversionMenu(parm=self.node.parm('conversion'))


        # input vars:
        self.input_normal = 'normal'


# parm menu classes:
class ConversionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_offset_to_signed = ("tosigned", 0)
        self.menu_signed_to_offset = ("tooffset", 1)



