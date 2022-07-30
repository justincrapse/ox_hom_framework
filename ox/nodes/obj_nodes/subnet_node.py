from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SubnetNode(OXNode):
    node_type = 'subnet'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz', 'scale': 'scale', 'pre_xform': 'pre_xform', 'keeppos': 'keeppos', 'childcomp': 'childcomp', 'constraints_on': 'constraints_on', 'constraints_path': 'constraints_path', 'lookatpath': 'lookatpath', 'lookupobjpath': 'lookupobjpath', 'lookup': 'lookup', 'pathobjpath': 'pathobjpath', 'roll': 'roll', 'pos': 'pos', 'uparmtype': 'uparmtype', 'pathorient': 'pathorient', 'upx': 'upx', 'upy': 'upy', 'upz': 'upz', 'bank': 'bank', 'label1': 'label1', 'label2': 'label2', 'label3': 'label3', 'label4': 'label4', 'tdisplay': 'tdisplay', 'display': 'display', 'outputobj': 'outputobj', 'visibleobjects': 'visibleobjects', 'picking': 'picking', 'pickscript': 'pickscript', 'caching': 'caching', 'use_dcolor': 'use_dcolor', 'dcolorr': 'dcolorr', 'dcolorg': 'dcolorg', 'dcolorb': 'dcolorb'}

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
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_sx = Parameter(parm=self.node.parm('sx'))
        self.parm_sy = Parameter(parm=self.node.parm('sy'))
        self.parm_sz = Parameter(parm=self.node.parm('sz'))
        self.parm_px = Parameter(parm=self.node.parm('px'))
        self.parm_py = Parameter(parm=self.node.parm('py'))
        self.parm_pz = Parameter(parm=self.node.parm('pz'))
        self.parm_prx = Parameter(parm=self.node.parm('prx'))
        self.parm_pry = Parameter(parm=self.node.parm('pry'))
        self.parm_prz = Parameter(parm=self.node.parm('prz'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_keeppos = Parameter(parm=self.node.parm('keeppos'))
        self.parm_childcomp = Parameter(parm=self.node.parm('childcomp'))
        self.parm_constraints_on = Parameter(parm=self.node.parm('constraints_on'))
        self.parm_constraints_path = Parameter(parm=self.node.parm('constraints_path'))
        self.parm_lookatpath = Parameter(parm=self.node.parm('lookatpath'))
        self.parm_lookupobjpath = Parameter(parm=self.node.parm('lookupobjpath'))
        self.parm_pathobjpath = Parameter(parm=self.node.parm('pathobjpath'))
        self.parm_roll = Parameter(parm=self.node.parm('roll'))
        self.parm_pos = Parameter(parm=self.node.parm('pos'))
        self.parm_pathorient = Parameter(parm=self.node.parm('pathorient'))
        self.parm_upx = Parameter(parm=self.node.parm('upx'))
        self.parm_upy = Parameter(parm=self.node.parm('upy'))
        self.parm_upz = Parameter(parm=self.node.parm('upz'))
        self.parm_bank = Parameter(parm=self.node.parm('bank'))
        self.parm_label1 = Parameter(parm=self.node.parm('label1'))
        self.parm_label2 = Parameter(parm=self.node.parm('label2'))
        self.parm_label3 = Parameter(parm=self.node.parm('label3'))
        self.parm_label4 = Parameter(parm=self.node.parm('label4'))
        self.parm_tdisplay = Parameter(parm=self.node.parm('tdisplay'))
        self.parm_display = Parameter(parm=self.node.parm('display'))
        self.parm_picking = Parameter(parm=self.node.parm('picking'))
        self.parm_caching = Parameter(parm=self.node.parm('caching'))
        self.parm_use_dcolor = Parameter(parm=self.node.parm('use_dcolor'))
        self.parm_dcolorr = Parameter(parm=self.node.parm('dcolorr'))
        self.parm_dcolorg = Parameter(parm=self.node.parm('dcolorg'))
        self.parm_dcolorb = Parameter(parm=self.node.parm('dcolorb'))

        
        # parm menu vars:
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))
        self.parm_pre_xform = PreXformMenu(parm=self.node.parm('pre_xform'))
        self.parm_lookup = LookupMenu(parm=self.node.parm('lookup'))
        self.parm_uparmtype = UparmtypeMenu(parm=self.node.parm('uparmtype'))
        self.parm_outputobj = OutputobjMenu(parm=self.node.parm('outputobj'))
        self.parm_visibleobjects = VisibleobjectsMenu(parm=self.node.parm('visibleobjects'))
        self.parm_pickscript = PickscriptMenu(parm=self.node.parm('pickscript'))


        # input vars:
        self.input_sub_network_input__1 = 'Sub-Network Input #1'
        self.input_sub_network_input__2 = 'Sub-Network Input #2'
        self.input_sub_network_input__3 = 'Sub-Network Input #3'
        self.input_sub_network_input__4 = 'Sub-Network Input #4'


# parm menu classes:
class XordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_rot_trans = 'srt'
        self.menu_scale_trans_rot = 'str'
        self.menu_rot_scale_trans = 'rst'
        self.menu_rot_trans_scale = 'rts'
        self.menu_trans_scale_rot = 'tsr'
        self.menu_trans_rot_scale = 'trs'


class RordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rx_ry_rz = 'xyz'
        self.menu_rx_rz_ry = 'xzy'
        self.menu_ry_rx_rz = 'yxz'
        self.menu_ry_rz_rx = 'yzx'
        self.menu_rz_rx_ry = 'zxy'
        self.menu_rz_ry_rx = 'zyx'


class PreXformMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_clean_transform = 'clean'
        self.menu_clean_translates = 'cleantrans'
        self.menu_clean_rotates = 'cleanrot'
        self.menu_clean_scales = 'cleanscales'
        self.menu_extract_pre_transform = 'extract'
        self.menu_reset_pre_transform = 'reset'


class LookupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_don_t_use_up_vector = 'off'
        self.menu_use_up_vector = 'on'
        self.menu_use_quaternions = 'quat'
        self.menu_use_global_position = 'pos'
        self.menu_use_up_object = 'obj'


class UparmtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uniform = 'uniform'
        self.menu_arc_length = 'arc'


class OutputobjMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_object = ''
        self.menu_input_object_1 = '_input1_obj_'
        self.menu_input_object_2 = '_input2_obj_'
        self.menu_input_object_3 = '_input3_obj_'
        self.menu_input_object_4 = '_input4_obj_'
        self.menu__separator_ = '_separator_'


class VisibleobjectsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_bundles_defined = ''


class PickscriptMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__job_desktop_articulatcf_bold_otf = '$JOB/Desktop/ArticulatCF-Bold.otf'
        self.menu__hip_desktop_articulatcf_bold_otf = '$HIP/Desktop/ArticulatCF-Bold.otf'
        self.menu_e__art_products_ox_mtlx_hf_test_out = 'E:/ART/PRODUCTS/OX-MTLX/hf_test_out'
        self.menu_d__minecraft_sub___ded_copper_sbsar = 'D:/Minecraft/substance/hazelnut_3/copper_block/grinded_copper.sbsar'
        self.menu_d__minecraft_sub___dirt_field_sbsar = 'D:/Minecraft/substance/hazelnut/farmland_wet/arid_dirt_field.sbsar'
        self.menu_e__art_products____ers_rock_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_cpu.jpg'
        self.menu_e__art_products____ers_rock_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_xpu.jpg'
        self.menu_e__art_products____rs_quilt_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_xpu.jpg'
        self.menu_e__art_products____rs_quilt_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_cpu.jpg'
        self.menu_e__art_products____ers_lava_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_cpu.jpg'
        self.menu_e__art_products____ers_lava_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_xpu.jpg'
        self.menu_e__art_products____s_glazed_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_xpu.jpg'



