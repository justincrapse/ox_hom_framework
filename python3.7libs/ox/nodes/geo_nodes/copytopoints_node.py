from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CopytopointsNode(OXNode):
    node_type = 'copytopoints::2.0'
    parm_lookup_dict = {'sourcegroup': 'sourcegroup', 'sourcegrouptype': 'sourcegrouptype', 'targetgroup': 'targetgroup', 'useidattrib': 'useidattrib', 'idattrib': 'idattrib', 'pack': 'pack', 'pivot': 'pivot', 'viewportlod': 'viewportlod', 'transform': 'transform', 'useimplicitn': 'useimplicitn', 'resettargetattribs': 'resettargetattribs', 'targetattribs': 'targetattribs'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
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
        self.parm_sourcegrouptype = SourcegrouptypeMenu(parm=self.node.parm('sourcegrouptype'))
        self.parm_pivot = PivotMenu(parm=self.node.parm('pivot'))
        self.parm_viewportlod = ViewportlodMenu(parm=self.node.parm('viewportlod'))


        # input vars:
        self.input_geometry_to_copy = 0
        self.input_target_points_to_copy_to = 1


# parm menu classes:
class SourcegrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = 0
        self.menu_primitives = 1
        self.menu_points = 2


class PivotMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_origin = 0
        self.menu_centroid = 1


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = 0
        self.menu_point_cloud = 1
        self.menu_bounding_box = 2
        self.menu_centroid = 3
        self.menu_hidden = 4



