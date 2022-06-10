from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CopNetNode(OXNode):
    node_type = 'cop2net'
    parm_lookup_dict = {'usecoppath': 'usecoppath', 'coppath': 'coppath', 'frame': 'frame', 'planemask': 'planemask', 'method': 'method', 'plane': 'plane', 'sampling': 'sampling', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'scale': 'scale', 'visualize': 'visualize', 'visrange1': 'visrange1', 'visrange2': 'visrange2'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_usecoppath = Parameter(parm=self.node.parm('usecoppath'))
        self.parm_coppath = Parameter(parm=self.node.parm('coppath'))
        self.parm_frame = Parameter(parm=self.node.parm('frame'))
        self.parm_planemask = Parameter(parm=self.node.parm('planemask'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_visualize = Parameter(parm=self.node.parm('visualize'))
        self.parm_visrange1 = Parameter(parm=self.node.parm('visrange1'))
        self.parm_visrange2 = Parameter(parm=self.node.parm('visrange2'))

        
        # parm menu vars:
        self.parm_method = MethodMenu(parm=self.node.parm('method'))
        self.parm_plane = PlaneMenu(parm=self.node.parm('plane'))
        self.parm_sampling = SamplingMenu(parm=self.node.parm('sampling'))


        # input vars:


# parm menu classes:
class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_volume_slice = 0
        self.menu_volume = 1
        self.menu_mesh = 2
        self.menu_points = 3
        self.menu_quad_with_uvs = 4


class PlaneMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_xy_plane = 0
        self.menu_yz_plane = 1
        self.menu_zx_plane = 2


class SamplingMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_center = 0
        self.menu_corner = 1



