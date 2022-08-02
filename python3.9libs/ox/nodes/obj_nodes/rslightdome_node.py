from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RslightdomeNode(OXNode):
    node_type = 'rslightdome::2.0'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz', 'scale': 'scale', 'pre_xform': 'pre_xform', 'keeppos': 'keeppos', 'childcomp': 'childcomp', 'constraints_on': 'constraints_on', 'constraints_path': 'constraints_path', 'lookatpath': 'lookatpath', 'lookupobjpath': 'lookupobjpath', 'lookup': 'lookup', 'pathobjpath': 'pathobjpath', 'roll': 'roll', 'pos': 'pos', 'uparmtype': 'uparmtype', 'pathorient': 'pathorient', 'upx': 'upx', 'upy': 'upy', 'upz': 'upz', 'bank': 'bank', 'tdisplay': 'tdisplay', 'display': 'display', 'dimmer': 'dimmer', 'picking': 'picking', 'pickscript': 'pickscript', 'caching': 'caching', 'use_dcolor': 'use_dcolor', 'dcolorr': 'dcolorr', 'dcolorg': 'dcolorg', 'dcolorb': 'dcolorb', 'folder01': 'folder01', 'folder1_21': 'folder1_21', 'l_iconscale': 'l_iconscale', 'folder3': 'folder3', 'light_enabled': 'light_enabled', 'on': 'on', 'ogl_enablelight': 'ogl_enablelight', 'rs_shadernodemainswitcher': 'RS_shaderNodeMainSwitcher', 'light_intensity': 'light_intensity', 'rsl_exposure': 'RSL_exposure', 'light_colorr': 'light_colorr', 'light_colorg': 'light_colorg', 'light_colorb': 'light_colorb', 'env_map': 'env_map', 'envtype': 'envType', 'tex0_colorspace': 'tex0_colorSpace', 'rsl_fliphorizontal': 'RSL_flipHorizontal', 'rsl_hue': 'RSL_hue', 'rsl_saturation': 'RSL_saturation', 'tex0_gamma': 'tex0_gamma', 'environment_alpha_channel_replace_2': 'Environment_Alpha_Channel_Replace_2', 'background_enable': 'background_enable', 'alphareplaceenable': 'alphaReplaceEnable', 'alphareplacevalue': 'alphaReplaceValue', 'rs_shadernodemainswitcher_1': 'RS_shaderNodeMainSwitcher_1', 'backplateenabled': 'backPlateEnabled', 'tex1': 'tex1', 'tex1_colorspace': 'tex1_colorSpace', 'tex1_gamma': 'tex1_gamma', 'rsl_exposure2': 'RSL_exposure2', 'rsl_hue2': 'RSL_hue2', 'rsl_saturation2': 'RSL_saturation2', 'backplateaspect': 'backPlateAspect', 'applyexposurecompensation': 'applyExposureCompensation', 'folder1': 'folder1', 'rsl_lightgroup': 'RSL_lightGroup', 'shadow_1': 'Shadow_1', 'shadow': 'shadow', 'shadowtransparency': 'shadowTransparency', 'folder2': 'folder2', 'rsl_affectdiffuse': 'RSL_affectDiffuse', 'rsl_affectspecular': 'RSL_affectSpecular', 'rsl_matteshadow': 'RSL_matteShadow', 'rsl_affectedbyrefraction': 'RSL_affectedByRefraction', 'rsl_indirectmaxtracedepth': 'RSL_indirectMaxTraceDepth', 'rsl_samples': 'RSL_samples', 'rsl_volumesamples': 'RSL_volumeSamples', 'rsl_diffusescale': 'RSL_diffuseScale', 'rsl_specularscale': 'RSL_specularScale', 'rsl_reflectionscale': 'RSL_reflectionScale', 'rsl_transmissionscale': 'RSL_transmissionScale', 'rsl_sssscale': 'RSL_sssScale', 'rsl_multisssscale': 'RSL_multisssScale', 'rsl_indirectscale': 'RSL_indirectScale', 'rsl_volumescale': 'RSL_volumeScale', 'folder5': 'folder5', 'folder7': 'folder7', 'rsl_emitcausticphotons': 'RSL_emitCausticPhotons', 'rsl_causticintensity': 'RSL_causticIntensity', 'rsl_causticphotons': 'RSL_causticPhotons', 'rsl_setinclusive': 'RSL_setInclusive', 'rsl_lightlinking': 'RSL_lightLinking', 'rsl_shadowlinking': 'RSL_shadowLinking', 'folder8': 'folder8', 'rsl_emitgiphotons': 'RSL_emitGIPhotons', 'rsl_giintensity': 'RSL_giIntensity', 'rsl_giphotons': 'RSL_giPhotons', 'light_enable': 'light_enable', 'shadow_type': 'shadow_type', 'gamma0': 'gamma0', 'gamma_override_0': 'Gamma_Override_0', 'tex0_gammaoverride': 'tex0_gammaoverride', 'tex0_srgb': 'tex0_srgb', 'gamma1': 'gamma1', 'gamma_override_3': 'Gamma_Override_3', 'tex1_gammaoverride': 'tex1_gammaoverride', 'tex1_srgb': 'tex1_srgb'}

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
        self.parm_tdisplay = Parameter(parm=self.node.parm('tdisplay'))
        self.parm_display = Parameter(parm=self.node.parm('display'))
        self.parm_dimmer = Parameter(parm=self.node.parm('dimmer'))
        self.parm_picking = Parameter(parm=self.node.parm('picking'))
        self.parm_pickscript = Parameter(parm=self.node.parm('pickscript'))
        self.parm_caching = Parameter(parm=self.node.parm('caching'))
        self.parm_use_dcolor = Parameter(parm=self.node.parm('use_dcolor'))
        self.parm_dcolorr = Parameter(parm=self.node.parm('dcolorr'))
        self.parm_dcolorg = Parameter(parm=self.node.parm('dcolorg'))
        self.parm_dcolorb = Parameter(parm=self.node.parm('dcolorb'))
        self.parm_folder01 = Parameter(parm=self.node.parm('folder01'))
        self.parm_folder1_21 = Parameter(parm=self.node.parm('folder1_21'))
        self.parm_l_iconscale = Parameter(parm=self.node.parm('l_iconscale'))
        self.parm_folder3 = Parameter(parm=self.node.parm('folder3'))
        self.parm_light_enabled = Parameter(parm=self.node.parm('light_enabled'))
        self.parm_on = Parameter(parm=self.node.parm('on'))
        self.parm_ogl_enablelight = Parameter(parm=self.node.parm('ogl_enablelight'))
        self.parm_rs_shadernodemainswitcher = Parameter(parm=self.node.parm('RS_shaderNodeMainSwitcher'))
        self.parm_light_intensity = Parameter(parm=self.node.parm('light_intensity'))
        self.parm_rsl_exposure = Parameter(parm=self.node.parm('RSL_exposure'))
        self.parm_light_colorr = Parameter(parm=self.node.parm('light_colorr'))
        self.parm_light_colorg = Parameter(parm=self.node.parm('light_colorg'))
        self.parm_light_colorb = Parameter(parm=self.node.parm('light_colorb'))
        self.parm_env_map = Parameter(parm=self.node.parm('env_map'))
        self.parm_rsl_fliphorizontal = Parameter(parm=self.node.parm('RSL_flipHorizontal'))
        self.parm_rsl_hue = Parameter(parm=self.node.parm('RSL_hue'))
        self.parm_rsl_saturation = Parameter(parm=self.node.parm('RSL_saturation'))
        self.parm_tex0_gamma = Parameter(parm=self.node.parm('tex0_gamma'))
        self.parm_environment_alpha_channel_replace_2 = Parameter(parm=self.node.parm('Environment_Alpha_Channel_Replace_2'))
        self.parm_background_enable = Parameter(parm=self.node.parm('background_enable'))
        self.parm_alphareplaceenable = Parameter(parm=self.node.parm('alphaReplaceEnable'))
        self.parm_alphareplacevalue = Parameter(parm=self.node.parm('alphaReplaceValue'))
        self.parm_rs_shadernodemainswitcher_1 = Parameter(parm=self.node.parm('RS_shaderNodeMainSwitcher_1'))
        self.parm_backplateenabled = Parameter(parm=self.node.parm('backPlateEnabled'))
        self.parm_tex1 = Parameter(parm=self.node.parm('tex1'))
        self.parm_tex1_gamma = Parameter(parm=self.node.parm('tex1_gamma'))
        self.parm_rsl_exposure2 = Parameter(parm=self.node.parm('RSL_exposure2'))
        self.parm_rsl_hue2 = Parameter(parm=self.node.parm('RSL_hue2'))
        self.parm_rsl_saturation2 = Parameter(parm=self.node.parm('RSL_saturation2'))
        self.parm_applyexposurecompensation = Parameter(parm=self.node.parm('applyExposureCompensation'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_rsl_lightgroup = Parameter(parm=self.node.parm('RSL_lightGroup'))
        self.parm_shadow_1 = Parameter(parm=self.node.parm('Shadow_1'))
        self.parm_shadow = Parameter(parm=self.node.parm('shadow'))
        self.parm_shadowtransparency = Parameter(parm=self.node.parm('shadowTransparency'))
        self.parm_folder2 = Parameter(parm=self.node.parm('folder2'))
        self.parm_rsl_affectdiffuse = Parameter(parm=self.node.parm('RSL_affectDiffuse'))
        self.parm_rsl_affectspecular = Parameter(parm=self.node.parm('RSL_affectSpecular'))
        self.parm_rsl_matteshadow = Parameter(parm=self.node.parm('RSL_matteShadow'))
        self.parm_rsl_indirectmaxtracedepth = Parameter(parm=self.node.parm('RSL_indirectMaxTraceDepth'))
        self.parm_rsl_samples = Parameter(parm=self.node.parm('RSL_samples'))
        self.parm_rsl_volumesamples = Parameter(parm=self.node.parm('RSL_volumeSamples'))
        self.parm_rsl_diffusescale = Parameter(parm=self.node.parm('RSL_diffuseScale'))
        self.parm_rsl_specularscale = Parameter(parm=self.node.parm('RSL_specularScale'))
        self.parm_rsl_reflectionscale = Parameter(parm=self.node.parm('RSL_reflectionScale'))
        self.parm_rsl_transmissionscale = Parameter(parm=self.node.parm('RSL_transmissionScale'))
        self.parm_rsl_sssscale = Parameter(parm=self.node.parm('RSL_sssScale'))
        self.parm_rsl_multisssscale = Parameter(parm=self.node.parm('RSL_multisssScale'))
        self.parm_rsl_indirectscale = Parameter(parm=self.node.parm('RSL_indirectScale'))
        self.parm_rsl_volumescale = Parameter(parm=self.node.parm('RSL_volumeScale'))
        self.parm_folder5 = Parameter(parm=self.node.parm('folder5'))
        self.parm_folder7 = Parameter(parm=self.node.parm('folder7'))
        self.parm_rsl_emitcausticphotons = Parameter(parm=self.node.parm('RSL_emitCausticPhotons'))
        self.parm_rsl_causticintensity = Parameter(parm=self.node.parm('RSL_causticIntensity'))
        self.parm_rsl_causticphotons = Parameter(parm=self.node.parm('RSL_causticPhotons'))
        self.parm_rsl_setinclusive = Parameter(parm=self.node.parm('RSL_setInclusive'))
        self.parm_rsl_lightlinking = Parameter(parm=self.node.parm('RSL_lightLinking'))
        self.parm_rsl_shadowlinking = Parameter(parm=self.node.parm('RSL_shadowLinking'))
        self.parm_folder8 = Parameter(parm=self.node.parm('folder8'))
        self.parm_rsl_emitgiphotons = Parameter(parm=self.node.parm('RSL_emitGIPhotons'))
        self.parm_rsl_giintensity = Parameter(parm=self.node.parm('RSL_giIntensity'))
        self.parm_rsl_giphotons = Parameter(parm=self.node.parm('RSL_giPhotons'))
        self.parm_light_enable = Parameter(parm=self.node.parm('light_enable'))
        self.parm_shadow_type = Parameter(parm=self.node.parm('shadow_type'))
        self.parm_gamma0 = Parameter(parm=self.node.parm('gamma0'))
        self.parm_gamma_override_0 = Parameter(parm=self.node.parm('Gamma_Override_0'))
        self.parm_tex0_gammaoverride = Parameter(parm=self.node.parm('tex0_gammaoverride'))
        self.parm_tex0_srgb = Parameter(parm=self.node.parm('tex0_srgb'))
        self.parm_gamma1 = Parameter(parm=self.node.parm('gamma1'))
        self.parm_gamma_override_3 = Parameter(parm=self.node.parm('Gamma_Override_3'))
        self.parm_tex1_gammaoverride = Parameter(parm=self.node.parm('tex1_gammaoverride'))
        self.parm_tex1_srgb = Parameter(parm=self.node.parm('tex1_srgb'))

        
        # parm menu vars:
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))
        self.parm_pre_xform = PreXformMenu(parm=self.node.parm('pre_xform'))
        self.parm_lookup = LookupMenu(parm=self.node.parm('lookup'))
        self.parm_uparmtype = UparmtypeMenu(parm=self.node.parm('uparmtype'))
        self.parm_envtype = EnvtypeMenu(parm=self.node.parm('envType'))
        self.parm_tex0_colorspace = Tex0ColorspaceMenu(parm=self.node.parm('tex0_colorSpace'))
        self.parm_tex1_colorspace = Tex1ColorspaceMenu(parm=self.node.parm('tex1_colorSpace'))
        self.parm_backplateaspect = BackplateaspectMenu(parm=self.node.parm('backPlateAspect'))
        self.parm_rsl_affectedbyrefraction = RslAffectedbyrefractionMenu(parm=self.node.parm('RSL_affectedByRefraction'))


        # input vars:
        self.input_sub_network_input__1 = 'Sub-Network Input #1'


# parm menu classes:
class XordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_rot_trans = "srt"
        self.menu_scale_trans_rot = "str"
        self.menu_rot_scale_trans = "rst"
        self.menu_rot_trans_scale = "rts"
        self.menu_trans_scale_rot = "tsr"
        self.menu_trans_rot_scale = "trs"


class RordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rx_ry_rz = "xyz"
        self.menu_rx_rz_ry = "xzy"
        self.menu_ry_rx_rz = "yxz"
        self.menu_ry_rz_rx = "yzx"
        self.menu_rz_rx_ry = "zxy"
        self.menu_rz_ry_rx = "zyx"


class PreXformMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_clean_transform = "clean"
        self.menu_clean_translates = "cleantrans"
        self.menu_clean_rotates = "cleanrot"
        self.menu_clean_scales = "cleanscales"
        self.menu_extract_pre_transform = "extract"
        self.menu_reset_pre_transform = "reset"


class LookupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_don_t_use_up_vector = "off"
        self.menu_use_up_vector = "on"
        self.menu_use_quaternions = "quat"
        self.menu_use_global_position = "pos"
        self.menu_use_up_object = "obj"


class UparmtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uniform = "uniform"
        self.menu_arc_length = "arc"


class EnvtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_spherical = "0"
        self.menu_hemispherical = "1"
        self.menu_mirror_ball = "2"
        self.menu_angular = "3"


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


class Tex1ColorspaceMenu(Menu):
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


class BackplateaspectMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_texture = "0"
        self.menu_render = "1"


class RslAffectedbyrefractionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_never = "never"
        self.menu_auto = "auto"
        self.menu_always = "always"



