from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SbsArchiveNode(OXNode):
    node_type = 'labs::sbs_archive'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'file': 'file', 'reload': 'reload', 'size1': 'size1', 'size2': 'size2', 'sizemenu': 'sizemenu', 'substance_parms': 'substance_parms', 'name_image_plane_from_usage': 'name_image_plane_from_usage', 'scopergba': 'scopergba', 'pscope': 'pscope', 'fscope': 'fscope', 'frange1': 'frange1', 'frange2': 'frange2', 'fdropoff1': 'fdropoff1', 'fdropoff2': 'fdropoff2', 'fdropfunc': 'fdropfunc', 'foutside': 'foutside', 'flist': 'flist', 'fmenu': 'fmenu', 'fautoadjust': 'fautoadjust', 'currange': 'currange', 'stdswitcher31': 'stdswitcher31', 'substance_parms2': 'substance_parms2', 'sbs__randomseed': 'sbs__randomseed', 'sbs_stone_colorr': 'sbs_stone_colorr', 'sbs_stone_colorg': 'sbs_stone_colorg', 'sbs_stone_colorb': 'sbs_stone_colorb', 'sbs_stone_roughness': 'sbs_stone_roughness', 'sbs_lichen_density': 'sbs_lichen_density', 'sbs_lichen_colorr': 'sbs_lichen_colorr', 'sbs_lichen_colorg': 'sbs_lichen_colorg', 'sbs_lichen_colorb': 'sbs_lichen_colorb', 'sbs_rock_rotation': 'sbs_rock_rotation', 'sbs_dirt_spread': 'sbs_dirt_spread', 'sbs_dirt_colorr': 'sbs_dirt_colorr', 'sbs_dirt_colorg': 'sbs_dirt_colorg', 'sbs_dirt_colorb': 'sbs_dirt_colorb', 'sbs_dirt_roughness': 'sbs_dirt_roughness', 'sbs_channels': 'sbs_channels', 'sbs_channel_diffuse': 'sbs_channel_diffuse', 'sbs_channel_basecolor': 'sbs_channel_basecolor', 'sbs_channel_normal': 'sbs_channel_normal', 'sbs_channel_specular': 'sbs_channel_specular', 'sbs_channel_glossiness': 'sbs_channel_glossiness', 'sbs_channel_roughness': 'sbs_channel_roughness', 'sbs_channel_metallic': 'sbs_channel_metallic', 'sbs_channel_height': 'sbs_channel_height', 'sbs_channel_ambientocclusion': 'sbs_channel_ambientocclusion', 'sbs_technical_parameters': 'sbs_technical_parameters', 'sbs_luminosity': 'sbs_luminosity', 'sbs_contrast': 'sbs_contrast', 'sbs_hue_shift': 'sbs_hue_shift', 'sbs_saturation': 'sbs_saturation', 'sbs_normal_intensity': 'sbs_normal_intensity', 'sbs_normal_format': 'sbs_normal_format', 'sbs_height_range': 'sbs_height_range', 'sbs_height_position': 'sbs_height_position', 'sbs_ambientocclusion_intensity': 'sbs_ambientocclusion_intensity'}

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
        self.parm_reload = Parameter(parm=self.node.parm('reload'))
        self.parm_size1 = Parameter(parm=self.node.parm('size1'))
        self.parm_size2 = Parameter(parm=self.node.parm('size2'))
        self.parm_substance_parms = Parameter(parm=self.node.parm('substance_parms'))
        self.parm_name_image_plane_from_usage = Parameter(parm=self.node.parm('name_image_plane_from_usage'))
        self.parm_scopergba = Parameter(parm=self.node.parm('scopergba'))
        self.parm_frange1 = Parameter(parm=self.node.parm('frange1'))
        self.parm_frange2 = Parameter(parm=self.node.parm('frange2'))
        self.parm_fdropoff1 = Parameter(parm=self.node.parm('fdropoff1'))
        self.parm_fdropoff2 = Parameter(parm=self.node.parm('fdropoff2'))
        self.parm_foutside = Parameter(parm=self.node.parm('foutside'))
        self.parm_flist = Parameter(parm=self.node.parm('flist'))
        self.parm_fautoadjust = Parameter(parm=self.node.parm('fautoadjust'))
        self.parm_currange = Parameter(parm=self.node.parm('currange'))
        self.parm_stdswitcher31 = Parameter(parm=self.node.parm('stdswitcher31'))
        self.parm_substance_parms2 = Parameter(parm=self.node.parm('substance_parms2'))
        self.parm_sbs__randomseed = Parameter(parm=self.node.parm('sbs__randomseed'))
        self.parm_sbs_stone_colorr = Parameter(parm=self.node.parm('sbs_stone_colorr'))
        self.parm_sbs_stone_colorg = Parameter(parm=self.node.parm('sbs_stone_colorg'))
        self.parm_sbs_stone_colorb = Parameter(parm=self.node.parm('sbs_stone_colorb'))
        self.parm_sbs_stone_roughness = Parameter(parm=self.node.parm('sbs_stone_roughness'))
        self.parm_sbs_lichen_density = Parameter(parm=self.node.parm('sbs_lichen_density'))
        self.parm_sbs_lichen_colorr = Parameter(parm=self.node.parm('sbs_lichen_colorr'))
        self.parm_sbs_lichen_colorg = Parameter(parm=self.node.parm('sbs_lichen_colorg'))
        self.parm_sbs_lichen_colorb = Parameter(parm=self.node.parm('sbs_lichen_colorb'))
        self.parm_sbs_rock_rotation = Parameter(parm=self.node.parm('sbs_rock_rotation'))
        self.parm_sbs_dirt_spread = Parameter(parm=self.node.parm('sbs_dirt_spread'))
        self.parm_sbs_dirt_colorr = Parameter(parm=self.node.parm('sbs_dirt_colorr'))
        self.parm_sbs_dirt_colorg = Parameter(parm=self.node.parm('sbs_dirt_colorg'))
        self.parm_sbs_dirt_colorb = Parameter(parm=self.node.parm('sbs_dirt_colorb'))
        self.parm_sbs_dirt_roughness = Parameter(parm=self.node.parm('sbs_dirt_roughness'))
        self.parm_sbs_channels = Parameter(parm=self.node.parm('sbs_channels'))
        self.parm_sbs_channel_diffuse = Parameter(parm=self.node.parm('sbs_channel_diffuse'))
        self.parm_sbs_channel_basecolor = Parameter(parm=self.node.parm('sbs_channel_basecolor'))
        self.parm_sbs_channel_normal = Parameter(parm=self.node.parm('sbs_channel_normal'))
        self.parm_sbs_channel_specular = Parameter(parm=self.node.parm('sbs_channel_specular'))
        self.parm_sbs_channel_glossiness = Parameter(parm=self.node.parm('sbs_channel_glossiness'))
        self.parm_sbs_channel_roughness = Parameter(parm=self.node.parm('sbs_channel_roughness'))
        self.parm_sbs_channel_metallic = Parameter(parm=self.node.parm('sbs_channel_metallic'))
        self.parm_sbs_channel_height = Parameter(parm=self.node.parm('sbs_channel_height'))
        self.parm_sbs_channel_ambientocclusion = Parameter(parm=self.node.parm('sbs_channel_ambientocclusion'))
        self.parm_sbs_technical_parameters = Parameter(parm=self.node.parm('sbs_technical_parameters'))
        self.parm_sbs_luminosity = Parameter(parm=self.node.parm('sbs_luminosity'))
        self.parm_sbs_contrast = Parameter(parm=self.node.parm('sbs_contrast'))
        self.parm_sbs_hue_shift = Parameter(parm=self.node.parm('sbs_hue_shift'))
        self.parm_sbs_saturation = Parameter(parm=self.node.parm('sbs_saturation'))
        self.parm_sbs_normal_intensity = Parameter(parm=self.node.parm('sbs_normal_intensity'))
        self.parm_sbs_height_range = Parameter(parm=self.node.parm('sbs_height_range'))
        self.parm_sbs_height_position = Parameter(parm=self.node.parm('sbs_height_position'))
        self.parm_sbs_ambientocclusion_intensity = Parameter(parm=self.node.parm('sbs_ambientocclusion_intensity'))

        
        # parm menu vars:
        self.parm_file = FileMenu(parm=self.node.parm('file'))
        self.parm_sizemenu = SizemenuMenu(parm=self.node.parm('sizemenu'))
        self.parm_pscope = PscopeMenu(parm=self.node.parm('pscope'))
        self.parm_fscope = FscopeMenu(parm=self.node.parm('fscope'))
        self.parm_fdropfunc = FdropfuncMenu(parm=self.node.parm('fdropfunc'))
        self.parm_fmenu = FmenuMenu(parm=self.node.parm('fmenu'))
        self.parm_sbs_normal_format = SbsNormalFormatMenu(parm=self.node.parm('sbs_normal_format'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class FileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_subst___wild_grass_sbsar = ("E:/ART_OLD/SUBSTANCES/00_SBSAR/stylized_wild_grass.sbsar", 0)
        self.menu_e__art_old_subst___cliff_rock_sbsar = ("E:/ART_OLD/SUBSTANCES/00_SBSAR/limestone_cliff_rock.sbsar", 1)
        self.menu_e__art_old_subst___ield_grass_sbsar = ("E:/ART_OLD/SUBSTANCES/00_SBSAR/stylized_small_field_grass.sbsar", 2)
        self.menu_g__shared_drives___9afe0fdb05fd_vox = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/vox_out/70685e07-ab3f-4666-a2ef-9afe0fdb05fd.vox", 3)
        self.menu_g__shared_drives___da1d7adf0724_vox = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/vox_out/00d315af-59af-4ff6-88a3-da1d7adf0724.vox", 4)
        self.menu_g__shared_drives___06aa76b0c67f_vox = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/vox_out/891ea123-1887-4d16-832c-06aa76b0c67f.vox", 5)
        self.menu__hip_test_meevil_output_gltf = ("$HIP/test_meevil_output.gltf", 6)
        self.menu_g__shared_drives___2595ce07864a_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0f0e1850-3f81-479b-aced-2595ce07864a.glb", 7)
        self.menu_g__shared_drives___8d389ba1e5e1_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0dad7559-f852-4170-b315-8d389ba1e5e1.glb", 8)
        self.menu__hip_meevil_mat_test_fbx = ("$HIP/meevil_mat_test.fbx", 9)
        self.menu__hip_meevil_test_abc = ("$HIP/meevil_test.abc", 10)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/pyrite_quartz_scatter/$HIPNAME.$OS.$F4.exr", 11)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/$HIPNAME.$OS.$F4.exr", 12)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/pyrite_small/$HIPNAME.$OS.$F4.exr", 13)
        self.menu_j__temp_misc_hou____os__aov__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/aov_crystal_test/$HIPNAME.$OS.$AOV.$F4.exr", 14)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/aov_crystal_test/$HIPNAME.$OS.$F4.exr", 15)
        self.menu__hip_exported_cr___stal_cluster_fbx = ("$HIP/exported_crystals/crystal_cluster.fbx", 16)
        self.menu_j__bmo_renders_p___name__os__f4_exr = ("J:/BMO_RENDERS/pdg_quarts_crystal/$HIPNAME.$OS.$F4.exr", 17)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/crystal_out/$HIPNAME.$OS.$F4.exr", 18)
        self.menu__hip_geo_quartz____g_index__bgeo_sc = ("$HIP/geo/quartz_test/$HIPNAME.$OS.`@pdg_index`.bgeo.sc", 19)


class SizemenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_480_640 = ("640 480 1", 0)
        self.menu_hdtv_720 = ("1280 720 1", 1)
        self.menu_hdtv_1080 = ("1920 1080 1", 2)
        self.menu_hdtv_2160__4k_ = ("3840 2160 1", 3)
        self.menu__________ = ("_separator_", 4)
        self.menu_ntsc = ("640 486 1", 5)
        self.menu_ntsc_d1 = ("720 486 0.9", 6)
        self.menu_pal = ("768 576 1", 7)
        self.menu_pal_d1 = ("720 576 1.067", 8)
        self.menu_pal_16_9_anamorphic = ("720 576 1.422", 9)
        self.menu_pal_16_9__1_to_1_ = ("1024 576 1", 10)
        self.menu__________ = ("_separator_", 11)
        self.menu_full_ap_4k = ("4096 3112 1", 12)
        self.menu_full_ap_2k = ("2048 1556 1", 13)
        self.menu_acad_4k = ("3656 2664 1", 14)
        self.menu_acad_2k = ("1828 1332 1", 15)
        self.menu_scope_4k = ("3656 3112 1", 16)
        self.menu_scope_2k = ("1828 1556 1", 17)
        self.menu_vista_4k = ("6144 4096 1", 18)
        self.menu_vista_2k = ("3072 2048 1", 19)
        self.menu__________ = ("_separator_", 20)
        self.menu__2_256 = ("256 256 1", 21)
        self.menu__2_512 = ("512 512 1", 22)
        self.menu__2_1024 = ("1024 1024 1", 23)
        self.menu__2_2048 = ("2048 2048 1", 24)
        self.menu__2_4096 = ("4096 4096 1", 25)
        self.menu__2_8192 = ("8192 8192 1", 26)


class PscopeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_480_640 = ("640 480 1", 0)


class FscopeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_frames = ("all", 0)
        self.menu_inside_range = ("inside", 1)
        self.menu_outside_range = ("outside", 2)
        self.menu_even_frames = ("even", 3)
        self.menu_odd_frames = ("odd", 4)
        self.menu_specific_frames = ("specific", 5)


class FdropfuncMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear = ("linear", 0)
        self.menu_ease_in = ("easein", 1)
        self.menu_ease_out = ("easeout", 2)
        self.menu_ease_in_ease_out = ("easeinout", 3)


class FmenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scope_all_frames = ("scopeall", 0)
        self.menu_scope_current_frame = ("scopecur", 1)
        self.menu_scope_from_start_to_current = ("scopetocur", 2)
        self.menu_scope_from_current_to_end = ("scopefromcur", 3)
        self.menu_unscope_all_frames = ("unscopeall", 4)
        self.menu_unscope_current_frame = ("unscopecur", 5)
        self.menu_unscope_from_start_to_current = ("unscopetocur", 6)
        self.menu_unscope_from_current_to_end = ("unscopefromcur", 7)


class SbsNormalFormatMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_directx = ("DirectX", 0)
        self.menu_opengl = ("OpenGL", 1)



