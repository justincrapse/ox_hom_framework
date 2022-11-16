from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class FileNode(OXNode):
    node_type = 'file'
    parm_lookup_dict = {'filemode': 'filemode', 'file': 'file', 'reload': 'reload', 'objpattern': 'objpattern', 'geodatapath': 'geodatapath', 'missingframe': 'missingframe', 'loadtype': 'loadtype', 'packedviewedit': 'packedviewedit', 'viewportlod': 'viewportlod', 'packexpanded': 'packexpanded', 'delayload': 'delayload', 'mkpath': 'mkpath', 'cachesize': 'cachesize', 'prefetch': 'prefetch', 'f1': 'f1', 'f2': 'f2', 'index': 'index', 'wrap': 'wrap', 'retry': 'retry'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_reload = Parameter(parm=self.node.parm('reload'))
        self.parm_objpattern = Parameter(parm=self.node.parm('objpattern'))
        self.parm_geodatapath = Parameter(parm=self.node.parm('geodatapath'))
        self.parm_packexpanded = Parameter(parm=self.node.parm('packexpanded'))
        self.parm_delayload = Parameter(parm=self.node.parm('delayload'))
        self.parm_mkpath = Parameter(parm=self.node.parm('mkpath'))
        self.parm_cachesize = Parameter(parm=self.node.parm('cachesize'))
        self.parm_prefetch = Parameter(parm=self.node.parm('prefetch'))
        self.parm_f1 = Parameter(parm=self.node.parm('f1'))
        self.parm_f2 = Parameter(parm=self.node.parm('f2'))
        self.parm_index = Parameter(parm=self.node.parm('index'))
        self.parm_retry = Parameter(parm=self.node.parm('retry'))

        
        # parm menu vars:
        self.parm_filemode = FilemodeMenu(parm=self.node.parm('filemode'))
        self.parm_file = FileMenu(parm=self.node.parm('file'))
        self.parm_missingframe = MissingframeMenu(parm=self.node.parm('missingframe'))
        self.parm_loadtype = LoadtypeMenu(parm=self.node.parm('loadtype'))
        self.parm_packedviewedit = PackedvieweditMenu(parm=self.node.parm('packedviewedit'))
        self.parm_viewportlod = ViewportlodMenu(parm=self.node.parm('viewportlod'))
        self.parm_wrap = WrapMenu(parm=self.node.parm('wrap'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class FilemodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_read_files = ("read", 1)
        self.menu_write_files = ("write", 2)
        self.menu_no_operation = ("none", 3)


class FileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_d__art_projects____che1__f4_bgeo_sc = ("D:/ART/PROJECTS/NEBULA/geo/NEBULA_supercharged_wist.filecache1/NEBULA_supercharged_wist.filecache1.$F4.bgeo.sc", 0)
        self.menu__hip_statue_bgeo_sc = ("$HIP/statue.bgeo.sc", 1)
        self.menu_e__art_projects____geo_upgraded_abc = ("E:/ART/PROJECTS/sword/full_sword_geo_upgraded.abc", 2)
        self.menu_e__art_projects____ll_sword_geo_abc = ("E:/ART/PROJECTS/sword/full_sword_geo.abc", 3)
        self.menu_e__art_projects____l_sword_geo_bgeo = ("E:/ART/PROJECTS/sword/full_sword_geo.bgeo", 4)


class MissingframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_report_error = ("error", 0)
        self.menu_no_geometry = ("empty", 1)


class LoadtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_geometry = ("full", 0)
        self.menu_info_bounding_box = ("infobbox", 1)
        self.menu_info = ("info", 2)
        self.menu_point_cloud = ("points", 3)
        self.menu_packed_disk_primitive = ("delayed", 4)
        self.menu_packed_disk_sequence = ("packedseq", 5)
        self.menu_packed_geometry = ("packedgeo", 6)


class PackedvieweditMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_use_file_setting = ("unchanged", 0)
        self.menu_full_geometry = ("full", 1)
        self.menu_point_cloud = ("points", 2)
        self.menu_bounding_box = ("box", 3)
        self.menu_centroid = ("centroid", 4)
        self.menu_hidden = ("hidden", 5)


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = ("full", 0)
        self.menu_point_cloud = ("points", 1)
        self.menu_bounding_box = ("box", 2)
        self.menu_centroid = ("centroid", 3)
        self.menu_hidden = ("hidden", 4)


class WrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_cycle = ("cycle", 0)
        self.menu_clamp = ("clamp", 1)
        self.menu_strict = ("strick", 2)
        self.menu_mirror = ("mirror", 3)



