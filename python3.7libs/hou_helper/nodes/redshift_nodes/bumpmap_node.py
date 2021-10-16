from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class BumpmapNode(HHNode):
    node_type = 'redshift::BumpMap'
    parm_lookup_dict = {'texture_0': 'Texture_0', 'inuse': 'inuse', 'inputtype': 'inputType', 'inputr': 'inputr', 'inputg': 'inputg', 'inputb': 'inputb', 'scale': 'scale', 'factorinobjscale': 'factorInObjScale', 'remap_1': 'Remap_1', 'oldrange_min': 'oldrange_min', 'oldrange_max': 'oldrange_max', 'newrange_min': 'newrange_min', 'newrange_max': 'newrange_max', 'unbiasednormalmap': 'unbiasedNormalMap', 'flipy': 'flipY'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_texture_0 = Parameter(parm=self.node.parm('texture_0'))
        self.parm_inuse = Parameter(parm=self.node.parm('inuse'))
        self.parm_inputr = Parameter(parm=self.node.parm('inputr'))
        self.parm_inputg = Parameter(parm=self.node.parm('inputg'))
        self.parm_inputb = Parameter(parm=self.node.parm('inputb'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_factorinobjscale = Parameter(parm=self.node.parm('factorinobjscale'))
        self.parm_remap_1 = Parameter(parm=self.node.parm('remap_1'))
        self.parm_oldrange_min = Parameter(parm=self.node.parm('oldrange_min'))
        self.parm_oldrange_max = Parameter(parm=self.node.parm('oldrange_max'))
        self.parm_newrange_min = Parameter(parm=self.node.parm('newrange_min'))
        self.parm_newrange_max = Parameter(parm=self.node.parm('newrange_max'))
        self.parm_unbiasednormalmap = Parameter(parm=self.node.parm('unbiasednormalmap'))
        self.parm_flipy = Parameter(parm=self.node.parm('flipy'))

        
        # parm menu vars:
        self.parm_inputtype_menu = InputtypeMenu(parm=self.node.parm('inputType'))


        # input vars:
        self.input_input = 0
        self.input_scale = 1
        self.input_oldrange_min = 2
        self.input_oldrange_max = 3
        self.input_newrange_min = 4
        self.input_newrange_max = 5


# parm menu classes:
class InputtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.height_field = 0
        self.tangent_space_normal = 1
        self.object_space_normal = 2



