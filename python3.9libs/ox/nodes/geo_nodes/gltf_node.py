from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class GltfNode(OXNode):
    node_type = 'gltf'
    parm_lookup_dict = {'filename': 'filename', 'loadby': 'loadby', 'meshid': 'meshid', 'meshchooser': 'meshchooser', 'primitiveindex': 'primitiveindex', 'nodeid': 'nodeid', 'nodechooser': 'nodechooser', 'scene': 'scene', 'scenechooser': 'scenechooser', 'geotype': 'geotype', 'promotepointattrs': 'promotepointattrs', 'pointconsolidatedist': 'pointconsolidatedist', 'usecustomattribs': 'usecustomattribs', 'loadnames': 'loadnames', 'materialassigns': 'materialassigns', 'addpathattribute': 'addpathattribute', 'pathattribute': 'pathattribute'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_meshid = Parameter(parm=self.node.parm('meshid'))
        self.parm_meshchooser = Parameter(parm=self.node.parm('meshchooser'))
        self.parm_primitiveindex = Parameter(parm=self.node.parm('primitiveindex'))
        self.parm_nodeid = Parameter(parm=self.node.parm('nodeid'))
        self.parm_nodechooser = Parameter(parm=self.node.parm('nodechooser'))
        self.parm_scene = Parameter(parm=self.node.parm('scene'))
        self.parm_scenechooser = Parameter(parm=self.node.parm('scenechooser'))
        self.parm_promotepointattrs = Parameter(parm=self.node.parm('promotepointattrs'))
        self.parm_pointconsolidatedist = Parameter(parm=self.node.parm('pointconsolidatedist'))
        self.parm_usecustomattribs = Parameter(parm=self.node.parm('usecustomattribs'))
        self.parm_loadnames = Parameter(parm=self.node.parm('loadnames'))
        self.parm_materialassigns = Parameter(parm=self.node.parm('materialassigns'))
        self.parm_addpathattribute = Parameter(parm=self.node.parm('addpathattribute'))
        self.parm_pathattribute = Parameter(parm=self.node.parm('pathattribute'))

        
        # parm menu vars:
        self.parm_filename = FilenameMenu(parm=self.node.parm('filename'))
        self.parm_loadby = LoadbyMenu(parm=self.node.parm('loadby'))
        self.parm_geotype = GeotypeMenu(parm=self.node.parm('geotype'))


        # input vars:


# parm menu classes:
class FilenameMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_g__shared_drives___526c419d3b3a_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0ae5bb5f-2683-4527-be5b-526c419d3b3a.glb", 0)
        self.menu__hip_test_anim_out_gltf = ("G:/Shared drives/meevil_pipeline_shared/resources/test_anim_out.gltf", 1)
        self.menu_g__shared_drives___f423e0423d56_glb = ("G:\Shared drives\meevil_pipeline_shared\output\meevils\glb_out\7954da3e-df0c-4ec4-b7c6-f423e0423d56.glb", 2)
        self.menu_g__shared_drives___ffe0afeab1ea_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/99133a1e-b879-4547-b7b5-ffe0afeab1ea.glb", 3)
        self.menu_g__shared_drives___8e9591b0bcca_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/238ed991-bde7-4e9d-9f61-8e9591b0bcca.glb", 4)
        self.menu_g__shared_drives___33bb1b125e37_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/13468745-6c1e-440b-ad68-33bb1b125e37.glb", 5)
        self.menu_g__shared_drives___909127aeebde_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/ed028b3b-890b-4ac5-8baa-909127aeebde.glb", 6)
        self.menu_g__shared_drives___9b0d335cd810_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0f0214e4-d76d-4ad9-aec3-9b0d335cd810.glb", 7)
        self.menu_g__shared_drives___0ee5d4da99ed_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0d2f4177-a776-458e-a038-0ee5d4da99ed.glb", 8)
        self.menu_g__shared_drives___t_traits_glb_out = ("G:\Shared drives\meevil_pipeline_shared\output\traits\glb_out", 9)
        self.menu_g__shared_drives___from_blender_fbx = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/fbx_out/from_blender.fbx", 10)
        self.menu_g__shared_drives___hy_legs_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Legs_Base.fbx", 11)
        self.menu_g__shared_drives___hy_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Body_Base.fbx", 12)
        self.menu__hip_geo_furdude_skel_bgeo_sc = ("$HIP/geo/furdude_skel.bgeo.sc", 13)
        self.menu__hip_geo_furdude_capt_bgeo_sc = ("$HIP/geo/furdude_capt.bgeo.sc", 14)
        self.menu_e__art_old_subst___wild_grass_sbsar = ("E:/ART_OLD/SUBSTANCES/00_SBSAR/stylized_wild_grass.sbsar", 15)
        self.menu_e__art_old_subst___cliff_rock_sbsar = ("E:/ART_OLD/SUBSTANCES/00_SBSAR/limestone_cliff_rock.sbsar", 16)
        self.menu_e__art_old_subst___ield_grass_sbsar = ("E:/ART_OLD/SUBSTANCES/00_SBSAR/stylized_small_field_grass.sbsar", 17)
        self.menu_g__shared_drives___9afe0fdb05fd_vox = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/vox_out/70685e07-ab3f-4666-a2ef-9afe0fdb05fd.vox", 18)
        self.menu_g__shared_drives___da1d7adf0724_vox = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/vox_out/00d315af-59af-4ff6-88a3-da1d7adf0724.vox", 19)
        self.menu_g__shared_drives___06aa76b0c67f_vox = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/vox_out/891ea123-1887-4d16-832c-06aa76b0c67f.vox", 20)
        self.menu__hip_test_meevil_output_gltf = ("$HIP/test_meevil_output.gltf", 21)
        self.menu_g__shared_drives___2595ce07864a_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0f0e1850-3f81-479b-aced-2595ce07864a.glb", 22)
        self.menu_g__shared_drives___8d389ba1e5e1_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0dad7559-f852-4170-b315-8d389ba1e5e1.glb", 23)
        self.menu__hip_meevil_mat_test_fbx = ("$HIP/meevil_mat_test.fbx", 24)
        self.menu__hip_meevil_test_abc = ("$HIP/meevil_test.abc", 25)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/pyrite_quartz_scatter/$HIPNAME.$OS.$F4.exr", 26)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/$HIPNAME.$OS.$F4.exr", 27)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/pyrite_small/$HIPNAME.$OS.$F4.exr", 28)
        self.menu_j__temp_misc_hou____os__aov__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/aov_crystal_test/$HIPNAME.$OS.$AOV.$F4.exr", 29)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/aov_crystal_test/$HIPNAME.$OS.$F4.exr", 30)
        self.menu__hip_exported_cr___stal_cluster_fbx = ("$HIP/exported_crystals/crystal_cluster.fbx", 31)
        self.menu_j__bmo_renders_p___name__os__f4_exr = ("J:/BMO_RENDERS/pdg_quarts_crystal/$HIPNAME.$OS.$F4.exr", 32)
        self.menu_j__temp_misc_hou___name__os__f4_exr = ("J:/TEMP_MISC/HOUDINI/SCRATCH_RENDER/crystal_out/$HIPNAME.$OS.$F4.exr", 33)
        self.menu__hip_geo_quartz____g_index__bgeo_sc = ("$HIP/geo/quartz_test/$HIPNAME.$OS.`@pdg_index`.bgeo.sc", 34)


class LoadbyMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitive = ("primitive", 0)
        self.menu_mesh = ("mesh", 1)
        self.menu_node = ("node", 2)
        self.menu_scene = ("scene", 3)


class GeotypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_flattened_geometry = ("flattenedgeo", 0)
        self.menu_packed_primitive = ("packedprim", 1)



