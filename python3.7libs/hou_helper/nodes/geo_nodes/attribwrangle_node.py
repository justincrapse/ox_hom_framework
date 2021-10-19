from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class AttribwrangleNode(HHNode):
    node_type = 'attribwrangle'
    parm_lookup_dict = {'folder01': 'folder01', 'group': 'group', 'grouptype': 'grouptype', 'class_alt': 'class', 'vex_numcount': 'vex_numcount', 'vex_threadjobsize': 'vex_threadjobsize', 'snippet': 'snippet', 'exportlist': 'exportlist', 'vex_strict': 'vex_strict', 'autobind': 'autobind', 'bindings': 'bindings', 'groupautobind': 'groupautobind', 'groupbindings': 'groupbindings', 'vex_cwdpath': 'vex_cwdpath', 'vex_outputmask': 'vex_outputmask', 'vex_updatenmls': 'vex_updatenmls', 'vex_matchattrib': 'vex_matchattrib', 'vex_inplace': 'vex_inplace', 'vex_selectiongroup': 'vex_selectiongroup', 'vex_precision': 'vex_precision'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder01 = Parameter(parm=self.node.parm('folder01'))
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_vex_numcount = Parameter(parm=self.node.parm('vex_numcount'))
        self.parm_vex_threadjobsize = Parameter(parm=self.node.parm('vex_threadjobsize'))
        self.parm_exportlist = Parameter(parm=self.node.parm('exportlist'))
        self.parm_vex_strict = Parameter(parm=self.node.parm('vex_strict'))
        self.parm_autobind = Parameter(parm=self.node.parm('autobind'))
        self.parm_bindings = Parameter(parm=self.node.parm('bindings'))
        self.parm_groupautobind = Parameter(parm=self.node.parm('groupautobind'))
        self.parm_groupbindings = Parameter(parm=self.node.parm('groupbindings'))
        self.parm_vex_cwdpath = Parameter(parm=self.node.parm('vex_cwdpath'))
        self.parm_vex_outputmask = Parameter(parm=self.node.parm('vex_outputmask'))
        self.parm_vex_updatenmls = Parameter(parm=self.node.parm('vex_updatenmls'))
        self.parm_vex_matchattrib = Parameter(parm=self.node.parm('vex_matchattrib'))
        self.parm_vex_inplace = Parameter(parm=self.node.parm('vex_inplace'))
        self.parm_vex_selectiongroup = Parameter(parm=self.node.parm('vex_selectiongroup'))

        
        # parm menu vars:
        self.parm_grouptype_menu = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_class_alt_menu = ClassAltMenu(parm=self.node.parm('class'))
        self.parm_snippet_menu = SnippetMenu(parm=self.node.parm('snippet'))
        self.parm_vex_precision_menu = VexPrecisionMenu(parm=self.node.parm('vex_precision'))


        # input vars:
        self.input_geometry_to_process_with_wrangle = 0
        self.input_ancillary_input__point_1_______to_access = 1
        self.input_ancillary_input__point_2_______to_access = 2
        self.input_ancillary_input__point_3_______to_access = 3


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.guess_from_group = 0
        self.vertices = 1
        self.edges = 2
        self.points = 3
        self.primitives = 4


class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.detail__only_once_ = 0
        self.primitives = 1
        self.points = 2
        self.vertices = 3
        self.numbers = 4


class SnippetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.color_from_bounding_box = 0
        self.random_point_color = 1
        self.color_based_on_threshold = 2
        self.point_group_on_threshold = 3
        self.fetch_second_input_cd_attribute = 4
        self.fetch_second_input_attribute_by_id_name = 5
        self.nearest_point_distance = 6
        self.grow_hairs = 7
        self.get_neighbouring_points_into_attribute = 8
        self.average_neighbouring_points = 9


class VexPrecisionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.auto = 0
        self.bit_32 = 1
        self.bit__experimental__64 = 2



