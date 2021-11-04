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
        self.input_input_1 = 0


# parm menu classes:
class FilemodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = 0
        self.menu_read_files = 1
        self.menu_write_files = 2
        self.menu_no_operation = 3


class FileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_projects_____1_erf_tall3_abc = 0
        self.menu__chs__file___ = 1
        self.menu_e__art_3d_00_my____las_4_forest_fbx = 2
        self.menu_e__art_3d_00_my____las_4_forest_abc = 3
        self.menu_e__art_3d_from_t___e_first_wind_abc = 4
        self.menu_e__art_projects____dgum_field_2_fbx = 5
        self.menu_e__art_projects____dgum_field_1_fbx = 6
        self.menu_e__art_3d_from_t____first_wind3_abc = 7
        self.menu_e__art_3d_from_t____wind_groups_abc = 8
        self.menu_e__art_3d_from_t___ind_particle_abc = 9
        self.menu_e__art_projects____s_spline_01_bgeo = 10
        self.menu_e__art_projects____dgum_field_2_fbx = 11


class MissingframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_report_error = 0
        self.menu_no_geometry = 1


class LoadtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_geometry = 0
        self.menu_info_bounding_box = 1
        self.menu_info = 2
        self.menu_point_cloud = 3
        self.menu_packed_disk_primitive = 4
        self.menu_packed_disk_sequence = 5


class PackedvieweditMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_use_file_setting = 0
        self.menu_full_geometry = 1
        self.menu_point_cloud = 2
        self.menu_bounding_box = 3
        self.menu_centroid = 4
        self.menu_hidden = 5


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = 0
        self.menu_point_cloud = 1
        self.menu_bounding_box = 2
        self.menu_centroid = 3
        self.menu_hidden = 4


class WrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_cycle = 0
        self.menu_clamp = 1
        self.menu_strict = 2
        self.menu_mirror = 3



