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
        self.menu_stretch_range_to_black_white = ("histogram", 0)
        self.menu_move_minimum_value_to_black = ("histblack", 1)
        self.menu_move_maximum_value_to_white = ("histwhite", 2)
        self.menu_move_average_luminance = ("average", 3)
        self.menu_equalize_luminance_across_frames = ("equalize", 4)


class FitMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_to_fit = ("scale", 0)
        self.menu_shift_to_fit = ("shift", 1)


class LumMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("lum", 0)
        self.menu_ntsc_luminance = ("ntsclum", 1)
        self.menu_max_component = ("max", 2)
        self.menu_min_component = ("min", 3)
        self.menu_average = ("average", 4)
        self.menu_red = ("r", 5)
        self.menu_green = ("g", 6)
        self.menu_blue = ("b", 7)
        self.menu_fourth_component = ("c4", 8)


class MaskinputMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_first_input = ("first", 0)
        self.menu_mask_input = ("mask", 1)
        self.menu_off = ("off", 2)


class MaskplaneMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_mask_input = ("none", 0)


class PscopeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("*", 0)


class FscopeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_frames = ("all", 0)
        self.menu_inside_range = ("inside", 1)
        self.menu_outside_range = ("outside", 2)
        self.menu_even_frames = ("even", 3)
        self.menu_odd_frames = ("odd", 4)
        self.menu_specific_frames = ("specific", 5)


class FdropfuncMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear = ("linear", 0)
        self.menu_ease_in = ("easein", 1)
        self.menu_ease_out = ("easeout", 2)
        self.menu_ease_in_ease_out = ("easeinout", 3)


class FmenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scope_all_frames = ("scopeall", 0)
        self.menu_scope_current_frame = ("scopecur", 1)
        self.menu_scope_from_start_to_current = ("scopetocur", 2)
        self.menu_scope_from_current_to_end = ("scopefromcur", 3)
        self.menu_unscope_all_frames = ("unscopeall", 4)
        self.menu_unscope_current_frame = ("unscopecur", 5)
        self.menu_unscope_from_start_to_current = ("unscopetocur", 6)
        self.menu_unscope_from_current_to_end = ("unscopefromcur", 7)



