from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldMaskbyobjectNode(HHNode):
    node_type = 'heightfield_maskbyobject'
    parm_lookup_dict = {'folder01': 'folder01', 'combine': 'combine', 'blend': 'blend', 'method': 'method', 'maskdir': 'maskdir', 'invertmask': 'invertmask', 'maxdist': 'maxdist', 'value': 'value', 'blurmethod': 'blurmethod', 'blurradius': 'blurradius', 'dojitter': 'dojitter', 'sample': 'sample', 'jitter': 'jitter', 'jittercombine': 'jittercombine', 'seed': 'seed', 'masklayer': 'masklayer', 'heightlayer': 'heightlayer'}

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
        self.parm_combine_menu = CombineMenu(parm=self.node.parm('combine'))
        self.parm_method_menu = MethodMenu(parm=self.node.parm('method'))
        self.parm_maskdir_menu = MaskdirMenu(parm=self.node.parm('maskdir'))
        self.parm_blurmethod_menu = BlurmethodMenu(parm=self.node.parm('blurmethod'))
        self.parm_jittercombine_menu = JittercombineMenu(parm=self.node.parm('jittercombine'))


        # input vars:
        self.input_terrain_to_mask = 0
        self.input_geometry_to_build_mask_from = 1


# parm menu classes:
class CombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.replace = 0
        self.add = 1
        self.subtract = 2
        self.difference = 3
        self.multiply = 4
        self.maximum = 5
        self.minimum = 6
        self.blend = 7


class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.project = 0
        self.fog_volume = 1
        self.sdf_volume = 2


class MaskdirMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.either_side = 0
        self.above_heightfield = 1
        self.below_heightfield = 2


class BlurmethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.blur = 0
        self.box_blur = 1
        self.expand = 2
        self.shrink = 3


class JittercombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.average = 0
        self.median = 1
        self.shortest = 2
        self.longest = 3



