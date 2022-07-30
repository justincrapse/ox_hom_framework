from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ObjectMergeNode(OXNode):
    node_type = 'object_merge'
    parm_lookup_dict = {'numobj': 'numobj', 'xformtype': 'xformtype', 'xformpath': 'xformpath', 'invertxform': 'invertxform', 'createptgroups': 'createptgroups', 'ptgroupprefix': 'ptgroupprefix', 'createprimgroups': 'createprimgroups', 'primgroupprefix': 'primgroupprefix', 'verbosegroups': 'verbosegroups', 'suffixfirstgroup': 'suffixfirstgroup', 'createptstring': 'createptstring', 'createprimstring': 'createprimstring', 'pathattrib': 'pathattrib', 'pack': 'pack', 'pivot': 'pivot', 'viewportlod': 'viewportlod', 'addpath': 'addpath', 'enable1': 'enable1', 'objpath1': 'objpath1', 'group1': 'group1', 'expand1': 'expand1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_numobj = Parameter(parm=self.node.parm('numobj'))
        self.parm_xformpath = Parameter(parm=self.node.parm('xformpath'))
        self.parm_invertxform = Parameter(parm=self.node.parm('invertxform'))
        self.parm_createptgroups = Parameter(parm=self.node.parm('createptgroups'))
        self.parm_ptgroupprefix = Parameter(parm=self.node.parm('ptgroupprefix'))
        self.parm_createprimgroups = Parameter(parm=self.node.parm('createprimgroups'))
        self.parm_primgroupprefix = Parameter(parm=self.node.parm('primgroupprefix'))
        self.parm_verbosegroups = Parameter(parm=self.node.parm('verbosegroups'))
        self.parm_suffixfirstgroup = Parameter(parm=self.node.parm('suffixfirstgroup'))
        self.parm_createptstring = Parameter(parm=self.node.parm('createptstring'))
        self.parm_createprimstring = Parameter(parm=self.node.parm('createprimstring'))
        self.parm_pathattrib = Parameter(parm=self.node.parm('pathattrib'))
        self.parm_pack = Parameter(parm=self.node.parm('pack'))
        self.parm_addpath = Parameter(parm=self.node.parm('addpath'))
        self.parm_enable1 = Parameter(parm=self.node.parm('enable1'))
        self.parm_objpath1 = Parameter(parm=self.node.parm('objpath1'))
        self.parm_group1 = Parameter(parm=self.node.parm('group1'))
        self.parm_expand1 = Parameter(parm=self.node.parm('expand1'))

        
        # parm menu vars:
        self.parm_xformtype = XformtypeMenu(parm=self.node.parm('xformtype'))
        self.parm_pivot = PivotMenu(parm=self.node.parm('pivot'))
        self.parm_viewportlod = ViewportlodMenu(parm=self.node.parm('viewportlod'))


        # input vars:


# parm menu classes:
class XformtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = "none"
        self.menu_into_this_object = "local"
        self.menu_into_specified_object = "object"


class PivotMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_origin = "origin"
        self.menu_centroid = "centroid"


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = "full"
        self.menu_point_cloud = "points"
        self.menu_bounding_box = "box"
        self.menu_centroid = "centroid"
        self.menu_hidden = "hidden"



