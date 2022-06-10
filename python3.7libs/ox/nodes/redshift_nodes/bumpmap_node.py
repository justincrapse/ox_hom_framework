from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class BumpmapNode(OXNode):
    node_type = 'redshift::BumpMap'
    parm_lookup_dict = {'texture_0': 'Texture_0', 'inuse': 'inuse', 'inputtype': 'inputType', 'inputr': 'inputr', 'inputg': 'inputg', 'inputb': 'inputb', 'scale': 'scale', 'factorinobjscale': 'factorInObjScale', 'remap_1': 'Remap_1', 'oldrange_min': 'oldrange_min', 'oldrange_max': 'oldrange_max', 'newrange_min': 'newrange_min', 'newrange_max': 'newrange_max', 'unbiasednormalmap': 'unbiasedNormalMap', 'flipy': 'flipY'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_texture_0 = Parameter(parm=self.node.parm('Texture_0'))
        self.parm_inuse = Parameter(parm=self.node.parm('inuse'))
        self.parm_inputr = Parameter(parm=self.node.parm('inputr'))
        self.parm_inputg = Parameter(parm=self.node.parm('inputg'))
        self.parm_inputb = Parameter(parm=self.node.parm('inputb'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_factorinobjscale = Parameter(parm=self.node.parm('factorInObjScale'))
        self.parm_remap_1 = Parameter(parm=self.node.parm('Remap_1'))
        self.parm_oldrange_min = Parameter(parm=self.node.parm('oldrange_min'))
        self.parm_oldrange_max = Parameter(parm=self.node.parm('oldrange_max'))
        self.parm_newrange_min = Parameter(parm=self.node.parm('newrange_min'))
        self.parm_newrange_max = Parameter(parm=self.node.parm('newrange_max'))
        self.parm_unbiasednormalmap = Parameter(parm=self.node.parm('unbiasedNormalMap'))
        self.parm_flipy = Parameter(parm=self.node.parm('flipY'))

        
        # parm menu vars:
        self.parm_inputtype = InputtypeMenu(parm=self.node.parm('inputType'))


        # input vars:
        self.input_input = 'input'
        self.input_scale = 'scale'
        self.input_oldrange_min = 'oldrange_min'
        self.input_oldrange_max = 'oldrange_max'
        self.input_newrange_min = 'newrange_min'
        self.input_newrange_max = 'newrange_max'


# parm menu classes:
class InputtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_height_field = 0
        self.menu_tangent_space_normal = 1
        self.menu_object_space_normal = 2



