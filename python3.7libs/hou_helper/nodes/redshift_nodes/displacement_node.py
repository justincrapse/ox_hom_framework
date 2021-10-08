from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class DisplacementNode(HHNode):
    node_type = 'redshift::Displacement'
    parm_lookup_dict = {'texture_0': 'Texture_0', 'texmapr': 'texMapr', 'texmapg': 'texMapg', 'texmapb': 'texMapb', 'scale': 'scale', 'map_encoding': 'map_encoding', 'space_type': 'space_type', 'tangents_1': 'Tangents_1', 'tangents': 'tangents', 'change_range_2': 'Change_Range_2', 'oldrange_min': 'oldrange_min', 'oldrange_max': 'oldrange_max', 'newrange_min': 'newrange_min', 'newrange_max': 'newrange_max'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_texture_0 = Parameter(parm=self.node.parm('texture_0'))
        self.parm_texmapr = Parameter(parm=self.node.parm('texmapr'))
        self.parm_texmapg = Parameter(parm=self.node.parm('texmapg'))
        self.parm_texmapb = Parameter(parm=self.node.parm('texmapb'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_tangents_1 = Parameter(parm=self.node.parm('tangents_1'))
        self.parm_tangents = Parameter(parm=self.node.parm('tangents'))
        self.parm_change_range_2 = Parameter(parm=self.node.parm('change_range_2'))
        self.parm_oldrange_min = Parameter(parm=self.node.parm('oldrange_min'))
        self.parm_oldrange_max = Parameter(parm=self.node.parm('oldrange_max'))
        self.parm_newrange_min = Parameter(parm=self.node.parm('newrange_min'))
        self.parm_newrange_max = Parameter(parm=self.node.parm('newrange_max'))

        
        # parm menu vars:
        self.parm_map_encoding_menu = MapEncodingMenu(parm=self.node.parm('map_encoding'))
        self.parm_space_type_menu = SpaceTypeMenu(parm=self.node.parm('space_type'))


        # input vars:
        self.input_texmap = 0
        self.input_scale = 1
        self.input_oldrange_min = 2
        self.input_oldrange_max = 3
        self.input_newrange_min = 4
        self.input_newrange_max = 5


# parm menu classes:
class MapEncodingMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.vector = 0
        self.height_field = 1


class SpaceTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.object = 0
        self.tangent = 1



