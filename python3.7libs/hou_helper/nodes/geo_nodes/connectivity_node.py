from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class ConnectivityNode(HHNode):
    node_type = 'connectivity'
    parm_lookup_dict = {'connecttype': 'connecttype', 'attribname': 'attribname', 'attribtype': 'attribtype', 'prefix': 'prefix', 'createvarmap': 'createvarmap', 'varname': 'varname', 'seamgroup': 'seamgroup', 'byuv': 'byuv', 'uvattrib': 'uvattrib'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_attribname = Parameter(parm=self.node.parm('attribname'))
        self.parm_prefix = Parameter(parm=self.node.parm('prefix'))
        self.parm_createvarmap = Parameter(parm=self.node.parm('createvarmap'))
        self.parm_varname = Parameter(parm=self.node.parm('varname'))
        self.parm_byuv = Parameter(parm=self.node.parm('byuv'))
        self.parm_uvattrib = Parameter(parm=self.node.parm('uvattrib'))

        
        # parm menu vars:
        self.parm_connecttype_menu = ConnecttypeMenu(parm=self.node.parm('connecttype'))
        self.parm_attribtype_menu = AttribtypeMenu(parm=self.node.parm('attribtype'))
        self.parm_seamgroup_menu = SeamgroupMenu(parm=self.node.parm('seamgroup'))


        # input vars:
        self.input_input_1 = 0


# parm menu classes:
class ConnecttypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.point = 0
        self.primitive = 1


class AttribtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.integer = 0
        self.string = 1


class SeamgroupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self._first_wind_first_wind = 0
        self.leaf_1_matsg = 1
        self.leaf_2_matsg = 2
        self.leaf_3_matsg = 3
        self.leaf_4_matsg = 4
        self.trunk_matsg = 5
        self._separator_ = 6
        self._tree_one = 7
        self._tree_two = 8



