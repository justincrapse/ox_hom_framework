from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class MaterialNode(HHNode):
    node_type = 'redshift::Material'
    parm_lookup_dict = {'rs_shadernodemainswitcher1': 'RS_shaderNodeMainSwitcher1', 'preset': 'preset', 'diffuse_0': 'Diffuse_0', 'diffuse_colorr': 'diffuse_colorr', 'diffuse_colorg': 'diffuse_colorg', 'diffuse_colorb': 'diffuse_colorb', 'diffuse_weight': 'diffuse_weight', 'diffuse_roughness': 'diffuse_roughness', 'back_lighting_translucency_1': 'Back_lighting/Translucency_1', 'transl_colorr': 'transl_colorr', 'transl_colorg': 'transl_colorg', 'transl_colorb': 'transl_colorb', 'transl_weight': 'transl_weight', 'reflection_2': 'Reflection_2', 'refl_colorr': 'refl_colorr', 'refl_colorg': 'refl_colorg', 'refl_colorb': 'refl_colorb', 'refl_weight': 'refl_weight', 'refl_roughness': 'refl_roughness', 'refl_samples': 'refl_samples', 'refl_brdf': 'refl_brdf', 'refl_aniso': 'refl_aniso', 'refl_aniso_rotation': 'refl_aniso_rotation', 'refl_fresnel_mode': 'refl_fresnel_mode', 'refl_reflectivityr': 'refl_reflectivityr', 'refl_reflectivityg': 'refl_reflectivityg', 'refl_reflectivityb': 'refl_reflectivityb', 'refl_edge_tintr': 'refl_edge_tintr', 'refl_edge_tintg': 'refl_edge_tintg', 'refl_edge_tintb': 'refl_edge_tintb', 'refl_ior31': 'refl_ior31', 'refl_ior32': 'refl_ior32', 'refl_ior33': 'refl_ior33', 'refl_k31': 'refl_k31', 'refl_k32': 'refl_k32', 'refl_k33': 'refl_k33', 'refl_metalness': 'refl_metalness', 'refl_ior': 'refl_ior', 'sheen_3': 'Sheen_3', 'sheen_colorr': 'sheen_colorr', 'sheen_colorg': 'sheen_colorg', 'sheen_colorb': 'sheen_colorb', 'sheen_weight': 'sheen_weight', 'sheen_roughness': 'sheen_roughness', 'sheen_samples': 'sheen_samples', 'refraction_transmission_4': 'Refraction/Transmission_4', 'refr_colorr': 'refr_colorr', 'refr_colorg': 'refr_colorg', 'refr_colorb': 'refr_colorb', 'refr_weight': 'refr_weight', 'refr_roughness': 'refr_roughness', 'refr_samples': 'refr_samples', 'refr_ior': 'refr_ior', 'refr_use_base_ior': 'refr_use_base_IOR', 'refr_abbe': 'refr_abbe', 'refr_thin_walled': 'refr_thin_walled', 'sub_surface_5': 'Sub_Surface_5', 'ss_unitsmode': 'ss_unitsMode', 'refr_transmittancer': 'refr_transmittancer', 'refr_transmittanceg': 'refr_transmittanceg', 'refr_transmittanceb': 'refr_transmittanceb', 'refr_absorption_scale': 'refr_absorption_scale', 'ss_extinction_coeffr': 'ss_extinction_coeffr', 'ss_extinction_coeffg': 'ss_extinction_coeffg', 'ss_extinction_coeffb': 'ss_extinction_coeffb', 'ss_extinction_scale': 'ss_extinction_scale', 'ss_scatter_coeffr': 'ss_scatter_coeffr', 'ss_scatter_coeffg': 'ss_scatter_coeffg', 'ss_scatter_coeffb': 'ss_scatter_coeffb', 'ss_amount': 'ss_amount', 'ss_phase': 'ss_phase', 'ss_samples': 'ss_samples', 'general_6': 'General_6', 'ms_amount': 'ms_amount', 'ms_radius_scale': 'ms_radius_scale', 'ms_mode': 'ms_mode', 'ms_samples': 'ms_samples', 'ms_include_mode': 'ms_include_mode', 'layer_1_7': 'Layer_1_7', 'ms_color0r': 'ms_color0r', 'ms_color0g': 'ms_color0g', 'ms_color0b': 'ms_color0b', 'ms_weight0': 'ms_weight0', 'ms_radius0': 'ms_radius0', 'layer_2_8': 'Layer_2_8', 'ms_color1r': 'ms_color1r', 'ms_color1g': 'ms_color1g', 'ms_color1b': 'ms_color1b', 'ms_weight1': 'ms_weight1', 'ms_radius1': 'ms_radius1', 'layer_3_9': 'Layer_3_9', 'ms_color2r': 'ms_color2r', 'ms_color2g': 'ms_color2g', 'ms_color2b': 'ms_color2b', 'ms_weight2': 'ms_weight2', 'ms_radius2': 'ms_radius2', 'general_10': 'General_10', 'coat_colorr': 'coat_colorr', 'coat_colorg': 'coat_colorg', 'coat_colorb': 'coat_colorb', 'coat_weight': 'coat_weight', 'coat_roughness': 'coat_roughness', 'coat_samples': 'coat_samples', 'coat_brdf': 'coat_brdf', 'coat_fresnel_mode': 'coat_fresnel_mode', 'coat_reflectivityr': 'coat_reflectivityr', 'coat_reflectivityg': 'coat_reflectivityg', 'coat_reflectivityb': 'coat_reflectivityb', 'coat_ior31': 'coat_ior31', 'coat_ior32': 'coat_ior32', 'coat_ior33': 'coat_ior33', 'coat_ior': 'coat_ior', 'advanced_11': 'Advanced_11', 'coat_transmittancer': 'coat_transmittancer', 'coat_transmittanceg': 'coat_transmittanceg', 'coat_transmittanceb': 'coat_transmittanceb', 'coat_thickness': 'coat_thickness', 'coat_bump_input': 'coat_bump_input', 'overall_colorr': 'overall_colorr', 'overall_colorg': 'overall_colorg', 'overall_colorb': 'overall_colorb', 'opacity_colorr': 'opacity_colorr', 'opacity_colorg': 'opacity_colorg', 'opacity_colorb': 'opacity_colorb', 'emission_colorr': 'emission_colorr', 'emission_colorg': 'emission_colorg', 'emission_colorb': 'emission_colorb', 'emission_weight': 'emission_weight', 'bump_input': 'bump_input', 'depth_override': 'depth_override', 'combined_depth': 'combined_depth', 'reflection_12': 'Reflection_12', 'refl_depth': 'refl_depth', 'refl_enablecutoff': 'refl_enablecutoff', 'refl_cutoff': 'refl_cutoff', 'skip_inside_refl': 'skip_inside_refl', 'refraction_13': 'Refraction_13', 'refr_depth': 'refr_depth', 'refr_enablecutoff': 'refr_enablecutoff', 'refr_cutoff': 'refr_cutoff', 'energycompmode': 'energyCompMode', 'overallaffectsemission': 'overallAffectsEmission', 'refl_endmode': 'refl_endmode', 'diffuse_14': 'Diffuse_14', 'diffuse_direct': 'diffuse_direct', 'diffuse_indirect': 'diffuse_indirect', 'reflection_15': 'Reflection_15', 'refl_direct': 'refl_direct', 'refl_indirect': 'refl_indirect', 'refl_isglossiness': 'refl_isGlossiness', 'coating_16': 'Coating_16', 'coat_direct': 'coat_direct', 'coat_indirect': 'coat_indirect', 'coat_isglossiness': 'coat_isGlossiness', 'sheen_17': 'Sheen_17', 'sheen_direct': 'sheen_direct', 'sheen_indirect': 'sheen_indirect', 'sheen_isglossiness': 'sheen_isGlossiness', 'refraction_18': 'Refraction_18', 'refr_isglossiness': 'refr_isGlossiness', 'decoupleiorfromroughness': 'decoupleIORFromRoughness', 'shadow_opacity': 'shadow_opacity', 'affects_alpha': 'affects_alpha', 'block_volumes': 'block_volumes', 'anisotropy_19': 'Anisotropy_19', 'anisotropy_orientation': 'anisotropy_orientation', 'anisotropy_uvchannel': 'anisotropy_uvChannel', 'anisotropy_tangentchannel': 'anisotropy_tangentChannel'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_rs_shadernodemainswitcher1 = Parameter(parm=self.node.parm('rs_shadernodemainswitcher1'))
        self.parm_diffuse_0 = Parameter(parm=self.node.parm('diffuse_0'))
        self.parm_diffuse_colorr = Parameter(parm=self.node.parm('diffuse_colorr'))
        self.parm_diffuse_colorg = Parameter(parm=self.node.parm('diffuse_colorg'))
        self.parm_diffuse_colorb = Parameter(parm=self.node.parm('diffuse_colorb'))
        self.parm_diffuse_weight = Parameter(parm=self.node.parm('diffuse_weight'))
        self.parm_diffuse_roughness = Parameter(parm=self.node.parm('diffuse_roughness'))
        self.parm_back_lighting_translucency_1 = Parameter(parm=self.node.parm('back_lighting_translucency_1'))
        self.parm_transl_colorr = Parameter(parm=self.node.parm('transl_colorr'))
        self.parm_transl_colorg = Parameter(parm=self.node.parm('transl_colorg'))
        self.parm_transl_colorb = Parameter(parm=self.node.parm('transl_colorb'))
        self.parm_transl_weight = Parameter(parm=self.node.parm('transl_weight'))
        self.parm_reflection_2 = Parameter(parm=self.node.parm('reflection_2'))
        self.parm_refl_colorr = Parameter(parm=self.node.parm('refl_colorr'))
        self.parm_refl_colorg = Parameter(parm=self.node.parm('refl_colorg'))
        self.parm_refl_colorb = Parameter(parm=self.node.parm('refl_colorb'))
        self.parm_refl_weight = Parameter(parm=self.node.parm('refl_weight'))
        self.parm_refl_roughness = Parameter(parm=self.node.parm('refl_roughness'))
        self.parm_refl_samples = Parameter(parm=self.node.parm('refl_samples'))
        self.parm_refl_aniso = Parameter(parm=self.node.parm('refl_aniso'))
        self.parm_refl_aniso_rotation = Parameter(parm=self.node.parm('refl_aniso_rotation'))
        self.parm_refl_reflectivityr = Parameter(parm=self.node.parm('refl_reflectivityr'))
        self.parm_refl_reflectivityg = Parameter(parm=self.node.parm('refl_reflectivityg'))
        self.parm_refl_reflectivityb = Parameter(parm=self.node.parm('refl_reflectivityb'))
        self.parm_refl_edge_tintr = Parameter(parm=self.node.parm('refl_edge_tintr'))
        self.parm_refl_edge_tintg = Parameter(parm=self.node.parm('refl_edge_tintg'))
        self.parm_refl_edge_tintb = Parameter(parm=self.node.parm('refl_edge_tintb'))
        self.parm_refl_ior31 = Parameter(parm=self.node.parm('refl_ior31'))
        self.parm_refl_ior32 = Parameter(parm=self.node.parm('refl_ior32'))
        self.parm_refl_ior33 = Parameter(parm=self.node.parm('refl_ior33'))
        self.parm_refl_k31 = Parameter(parm=self.node.parm('refl_k31'))
        self.parm_refl_k32 = Parameter(parm=self.node.parm('refl_k32'))
        self.parm_refl_k33 = Parameter(parm=self.node.parm('refl_k33'))
        self.parm_refl_metalness = Parameter(parm=self.node.parm('refl_metalness'))
        self.parm_refl_ior = Parameter(parm=self.node.parm('refl_ior'))
        self.parm_sheen_3 = Parameter(parm=self.node.parm('sheen_3'))
        self.parm_sheen_colorr = Parameter(parm=self.node.parm('sheen_colorr'))
        self.parm_sheen_colorg = Parameter(parm=self.node.parm('sheen_colorg'))
        self.parm_sheen_colorb = Parameter(parm=self.node.parm('sheen_colorb'))
        self.parm_sheen_weight = Parameter(parm=self.node.parm('sheen_weight'))
        self.parm_sheen_roughness = Parameter(parm=self.node.parm('sheen_roughness'))
        self.parm_sheen_samples = Parameter(parm=self.node.parm('sheen_samples'))
        self.parm_refraction_transmission_4 = Parameter(parm=self.node.parm('refraction_transmission_4'))
        self.parm_refr_colorr = Parameter(parm=self.node.parm('refr_colorr'))
        self.parm_refr_colorg = Parameter(parm=self.node.parm('refr_colorg'))
        self.parm_refr_colorb = Parameter(parm=self.node.parm('refr_colorb'))
        self.parm_refr_weight = Parameter(parm=self.node.parm('refr_weight'))
        self.parm_refr_roughness = Parameter(parm=self.node.parm('refr_roughness'))
        self.parm_refr_samples = Parameter(parm=self.node.parm('refr_samples'))
        self.parm_refr_ior = Parameter(parm=self.node.parm('refr_ior'))
        self.parm_refr_use_base_ior = Parameter(parm=self.node.parm('refr_use_base_ior'))
        self.parm_refr_abbe = Parameter(parm=self.node.parm('refr_abbe'))
        self.parm_refr_thin_walled = Parameter(parm=self.node.parm('refr_thin_walled'))
        self.parm_sub_surface_5 = Parameter(parm=self.node.parm('sub_surface_5'))
        self.parm_refr_transmittancer = Parameter(parm=self.node.parm('refr_transmittancer'))
        self.parm_refr_transmittanceg = Parameter(parm=self.node.parm('refr_transmittanceg'))
        self.parm_refr_transmittanceb = Parameter(parm=self.node.parm('refr_transmittanceb'))
        self.parm_refr_absorption_scale = Parameter(parm=self.node.parm('refr_absorption_scale'))
        self.parm_ss_extinction_coeffr = Parameter(parm=self.node.parm('ss_extinction_coeffr'))
        self.parm_ss_extinction_coeffg = Parameter(parm=self.node.parm('ss_extinction_coeffg'))
        self.parm_ss_extinction_coeffb = Parameter(parm=self.node.parm('ss_extinction_coeffb'))
        self.parm_ss_extinction_scale = Parameter(parm=self.node.parm('ss_extinction_scale'))
        self.parm_ss_scatter_coeffr = Parameter(parm=self.node.parm('ss_scatter_coeffr'))
        self.parm_ss_scatter_coeffg = Parameter(parm=self.node.parm('ss_scatter_coeffg'))
        self.parm_ss_scatter_coeffb = Parameter(parm=self.node.parm('ss_scatter_coeffb'))
        self.parm_ss_amount = Parameter(parm=self.node.parm('ss_amount'))
        self.parm_ss_phase = Parameter(parm=self.node.parm('ss_phase'))
        self.parm_ss_samples = Parameter(parm=self.node.parm('ss_samples'))
        self.parm_general_6 = Parameter(parm=self.node.parm('general_6'))
        self.parm_ms_amount = Parameter(parm=self.node.parm('ms_amount'))
        self.parm_ms_radius_scale = Parameter(parm=self.node.parm('ms_radius_scale'))
        self.parm_ms_samples = Parameter(parm=self.node.parm('ms_samples'))
        self.parm_layer_1_7 = Parameter(parm=self.node.parm('layer_1_7'))
        self.parm_ms_color0r = Parameter(parm=self.node.parm('ms_color0r'))
        self.parm_ms_color0g = Parameter(parm=self.node.parm('ms_color0g'))
        self.parm_ms_color0b = Parameter(parm=self.node.parm('ms_color0b'))
        self.parm_ms_weight0 = Parameter(parm=self.node.parm('ms_weight0'))
        self.parm_ms_radius0 = Parameter(parm=self.node.parm('ms_radius0'))
        self.parm_layer_2_8 = Parameter(parm=self.node.parm('layer_2_8'))
        self.parm_ms_color1r = Parameter(parm=self.node.parm('ms_color1r'))
        self.parm_ms_color1g = Parameter(parm=self.node.parm('ms_color1g'))
        self.parm_ms_color1b = Parameter(parm=self.node.parm('ms_color1b'))
        self.parm_ms_weight1 = Parameter(parm=self.node.parm('ms_weight1'))
        self.parm_ms_radius1 = Parameter(parm=self.node.parm('ms_radius1'))
        self.parm_layer_3_9 = Parameter(parm=self.node.parm('layer_3_9'))
        self.parm_ms_color2r = Parameter(parm=self.node.parm('ms_color2r'))
        self.parm_ms_color2g = Parameter(parm=self.node.parm('ms_color2g'))
        self.parm_ms_color2b = Parameter(parm=self.node.parm('ms_color2b'))
        self.parm_ms_weight2 = Parameter(parm=self.node.parm('ms_weight2'))
        self.parm_ms_radius2 = Parameter(parm=self.node.parm('ms_radius2'))
        self.parm_general_10 = Parameter(parm=self.node.parm('general_10'))
        self.parm_coat_colorr = Parameter(parm=self.node.parm('coat_colorr'))
        self.parm_coat_colorg = Parameter(parm=self.node.parm('coat_colorg'))
        self.parm_coat_colorb = Parameter(parm=self.node.parm('coat_colorb'))
        self.parm_coat_weight = Parameter(parm=self.node.parm('coat_weight'))
        self.parm_coat_roughness = Parameter(parm=self.node.parm('coat_roughness'))
        self.parm_coat_samples = Parameter(parm=self.node.parm('coat_samples'))
        self.parm_coat_reflectivityr = Parameter(parm=self.node.parm('coat_reflectivityr'))
        self.parm_coat_reflectivityg = Parameter(parm=self.node.parm('coat_reflectivityg'))
        self.parm_coat_reflectivityb = Parameter(parm=self.node.parm('coat_reflectivityb'))
        self.parm_coat_ior31 = Parameter(parm=self.node.parm('coat_ior31'))
        self.parm_coat_ior32 = Parameter(parm=self.node.parm('coat_ior32'))
        self.parm_coat_ior33 = Parameter(parm=self.node.parm('coat_ior33'))
        self.parm_coat_ior = Parameter(parm=self.node.parm('coat_ior'))
        self.parm_advanced_11 = Parameter(parm=self.node.parm('advanced_11'))
        self.parm_coat_transmittancer = Parameter(parm=self.node.parm('coat_transmittancer'))
        self.parm_coat_transmittanceg = Parameter(parm=self.node.parm('coat_transmittanceg'))
        self.parm_coat_transmittanceb = Parameter(parm=self.node.parm('coat_transmittanceb'))
        self.parm_coat_thickness = Parameter(parm=self.node.parm('coat_thickness'))
        self.parm_coat_bump_input = Parameter(parm=self.node.parm('coat_bump_input'))
        self.parm_overall_colorr = Parameter(parm=self.node.parm('overall_colorr'))
        self.parm_overall_colorg = Parameter(parm=self.node.parm('overall_colorg'))
        self.parm_overall_colorb = Parameter(parm=self.node.parm('overall_colorb'))
        self.parm_opacity_colorr = Parameter(parm=self.node.parm('opacity_colorr'))
        self.parm_opacity_colorg = Parameter(parm=self.node.parm('opacity_colorg'))
        self.parm_opacity_colorb = Parameter(parm=self.node.parm('opacity_colorb'))
        self.parm_emission_colorr = Parameter(parm=self.node.parm('emission_colorr'))
        self.parm_emission_colorg = Parameter(parm=self.node.parm('emission_colorg'))
        self.parm_emission_colorb = Parameter(parm=self.node.parm('emission_colorb'))
        self.parm_emission_weight = Parameter(parm=self.node.parm('emission_weight'))
        self.parm_bump_input = Parameter(parm=self.node.parm('bump_input'))
        self.parm_depth_override = Parameter(parm=self.node.parm('depth_override'))
        self.parm_combined_depth = Parameter(parm=self.node.parm('combined_depth'))
        self.parm_reflection_12 = Parameter(parm=self.node.parm('reflection_12'))
        self.parm_refl_depth = Parameter(parm=self.node.parm('refl_depth'))
        self.parm_refl_enablecutoff = Parameter(parm=self.node.parm('refl_enablecutoff'))
        self.parm_refl_cutoff = Parameter(parm=self.node.parm('refl_cutoff'))
        self.parm_skip_inside_refl = Parameter(parm=self.node.parm('skip_inside_refl'))
        self.parm_refraction_13 = Parameter(parm=self.node.parm('refraction_13'))
        self.parm_refr_depth = Parameter(parm=self.node.parm('refr_depth'))
        self.parm_refr_enablecutoff = Parameter(parm=self.node.parm('refr_enablecutoff'))
        self.parm_refr_cutoff = Parameter(parm=self.node.parm('refr_cutoff'))
        self.parm_overallaffectsemission = Parameter(parm=self.node.parm('overallaffectsemission'))
        self.parm_diffuse_14 = Parameter(parm=self.node.parm('diffuse_14'))
        self.parm_diffuse_direct = Parameter(parm=self.node.parm('diffuse_direct'))
        self.parm_diffuse_indirect = Parameter(parm=self.node.parm('diffuse_indirect'))
        self.parm_reflection_15 = Parameter(parm=self.node.parm('reflection_15'))
        self.parm_refl_direct = Parameter(parm=self.node.parm('refl_direct'))
        self.parm_refl_indirect = Parameter(parm=self.node.parm('refl_indirect'))
        self.parm_refl_isglossiness = Parameter(parm=self.node.parm('refl_isglossiness'))
        self.parm_coating_16 = Parameter(parm=self.node.parm('coating_16'))
        self.parm_coat_direct = Parameter(parm=self.node.parm('coat_direct'))
        self.parm_coat_indirect = Parameter(parm=self.node.parm('coat_indirect'))
        self.parm_coat_isglossiness = Parameter(parm=self.node.parm('coat_isglossiness'))
        self.parm_sheen_17 = Parameter(parm=self.node.parm('sheen_17'))
        self.parm_sheen_direct = Parameter(parm=self.node.parm('sheen_direct'))
        self.parm_sheen_indirect = Parameter(parm=self.node.parm('sheen_indirect'))
        self.parm_sheen_isglossiness = Parameter(parm=self.node.parm('sheen_isglossiness'))
        self.parm_refraction_18 = Parameter(parm=self.node.parm('refraction_18'))
        self.parm_refr_isglossiness = Parameter(parm=self.node.parm('refr_isglossiness'))
        self.parm_decoupleiorfromroughness = Parameter(parm=self.node.parm('decoupleiorfromroughness'))
        self.parm_shadow_opacity = Parameter(parm=self.node.parm('shadow_opacity'))
        self.parm_affects_alpha = Parameter(parm=self.node.parm('affects_alpha'))
        self.parm_block_volumes = Parameter(parm=self.node.parm('block_volumes'))
        self.parm_anisotropy_19 = Parameter(parm=self.node.parm('anisotropy_19'))
        self.parm_anisotropy_uvchannel = Parameter(parm=self.node.parm('anisotropy_uvchannel'))
        self.parm_anisotropy_tangentchannel = Parameter(parm=self.node.parm('anisotropy_tangentchannel'))

        
        # parm menu vars:
        self.parm_preset_menu = PresetMenu(parm=self.node.parm('preset'))
        self.parm_refl_brdf_menu = ReflBrdfMenu(parm=self.node.parm('refl_brdf'))
        self.parm_refl_fresnel_mode_menu = ReflFresnelModeMenu(parm=self.node.parm('refl_fresnel_mode'))
        self.parm_ss_unitsmode_menu = SsUnitsmodeMenu(parm=self.node.parm('ss_unitsMode'))
        self.parm_ms_mode_menu = MsModeMenu(parm=self.node.parm('ms_mode'))
        self.parm_ms_include_mode_menu = MsIncludeModeMenu(parm=self.node.parm('ms_include_mode'))
        self.parm_coat_brdf_menu = CoatBrdfMenu(parm=self.node.parm('coat_brdf'))
        self.parm_coat_fresnel_mode_menu = CoatFresnelModeMenu(parm=self.node.parm('coat_fresnel_mode'))
        self.parm_energycompmode_menu = EnergycompmodeMenu(parm=self.node.parm('energyCompMode'))
        self.parm_refl_endmode_menu = ReflEndmodeMenu(parm=self.node.parm('refl_endmode'))
        self.parm_anisotropy_orientation_menu = AnisotropyOrientationMenu(parm=self.node.parm('anisotropy_orientation'))


        # input vars:
        self.input_diffuse_color = 0
        self.input_diffuse_weight = 1
        self.input_diffuse_roughness = 2
        self.input_transl_color = 3
        self.input_transl_weight = 4
        self.input_refl_color = 5
        self.input_refl_weight = 6
        self.input_refl_roughness = 7
        self.input_refl_aniso = 8
        self.input_refl_aniso_rotation = 9
        self.input_refl_reflectivity = 10
        self.input_refl_edge_tint = 11
        self.input_refl_ior3 = 12
        self.input_refl_k3 = 13
        self.input_refl_metalness = 14
        self.input_refl_ior = 15
        self.input_sheen_color = 16
        self.input_sheen_weight = 17
        self.input_sheen_roughness = 18
        self.input_refr_color = 19
        self.input_refr_weight = 20
        self.input_refr_roughness = 21
        self.input_refr_ior = 22
        self.input_refr_abbe = 23
        self.input_refr_transmittance = 24
        self.input_refr_absorption_scale = 25
        self.input_ss_extinction_coeff = 26
        self.input_ss_extinction_scale = 27
        self.input_ss_scatter_coeff = 28
        self.input_ss_amount = 29
        self.input_ms_amount = 30
        self.input_ms_color0 = 31
        self.input_ms_weight0 = 32
        self.input_ms_radius0 = 33
        self.input_ms_color1 = 34
        self.input_ms_weight1 = 35
        self.input_ms_radius1 = 36
        self.input_ms_color2 = 37
        self.input_ms_weight2 = 38
        self.input_ms_radius2 = 39
        self.input_coat_color = 40
        self.input_coat_weight = 41
        self.input_coat_roughness = 42
        self.input_coat_reflectivity = 43
        self.input_coat_ior3 = 44
        self.input_coat_ior = 45
        self.input_coat_transmittance = 46
        self.input_coat_thickness = 47
        self.input_coat_bump_input = 48
        self.input_overall_color = 49
        self.input_opacity_color = 50
        self.input_emission_color = 51
        self.input_bump_input = 52


# parm menu classes:
class PresetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.custom = 0
        self.glass = 1
        self.tinted_glass = 2
        self.water = 3
        self.plastic = 4
        self.aluminium = 5
        self.copper = 6
        self.gold = 7
        self.iron = 8
        self.lead = 9
        self.platinum = 10
        self.silver = 11
        self.milky_coffee = 12
        self.jade = 13
        self.paper = 14


class ReflBrdfMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.beckmann__cook_torrance_ = 0
        self.ggx = 1
        self.ashikhmin_shirley = 2


class ReflFresnelModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.ior__advanced_ = 0
        self.color___edge_tint = 1
        self.metalness = 2
        self.ior = 3


class SsUnitsmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.transmittance = 0
        self.extinction = 1


class MsModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.point_based = 0
        self.ray_traced = 1


class MsIncludeModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.all_objects = 0
        self.only_self = 1


class CoatBrdfMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.beckmann__cook_torrance_ = 0
        self.ggx = 1
        self.ashikhmin_shirley = 2


class CoatFresnelModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.ior__advanced_ = 0
        self.color = 1
        self.ior = 2


class EnergycompmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.mono = 0
        self.rgb = 1


class ReflEndmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.environment = 0
        self.diffuse = 1


class AnisotropyOrientationMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.none = 0
        self.from_tangent_channel = 1



