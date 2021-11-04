from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HfCombineMasksNode(OXNode):
    node_type = 'labs::hf_combine_masks'
    parm_lookup_dict = {'bflood': 'bFlood', 'srcname1': 'srcname1', 'folder0': 'folder0', 'folder1': 'folder1', 'clampmin': 'clampmin', 'clampmax': 'clampmax', 'remap': 'remap', 'remap1pos': 'remap1pos', 'remap1value': 'remap1value', 'remap1interp': 'remap1interp', 'remap2pos': 'remap2pos', 'remap2value': 'remap2value', 'remap2interp': 'remap2interp', 'layername_1': 'layername_1', 'clamp_1': 'clamp_1', 'blend_1': 'blend_1', 'method_1': 'method_1', 'radius_1': 'radius_1', 'mode_1': 'mode_1', 'layername_2': 'layername_2', 'clamp_2': 'clamp_2', 'blend_2': 'blend_2', 'method_2': 'method_2', 'radius_2': 'radius_2', 'mode_2': 'mode_2', 'layername_3': 'layername_3', 'clamp_3': 'clamp_3', 'blend_3': 'blend_3', 'method_3': 'method_3', 'radius_3': 'radius_3', 'mode_3': 'mode_3', 'layername_4': 'layername_4', 'clamp_4': 'clamp_4', 'blend_4': 'blend_4', 'method_4': 'method_4', 'radius_4': 'radius_4', 'mode_4': 'mode_4', 'layername_5': 'layername_5', 'clamp_5': 'clamp_5', 'blend_5': 'blend_5', 'method_5': 'method_5', 'radius_5': 'radius_5', 'mode_5': 'mode_5'}

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
        self.parm_layername_1 = Parameter(parm=self.node.parm('layername_1'))
        self.parm_clamp_1 = Parameter(parm=self.node.parm('clamp_1'))
        self.parm_blend_1 = Parameter(parm=self.node.parm('blend_1'))
        self.parm_radius_1 = Parameter(parm=self.node.parm('radius_1'))
        self.parm_layername_2 = Parameter(parm=self.node.parm('layername_2'))
        self.parm_clamp_2 = Parameter(parm=self.node.parm('clamp_2'))
        self.parm_blend_2 = Parameter(parm=self.node.parm('blend_2'))
        self.parm_radius_2 = Parameter(parm=self.node.parm('radius_2'))
        self.parm_layername_3 = Parameter(parm=self.node.parm('layername_3'))
        self.parm_clamp_3 = Parameter(parm=self.node.parm('clamp_3'))
        self.parm_blend_3 = Parameter(parm=self.node.parm('blend_3'))
        self.parm_radius_3 = Parameter(parm=self.node.parm('radius_3'))
        self.parm_layername_4 = Parameter(parm=self.node.parm('layername_4'))
        self.parm_clamp_4 = Parameter(parm=self.node.parm('clamp_4'))
        self.parm_blend_4 = Parameter(parm=self.node.parm('blend_4'))
        self.parm_radius_4 = Parameter(parm=self.node.parm('radius_4'))
        self.parm_layername_5 = Parameter(parm=self.node.parm('layername_5'))
        self.parm_clamp_5 = Parameter(parm=self.node.parm('clamp_5'))
        self.parm_blend_5 = Parameter(parm=self.node.parm('blend_5'))
        self.parm_radius_5 = Parameter(parm=self.node.parm('radius_5'))

        
        # parm menu vars:
        self.parm_remap1interp = Remap1InterpMenu(parm=self.node.parm('remap1interp'))
        self.parm_remap2interp = Remap2InterpMenu(parm=self.node.parm('remap2interp'))
        self.parm_method_1 = Method1Menu(parm=self.node.parm('method_1'))
        self.parm_mode_1 = Mode1Menu(parm=self.node.parm('mode_1'))
        self.parm_method_2 = Method2Menu(parm=self.node.parm('method_2'))
        self.parm_mode_2 = Mode2Menu(parm=self.node.parm('mode_2'))
        self.parm_method_3 = Method3Menu(parm=self.node.parm('method_3'))
        self.parm_mode_3 = Mode3Menu(parm=self.node.parm('mode_3'))
        self.parm_method_4 = Method4Menu(parm=self.node.parm('method_4'))
        self.parm_mode_4 = Mode4Menu(parm=self.node.parm('mode_4'))
        self.parm_method_5 = Method5Menu(parm=self.node.parm('method_5'))
        self.parm_mode_5 = Mode5Menu(parm=self.node.parm('mode_5'))


        # input vars:
        self.input_heightfield = 0


# parm menu classes:
class Remap1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class Remap2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class Method1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = 0
        self.menu_box_blur = 1
        self.menu_expand = 2
        self.menu_shrink = 3


class Mode1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_add = 1
        self.menu_subtract = 2
        self.menu_difference = 3
        self.menu_multiply = 4
        self.menu_maximum = 5
        self.menu_minimum = 6
        self.menu_blend = 7


class Method2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = 0
        self.menu_box_blur = 1
        self.menu_expand = 2
        self.menu_shrink = 3


class Mode2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_add = 1
        self.menu_subtract = 2
        self.menu_difference = 3
        self.menu_multiply = 4
        self.menu_maximum = 5
        self.menu_minimum = 6
        self.menu_blend = 7


class Method3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = 0
        self.menu_box_blur = 1
        self.menu_expand = 2
        self.menu_shrink = 3


class Mode3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_add = 1
        self.menu_subtract = 2
        self.menu_difference = 3
        self.menu_multiply = 4
        self.menu_maximum = 5
        self.menu_minimum = 6
        self.menu_blend = 7


class Method4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = 0
        self.menu_box_blur = 1
        self.menu_expand = 2
        self.menu_shrink = 3


class Mode4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_add = 1
        self.menu_subtract = 2
        self.menu_difference = 3
        self.menu_multiply = 4
        self.menu_maximum = 5
        self.menu_minimum = 6
        self.menu_blend = 7


class Method5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = 0
        self.menu_box_blur = 1
        self.menu_expand = 2
        self.menu_shrink = 3


class Mode5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_add = 1
        self.menu_subtract = 2
        self.menu_difference = 3
        self.menu_multiply = 4
        self.menu_maximum = 5
        self.menu_minimum = 6
        self.menu_blend = 7



