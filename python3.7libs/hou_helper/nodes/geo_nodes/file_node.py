from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class FileNode(HHNode):
    node_type = 'file'
    parm_lookup_dict = {'filemode': 'filemode', 'file': 'file', 'reload': 'reload', 'objpattern': 'objpattern', 'geodatapath': 'geodatapath', 'missingframe': 'missingframe', 'loadtype': 'loadtype', 'packedviewedit': 'packedviewedit', 'viewportlod': 'viewportlod', 'packexpanded': 'packexpanded', 'delayload': 'delayload', 'mkpath': 'mkpath', 'cachesize': 'cachesize', 'prefetch': 'prefetch', 'f1': 'f1', 'f2': 'f2', 'index': 'index', 'wrap': 'wrap', 'retry': 'retry'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
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
        self.parm_filemode_menu = FilemodeMenu(parm=self.node.parm('filemode'))
        self.parm_file_menu = FileMenu(parm=self.node.parm('file'))
        self.parm_missingframe_menu = MissingframeMenu(parm=self.node.parm('missingframe'))
        self.parm_loadtype_menu = LoadtypeMenu(parm=self.node.parm('loadtype'))
        self.parm_packedviewedit_menu = PackedvieweditMenu(parm=self.node.parm('packedviewedit'))
        self.parm_viewportlod_menu = ViewportlodMenu(parm=self.node.parm('viewportlod'))
        self.parm_wrap_menu = WrapMenu(parm=self.node.parm('wrap'))


        # input vars:
        self.input_input_1 = 0


# parm menu classes:
class FilemodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.automatic = 0
        self.read_files = 1
        self.write_files = 2
        self.no_operation = 3


class FileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self._chs__file___ = 0
        self.e__art_3d_00_my____las_4_forest_fbx = 1
        self.e__art_3d_00_my____las_4_forest_abc = 2
        self.e__art_3d_from_t___e_first_wind_abc = 3
        self.e__art_projects____dgum_field_2_fbx = 4
        self.e__art_projects____dgum_field_1_fbx = 5
        self.e__art_3d_from_t____first_wind3_abc = 6
        self.e__art_3d_from_t____wind_groups_abc = 7
        self.e__art_3d_from_t___ind_particle_abc = 8
        self.e__art_projects____s_spline_01_bgeo = 9
        self.e__art_projects____dgum_field_2_fbx = 10


class MissingframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.report_error = 0
        self.no_geometry = 1


class LoadtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.all_geometry = 0
        self.info_bounding_box = 1
        self.info = 2
        self.point_cloud = 3
        self.packed_disk_primitive = 4
        self.packed_disk_sequence = 5


class PackedvieweditMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.use_file_setting = 0
        self.full_geometry = 1
        self.point_cloud = 2
        self.bounding_box = 3
        self.centroid = 4
        self.hidden = 5


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.full_geometry = 0
        self.point_cloud = 1
        self.bounding_box = 2
        self.centroid = 3
        self.hidden = 4


class WrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.cycle = 0
        self.clamp = 1
        self.strict = 2
        self.mirror = 3



