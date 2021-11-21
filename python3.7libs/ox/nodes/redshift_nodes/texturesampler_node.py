from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class TexturesamplerNode(OXNode):
    node_type = 'redshift::TextureSampler'
    parm_lookup_dict = {'rs_shadernodemainswitcher1': 'RS_shaderNodeMainSwitcher1', 'image_0': 'Image_0', 'tex0': 'tex0', 'tex0_layername': 'tex0_layername', 'tex0_colorspace': 'tex0_colorSpace', 'tex0_gamma': 'tex0_gamma', 'uv_1': 'UV_1', 'tspace_id': 'tspace_id', 'mirroru': 'mirrorU', 'mirrorv': 'mirrorV', 'wrapu': 'wrapU', 'wrapv': 'wrapV', 'remap_2': 'Remap_2', 'scale1': 'scale1', 'scale2': 'scale2', 'offset1': 'offset1', 'offset2': 'offset2', 'rotate': 'rotate', 'color_multiplierr': 'color_multiplierr', 'color_multiplierg': 'color_multiplierg', 'color_multiplierb': 'color_multiplierb', 'color_offsetr': 'color_offsetr', 'color_offsetg': 'color_offsetg', 'color_offsetb': 'color_offsetb', 'alpha_multiplier': 'alpha_multiplier', 'alpha_offset': 'alpha_offset', 'alpha_is_luminance': 'alpha_is_luminance', 'invalid_colorr': 'invalid_colorr', 'invalid_colorg': 'invalid_colorg', 'invalid_colorb': 'invalid_colorb', 'invalid_colora': 'invalid_colora', 'filter_enable_type': 'filter_enable_type', 'filter_bicubic': 'filter_bicubic', 'prefer_sharp': 'prefer_sharp', 'mip_bias': 'mip_bias'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_rs_shadernodemainswitcher1 = Parameter(parm=self.node.parm('RS_shaderNodeMainSwitcher1'))
        self.parm_image_0 = Parameter(parm=self.node.parm('Image_0'))
        self.parm_tex0_layername = Parameter(parm=self.node.parm('tex0_layername'))
        self.parm_tex0_gamma = Parameter(parm=self.node.parm('tex0_gamma'))
        self.parm_uv_1 = Parameter(parm=self.node.parm('UV_1'))
        self.parm_tspace_id = Parameter(parm=self.node.parm('tspace_id'))
        self.parm_mirroru = Parameter(parm=self.node.parm('mirrorU'))
        self.parm_mirrorv = Parameter(parm=self.node.parm('mirrorV'))
        self.parm_wrapu = Parameter(parm=self.node.parm('wrapU'))
        self.parm_wrapv = Parameter(parm=self.node.parm('wrapV'))
        self.parm_remap_2 = Parameter(parm=self.node.parm('Remap_2'))
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
        self.parm_tex0 = Tex0Menu(parm=self.node.parm('tex0'))
        self.parm_tex0_colorspace = Tex0ColorspaceMenu(parm=self.node.parm('tex0_colorSpace'))
        self.parm_filter_enable_type = FilterEnableTypeMenu(parm=self.node.parm('filter_enable_type'))


        # input vars:
        self.input_scale = 'scale'
        self.input_offset = 'offset'
        self.input_rotate = 'rotate'
        self.input_color_multiplier = 'color_multiplier'
        self.input_color_offset = 'color_offset'
        self.input_alpha_multiplier = 'alpha_multiplier'
        self.input_alpha_offset = 'alpha_offset'
        self.input_invalid_color = 'invalid_color'


# parm menu classes:
class Tex0Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_projects____anga_veld_4k_exr = 0
        self.menu_e__art_3d_00_my____ring_opacity_png = 1
        self.menu_e__art_projects____ly_cloudy_4k_exr = 2
        self.menu_e__art_projects_____1d_clear_4k_exr = 3
        self.menu_op__opfullpath______gen_displace___ = 4
        self.menu_op__opfullpath__________ocean_s____ = 5
        self.menu_op__opfullpath_____ean_interior____ = 6
        self.menu_e__art_3d_eucaly___ark_3_height_png = 7
        self.menu_e__art_projects____quarry_02_4k_exr = 8
        self.menu_e__art_projects____a_sunrise_4k_exr = 9
        self.menu_e__art_projects____in_cellar_4k_exr = 10
        self.menu_e__art_projects____oon_grass_4k_exr = 11


class Tex0ColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = 0
        self.menu_srgb = 1
        self.menu_adobergb = 2
        self.menu_acescg = 3
        self.menu_aces2065_1 = 4
        self.menu_scene_linear_rec_709_srgb = 5
        self.menu_scene_linear_dci_p3_d65 = 6
        self.menu_scene_linear_rec_2020 = 7
        self.menu_raw = 8
        self.menu_acescct = 9
        self.menu_arri_logc___alexawidegamut = 10
        self.menu_red_log3g10___redwidegamutrgb = 11
        self.menu_sony_slog3___sgamut3 = 12
        self.menu_panasonic_v_log___v_gamut = 13
        self.menu_log_film_scan__adx10_ = 14
        self.menu_invert_aces_1_0_sdr_video = 15


class FilterEnableTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = 0
        self.menu_magnification = 1
        self.menu_magnification_minification = 2



