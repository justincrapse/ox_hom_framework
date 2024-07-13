from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CopnetNode(OXNode):
    node_type = 'copnet'
    parm_lookup_dict = {'usecoppath': 'usecoppath', 'coppath': 'coppath', 'singleoutput': 'singleoutput', 'output': 'output', 'plane': 'plane', 'docompile': 'docompile', 'outputapexgraph': 'outputapexgraph', 'setres': 'setres', 'res1': 'res1', 'res2': 'res2', 'resmenu': 'resmenu', 'setpixelscale': 'setpixelscale', 'pixelscale': 'pixelscale', 'setborder': 'setborder', 'border': 'border', 'setprecision': 'setprecision', 'precision': 'precision', 'setvistile': 'setvistile', 'vistile': 'vistile'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_usecoppath = Parameter(parm=self.node.parm('usecoppath'))
        self.parm_coppath = Parameter(parm=self.node.parm('coppath'))
        self.parm_singleoutput = Parameter(parm=self.node.parm('singleoutput'))
        self.parm_output = Parameter(parm=self.node.parm('output'))
        self.parm_docompile = Parameter(parm=self.node.parm('docompile'))
        self.parm_outputapexgraph = Parameter(parm=self.node.parm('outputapexgraph'))
        self.parm_setres = Parameter(parm=self.node.parm('setres'))
        self.parm_res1 = Parameter(parm=self.node.parm('res1'))
        self.parm_res2 = Parameter(parm=self.node.parm('res2'))
        self.parm_resmenu = Parameter(parm=self.node.parm('resmenu'))
        self.parm_setpixelscale = Parameter(parm=self.node.parm('setpixelscale'))
        self.parm_pixelscale = Parameter(parm=self.node.parm('pixelscale'))
        self.parm_setborder = Parameter(parm=self.node.parm('setborder'))
        self.parm_setprecision = Parameter(parm=self.node.parm('setprecision'))
        self.parm_setvistile = Parameter(parm=self.node.parm('setvistile'))
        self.parm_vistile = Parameter(parm=self.node.parm('vistile'))

        
        # parm menu vars:
        self.parm_plane = PlaneMenu(parm=self.node.parm('plane'))
        self.parm_border = BorderMenu(parm=self.node.parm('border'))
        self.parm_precision = PrecisionMenu(parm=self.node.parm('precision'))


        # input vars:


# parm menu classes:
class PlaneMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_xy_plane = ("xy", 0)
        self.menu_yz_plane = ("yz", 1)
        self.menu_zx_plane = ("zx", 2)


class BorderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_clamp = ("clamp", 1)
        self.menu_mirror = ("mirror", 2)
        self.menu_wrap = ("wrap", 3)


class PrecisionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bit_16 = ("b16", 0)
        self.menu_bit_32 = ("b32", 1)



