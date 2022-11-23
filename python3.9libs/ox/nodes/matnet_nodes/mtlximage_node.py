from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlximageNode(OXNode):
    node_type = 'mtlximage'
    parm_lookup_dict = {'signature': 'signature', 'file': 'file', 'filecolorspace': 'filecolorspace', 'layer': 'layer', 'default': 'default', 'texcoordx': 'texcoordx', 'texcoordy': 'texcoordy', 'uaddressmode': 'uaddressmode', 'vaddressmode': 'vaddressmode', 'filtertype': 'filtertype', 'framerange': 'framerange', 'frameoffset': 'frameoffset', 'frameendaction': 'frameendaction', 'default_color3r': 'default_color3r', 'default_color3g': 'default_color3g', 'default_color3b': 'default_color3b', 'default_color4r': 'default_color4r', 'default_color4g': 'default_color4g', 'default_color4b': 'default_color4b', 'default_color4a': 'default_color4a', 'default_vector2x': 'default_vector2x', 'default_vector2y': 'default_vector2y', 'default_vector3x': 'default_vector3x', 'default_vector3y': 'default_vector3y', 'default_vector3z': 'default_vector3z', 'default_vector4x': 'default_vector4x', 'default_vector4y': 'default_vector4y', 'default_vector4z': 'default_vector4z', 'default_vector4w': 'default_vector4w'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_layer = Parameter(parm=self.node.parm('layer'))
        self.parm_default = Parameter(parm=self.node.parm('default'))
        self.parm_texcoordx = Parameter(parm=self.node.parm('texcoordx'))
        self.parm_texcoordy = Parameter(parm=self.node.parm('texcoordy'))
        self.parm_framerange = Parameter(parm=self.node.parm('framerange'))
        self.parm_frameoffset = Parameter(parm=self.node.parm('frameoffset'))
        self.parm_default_color3r = Parameter(parm=self.node.parm('default_color3r'))
        self.parm_default_color3g = Parameter(parm=self.node.parm('default_color3g'))
        self.parm_default_color3b = Parameter(parm=self.node.parm('default_color3b'))
        self.parm_default_color4r = Parameter(parm=self.node.parm('default_color4r'))
        self.parm_default_color4g = Parameter(parm=self.node.parm('default_color4g'))
        self.parm_default_color4b = Parameter(parm=self.node.parm('default_color4b'))
        self.parm_default_color4a = Parameter(parm=self.node.parm('default_color4a'))
        self.parm_default_vector2x = Parameter(parm=self.node.parm('default_vector2x'))
        self.parm_default_vector2y = Parameter(parm=self.node.parm('default_vector2y'))
        self.parm_default_vector3x = Parameter(parm=self.node.parm('default_vector3x'))
        self.parm_default_vector3y = Parameter(parm=self.node.parm('default_vector3y'))
        self.parm_default_vector3z = Parameter(parm=self.node.parm('default_vector3z'))
        self.parm_default_vector4x = Parameter(parm=self.node.parm('default_vector4x'))
        self.parm_default_vector4y = Parameter(parm=self.node.parm('default_vector4y'))
        self.parm_default_vector4z = Parameter(parm=self.node.parm('default_vector4z'))
        self.parm_default_vector4w = Parameter(parm=self.node.parm('default_vector4w'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))
        self.parm_file = FileMenu(parm=self.node.parm('file'))
        self.parm_filecolorspace = FilecolorspaceMenu(parm=self.node.parm('filecolorspace'))
        self.parm_uaddressmode = UaddressmodeMenu(parm=self.node.parm('uaddressmode'))
        self.parm_vaddressmode = VaddressmodeMenu(parm=self.node.parm('vaddressmode'))
        self.parm_filtertype = FiltertypeMenu(parm=self.node.parm('filtertype'))
        self.parm_frameendaction = FrameendactionMenu(parm=self.node.parm('frameendaction'))


        # input vars:
        self.input_default_color = 'Default Color'
        self.input_texture_coordinates = 'Texture Coordinates'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = ("default", 0)
        self.menu_color = ("color3", 1)
        self.menu_color_4 = ("color4", 2)
        self.menu_vector_2 = ("vector2", 3)
        self.menu_vector_3 = ("vector3", 4)
        self.menu_vector_4 = ("vector4", 5)


class FileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__quixel_librar____normal_lod0_jpg = ("E:/quixel_library/Downloaded/3d/industrial_construction_vk2nfgu/vk2nfgu_4K_Normal_LOD0.jpg", 0)
        self.menu_e__art_old_proje___s_on_fire_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr", 1)
        self.menu_e__art_old_proje___quarry_02_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/quarry_02_4k.exr", 2)
        self.menu_e__art_old_proje____1d_clear_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr", 3)
        self.menu_e__art_old_proje___a_sunrise_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr", 4)
        self.menu_d__art_projects____e_background_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/hdri_exrs/subtle_background.exr", 5)
        self.menu_e__art_old_proje___enheim_05_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr", 6)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 7)
        self.menu_e__art_old_proje___oon_grass_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/noon_grass_4k.exr", 8)
        self.menu_d__art_projects____arfield_hdri_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/first_starfield_hdri.exr", 9)
        self.menu_e__art_old_proje___e_purple_neb_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/purple_neb.jpg", 10)
        self.menu_e__art_old_proje___xl_128051940_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/dreamstime_xxl_128051940.jpg", 11)


class FilecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear___rec_709 = ("lin_rec709", 0)
        self.menu_linear_texture___srgb = ("srgb_texture", 1)


class UaddressmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_clamp = ("clamp", 1)
        self.menu_periodic = ("periodic", 2)
        self.menu_mirror = ("mirror", 3)


class VaddressmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_clamp = ("clamp", 1)
        self.menu_periodic = ("periodic", 2)
        self.menu_mirror = ("mirror", 3)


class FiltertypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_closest = ("closest", 0)
        self.menu_linear = ("linear", 1)
        self.menu_cubic = ("cubic", 2)


class FrameendactionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_clamp = ("clamp", 1)
        self.menu_periodic = ("periodic", 2)
        self.menu_mirror = ("mirror", 3)



