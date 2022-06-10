from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldMaskbyobjectNode(OXNode):
    node_type = 'heightfield_maskbyobject'
    parm_lookup_dict = {'folder01': 'folder01', 'combine': 'combine', 'blend': 'blend', 'method': 'method', 'maskdir': 'maskdir', 'invertmask': 'invertmask', 'maxdist': 'maxdist', 'value': 'value', 'blurmethod': 'blurmethod', 'blurradius': 'blurradius', 'dojitter': 'dojitter', 'sample': 'sample', 'jitter': 'jitter', 'jittercombine': 'jittercombine', 'seed': 'seed', 'masklayer': 'masklayer', 'heightlayer': 'heightlayer'}

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
        self.parm_blend = Parameter(parm=self.node.parm('blend'))
        self.parm_invertmask = Parameter(parm=self.node.parm('invertmask'))
        self.parm_maxdist = Parameter(parm=self.node.parm('maxdist'))
        self.parm_value = Parameter(parm=self.node.parm('value'))
        self.parm_blurradius = Parameter(parm=self.node.parm('blurradius'))
        self.parm_dojitter = Parameter(parm=self.node.parm('dojitter'))
        self.parm_sample = Parameter(parm=self.node.parm('sample'))
        self.parm_jitter = Parameter(parm=self.node.parm('jitter'))
        self.parm_seed = Parameter(parm=self.node.parm('seed'))
        self.parm_masklayer = Parameter(parm=self.node.parm('masklayer'))
        self.parm_heightlayer = Parameter(parm=self.node.parm('heightlayer'))

        
        # parm menu vars:
        self.parm_combine = CombineMenu(parm=self.node.parm('combine'))
        self.parm_method = MethodMenu(parm=self.node.parm('method'))
        self.parm_maskdir = MaskdirMenu(parm=self.node.parm('maskdir'))
        self.parm_blurmethod = BlurmethodMenu(parm=self.node.parm('blurmethod'))
        self.parm_jittercombine = JittercombineMenu(parm=self.node.parm('jittercombine'))


        # input vars:
        self.input_terrain_to_mask = 'Terrain to Mask'
        self.input_geometry_to_build_mask_from = 'Geometry to Build Mask From'


# parm menu classes:
class CombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_add = 1
        self.menu_subtract = 2
        self.menu_difference = 3
        self.menu_multiply = 4
        self.menu_maximum = 5
        self.menu_minimum = 6
        self.menu_blend = 7


class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_project = 0
        self.menu_fog_volume = 1
        self.menu_sdf_volume = 2


class MaskdirMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_either_side = 0
        self.menu_above_heightfield = 1
        self.menu_below_heightfield = 2


class BlurmethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = 0
        self.menu_box_blur = 1
        self.menu_expand = 2
        self.menu_shrink = 3


class JittercombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_average = 0
        self.menu_median = 1
        self.menu_shortest = 2
        self.menu_longest = 3



