from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SopimportNode(OXNode):
    node_type = 'sopimport'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'soppath': 'soppath', 'importmask': 'importmask', 'setres': 'setres', 'setplanes': 'setplanes', 'remap': 'remap', 'remaprange1': 'remaprange1', 'remaprange2': 'remaprange2', 'effectamount': 'effectamount', 'maskplane': 'maskplane', 'maskresize': 'maskresize', 'maskinvert': 'maskinvert', 'overridesize': 'overridesize', 'size1': 'size1', 'size2': 'size2', 'sizemenu': 'sizemenu', 'overrideaspect': 'overrideaspect', 'aspect': 'aspect', 'planes': 'planes', 'addplanes': 'addplanes', 'addplaneop': 'addplaneop', 'customplanes': 'customplanes', 'depth': 'depth', 'depthmenu': 'depthmenu', 'depthglobal': 'depthglobal', 'usebwpoints': 'usebwpoints', 'bwpoints1': 'bwpoints1', 'bwpoints2': 'bwpoints2', 'interlace': 'interlace', 'idominance': 'idominance', 'overriderange': 'overriderange', 'singleimage': 'singleimage', 'start': 'start', 'length': 'length', 'preextend': 'preextend', 'prehold': 'prehold', 'postextend': 'postextend', 'posthold': 'posthold'}

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
        self.parm_soppath = Parameter(parm=self.node.parm('soppath'))
        self.parm_importmask = Parameter(parm=self.node.parm('importmask'))
        self.parm_setres = Parameter(parm=self.node.parm('setres'))
        self.parm_setplanes = Parameter(parm=self.node.parm('setplanes'))
        self.parm_remap = Parameter(parm=self.node.parm('remap'))
        self.parm_remaprange1 = Parameter(parm=self.node.parm('remaprange1'))
        self.parm_remaprange2 = Parameter(parm=self.node.parm('remaprange2'))
        self.parm_effectamount = Parameter(parm=self.node.parm('effectamount'))
        self.parm_maskresize = Parameter(parm=self.node.parm('maskresize'))
        self.parm_maskinvert = Parameter(parm=self.node.parm('maskinvert'))
        self.parm_overridesize = Parameter(parm=self.node.parm('overridesize'))
        self.parm_size1 = Parameter(parm=self.node.parm('size1'))
        self.parm_size2 = Parameter(parm=self.node.parm('size2'))
        self.parm_overrideaspect = Parameter(parm=self.node.parm('overrideaspect'))
        self.parm_aspect = Parameter(parm=self.node.parm('aspect'))
        self.parm_customplanes = Parameter(parm=self.node.parm('customplanes'))
        self.parm_depthglobal = Parameter(parm=self.node.parm('depthglobal'))
        self.parm_usebwpoints = Parameter(parm=self.node.parm('usebwpoints'))
        self.parm_bwpoints1 = Parameter(parm=self.node.parm('bwpoints1'))
        self.parm_bwpoints2 = Parameter(parm=self.node.parm('bwpoints2'))
        self.parm_overriderange = Parameter(parm=self.node.parm('overriderange'))
        self.parm_singleimage = Parameter(parm=self.node.parm('singleimage'))
        self.parm_start = Parameter(parm=self.node.parm('start'))
        self.parm_length = Parameter(parm=self.node.parm('length'))
        self.parm_prehold = Parameter(parm=self.node.parm('prehold'))
        self.parm_posthold = Parameter(parm=self.node.parm('posthold'))

        
        # parm menu vars:
        self.parm_maskplane = MaskplaneMenu(parm=self.node.parm('maskplane'))
        self.parm_sizemenu = SizemenuMenu(parm=self.node.parm('sizemenu'))
        self.parm_planes = PlanesMenu(parm=self.node.parm('planes'))
        self.parm_addplanes = AddplanesMenu(parm=self.node.parm('addplanes'))
        self.parm_addplaneop = AddplaneopMenu(parm=self.node.parm('addplaneop'))
        self.parm_depth = DepthMenu(parm=self.node.parm('depth'))
        self.parm_depthmenu = DepthmenuMenu(parm=self.node.parm('depthmenu'))
        self.parm_interlace = InterlaceMenu(parm=self.node.parm('interlace'))
        self.parm_idominance = IdominanceMenu(parm=self.node.parm('idominance'))
        self.parm_preextend = PreextendMenu(parm=self.node.parm('preextend'))
        self.parm_postextend = PostextendMenu(parm=self.node.parm('postextend'))


        # input vars:


# parm menu classes:
class MaskplaneMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_mask_input = 'none'


class SizemenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_480_640 = '640 480 1'
        self.menu_hdtv_720 = '1280 720 1'
        self.menu_hdtv_1080 = '1920 1080 1'
        self.menu_hdtv_2160__4k_ = '3840 2160 1'
        self.menu__________ = '_separator_'
        self.menu_ntsc = '640 486 1'
        self.menu_ntsc_d1 = '720 486 0.9'
        self.menu_pal = '768 576 1'
        self.menu_pal_d1 = '720 576 1.067'
        self.menu_pal_16_9_anamorphic = '720 576 1.422'
        self.menu_pal_16_9__1_to_1_ = '1024 576 1'
        self.menu__________ = '_separator_'
        self.menu_full_ap_4k = '4096 3112 1'
        self.menu_full_ap_2k = '2048 1556 1'
        self.menu_acad_4k = '3656 2664 1'
        self.menu_acad_2k = '1828 1332 1'
        self.menu_scope_4k = '3656 3112 1'
        self.menu_scope_2k = '1828 1556 1'
        self.menu_vista_4k = '6144 4096 1'
        self.menu_vista_2k = '3072 2048 1'
        self.menu__________ = '_separator_'
        self.menu__2_256 = '256 256 1'
        self.menu__2_512 = '512 512 1'
        self.menu__2_1024 = '1024 1024 1'
        self.menu__2_2048 = '2048 2048 1'
        self.menu__2_4096 = '4096 4096 1'
        self.menu__2_8192 = '8192 8192 1'


class PlanesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_c__a__c_rgb_a_ = 'rgba'
        self.menu_c__a__c_rgb_a_rgb_ = 'rgba3'
        self.menu_c_____rgb_ = 'rgb'
        self.menu_a = 'a'
        self.menu_a_____rgb_ = 'a3'
        self.menu_m = 'm'
        self.menu_m_____rgb_ = 'm3'
        self.menu_z = 'z'
        self.menu_l = 'l'
        self.menu_b_____uv_ = 'b'
        self.menu_p_____xyz_ = 'p'
        self.menu_n_____xyz_ = 'n'
        self.menu_v_____xyz_ = 'v'
        self.menu_terrain__height = 'terrain_height'
        self.menu_none = 'none'


class AddplanesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_c__a__c_rgb_a_ = 'rgba'
        self.menu_c__a__c_rgb_a_rgb_ = 'rgba3'
        self.menu_c_____rgb_ = 'rgb'
        self.menu_a = 'a'
        self.menu_a_____rgb_ = 'a3'
        self.menu_m = 'm'
        self.menu_m_____rgb_ = 'm3'
        self.menu_z = 'z'
        self.menu_l = 'l'
        self.menu_b_____uv_ = 'b'
        self.menu_p_____xyz_ = 'p'
        self.menu_n_____xyz_ = 'n'
        self.menu_v_____xyz_ = 'v'
        self.menu_terrain__height = 'terrain_height'
        self.menu_none = 'none'


class AddplaneopMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 'replace'
        self.menu_rename = 'rename'
        self.menu_add = 'add'
        self.menu_screen = 'screen'
        self.menu_subtract = 'subtract'
        self.menu_multiply = 'multiply'
        self.menu_min = 'min'
        self.menu_max = 'max'
        self.menu_average = 'avg'


class DepthMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bit_integer_8 = 'int8'
        self.menu_bit_integer_16 = 'int16'
        self.menu_bit_integer_32 = 'int32'
        self.menu_bit_floating_point_16 = 'float16'
        self.menu_bit_floating_point_32 = 'float32'
        self.menu_default_depth = 'default'


class DepthmenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bit_unsigned_8 = 'int8 0 255'
        self.menu_bit_signed_8 = 'int8 128 255'
        self.menu_bit_unsigned_with_5__head_foot_room_8 = 'int8 12 244'
        self.menu_bit_unsigned_with_25__head_foot_room_8 = 'int8 64 192'
        self.menu__separator_ = '_separator_'
        self.menu_bit_unsigned_16 = 'int16 0 65535'
        self.menu_bit_signed_16 = 'int16 32768 65535'
        self.menu_bit_unsigned_with_5__head_foot_room_16 = 'int16 2980 62555'
        self.menu_bit_unsigned_with_25__head_foot_room_16 = 'int16 16384 49152'
        self.menu_bit_extended_8 = 'int16 32640 32895'
        self.menu_bit_full_range_cineon_16 = 'int16 0 4096'
        self.menu__separator_ = '_separator_'
        self.menu_bit_unsigned_32 = 'int32 0 4294967295'
        self.menu_bit_signed_32 = 'int32 2147483648 4294967295'
        self.menu_bit_extended_16 = 'int32 2147450880 2147516415'


class InterlaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = 'none'
        self.menu_half_res_interlaced = 'inthalf'
        self.menu_black_interlaced = 'intblack'
        self.menu_line_doubled = 'intdouble'


class IdominanceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_odd_first = 'odd'
        self.menu_even_first = 'even'
        self.menu_odd_only = 'oddonly'
        self.menu_even_only = 'evenonly'


class PreextendMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_black_frames = 'black'
        self.menu_cycle = 'cycle'
        self.menu_mirror = 'mirror'
        self.menu_hold = 'hold'
        self.menu_hold_n_frames = 'holdn'


class PostextendMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_black_frames = 'black'
        self.menu_cycle = 'cycle'
        self.menu_mirror = 'mirror'
        self.menu_hold = 'hold'
        self.menu_hold_n_frames = 'holdn'



