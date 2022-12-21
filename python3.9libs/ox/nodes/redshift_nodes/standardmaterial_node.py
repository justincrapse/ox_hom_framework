from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class StandardmaterialNode(OXNode):
    node_type = "redshift::StandardMaterial"
    parm_lookup_dict = {
        "rs_shadernodemainswitcher1": "RS_shaderNodeMainSwitcher1",
        "base_0": "Base_0",
        "base_colorr": "base_colorr",
        "base_colorg": "base_colorg",
        "base_colorb": "base_colorb",
        "base_color_weight": "base_color_weight",
        "diffuse_model": "diffuse_model",
        "diffuse_roughness": "diffuse_roughness",
        "metalness": "metalness",
        "reflection_1": "Reflection_1",
        "refl_colorr": "refl_colorr",
        "refl_colorg": "refl_colorg",
        "refl_colorb": "refl_colorb",
        "refl_weight": "refl_weight",
        "refl_roughness": "refl_roughness",
        "refl_ior": "refl_ior",
        "refl_aniso": "refl_aniso",
        "refl_aniso_rotation": "refl_aniso_rotation",
        "refl_samples": "refl_samples",
        "transmission_2": "Transmission_2",
        "refr_colorr": "refr_colorr",
        "refr_colorg": "refr_colorg",
        "refr_colorb": "refr_colorb",
        "refr_weight": "refr_weight",
        "refr_roughness": "refr_roughness",
        "refr_samples": "refr_samples",
        "ss_depth": "ss_depth",
        "ss_scatter_colorr": "ss_scatter_colorr",
        "ss_scatter_colorg": "ss_scatter_colorg",
        "ss_scatter_colorb": "ss_scatter_colorb",
        "ss_phase": "ss_phase",
        "ss_samples": "ss_samples",
        "refr_abbe": "refr_abbe",
        "subsurface_3": "Subsurface_3",
        "ms_colorr": "ms_colorr",
        "ms_colorg": "ms_colorg",
        "ms_colorb": "ms_colorb",
        "ms_amount": "ms_amount",
        "ms_radiusr": "ms_radiusr",
        "ms_radiusg": "ms_radiusg",
        "ms_radiusb": "ms_radiusb",
        "ms_radius_scale": "ms_radius_scale",
        "ms_phase": "ms_phase",
        "ms_mode": "ms_mode",
        "ms_samples": "ms_samples",
        "ms_include_mode": "ms_include_mode",
        "sheen_4": "Sheen_4",
        "sheen_colorr": "sheen_colorr",
        "sheen_colorg": "sheen_colorg",
        "sheen_colorb": "sheen_colorb",
        "sheen_weight": "sheen_weight",
        "sheen_roughness": "sheen_roughness",
        "sheen_samples": "sheen_samples",
        "thin_film_5": "Thin_Film_5",
        "thinfilm_ior": "thinfilm_ior",
        "thinfilm_thickness": "thinfilm_thickness",
        "coat_6": "Coat_6",
        "coat_colorr": "coat_colorr",
        "coat_colorg": "coat_colorg",
        "coat_colorb": "coat_colorb",
        "coat_weight": "coat_weight",
        "coat_roughness": "coat_roughness",
        "coat_ior": "coat_ior",
        "coat_aniso": "coat_aniso",
        "coat_aniso_rotation": "coat_aniso_rotation",
        "coat_samples": "coat_samples",
        "coat_bump_input": "coat_bump_input",
        "emission_7": "Emission_7",
        "emission_colorr": "emission_colorr",
        "emission_colorg": "emission_colorg",
        "emission_colorb": "emission_colorb",
        "emission_weight": "emission_weight",
        "geometry_8": "Geometry_8",
        "opacity_colorr": "opacity_colorr",
        "opacity_colorg": "opacity_colorg",
        "opacity_colorb": "opacity_colorb",
        "refr_thin_walled": "refr_thin_walled",
        "bump_input": "bump_input",
        "overall_colorr": "overall_colorr",
        "overall_colorg": "overall_colorg",
        "overall_colorb": "overall_colorb",
        "overallaffectsemission": "overallAffectsEmission",
        "depth_override": "depth_override",
        "combined_depth": "combined_depth",
        "reflection_9": "Reflection_9",
        "refl_depth": "refl_depth",
        "refl_enablecutoff": "refl_enablecutoff",
        "refl_cutoff": "refl_cutoff",
        "transmission_10": "Transmission_10",
        "refr_depth": "refr_depth",
        "refr_enablecutoff": "refr_enablecutoff",
        "refr_cutoff": "refr_cutoff",
        "refl_enablemultiscattercomp": "refl_enableMultiScatterComp",
        "diffuse_11": "Diffuse_11",
        "diffuse_direct": "diffuse_direct",
        "diffuse_indirect": "diffuse_indirect",
        "reflection_12": "Reflection_12",
        "refl_direct": "refl_direct",
        "refl_indirect": "refl_indirect",
        "refl_isglossiness": "refl_isGlossiness",
        "refl_endmode": "refl_endmode",
        "transmission_13": "Transmission_13",
        "shadow_opacity": "shadow_opacity",
        "refr_isglossiness": "refr_isGlossiness",
        "affects_alpha": "affects_alpha",
        "block_volumes": "block_volumes",
        "sheen_14": "Sheen_14",
        "sheen_direct": "sheen_direct",
        "sheen_indirect": "sheen_indirect",
        "sheen_isglossiness": "sheen_isGlossiness",
        "coat_15": "Coat_15",
        "coat_direct": "coat_direct",
        "coat_indirect": "coat_indirect",
        "coat_isglossiness": "coat_isGlossiness",
        "anisotropy_16": "Anisotropy_16",
        "anisotropy_orientation": "anisotropy_orientation",
        "anisotropy_uvchannel": "anisotropy_uvChannel",
        "anisotropy_tangentchannel": "anisotropy_tangentChannel",
        "shader_skipdefvalparms": "shader_skipdefvalparms",
    }

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(
                node_type_name=self.node_type, node_name=node_name
            )
        self.node_name = self.node.name()
        super().__init__(node=self.node)

        # parm vars:
        self.parm_rs_shadernodemainswitcher1 = Parameter(
            parm=self.node.parm("RS_shaderNodeMainSwitcher1")
        )
        self.parm_base_0 = Parameter(parm=self.node.parm("Base_0"))
        self.parm_base_colorr = Parameter(parm=self.node.parm("base_colorr"))
        self.parm_base_colorg = Parameter(parm=self.node.parm("base_colorg"))
        self.parm_base_colorb = Parameter(parm=self.node.parm("base_colorb"))
        self.parm_base_color_weight = Parameter(
            parm=self.node.parm("base_color_weight")
        )
        self.parm_diffuse_roughness = Parameter(
            parm=self.node.parm("diffuse_roughness")
        )
        self.parm_metalness = Parameter(parm=self.node.parm("metalness"))
        self.parm_reflection_1 = Parameter(parm=self.node.parm("Reflection_1"))
        self.parm_refl_colorr = Parameter(parm=self.node.parm("refl_colorr"))
        self.parm_refl_colorg = Parameter(parm=self.node.parm("refl_colorg"))
        self.parm_refl_colorb = Parameter(parm=self.node.parm("refl_colorb"))
        self.parm_refl_weight = Parameter(parm=self.node.parm("refl_weight"))
        self.parm_refl_roughness = Parameter(parm=self.node.parm("refl_roughness"))
        self.parm_refl_ior = Parameter(parm=self.node.parm("refl_ior"))
        self.parm_refl_aniso = Parameter(parm=self.node.parm("refl_aniso"))
        self.parm_refl_aniso_rotation = Parameter(
            parm=self.node.parm("refl_aniso_rotation")
        )
        self.parm_refl_samples = Parameter(parm=self.node.parm("refl_samples"))
        self.parm_transmission_2 = Parameter(parm=self.node.parm("Transmission_2"))
        self.parm_refr_colorr = Parameter(parm=self.node.parm("refr_colorr"))
        self.parm_refr_colorg = Parameter(parm=self.node.parm("refr_colorg"))
        self.parm_refr_colorb = Parameter(parm=self.node.parm("refr_colorb"))
        self.parm_refr_weight = Parameter(parm=self.node.parm("refr_weight"))
        self.parm_refr_roughness = Parameter(parm=self.node.parm("refr_roughness"))
        self.parm_refr_samples = Parameter(parm=self.node.parm("refr_samples"))
        self.parm_ss_depth = Parameter(parm=self.node.parm("ss_depth"))
        self.parm_ss_scatter_colorr = Parameter(
            parm=self.node.parm("ss_scatter_colorr")
        )
        self.parm_ss_scatter_colorg = Parameter(
            parm=self.node.parm("ss_scatter_colorg")
        )
        self.parm_ss_scatter_colorb = Parameter(
            parm=self.node.parm("ss_scatter_colorb")
        )
        self.parm_ss_phase = Parameter(parm=self.node.parm("ss_phase"))
        self.parm_ss_samples = Parameter(parm=self.node.parm("ss_samples"))
        self.parm_refr_abbe = Parameter(parm=self.node.parm("refr_abbe"))
        self.parm_subsurface_3 = Parameter(parm=self.node.parm("Subsurface_3"))
        self.parm_ms_colorr = Parameter(parm=self.node.parm("ms_colorr"))
        self.parm_ms_colorg = Parameter(parm=self.node.parm("ms_colorg"))
        self.parm_ms_colorb = Parameter(parm=self.node.parm("ms_colorb"))
        self.parm_ms_amount = Parameter(parm=self.node.parm("ms_amount"))
        self.parm_ms_radiusr = Parameter(parm=self.node.parm("ms_radiusr"))
        self.parm_ms_radiusg = Parameter(parm=self.node.parm("ms_radiusg"))
        self.parm_ms_radiusb = Parameter(parm=self.node.parm("ms_radiusb"))
        self.parm_ms_radius_scale = Parameter(parm=self.node.parm("ms_radius_scale"))
        self.parm_ms_phase = Parameter(parm=self.node.parm("ms_phase"))
        self.parm_ms_samples = Parameter(parm=self.node.parm("ms_samples"))
        self.parm_sheen_4 = Parameter(parm=self.node.parm("Sheen_4"))
        self.parm_sheen_colorr = Parameter(parm=self.node.parm("sheen_colorr"))
        self.parm_sheen_colorg = Parameter(parm=self.node.parm("sheen_colorg"))
        self.parm_sheen_colorb = Parameter(parm=self.node.parm("sheen_colorb"))
        self.parm_sheen_weight = Parameter(parm=self.node.parm("sheen_weight"))
        self.parm_sheen_roughness = Parameter(parm=self.node.parm("sheen_roughness"))
        self.parm_sheen_samples = Parameter(parm=self.node.parm("sheen_samples"))
        self.parm_thin_film_5 = Parameter(parm=self.node.parm("Thin_Film_5"))
        self.parm_thinfilm_ior = Parameter(parm=self.node.parm("thinfilm_ior"))
        self.parm_thinfilm_thickness = Parameter(
            parm=self.node.parm("thinfilm_thickness")
        )
        self.parm_coat_6 = Parameter(parm=self.node.parm("Coat_6"))
        self.parm_coat_colorr = Parameter(parm=self.node.parm("coat_colorr"))
        self.parm_coat_colorg = Parameter(parm=self.node.parm("coat_colorg"))
        self.parm_coat_colorb = Parameter(parm=self.node.parm("coat_colorb"))
        self.parm_coat_weight = Parameter(parm=self.node.parm("coat_weight"))
        self.parm_coat_roughness = Parameter(parm=self.node.parm("coat_roughness"))
        self.parm_coat_ior = Parameter(parm=self.node.parm("coat_ior"))
        self.parm_coat_aniso = Parameter(parm=self.node.parm("coat_aniso"))
        self.parm_coat_aniso_rotation = Parameter(
            parm=self.node.parm("coat_aniso_rotation")
        )
        self.parm_coat_samples = Parameter(parm=self.node.parm("coat_samples"))
        self.parm_coat_bump_input = Parameter(parm=self.node.parm("coat_bump_input"))
        self.parm_emission_7 = Parameter(parm=self.node.parm("Emission_7"))
        self.parm_emission_colorr = Parameter(parm=self.node.parm("emission_colorr"))
        self.parm_emission_colorg = Parameter(parm=self.node.parm("emission_colorg"))
        self.parm_emission_colorb = Parameter(parm=self.node.parm("emission_colorb"))
        self.parm_emission_weight = Parameter(parm=self.node.parm("emission_weight"))
        self.parm_geometry_8 = Parameter(parm=self.node.parm("Geometry_8"))
        self.parm_opacity_colorr = Parameter(parm=self.node.parm("opacity_colorr"))
        self.parm_opacity_colorg = Parameter(parm=self.node.parm("opacity_colorg"))
        self.parm_opacity_colorb = Parameter(parm=self.node.parm("opacity_colorb"))
        self.parm_refr_thin_walled = Parameter(parm=self.node.parm("refr_thin_walled"))
        self.parm_bump_input = Parameter(parm=self.node.parm("bump_input"))
        self.parm_overall_colorr = Parameter(parm=self.node.parm("overall_colorr"))
        self.parm_overall_colorg = Parameter(parm=self.node.parm("overall_colorg"))
        self.parm_overall_colorb = Parameter(parm=self.node.parm("overall_colorb"))
        self.parm_overallaffectsemission = Parameter(
            parm=self.node.parm("overallAffectsEmission")
        )
        self.parm_depth_override = Parameter(parm=self.node.parm("depth_override"))
        self.parm_combined_depth = Parameter(parm=self.node.parm("combined_depth"))
        self.parm_reflection_9 = Parameter(parm=self.node.parm("Reflection_9"))
        self.parm_refl_depth = Parameter(parm=self.node.parm("refl_depth"))
        self.parm_refl_enablecutoff = Parameter(
            parm=self.node.parm("refl_enablecutoff")
        )
        self.parm_refl_cutoff = Parameter(parm=self.node.parm("refl_cutoff"))
        self.parm_transmission_10 = Parameter(parm=self.node.parm("Transmission_10"))
        self.parm_refr_depth = Parameter(parm=self.node.parm("refr_depth"))
        self.parm_refr_enablecutoff = Parameter(
            parm=self.node.parm("refr_enablecutoff")
        )
        self.parm_refr_cutoff = Parameter(parm=self.node.parm("refr_cutoff"))
        self.parm_refl_enablemultiscattercomp = Parameter(
            parm=self.node.parm("refl_enableMultiScatterComp")
        )
        self.parm_diffuse_11 = Parameter(parm=self.node.parm("Diffuse_11"))
        self.parm_diffuse_direct = Parameter(parm=self.node.parm("diffuse_direct"))
        self.parm_diffuse_indirect = Parameter(parm=self.node.parm("diffuse_indirect"))
        self.parm_reflection_12 = Parameter(parm=self.node.parm("Reflection_12"))
        self.parm_refl_direct = Parameter(parm=self.node.parm("refl_direct"))
        self.parm_refl_indirect = Parameter(parm=self.node.parm("refl_indirect"))
        self.parm_refl_isglossiness = Parameter(
            parm=self.node.parm("refl_isGlossiness")
        )
        self.parm_transmission_13 = Parameter(parm=self.node.parm("Transmission_13"))
        self.parm_shadow_opacity = Parameter(parm=self.node.parm("shadow_opacity"))
        self.parm_refr_isglossiness = Parameter(
            parm=self.node.parm("refr_isGlossiness")
        )
        self.parm_affects_alpha = Parameter(parm=self.node.parm("affects_alpha"))
        self.parm_block_volumes = Parameter(parm=self.node.parm("block_volumes"))
        self.parm_sheen_14 = Parameter(parm=self.node.parm("Sheen_14"))
        self.parm_sheen_direct = Parameter(parm=self.node.parm("sheen_direct"))
        self.parm_sheen_indirect = Parameter(parm=self.node.parm("sheen_indirect"))
        self.parm_sheen_isglossiness = Parameter(
            parm=self.node.parm("sheen_isGlossiness")
        )
        self.parm_coat_15 = Parameter(parm=self.node.parm("Coat_15"))
        self.parm_coat_direct = Parameter(parm=self.node.parm("coat_direct"))
        self.parm_coat_indirect = Parameter(parm=self.node.parm("coat_indirect"))
        self.parm_coat_isglossiness = Parameter(
            parm=self.node.parm("coat_isGlossiness")
        )
        self.parm_anisotropy_16 = Parameter(parm=self.node.parm("Anisotropy_16"))
        self.parm_anisotropy_uvchannel = Parameter(
            parm=self.node.parm("anisotropy_uvChannel")
        )
        self.parm_anisotropy_tangentchannel = Parameter(
            parm=self.node.parm("anisotropy_tangentChannel")
        )
        self.parm_shader_skipdefvalparms = Parameter(
            parm=self.node.parm("shader_skipdefvalparms")
        )

        # parm menu vars:
        self.parm_diffuse_model = DiffuseModelMenu(parm=self.node.parm("diffuse_model"))
        self.parm_ms_mode = MsModeMenu(parm=self.node.parm("ms_mode"))
        self.parm_ms_include_mode = MsIncludeModeMenu(
            parm=self.node.parm("ms_include_mode")
        )
        self.parm_refl_endmode = ReflEndmodeMenu(parm=self.node.parm("refl_endmode"))
        self.parm_anisotropy_orientation = AnisotropyOrientationMenu(
            parm=self.node.parm("anisotropy_orientation")
        )

        # input vars:
        self.input_base_color = "base_color"
        self.input_base_color_weight = "base_color_weight"
        self.input_diffuse_roughness = "diffuse_roughness"
        self.input_metalness = "metalness"
        self.input_refl_color = "refl_color"
        self.input_refl_weight = "refl_weight"
        self.input_refl_roughness = "refl_roughness"
        self.input_refl_ior = "refl_ior"
        self.input_refl_aniso = "refl_aniso"
        self.input_refl_aniso_rotation = "refl_aniso_rotation"
        self.input_refr_color = "refr_color"
        self.input_refr_weight = "refr_weight"
        self.input_refr_roughness = "refr_roughness"
        self.input_ss_depth = "ss_depth"
        self.input_ss_scatter_color = "ss_scatter_color"
        self.input_refr_abbe = "refr_abbe"
        self.input_ms_color = "ms_color"
        self.input_ms_amount = "ms_amount"
        self.input_ms_radius = "ms_radius"
        self.input_ms_phase = "ms_phase"
        self.input_sheen_color = "sheen_color"
        self.input_sheen_weight = "sheen_weight"
        self.input_sheen_roughness = "sheen_roughness"
        self.input_thinfilm_ior = "thinfilm_ior"
        self.input_thinfilm_thickness = "thinfilm_thickness"
        self.input_coat_color = "coat_color"
        self.input_coat_weight = "coat_weight"
        self.input_coat_roughness = "coat_roughness"
        self.input_coat_ior = "coat_ior"
        self.input_coat_aniso = "coat_aniso"
        self.input_coat_aniso_rotation = "coat_aniso_rotation"
        self.input_coat_bump_input = "coat_bump_input"
        self.input_emission_color = "emission_color"
        self.input_opacity_color = "opacity_color"
        self.input_bump_input = "bump_input"
        self.input_overall_color = "overall_color"


# parm menu classes:
class DiffuseModelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_oren_nayar = ("0", 0)
        self.menu_d_eon_lambertian_spheres = ("1", 1)


class MsModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_point_based_diffusion = ("0", 0)
        self.menu_ray_traced_diffusion = ("1", 1)
        self.menu_random_walk = ("2", 2)


class MsIncludeModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_objects = ("0", 0)
        self.menu_only_self = ("1", 1)


class ReflEndmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_environment = ("0", 0)
        self.menu_diffuse = ("1", 1)


class AnisotropyOrientationMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("2", 0)
        self.menu_from_tangent_channel = ("1", 1)
