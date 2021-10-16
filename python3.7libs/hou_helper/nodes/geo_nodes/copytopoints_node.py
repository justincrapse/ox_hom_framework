from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class CopytopointsNode(HHNode):
    node_type = 'copytopoints::2.0'
    parm_lookup_dict = {'sourcegroup': 'sourcegroup', 'sourcegrouptype': 'sourcegrouptype', 'targetgroup': 'targetgroup', 'useidattrib': 'useidattrib', 'idattrib': 'idattrib', 'pack': 'pack', 'pivot': 'pivot', 'viewportlod': 'viewportlod', 'transform': 'transform', 'useimplicitn': 'useimplicitn', 'resettargetattribs': 'resettargetattribs', 'targetattribs': 'targetattribs'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_sourcegroup = Parameter(parm=self.node.parm('sourcegroup'))
        self.parm_targetgroup = Parameter(parm=self.node.parm('targetgroup'))
        self.parm_useidattrib = Parameter(parm=self.node.parm('useidattrib'))
        self.parm_idattrib = Parameter(parm=self.node.parm('idattrib'))
        self.parm_pack = Parameter(parm=self.node.parm('pack'))
        self.parm_transform = Parameter(parm=self.node.parm('transform'))
        self.parm_useimplicitn = Parameter(parm=self.node.parm('useimplicitn'))
        self.parm_resettargetattribs = Parameter(parm=self.node.parm('resettargetattribs'))
        self.parm_targetattribs = Parameter(parm=self.node.parm('targetattribs'))

        
        # parm menu vars:
        self.parm_sourcegrouptype_menu = SourcegrouptypeMenu(parm=self.node.parm('sourcegrouptype'))
        self.parm_pivot_menu = PivotMenu(parm=self.node.parm('pivot'))
        self.parm_viewportlod_menu = ViewportlodMenu(parm=self.node.parm('viewportlod'))


        # input vars:
        self.input_geometry_to_copy = 0
        self.input_target_points_to_copy_to = 1


# parm menu classes:
class SourcegrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.guess_from_group = 0
        self.primitives = 1
        self.points = 2


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



