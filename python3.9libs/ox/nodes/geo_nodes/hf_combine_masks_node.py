from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HfCombineMasksNode(OXNode):
    node_type = 'labs::hf_combine_masks'
    parm_lookup_dict = {'bflood': 'bFlood', 'srcname1': 'srcname1', 'folder0': 'folder0', 'folder1': 'folder1', 'clampmin': 'clampmin', 'clampmax': 'clampmax', 'remap': 'remap', 'remap1pos': 'remap1pos', 'remap1value': 'remap1value', 'remap1interp': 'remap1interp', 'remap2pos': 'remap2pos', 'remap2value': 'remap2value', 'remap2interp': 'remap2interp'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_bflood = Parameter(parm=self.node.parm('bFlood'))
        self.parm_srcname1 = Parameter(parm=self.node.parm('srcname1'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_clampmin = Parameter(parm=self.node.parm('clampmin'))
        self.parm_clampmax = Parameter(parm=self.node.parm('clampmax'))
        self.parm_remap = Parameter(parm=self.node.parm('remap'))
        self.parm_remap1pos = Parameter(parm=self.node.parm('remap1pos'))
        self.parm_remap1value = Parameter(parm=self.node.parm('remap1value'))
        self.parm_remap2pos = Parameter(parm=self.node.parm('remap2pos'))
        self.parm_remap2value = Parameter(parm=self.node.parm('remap2value'))

        
        # parm menu vars:
        self.parm_remap1interp = Remap1InterpMenu(parm=self.node.parm('remap1interp'))
        self.parm_remap2interp = Remap2InterpMenu(parm=self.node.parm('remap2interp'))


        # input vars:
        self.input_heightfield = 'Heightfield'


# parm menu classes:
class Remap1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Remap2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"



