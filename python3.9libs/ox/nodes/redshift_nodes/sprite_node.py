from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SpriteNode(OXNode):
    node_type = 'redshift::Sprite'
    parm_lookup_dict = {'shader_input_0': 'Shader_Input_0', 'inputr': 'inputr', 'inputg': 'inputg', 'inputb': 'inputb', 'inputa': 'inputa', 'stencil_1': 'Stencil_1', 'tex0': 'tex0', 'tspace_id': 'tspace_id', 'mode': 'mode', 'threshold': 'threshold', 'repeats1': 'repeats1', 'repeats2': 'repeats2', 'tex0_colorspace': 'tex0_colorSpace', 'tex0_gamma': 'tex0_gamma', 'shader_skipdefvalparms': 'shader_skipdefvalparms'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_shader_input_0 = Parameter(parm=self.node.parm('Shader_Input_0'))
        self.parm_inputr = Parameter(parm=self.node.parm('inputr'))
        self.parm_inputg = Parameter(parm=self.node.parm('inputg'))
        self.parm_inputb = Parameter(parm=self.node.parm('inputb'))
        self.parm_inputa = Parameter(parm=self.node.parm('inputa'))
        self.parm_stencil_1 = Parameter(parm=self.node.parm('Stencil_1'))
        self.parm_tspace_id = Parameter(parm=self.node.parm('tspace_id'))
        self.parm_threshold = Parameter(parm=self.node.parm('threshold'))
        self.parm_repeats1 = Parameter(parm=self.node.parm('repeats1'))
        self.parm_repeats2 = Parameter(parm=self.node.parm('repeats2'))
        self.parm_tex0_gamma = Parameter(parm=self.node.parm('tex0_gamma'))
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))

        
        # parm menu vars:
        self.parm_tex0 = Tex0Menu(parm=self.node.parm('tex0'))
        self.parm_mode = ModeMenu(parm=self.node.parm('mode'))
        self.parm_tex0_colorspace = Tex0ColorspaceMenu(parm=self.node.parm('tex0_colorSpace'))


        # input vars:
        self.input_input = 'input'


# parm menu classes:
class Tex0Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_projects____a_sunrise_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr"
        self.menu_e__art_projects____anga_veld_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr"
        self.menu_e__art_projects____s_on_fire_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr"
        self.menu_e__art_projects____ly_cloudy_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/kloofendal_48d_partly_cloudy_4k.exr"
        self.menu_e__art_projects____enheim_05_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr"
        self.menu_e__art_projects____quarry_02_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/quarry_02_4k.exr"
        self.menu_e__art_projects_____1d_clear_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr"
        self.menu_e__art_projects____oon_grass_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/noon_grass_4k.exr"
        self.menu_e__art_projects____in_cellar_4k_exr = "E:/ART/PROJECTS/00_shared/hdri/castle_zavelstein_cellar_4k.exr"
        self.menu_e__art_products____ers_tip_mask_jpg = "E:/ART/PRODUCTS/OX-Terrain_Textuers/tip_mask.jpg"
        self.menu_e__art_products____ck_basecolor_jpg = "E:/ART/PRODUCTS/OX-MTLX/multi_texture_folder/green_tiles/wall_tile_unstuck_basecolor.jpg"
        self.menu_e__art_products____ck_basecolor_jpg = "E:/ART/PRODUCTS/OX-MTLX/glazed_terracotta/wall_tile_unstuck_basecolor.jpg"


class ModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_from_color_intensity = "0"
        self.menu_from_alpha = "1"


class Tex0ColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = ""
        self.menu_srgb = "sRGB"
        self.menu_adobergb = "AdobeRGB"
        self.menu_acescg = "ACEScg"
        self.menu_aces2065_1 = "ACES2065-1"
        self.menu_scene_linear_rec_709_srgb = "scene-linear Rec.709-sRGB"
        self.menu_scene_linear_dci_p3_d65 = "scene-linear DCI-P3 D65"
        self.menu_scene_linear_rec_2020 = "scene-linear Rec.2020"
        self.menu_raw = "Raw"
        self.menu_acescct = "ACEScct"
        self.menu_arri_logc___alexawidegamut = "ARRI LogC / AlexaWideGamut"
        self.menu_red_log3g10___redwidegamutrgb = "RED Log3G10 / REDWideGamutRGB"
        self.menu_sony_slog3___sgamut3 = "Sony SLog3 / SGamut3"
        self.menu_panasonic_v_log___v_gamut = "Panasonic V-Log / V-Gamut"
        self.menu_log_film_scan__adx10_ = "Log film scan (ADX10)"
        self.menu_invert_aces_1_0_sdr_video = "Invert ACES 1.0 SDR-video"



