from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class QuixelRedshiftTriplanarNode(OXNode):
    node_type = 'quixel_redshift_triplanar::1.0'
    parm_lookup_dict = {'ts1': 'ts1', 'texture': 'texture', 'blendamount': 'blendAmount', 'blendcurve': 'blendCurve', 'coordinates': 'coordinates', 'scalex': 'scalex', 'scaley': 'scaley', 'scalez': 'scalez', 'offsetx': 'offsetx', 'offsety': 'offsety', 'offsetz': 'offsetz', 'rotationx': 'rotationx', 'rotationy': 'rotationy', 'rotationz': 'rotationz', 'projspacetype': 'projSpaceType', 'albedo': 'albedo', 'ao': 'ao', 'bump': 'bump', 'cavity': 'cavity', 'diffuse': 'diffuse', 'displacement': 'displacement', 'gloss': 'gloss', 'fuzz': 'fuzz', 'mask': 'mask', 'metalness': 'metalness', 'normal': 'normal', 'normalbump': 'normalbump', 'opacity': 'opacity', 'roughness': 'roughness', 'specular': 'specular', 'translucency': 'translucency'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_ts1 = Parameter(parm=self.node.parm('ts1'))
        self.parm_texture = Parameter(parm=self.node.parm('texture'))
        self.parm_blendamount = Parameter(parm=self.node.parm('blendAmount'))
        self.parm_blendcurve = Parameter(parm=self.node.parm('blendCurve'))
        self.parm_coordinates = Parameter(parm=self.node.parm('coordinates'))
        self.parm_scalex = Parameter(parm=self.node.parm('scalex'))
        self.parm_scaley = Parameter(parm=self.node.parm('scaley'))
        self.parm_scalez = Parameter(parm=self.node.parm('scalez'))
        self.parm_offsetx = Parameter(parm=self.node.parm('offsetx'))
        self.parm_offsety = Parameter(parm=self.node.parm('offsety'))
        self.parm_offsetz = Parameter(parm=self.node.parm('offsetz'))
        self.parm_rotationx = Parameter(parm=self.node.parm('rotationx'))
        self.parm_rotationy = Parameter(parm=self.node.parm('rotationy'))
        self.parm_rotationz = Parameter(parm=self.node.parm('rotationz'))

        
        # parm menu vars:
        self.parm_projspacetype = ProjspacetypeMenu(parm=self.node.parm('projSpaceType'))
        self.parm_albedo = AlbedoMenu(parm=self.node.parm('albedo'))
        self.parm_ao = AoMenu(parm=self.node.parm('ao'))
        self.parm_bump = BumpMenu(parm=self.node.parm('bump'))
        self.parm_cavity = CavityMenu(parm=self.node.parm('cavity'))
        self.parm_diffuse = DiffuseMenu(parm=self.node.parm('diffuse'))
        self.parm_displacement = DisplacementMenu(parm=self.node.parm('displacement'))
        self.parm_gloss = GlossMenu(parm=self.node.parm('gloss'))
        self.parm_fuzz = FuzzMenu(parm=self.node.parm('fuzz'))
        self.parm_mask = MaskMenu(parm=self.node.parm('mask'))
        self.parm_metalness = MetalnessMenu(parm=self.node.parm('metalness'))
        self.parm_normal = NormalMenu(parm=self.node.parm('normal'))
        self.parm_normalbump = NormalbumpMenu(parm=self.node.parm('normalbump'))
        self.parm_opacity = OpacityMenu(parm=self.node.parm('opacity'))
        self.parm_roughness = RoughnessMenu(parm=self.node.parm('roughness'))
        self.parm_specular = SpecularMenu(parm=self.node.parm('specular'))
        self.parm_translucency = TranslucencyMenu(parm=self.node.parm('translucency'))


        # input vars:
        self.input_scale = 'Scale'
        self.input_offset = 'Offset'
        self.input_rotation = 'Rotation'
        self.input_blendamount = 'BlendAmount'


# parm menu classes:
class ProjspacetypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_world = ("0", 0)
        self.menu_object = ("1", 1)
        self.menu_reference = ("2", 2)


class AlbedoMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class AoMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class BumpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class CavityMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class DiffuseMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class DisplacementMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class GlossMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class FuzzMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class MaskMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class MetalnessMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class NormalMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class NormalbumpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class OpacityMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class RoughnessMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class SpecularMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)


class TranslucencyMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___uds_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Sunny.Early.Day.Cumulus.Clouds.HDR.0001.exr", 0)
        self.menu_e__art_old_proje___lus_hdr_0001_exr = ("E:/ART_OLD/PROJECTS/00_shared/cloud_hdri/Patreon_HDRs/Cloudy.Afternoon.Cumulus.HDR.0001.exr", 1)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 2)
        self.menu_e__art_old_proje____sunrise_16k_exr = ("E:/ART_OLD/PROJECTS/00_hdri_hd/kiara_2_sunrise_16k.exr", 3)
        self.menu_opdef__obj_ox_te___mapper1_rock_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?rock.jpg", 4)
        self.menu_opdef___rock_jpg = ("opdef:.?rock.jpg", 5)
        self.menu_opdef___default_texture_jpg = ("opdef:.?default_texture.jpg", 6)
        self.menu_e__art_old_subst___mw_8k_albedo_jpg = ("E:/ART_OLD/SUBSTANCES/desert_rock/ukohaj0mw_8K_Albedo.jpg", 7)
        self.menu_opdef__ox_terrai___ault_texture_jpg = ("opdef:/ox_terrain_texture_mapper1?default_texture.jpg", 8)
        self.menu_opdef__obj_ox_te___ault_texture_jpg = ("opdef:/obj/ox_terrain_texture_mapper1?default_texture.jpg", 9)
        self.menu_mandril_pic = ("Mandril.pic", 10)
        self.menu_default_pic = ("default.pic", 11)



