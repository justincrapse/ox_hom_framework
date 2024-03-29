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
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_project = ("ray", 0)
        self.menu_fog_volume = ("volume", 1)
        self.menu_sdf_volume = ("sdf", 2)


class MaskdirMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_either_side = ("both", 0)
        self.menu_above_heightfield = ("above", 1)
        self.menu_below_heightfield = ("below", 2)


class BlurmethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class JittercombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_average = ("avg", 0)
        self.menu_median = ("median", 1)
        self.menu_shortest = ("min", 2)
        self.menu_longest = ("max", 3)



