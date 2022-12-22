from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ScatterNode(OXNode):
    node_type = 'scatter::2.0'
    parm_lookup_dict = {'group': 'group', 'stdswitcher1': 'stdswitcher1', 'generateby': 'generateby', 'indepvoxel': 'indepvoxel', 'forcetotal': 'forcetotal', 'npts': 'npts', 'densityscale': 'densityscale', 'usedensityattrib': 'usedensityattrib', 'densityattrib': 'densityattrib', 'useareaattrib': 'useareaattrib', 'areaattrib': 'areaattrib', 'useareaforvolumes': 'useareaforvolumes', 'usedensitytexture': 'usedensitytexture', 'densitytexture': 'densitytexture', 'uvattrib': 'uvattrib', 'primcountattrib': 'primcountattrib', 'useemergencylimit': 'useemergencylimit', 'emergencylimit': 'emergencylimit', 'seed': 'seed', 'overrideprimseed': 'overrideprimseed', 'primseedattrib': 'primseedattrib', 'randomizeorder': 'randomizeorder', 'relaxpoints': 'relaxpoints', 'relaxiterations': 'relaxiterations', 'scaleradiiby': 'scaleradiiby', 'usemaxradius': 'usemaxradius', 'maxradius': 'maxradius', 'useprimnumattrib': 'useprimnumattrib', 'primnumattrib': 'primnumattrib', 'useprimuvwattrib': 'useprimuvwattrib', 'primuvwattrib': 'primuvwattrib', 'useoutputdensityattrib': 'useoutputdensityattrib', 'outputdensityattrib': 'outputdensityattrib', 'useoutputradiusattrib': 'useoutputradiusattrib', 'outputradiusattrib': 'outputradiusattrib', 'radiusintexturespace': 'radiusintexturespace', 'pointattribs': 'pointattribs', 'vertattribs': 'vertattribs', 'primattribs': 'primattribs', 'detailattribs': 'detailattribs'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_indepvoxel = Parameter(parm=self.node.parm('indepvoxel'))
        self.parm_forcetotal = Parameter(parm=self.node.parm('forcetotal'))
        self.parm_npts = Parameter(parm=self.node.parm('npts'))
        self.parm_densityscale = Parameter(parm=self.node.parm('densityscale'))
        self.parm_usedensityattrib = Parameter(parm=self.node.parm('usedensityattrib'))
        self.parm_densityattrib = Parameter(parm=self.node.parm('densityattrib'))
        self.parm_useareaattrib = Parameter(parm=self.node.parm('useareaattrib'))
        self.parm_areaattrib = Parameter(parm=self.node.parm('areaattrib'))
        self.parm_useareaforvolumes = Parameter(parm=self.node.parm('useareaforvolumes'))
        self.parm_usedensitytexture = Parameter(parm=self.node.parm('usedensitytexture'))
        self.parm_uvattrib = Parameter(parm=self.node.parm('uvattrib'))
        self.parm_primcountattrib = Parameter(parm=self.node.parm('primcountattrib'))
        self.parm_useemergencylimit = Parameter(parm=self.node.parm('useemergencylimit'))
        self.parm_emergencylimit = Parameter(parm=self.node.parm('emergencylimit'))
        self.parm_seed = Parameter(parm=self.node.parm('seed'))
        self.parm_overrideprimseed = Parameter(parm=self.node.parm('overrideprimseed'))
        self.parm_primseedattrib = Parameter(parm=self.node.parm('primseedattrib'))
        self.parm_randomizeorder = Parameter(parm=self.node.parm('randomizeorder'))
        self.parm_relaxpoints = Parameter(parm=self.node.parm('relaxpoints'))
        self.parm_relaxiterations = Parameter(parm=self.node.parm('relaxiterations'))
        self.parm_scaleradiiby = Parameter(parm=self.node.parm('scaleradiiby'))
        self.parm_usemaxradius = Parameter(parm=self.node.parm('usemaxradius'))
        self.parm_maxradius = Parameter(parm=self.node.parm('maxradius'))
        self.parm_useprimnumattrib = Parameter(parm=self.node.parm('useprimnumattrib'))
        self.parm_primnumattrib = Parameter(parm=self.node.parm('primnumattrib'))
        self.parm_useprimuvwattrib = Parameter(parm=self.node.parm('useprimuvwattrib'))
        self.parm_primuvwattrib = Parameter(parm=self.node.parm('primuvwattrib'))
        self.parm_useoutputdensityattrib = Parameter(parm=self.node.parm('useoutputdensityattrib'))
        self.parm_outputdensityattrib = Parameter(parm=self.node.parm('outputdensityattrib'))
        self.parm_useoutputradiusattrib = Parameter(parm=self.node.parm('useoutputradiusattrib'))
        self.parm_outputradiusattrib = Parameter(parm=self.node.parm('outputradiusattrib'))
        self.parm_radiusintexturespace = Parameter(parm=self.node.parm('radiusintexturespace'))
        self.parm_pointattribs = Parameter(parm=self.node.parm('pointattribs'))
        self.parm_vertattribs = Parameter(parm=self.node.parm('vertattribs'))
        self.parm_primattribs = Parameter(parm=self.node.parm('primattribs'))
        self.parm_detailattribs = Parameter(parm=self.node.parm('detailattribs'))

        
        # parm menu vars:
        self.parm_generateby = GeneratebyMenu(parm=self.node.parm('generateby'))
        self.parm_densitytexture = DensitytextureMenu(parm=self.node.parm('densitytexture'))


        # input vars:
        self.input_geometry_to_scatter_points_onto = 'Geometry to scatter points onto'


# parm menu classes:
class GeneratebyMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_by_density = ("bydensity", 0)
        self.menu_count_per_primitive = ("countperprimitive", 1)
        self.menu_in_texture_space = ("texturespace", 2)


class DensitytextureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_render_part___name__os__f4_exr = ("$HIP/render_particle_stars/$HIPNAME.$OS.$F4.exr", 0)
        self.menu__hip_render_neb____name__os__f4_exr = ("$HIP/render_neb_full_360/$HIPNAME.$OS.$F4.exr", 1)
        self.menu__hip_render_whit___name__os__f4_exr = ("$HIP/render_white_desert_closeup/$HIPNAME.$OS.$F4.exr", 2)
        self.menu__hip_tunder_rend___name__os__f4_exr = ("$HIP/tunder_render_closeup/$HIPNAME.$OS.$F4.exr", 3)
        self.menu__hip_render_gras___name__os__f4_exr = ("$HIP/render_grassy_hills_closeup/$HIPNAME.$OS.$F4.exr", 4)
        self.menu__hip_render_gras___name__os__f4_exr = ("$HIP/render_grassy_hills/$HIPNAME.$OS.$F4.exr", 5)
        self.menu__hip_tunder_rend___name__os__f4_exr = ("$HIP/tunder_render/$HIPNAME.$OS.$F4.exr", 6)
        self.menu_e__art_old_3d_as___field_wind_2_abc = ("E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind_2.abc", 7)
        self.menu_e__art_old_3d_as___t_field_wind_abc = ("E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind.abc", 8)
        self.menu_e__renders_houdi___name__os__f4_exr = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/$HIPNAME.$OS.$F4.exr", 9)
        self.menu_e__renders_houdi___r_magic_prev__f3 = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/magic_prev.$F3", 10)
        self.menu_e__art_projects____y_first_hdrlight = ("E:/ART/PROJECTS/00_shared/hdri/my_first_hdrlight", 11)



