from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AttribwrangleNode(OXNode):
    node_type = 'attribwrangle'
    parm_lookup_dict = {'folder01': 'folder01', 'group': 'group', 'grouptype': 'grouptype', 'class_alt': 'class', 'vex_numcount': 'vex_numcount', 'vex_threadjobsize': 'vex_threadjobsize', 'snippet': 'snippet', 'exportlist': 'exportlist', 'vex_strict': 'vex_strict', 'autobind': 'autobind', 'bindings': 'bindings', 'groupautobind': 'groupautobind', 'groupbindings': 'groupbindings', 'vex_cwdpath': 'vex_cwdpath', 'vex_outputmask': 'vex_outputmask', 'vex_updatenmls': 'vex_updatenmls', 'vex_matchattrib': 'vex_matchattrib', 'vex_inplace': 'vex_inplace', 'vex_selectiongroup': 'vex_selectiongroup', 'vex_precision': 'vex_precision'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
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
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_class_alt = ClassAltMenu(parm=self.node.parm('class'))
        self.parm_snippet = SnippetMenu(parm=self.node.parm('snippet'))
        self.parm_vex_precision = VexPrecisionMenu(parm=self.node.parm('vex_precision'))


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
        self.menu_guess_from_group = 0
        self.menu_vertices = 1
        self.menu_edges = 2
        self.menu_points = 3
        self.menu_primitives = 4


class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_detail__only_once_ = 0
        self.menu_primitives = 1
        self.menu_points = 2
        self.menu_vertices = 3
        self.menu_numbers = 4


class SnippetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_color_from_bounding_box = 0
        self.menu_random_point_color = 1
        self.menu_color_based_on_threshold = 2
        self.menu_point_group_on_threshold = 3
        self.menu_fetch_second_input_cd_attribute = 4
        self.menu_fetch_second_input_attribute_by_id_name = 5
        self.menu_nearest_point_distance = 6
        self.menu_grow_hairs = 7
        self.menu_get_neighbouring_points_into_attribute = 8
        self.menu_average_neighbouring_points = 9


class VexPrecisionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = 0
        self.menu_bit_32 = 1
        self.menu_bit__experimental__64 = 2



