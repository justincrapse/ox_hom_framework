from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RemapNode(OXNode):
    node_type = 'remap'
    parm_lookup_dict = {'signature': 'signature', 'mask': 'mask', 'scopergba': 'scopergba', 'op': 'op', 'side': 'side', 'threshold': 'threshold', 'width': 'width', 'inputmin': 'inputmin', 'inputmax': 'inputmax', 'outputmin': 'outputmin', 'outputmax': 'outputmax', 'method': 'method', 'ramp': 'ramp', 'ramp1pos': 'ramp1pos', 'ramp1value': 'ramp1value', 'ramp1interp': 'ramp1interp', 'ramp2pos': 'ramp2pos', 'ramp2value': 'ramp2value', 'ramp2interp': 'ramp2interp'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_mask = Parameter(parm=self.node.parm('mask'))
        self.parm_scopergba = Parameter(parm=self.node.parm('scopergba'))
        self.parm_threshold = Parameter(parm=self.node.parm('threshold'))
        self.parm_width = Parameter(parm=self.node.parm('width'))
        self.parm_inputmin = Parameter(parm=self.node.parm('inputmin'))
        self.parm_inputmax = Parameter(parm=self.node.parm('inputmax'))
        self.parm_outputmin = Parameter(parm=self.node.parm('outputmin'))
        self.parm_outputmax = Parameter(parm=self.node.parm('outputmax'))
        self.parm_ramp = Parameter(parm=self.node.parm('ramp'))
        self.parm_ramp1pos = Parameter(parm=self.node.parm('ramp1pos'))
        self.parm_ramp1value = Parameter(parm=self.node.parm('ramp1value'))
        self.parm_ramp2pos = Parameter(parm=self.node.parm('ramp2pos'))
        self.parm_ramp2value = Parameter(parm=self.node.parm('ramp2value'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))
        self.parm_op = OpMenu(parm=self.node.parm('op'))
        self.parm_side = SideMenu(parm=self.node.parm('side'))
        self.parm_method = MethodMenu(parm=self.node.parm('method'))
        self.parm_ramp1interp = Ramp1InterpMenu(parm=self.node.parm('ramp1interp'))
        self.parm_ramp2interp = Ramp2InterpMenu(parm=self.node.parm('ramp2interp'))


        # input vars:
        self.input_source = 'source'
        self.input_ramp = 'ramp'
        self.input_mask = 'mask'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_select_automatically = ("auto", 0)
        self.menu_mono = ("f1", 1)
        self.menu_uv = ("f2", 2)
        self.menu_rgb = ("f3", 3)
        self.menu_rgba = ("f4", 4)


class OpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_remap = ("remap", 0)
        self.menu_threshold = ("threshold", 1)


class SideMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_greater = ("greater", 0)
        self.menu_greater_or_equal = ("greaterequal", 1)
        self.menu_less = ("less", 2)
        self.menu_less_or_equal = ("lessequal", 3)


class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_clamp_at_end = ("clamp", 0)
        self.menu_repeat = ("repeat", 1)
        self.menu_extend = ("extend", 2)


class Ramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_linear = ("linear", 1)
        self.menu_catmull_rom = ("catmull-rom", 2)
        self.menu_monotone_cubic = ("monotonecubic", 3)
        self.menu_bezier = ("bezier", 4)
        self.menu_b_spline = ("bspline", 5)
        self.menu_hermite = ("hermite", 6)


class Ramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_linear = ("linear", 1)
        self.menu_catmull_rom = ("catmull-rom", 2)
        self.menu_monotone_cubic = ("monotonecubic", 3)
        self.menu_bezier = ("bezier", 4)
        self.menu_b_spline = ("bspline", 5)
        self.menu_hermite = ("hermite", 6)



