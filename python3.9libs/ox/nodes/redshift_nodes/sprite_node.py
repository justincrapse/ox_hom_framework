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
        self.menu_e__art_old_proje___a_sunrise_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr", 0)
        self.menu_e__art_old_proje___s_on_fire_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr", 1)
        self.menu_d__art_products____s_white_back_jpg = ("D:/ART/PRODUCTS/OX-BIOMES/white_back.jpg", 2)
        self.menu__job_desktop_dop___al_02_2_2000_jpg = ("$JOB/Desktop/dope_backgrounds_6/hole_final_02-2_2000.jpg", 3)
        self.menu_e__quixel_librar___hc_4k_albedo_jpg = ("E:/quixel_library/Downloaded/surface/sand_desert_vd5hfhc/vd5hfhc_4K_Albedo.jpg", 4)
        self.menu_e__art_old_proje___quarry_02_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/quarry_02_4k.exr", 5)
        self.menu_e__art_old_proje___oon_grass_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/noon_grass_4k.exr", 6)
        self.menu_e__art_old_proje___enheim_05_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr", 7)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 8)
        self.menu_e__art_old_proje____1d_clear_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr", 9)
        self.menu_e__art_old_proje___in_cellar_4k_exr = ("E:\ART_OLD\PROJECTS\00_shared\hdri\castle_zavelstein_cellar_4k.exr", 10)
        self.menu_e__quixel_librar____normal_lod0_jpg = ("E:/quixel_library/Downloaded/3d/industrial_construction_vk2nfgu/vk2nfgu_4K_Normal_LOD0.jpg", 11)


class ModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_from_color_intensity = ("0", 0)
        self.menu_from_alpha = ("1", 1)


class Tex0ColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = ("", 0)
        self.menu_srgb = ("sRGB", 1)
        self.menu_adobergb = ("AdobeRGB", 2)
        self.menu_acescg = ("ACEScg", 3)
        self.menu_aces2065_1 = ("ACES2065-1", 4)
        self.menu_scene_linear_rec_709_srgb = ("scene-linear Rec.709-sRGB", 5)
        self.menu_scene_linear_dci_p3_d65 = ("scene-linear DCI-P3 D65", 6)
        self.menu_scene_linear_rec_2020 = ("scene-linear Rec.2020", 7)
        self.menu_raw = ("Raw", 8)
        self.menu_acescct = ("ACEScct", 9)
        self.menu_arri_logc___alexawidegamut = ("ARRI LogC / AlexaWideGamut", 10)
        self.menu_red_log3g10___redwidegamutrgb = ("RED Log3G10 / REDWideGamutRGB", 11)
        self.menu_sony_slog3___sgamut3 = ("Sony SLog3 / SGamut3", 12)
        self.menu_panasonic_v_log___v_gamut = ("Panasonic V-Log / V-Gamut", 13)
        self.menu_log_film_scan__adx10_ = ("Log film scan (ADX10)", 14)
        self.menu_invert_aces_1_0_sdr_video = ("Invert ACES 1.0 SDR-video", 15)



