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
        self.menu_no_mask_input = 0


class SizemenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_480_640 = 0
        self.menu_hdtv_720 = 1
        self.menu_hdtv_1080 = 2
        self.menu_hdtv_2160__4k_ = 3
        self.menu__________ = 4
        self.menu_ntsc = 5
        self.menu_ntsc_d1 = 6
        self.menu_pal = 7
        self.menu_pal_d1 = 8
        self.menu_pal_16_9_anamorphic = 9
        self.menu_pal_16_9__1_to_1_ = 10
        self.menu__________ = 11
        self.menu_full_ap_4k = 12
        self.menu_full_ap_2k = 13
        self.menu_acad_4k = 14
        self.menu_acad_2k = 15
        self.menu_scope_4k = 16
        self.menu_scope_2k = 17
        self.menu_vista_4k = 18
        self.menu_vista_2k = 19
        self.menu__________ = 20
        self.menu__2_256 = 21
        self.menu__2_512 = 22
        self.menu__2_1024 = 23
        self.menu__2_2048 = 24
        self.menu__2_4096 = 25
        self.menu__2_8192 = 26
        self.menu_x_480_640 = 27
        self.menu_hdtv_720 = 28
        self.menu_hdtv_1080 = 29
        self.menu_hdtv_2160__4k_ = 30
        self.menu__________ = 31
        self.menu_ntsc = 32
        self.menu_ntsc_d1 = 33
        self.menu_pal = 34
        self.menu_pal_d1 = 35
        self.menu_pal_16_9_anamorphic = 36
        self.menu_pal_16_9__1_to_1_ = 37
        self.menu__________ = 38
        self.menu_full_ap_4k = 39
        self.menu_full_ap_2k = 40
        self.menu_acad_4k = 41
        self.menu_acad_2k = 42
        self.menu_scope_4k = 43
        self.menu_scope_2k = 44
        self.menu_vista_4k = 45
        self.menu_vista_2k = 46
        self.menu__________ = 47
        self.menu__2_256 = 48
        self.menu__2_512 = 49
        self.menu__2_1024 = 50
        self.menu__2_2048 = 51
        self.menu__2_4096 = 52
        self.menu__2_8192 = 53


class PlanesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_c__a__c_rgb_a_ = 0
        self.menu_c__a__c_rgb_a_rgb_ = 1
        self.menu_c_____rgb_ = 2
        self.menu_a = 3
        self.menu_a_____rgb_ = 4
        self.menu_m = 5
        self.menu_m_____rgb_ = 6
        self.menu_z = 7
        self.menu_l = 8
        self.menu_b_____uv_ = 9
        self.menu_p_____xyz_ = 10
        self.menu_n_____xyz_ = 11
        self.menu_v_____xyz_ = 12
        self.menu_terrain__height = 13
        self.menu_none = 14


class AddplanesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_c__a__c_rgb_a_ = 0
        self.menu_c__a__c_rgb_a_rgb_ = 1
        self.menu_c_____rgb_ = 2
        self.menu_a = 3
        self.menu_a_____rgb_ = 4
        self.menu_m = 5
        self.menu_m_____rgb_ = 6
        self.menu_z = 7
        self.menu_l = 8
        self.menu_b_____uv_ = 9
        self.menu_p_____xyz_ = 10
        self.menu_n_____xyz_ = 11
        self.menu_v_____xyz_ = 12
        self.menu_terrain__height = 13
        self.menu_none = 14


class AddplaneopMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_rename = 1
        self.menu_add = 2
        self.menu_screen = 3
        self.menu_subtract = 4
        self.menu_multiply = 5
        self.menu_min = 6
        self.menu_max = 7
        self.menu_average = 8


class DepthMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bit_integer_8 = 0
        self.menu_bit_integer_16 = 1
        self.menu_bit_integer_32 = 2
        self.menu_bit_floating_point_16 = 3
        self.menu_bit_floating_point_32 = 4
        self.menu_default_depth = 5


class DepthmenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bit_unsigned_8 = 0
        self.menu_bit_signed_8 = 1
        self.menu_bit_unsigned_with_5__head_foot_room_8 = 2
        self.menu_bit_unsigned_with_25__head_foot_room_8 = 3
        self.menu__separator_ = 4
        self.menu_bit_unsigned_16 = 5
        self.menu_bit_signed_16 = 6
        self.menu_bit_unsigned_with_5__head_foot_room_16 = 7
        self.menu_bit_unsigned_with_25__head_foot_room_16 = 8
        self.menu_bit_extended_8 = 9
        self.menu_bit_full_range_cineon_16 = 10
        self.menu__separator_ = 11
        self.menu_bit_unsigned_32 = 12
        self.menu_bit_signed_32 = 13
        self.menu_bit_extended_16 = 14
        self.menu_bit_unsigned_8 = 15
        self.menu_bit_signed_8 = 16
        self.menu_bit_unsigned_with_5__head_foot_room_8 = 17
        self.menu_bit_unsigned_with_25__head_foot_room_8 = 18
        self.menu__separator_ = 19
        self.menu_bit_unsigned_16 = 20
        self.menu_bit_signed_16 = 21
        self.menu_bit_unsigned_with_5__head_foot_room_16 = 22
        self.menu_bit_unsigned_with_25__head_foot_room_16 = 23
        self.menu_bit_extended_8 = 24
        self.menu_bit_full_range_cineon_16 = 25
        self.menu__separator_ = 26
        self.menu_bit_unsigned_32 = 27
        self.menu_bit_signed_32 = 28
        self.menu_bit_extended_16 = 29


class InterlaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = 0
        self.menu_half_res_interlaced = 1
        self.menu_black_interlaced = 2
        self.menu_line_doubled = 3


class IdominanceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_odd_first = 0
        self.menu_even_first = 1
        self.menu_odd_only = 2
        self.menu_even_only = 3


class PreextendMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_black_frames = 0
        self.menu_cycle = 1
        self.menu_mirror = 2
        self.menu_hold = 3
        self.menu_hold_n_frames = 4


class PostextendMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_black_frames = 0
        self.menu_cycle = 1
        self.menu_mirror = 2
        self.menu_hold = 3
        self.menu_hold_n_frames = 4



