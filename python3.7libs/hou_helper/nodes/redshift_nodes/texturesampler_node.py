from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class TexturesamplerNode(HHNode):
    node_type = 'redshift::TextureSampler'
    parm_lookup_dict = {'rs_shadernodemainswitcher1': 'RS_shaderNodeMainSwitcher1', 'image_0': 'Image_0', 'tex0': 'tex0', 'tex0_layername': 'tex0_layername', 'tex0_colorspace': 'tex0_colorSpace', 'tex0_gamma': 'tex0_gamma', 'uv_1': 'UV_1', 'tspace_id': 'tspace_id', 'mirroru': 'mirrorU', 'mirrorv': 'mirrorV', 'wrapu': 'wrapU', 'wrapv': 'wrapV', 'remap_2': 'Remap_2', 'scale1': 'scale1', 'scale2': 'scale2', 'offset1': 'offset1', 'offset2': 'offset2', 'rotate': 'rotate', 'color_multiplierr': 'color_multiplierr', 'color_multiplierg': 'color_multiplierg', 'color_multiplierb': 'color_multiplierb', 'color_offsetr': 'color_offsetr', 'color_offsetg': 'color_offsetg', 'color_offsetb': 'color_offsetb', 'alpha_multiplier': 'alpha_multiplier', 'alpha_offset': 'alpha_offset', 'alpha_is_luminance': 'alpha_is_luminance', 'invalid_colorr': 'invalid_colorr', 'invalid_colorg': 'invalid_colorg', 'invalid_colorb': 'invalid_colorb', 'invalid_colora': 'invalid_colora', 'filter_enable_type': 'filter_enable_type', 'filter_bicubic': 'filter_bicubic', 'prefer_sharp': 'prefer_sharp', 'mip_bias': 'mip_bias'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_rs_shadernodemainswitcher1 = Parameter(parm=self.node.parm('rs_shadernodemainswitcher1'))
        self.parm_image_0 = Parameter(parm=self.node.parm('image_0'))
        self.parm_tex0_layername = Parameter(parm=self.node.parm('tex0_layername'))
        self.parm_tex0_gamma = Parameter(parm=self.node.parm('tex0_gamma'))
        self.parm_uv_1 = Parameter(parm=self.node.parm('uv_1'))
        self.parm_tspace_id = Parameter(parm=self.node.parm('tspace_id'))
        self.parm_mirroru = Parameter(parm=self.node.parm('mirroru'))
        self.parm_mirrorv = Parameter(parm=self.node.parm('mirrorv'))
        self.parm_wrapu = Parameter(parm=self.node.parm('wrapu'))
        self.parm_wrapv = Parameter(parm=self.node.parm('wrapv'))
        self.parm_remap_2 = Parameter(parm=self.node.parm('remap_2'))
        self.parm_scale1 = Parameter(parm=self.node.parm('scale1'))
        self.parm_scale2 = Parameter(parm=self.node.parm('scale2'))
        self.parm_offset1 = Parameter(parm=self.node.parm('offset1'))
        self.parm_offset2 = Parameter(parm=self.node.parm('offset2'))
        self.parm_rotate = Parameter(parm=self.node.parm('rotate'))
        self.parm_color_multiplierr = Parameter(parm=self.node.parm('color_multiplierr'))
        self.parm_color_multiplierg = Parameter(parm=self.node.parm('color_multiplierg'))
        self.parm_color_multiplierb = Parameter(parm=self.node.parm('color_multiplierb'))
        self.parm_color_offsetr = Parameter(parm=self.node.parm('color_offsetr'))
        self.parm_color_offsetg = Parameter(parm=self.node.parm('color_offsetg'))
        self.parm_color_offsetb = Parameter(parm=self.node.parm('color_offsetb'))
        self.parm_alpha_multiplier = Parameter(parm=self.node.parm('alpha_multiplier'))
        self.parm_alpha_offset = Parameter(parm=self.node.parm('alpha_offset'))
        self.parm_alpha_is_luminance = Parameter(parm=self.node.parm('alpha_is_luminance'))
        self.parm_invalid_colorr = Parameter(parm=self.node.parm('invalid_colorr'))
        self.parm_invalid_colorg = Parameter(parm=self.node.parm('invalid_colorg'))
        self.parm_invalid_colorb = Parameter(parm=self.node.parm('invalid_colorb'))
        self.parm_invalid_colora = Parameter(parm=self.node.parm('invalid_colora'))
        self.parm_filter_bicubic = Parameter(parm=self.node.parm('filter_bicubic'))
        self.parm_prefer_sharp = Parameter(parm=self.node.parm('prefer_sharp'))
        self.parm_mip_bias = Parameter(parm=self.node.parm('mip_bias'))

        
        # parm menu vars:
        self.parm_tex0_menu = Tex0Menu(parm=self.node.parm('tex0'))
        self.parm_tex0_colorspace_menu = Tex0ColorspaceMenu(parm=self.node.parm('tex0_colorSpace'))
        self.parm_filter_enable_type_menu = FilterEnableTypeMenu(parm=self.node.parm('filter_enable_type'))


        # input vars:
        self.input_scale = 0
        self.input_offset = 1
        self.input_rotate = 2
        self.input_color_multiplier = 3
        self.input_color_offset = 4
        self.input_alpha_multiplier = 5
        self.input_alpha_offset = 6
        self.input_invalid_color = 7


# parm menu classes:
class Tex0Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.e__art_projects____in_cellar_4k_exr = 0
        self.e__art_projects____oon_grass_4k_exr = 1
        self.e__art_3d_from_t___urfaceamount_png = 2
        self.e__art_3d_from_t___rfaceamount2_png = 3
        self.e__art_3d_from_t___surfacecolor_png = 4
        self.e__art_3d_from_t___af_1_opacity_png = 5
        self.e__art_3d_from_t___eaf_1_normal_png = 6
        self.e__art_3d_from_t___leaf_1_gloss_png = 7
        self.e__art_3d_from_t___te_leaf_1_ao_png = 8
        self.e__art_3d_from_template_leaf_1_png = 9
        self.e__art_3d_from_t___f___f__gloss_png = 10
        self.e__art_3d_from_t___leaf___f__ao_png = 11


class Tex0ColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.auto = 0
        self.srgb = 1
        self.adobergb = 2
        self.acescg = 3
        self.aces2065_1 = 4
        self.scene_linear_rec_709_srgb = 5
        self.scene_linear_dci_p3_d65 = 6
        self.scene_linear_rec_2020 = 7
        self.raw = 8
        self.acescct = 9
        self.arri_logc___alexawidegamut = 10
        self.red_log3g10___redwidegamutrgb = 11
        self.sony_slog3___sgamut3 = 12
        self.panasonic_v_log___v_gamut = 13
        self.log_film_scan__adx10_ = 14
        self.invert_aces_1_0_sdr_video = 15


class FilterEnableTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.none = 0
        self.magnification = 1
        self.magnification_minification = 2



