from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class ScatterNode(HHNode):
    node_type = 'scatter::2.0'
    parm_lookup_dict = {'group': 'group', 'stdswitcher1': 'stdswitcher1', 'generateby': 'generateby', 'densityscale': 'densityscale', 'usedensityattrib': 'usedensityattrib', 'densityattrib': 'densityattrib', 'useareaattrib': 'useareaattrib', 'areaattrib': 'areaattrib', 'indepvoxel': 'indepvoxel', 'useareaforvolumes': 'useareaforvolumes', 'forcetotal': 'forcetotal', 'npts': 'npts', 'usedensitytexture': 'usedensitytexture', 'densitytexture': 'densitytexture', 'primcountattrib': 'primcountattrib', 'useemergencylimit': 'useemergencylimit', 'emergencylimit': 'emergencylimit', 'seed': 'seed', 'overrideprimseed': 'overrideprimseed', 'primseedattrib': 'primseedattrib', 'randomizeorder': 'randomizeorder', 'relaxpoints': 'relaxpoints', 'relaxiterations': 'relaxiterations', 'scaleradiiby': 'scaleradiiby', 'usemaxradius': 'usemaxradius', 'maxradius': 'maxradius', 'useprimnumattrib': 'useprimnumattrib', 'primnumattrib': 'primnumattrib', 'useprimuvwattrib': 'useprimuvwattrib', 'primuvwattrib': 'primuvwattrib', 'useoutputdensityattrib': 'useoutputdensityattrib', 'outputdensityattrib': 'outputdensityattrib', 'useoutputradiusattrib': 'useoutputradiusattrib', 'outputradiusattrib': 'outputradiusattrib', 'radiusintexturespace': 'radiusintexturespace', 'pointattribs': 'pointattribs', 'vertattribs': 'vertattribs', 'primattribs': 'primattribs', 'detailattribs': 'detailattribs'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_densityscale = Parameter(parm=self.node.parm('densityscale'))
        self.parm_usedensityattrib = Parameter(parm=self.node.parm('usedensityattrib'))
        self.parm_useareaattrib = Parameter(parm=self.node.parm('useareaattrib'))
        self.parm_areaattrib = Parameter(parm=self.node.parm('areaattrib'))
        self.parm_indepvoxel = Parameter(parm=self.node.parm('indepvoxel'))
        self.parm_useareaforvolumes = Parameter(parm=self.node.parm('useareaforvolumes'))
        self.parm_forcetotal = Parameter(parm=self.node.parm('forcetotal'))
        self.parm_npts = Parameter(parm=self.node.parm('npts'))
        self.parm_usedensitytexture = Parameter(parm=self.node.parm('usedensitytexture'))
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
        self.parm_vertattribs = Parameter(parm=self.node.parm('vertattribs'))
        self.parm_primattribs = Parameter(parm=self.node.parm('primattribs'))
        self.parm_detailattribs = Parameter(parm=self.node.parm('detailattribs'))

        
        # parm menu vars:
        self.parm_generateby_menu = GeneratebyMenu(parm=self.node.parm('generateby'))
        self.parm_densityattrib_menu = DensityattribMenu(parm=self.node.parm('densityattrib'))
        self.parm_densitytexture_menu = DensitytextureMenu(parm=self.node.parm('densitytexture'))
        self.parm_pointattribs_menu = PointattribsMenu(parm=self.node.parm('pointattribs'))


        # input vars:
        self.input_geometry_to_scatter_points_onto = 0


# parm menu classes:
class GeneratebyMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.by_density = 0
        self.count_per_primitive = 1
        self.in_texture_space = 2


class DensityattribMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.position____p_ = 0


class DensitytextureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self._hip_my_first_tree_prox_rs = 0
        self.c__programdata_r____portra_800_cube = 1
        self._hip_grasses_grass_card_001_fbx = 2
        self.e__art_projects____rock_stone_sbsar = 3
        self.e__art_projects____mud_ground_sbsar = 4
        self.e__art_projects____u_sugi_ban_sbsar = 5
        self.e__art_projects_____facade_02_sbsar = 6
        self.e__art_projects____and_smooth_sbsar = 7
        self._hip_crystallize___ice_nugget_sbsar = 8
        self._hip_chromatic_glass_gradient_sbsar = 9
        self._hip_acid_etched_glass_rough_sbsar = 10
        self.e__art_projects____agon_tiles_sbsar = 11


class PointattribsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.position____p_ = 0



