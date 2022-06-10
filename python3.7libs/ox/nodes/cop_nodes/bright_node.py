from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class BrightNode(OXNode):
    node_type = 'bright'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'bright': 'bright', 'bshift': 'bshift', 'usecomp': 'usecomp', 'complabel1': 'complabel1', 'complabel2': 'complabel2', 'red1': 'red1', 'red2': 'red2', 'green1': 'green1', 'green2': 'green2', 'blue1': 'blue1', 'blue2': 'blue2', 'alpha1': 'alpha1', 'alpha2': 'alpha2', 'comp41': 'comp41', 'comp42': 'comp42', 'showcurves': 'showcurves', 'dounpremult': 'dounpremult', 'quantize': 'quantize', 'effectamount': 'effectamount', 'maskinput': 'maskinput', 'maskplane': 'maskplane', 'maskresize': 'maskresize', 'maskinvert': 'maskinvert', 'scopergba': 'scopergba', 'pscope': 'pscope', 'fscope': 'fscope', 'frange1': 'frange1', 'frange2': 'frange2', 'fdropoff1': 'fdropoff1', 'fdropoff2': 'fdropoff2', 'fdropfunc': 'fdropfunc', 'foutside': 'foutside', 'flist': 'flist', 'fmenu': 'fmenu', 'fautoadjust': 'fautoadjust', 'currange': 'currange'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_bright = Parameter(parm=self.node.parm('bright'))
        self.parm_bshift = Parameter(parm=self.node.parm('bshift'))
        self.parm_usecomp = Parameter(parm=self.node.parm('usecomp'))
        self.parm_complabel1 = Parameter(parm=self.node.parm('complabel1'))
        self.parm_complabel2 = Parameter(parm=self.node.parm('complabel2'))
        self.parm_red1 = Parameter(parm=self.node.parm('red1'))
        self.parm_red2 = Parameter(parm=self.node.parm('red2'))
        self.parm_green1 = Parameter(parm=self.node.parm('green1'))
        self.parm_green2 = Parameter(parm=self.node.parm('green2'))
        self.parm_blue1 = Parameter(parm=self.node.parm('blue1'))
        self.parm_blue2 = Parameter(parm=self.node.parm('blue2'))
        self.parm_alpha1 = Parameter(parm=self.node.parm('alpha1'))
        self.parm_alpha2 = Parameter(parm=self.node.parm('alpha2'))
        self.parm_comp41 = Parameter(parm=self.node.parm('comp41'))
        self.parm_comp42 = Parameter(parm=self.node.parm('comp42'))
        self.parm_showcurves = Parameter(parm=self.node.parm('showcurves'))
        self.parm_dounpremult = Parameter(parm=self.node.parm('dounpremult'))
        self.parm_effectamount = Parameter(parm=self.node.parm('effectamount'))
        self.parm_maskresize = Parameter(parm=self.node.parm('maskresize'))
        self.parm_maskinvert = Parameter(parm=self.node.parm('maskinvert'))
        self.parm_scopergba = Parameter(parm=self.node.parm('scopergba'))
        self.parm_frange1 = Parameter(parm=self.node.parm('frange1'))
        self.parm_frange2 = Parameter(parm=self.node.parm('frange2'))
        self.parm_fdropoff1 = Parameter(parm=self.node.parm('fdropoff1'))
        self.parm_fdropoff2 = Parameter(parm=self.node.parm('fdropoff2'))
        self.parm_foutside = Parameter(parm=self.node.parm('foutside'))
        self.parm_flist = Parameter(parm=self.node.parm('flist'))
        self.parm_fautoadjust = Parameter(parm=self.node.parm('fautoadjust'))
        self.parm_currange = Parameter(parm=self.node.parm('currange'))

        
        # parm menu vars:
        self.parm_quantize = QuantizeMenu(parm=self.node.parm('quantize'))
        self.parm_maskinput = MaskinputMenu(parm=self.node.parm('maskinput'))
        self.parm_maskplane = MaskplaneMenu(parm=self.node.parm('maskplane'))
        self.parm_pscope = PscopeMenu(parm=self.node.parm('pscope'))
        self.parm_fscope = FscopeMenu(parm=self.node.parm('fscope'))
        self.parm_fdropfunc = FdropfuncMenu(parm=self.node.parm('fdropfunc'))
        self.parm_fmenu = FmenuMenu(parm=self.node.parm('fmenu'))


        # input vars:
        self.input_image_to_brighten = 'Image to Brighten'
        self.input_mask_input = 'Mask Input'


# parm menu classes:
class QuantizeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_where_optimal = 0
        self.menu_quantize_at_this_node = 1


class MaskinputMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_first_input = 0
        self.menu_mask_input = 1
        self.menu_off = 2


class MaskplaneMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_mask_input = 0


class PscopeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = 0


class FscopeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_frames = 0
        self.menu_inside_range = 1
        self.menu_outside_range = 2
        self.menu_even_frames = 3
        self.menu_odd_frames = 4
        self.menu_specific_frames = 5


class FdropfuncMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear = 0
        self.menu_ease_in = 1
        self.menu_ease_out = 2
        self.menu_ease_in_ease_out = 3


class FmenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scope_all_frames = 0
        self.menu_scope_current_frame = 1
        self.menu_scope_from_start_to_current = 2
        self.menu_scope_from_current_to_end = 3
        self.menu_unscope_all_frames = 4
        self.menu_unscope_current_frame = 5
        self.menu_unscope_from_start_to_current = 6
        self.menu_unscope_from_current_to_end = 7



