from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SpriteNode(OXNode):
    node_type = 'redshift::Sprite'
    parm_lookup_dict = {'shader_input_0': 'Shader_Input_0', 'inputr': 'inputr', 'inputg': 'inputg', 'inputb': 'inputb', 'inputa': 'inputa', 'stencil_1': 'Stencil_1', 'tex0': 'tex0', 'tspace_id': 'tspace_id', 'mode': 'mode', 'threshold': 'threshold', 'repeats1': 'repeats1', 'repeats2': 'repeats2', 'tex0_colorspace': 'tex0_colorSpace', 'tex0_gamma': 'tex0_gamma'}

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


class ModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_from_color_intensity = 0
        self.menu_from_alpha = 1


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



