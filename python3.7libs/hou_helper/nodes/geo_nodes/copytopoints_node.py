from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class CopytopointsNode(HHNode):
    node_type = 'copytopoints::2.0'
    parm_lookup_dict = {'sourcegroup': 'sourcegroup', 'sourcegrouptype': 'sourcegrouptype', 'targetgroup': 'targetgroup', 'useidattrib': 'useidattrib', 'idattrib': 'idattrib', 'pack': 'pack', 'pivot': 'pivot', 'viewportlod': 'viewportlod', 'transform': 'transform', 'useimplicitn': 'useimplicitn', 'resettargetattribs': 'resettargetattribs', 'targetattribs': 'targetattribs', 'useapply1': 'useapply1', 'applyto1': 'applyto1', 'applymethod1': 'applymethod1', 'applyattribs1': 'applyattribs1', 'useapply2': 'useapply2', 'applyto2': 'applyto2', 'applymethod2': 'applymethod2', 'applyattribs2': 'applyattribs2', 'useapply3': 'useapply3', 'applyto3': 'applyto3', 'applymethod3': 'applymethod3', 'applyattribs3': 'applyattribs3'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_targetgroup = Parameter(parm=self.node.parm('targetgroup'))
        self.parm_useidattrib = Parameter(parm=self.node.parm('useidattrib'))
        self.parm_pack = Parameter(parm=self.node.parm('pack'))
        self.parm_transform = Parameter(parm=self.node.parm('transform'))
        self.parm_useimplicitn = Parameter(parm=self.node.parm('useimplicitn'))
        self.parm_resettargetattribs = Parameter(parm=self.node.parm('resettargetattribs'))
        self.parm_targetattribs = Parameter(parm=self.node.parm('targetattribs'))
        self.parm_useapply1 = Parameter(parm=self.node.parm('useapply1'))
        self.parm_useapply2 = Parameter(parm=self.node.parm('useapply2'))
        self.parm_useapply3 = Parameter(parm=self.node.parm('useapply3'))

        
        # parm menu vars:
        self.parm_sourcegroup_menu = SourcegroupMenu(parm=self.node.parm('sourcegroup'))
        self.parm_sourcegrouptype_menu = SourcegrouptypeMenu(parm=self.node.parm('sourcegrouptype'))
        self.parm_idattrib_menu = IdattribMenu(parm=self.node.parm('idattrib'))
        self.parm_pivot_menu = PivotMenu(parm=self.node.parm('pivot'))
        self.parm_viewportlod_menu = ViewportlodMenu(parm=self.node.parm('viewportlod'))
        self.parm_applyto1_menu = Applyto1Menu(parm=self.node.parm('applyto1'))
        self.parm_applymethod1_menu = Applymethod1Menu(parm=self.node.parm('applymethod1'))
        self.parm_applyattribs1_menu = Applyattribs1Menu(parm=self.node.parm('applyattribs1'))
        self.parm_applyto2_menu = Applyto2Menu(parm=self.node.parm('applyto2'))
        self.parm_applymethod2_menu = Applymethod2Menu(parm=self.node.parm('applymethod2'))
        self.parm_applyattribs2_menu = Applyattribs2Menu(parm=self.node.parm('applyattribs2'))
        self.parm_applyto3_menu = Applyto3Menu(parm=self.node.parm('applyto3'))
        self.parm_applymethod3_menu = Applymethod3Menu(parm=self.node.parm('applymethod3'))
        self.parm_applyattribs3_menu = Applyattribs3Menu(parm=self.node.parm('applyattribs3'))


        # input vars:
        self.input_geometry_to_copy = 0
        self.input_target_points_to_copy_to = 1


# parm menu classes:
class SourcegroupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self._first_wind_first_wind = 0
        self.leaf_1_matsg = 1
        self.leaf_2_matsg = 2
        self.leaf_3_matsg = 3
        self.leaf_4_matsg = 4
        self.trunk_matsg = 5
        self._separator_ = 6
        self._tree_one = 7
        self._tree_two = 8


class SourcegrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.guess_from_group = 0
        self.primitives = 1
        self.points = 2


class IdattribMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.name = 0


class PivotMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.origin = 0
        self.centroid = 1


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.full_geometry = 0
        self.point_cloud = 1
        self.bounding_box = 2
        self.centroid = 3
        self.hidden = 4


class Applyto1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.points = 0
        self.vertices = 1
        self.primitives = 2


class Applymethod1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.copying = 0
        self.nothing = 1
        self.multiplying = 2
        self.adding = 3
        self.subtracting = 4


class Applyattribs1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.position____p_ = 0
        self.name = 1


class Applyto2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.points = 0
        self.vertices = 1
        self.primitives = 2


class Applymethod2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.copying = 0
        self.nothing = 1
        self.multiplying = 2
        self.adding = 3
        self.subtracting = 4


class Applyattribs2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.position____p_ = 0
        self.name = 1


class Applyto3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.points = 0
        self.vertices = 1
        self.primitives = 2


class Applymethod3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.copying = 0
        self.nothing = 1
        self.multiplying = 2
        self.adding = 3
        self.subtracting = 4


class Applyattribs3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.position____p_ = 0
        self.name = 1



