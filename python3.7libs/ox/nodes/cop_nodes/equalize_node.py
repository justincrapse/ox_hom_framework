from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class EqualizeNode(OXNode):
    node_type = 'equalize'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'op': 'op', 'fit': 'fit', 'lum': 'lum', 'black': 'black', 'white': 'white', 'average': 'average', 'before': 'before', 'after': 'after', 'effect': 'effect', 'effectamount': 'effectamount', 'maskinput': 'maskinput', 'maskplane': 'maskplane', 'maskresize': 'maskresize', 'maskinvert': 'maskinvert', 'scopergba': 'scopergba', 'pscope': 'pscope', 'fscope': 'fscope', 'frange1': 'frange1', 'frange2': 'frange2', 'fdropoff1': 'fdropoff1', 'fdropoff2': 'fdropoff2', 'fdropfunc': 'fdropfunc', 'foutside': 'foutside', 'flist': 'flist', 'fmenu': 'fmenu', 'fautoadjust': 'fautoadjust', 'currange': 'currange'}

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
        self.parm_black = Parameter(parm=self.node.parm('black'))
        self.parm_white = Parameter(parm=self.node.parm('white'))
        self.parm_average = Parameter(parm=self.node.parm('average'))
        self.parm_before = Parameter(parm=self.node.parm('before'))
        self.parm_after = Parameter(parm=self.node.parm('after'))
        self.parm_effect = Parameter(parm=self.node.parm('effect'))
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
        self.parm_op = OpMenu(parm=self.node.parm('op'))
        self.parm_fit = FitMenu(parm=self.node.parm('fit'))
        self.parm_lum = LumMenu(parm=self.node.parm('lum'))
        self.parm_maskinput = MaskinputMenu(parm=self.node.parm('maskinput'))
        self.parm_maskplane = MaskplaneMenu(parm=self.node.parm('maskplane'))
        self.parm_pscope = PscopeMenu(parm=self.node.parm('pscope'))
        self.parm_fscope = FscopeMenu(parm=self.node.parm('fscope'))
        self.parm_fdropfunc = FdropfuncMenu(parm=self.node.parm('fdropfunc'))
        self.parm_fmenu = FmenuMenu(parm=self.node.parm('fmenu'))


        # input vars:
        self.input_image_to_equalize = 'Image to Equalize'
        self.input_mask_input = 'Mask Input'


# parm menu classes:
class OpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_stretch_range_to_black_white = 0
        self.menu_move_minimum_value_to_black = 1
        self.menu_move_maximum_value_to_white = 2
        self.menu_move_average_luminance = 3
        self.menu_equalize_luminance_across_frames = 4


class FitMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_to_fit = 0
        self.menu_shift_to_fit = 1


class LumMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = 0
        self.menu_ntsc_luminance = 1
        self.menu_max_component = 2
        self.menu_min_component = 3
        self.menu_average = 4
        self.menu_red = 5
        self.menu_green = 6
        self.menu_blue = 7
        self.menu_fourth_component = 8


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



