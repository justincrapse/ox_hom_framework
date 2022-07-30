from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ScatterNode(OXNode):
    node_type = 'scatter::2.0'
    parm_lookup_dict = {'group': 'group', 'stdswitcher1': 'stdswitcher1', 'generateby': 'generateby', 'densityscale': 'densityscale', 'usedensityattrib': 'usedensityattrib', 'densityattrib': 'densityattrib', 'useareaattrib': 'useareaattrib', 'areaattrib': 'areaattrib', 'indepvoxel': 'indepvoxel', 'useareaforvolumes': 'useareaforvolumes', 'forcetotal': 'forcetotal', 'npts': 'npts', 'usedensitytexture': 'usedensitytexture', 'densitytexture': 'densitytexture', 'primcountattrib': 'primcountattrib', 'useemergencylimit': 'useemergencylimit', 'emergencylimit': 'emergencylimit', 'seed': 'seed', 'overrideprimseed': 'overrideprimseed', 'primseedattrib': 'primseedattrib', 'randomizeorder': 'randomizeorder', 'relaxpoints': 'relaxpoints', 'relaxiterations': 'relaxiterations', 'scaleradiiby': 'scaleradiiby', 'usemaxradius': 'usemaxradius', 'maxradius': 'maxradius', 'useprimnumattrib': 'useprimnumattrib', 'primnumattrib': 'primnumattrib', 'useprimuvwattrib': 'useprimuvwattrib', 'primuvwattrib': 'primuvwattrib', 'useoutputdensityattrib': 'useoutputdensityattrib', 'outputdensityattrib': 'outputdensityattrib', 'useoutputradiusattrib': 'useoutputradiusattrib', 'outputradiusattrib': 'outputradiusattrib', 'radiusintexturespace': 'radiusintexturespace', 'pointattribs': 'pointattribs', 'vertattribs': 'vertattribs', 'primattribs': 'primattribs', 'detailattribs': 'detailattribs'}

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
        self.parm_densityscale = Parameter(parm=self.node.parm('densityscale'))
        self.parm_usedensityattrib = Parameter(parm=self.node.parm('usedensityattrib'))
        self.parm_densityattrib = Parameter(parm=self.node.parm('densityattrib'))
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
        self.menu_by_density = "bydensity"
        self.menu_count_per_primitive = "countperprimitive"
        self.menu_in_texture_space = "texturespace"


class DensitytextureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__job_desktop_articulatcf_bold_otf = "$JOB/Desktop/ArticulatCF-Bold.otf"
        self.menu__hip_desktop_articulatcf_bold_otf = "$HIP/Desktop/ArticulatCF-Bold.otf"
        self.menu_e__art_products_ox_mtlx_hf_test_out = "E:/ART/PRODUCTS/OX-MTLX/hf_test_out"
        self.menu_d__minecraft_sub___ded_copper_sbsar = "D:/Minecraft/substance/hazelnut_3/copper_block/grinded_copper.sbsar"
        self.menu_d__minecraft_sub___dirt_field_sbsar = "D:/Minecraft/substance/hazelnut/farmland_wet/arid_dirt_field.sbsar"
        self.menu_e__art_products____ers_rock_cpu_jpg = "E:/ART/PRODUCTS/OX-MTLX/renders/rock_cpu.jpg"
        self.menu_e__art_products____ers_rock_xpu_jpg = "E:/ART/PRODUCTS/OX-MTLX/renders/rock_xpu.jpg"
        self.menu_e__art_products____rs_quilt_xpu_jpg = "E:/ART/PRODUCTS/OX-MTLX/renders/quilt_xpu.jpg"
        self.menu_e__art_products____rs_quilt_cpu_jpg = "E:/ART/PRODUCTS/OX-MTLX/renders/quilt_cpu.jpg"
        self.menu_e__art_products____ers_lava_cpu_jpg = "E:/ART/PRODUCTS/OX-MTLX/renders/lava_cpu.jpg"
        self.menu_e__art_products____ers_lava_xpu_jpg = "E:/ART/PRODUCTS/OX-MTLX/renders/lava_xpu.jpg"
        self.menu_e__art_products____s_glazed_xpu_jpg = "E:/ART/PRODUCTS/OX-MTLX/renders/glazed_xpu.jpg"



