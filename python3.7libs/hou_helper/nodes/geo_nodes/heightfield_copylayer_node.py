from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class HeightfieldCopylayerNode(HHNode):
    node_type = 'heightfield_copylayer'
    parm_lookup_dict = {'numcopy': 'numcopy', 'srcname1': 'srcname1', 'dstname1': 'dstname1', 'copysrc1': 'copysrc1', 'replacedst1': 'replacedst1'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_numcopy = Parameter(parm=self.node.parm('numcopy'))
        self.parm_copysrc1 = Parameter(parm=self.node.parm('copysrc1'))
        self.parm_replacedst1 = Parameter(parm=self.node.parm('replacedst1'))

        
        # parm menu vars:
        self.parm_srcname1_menu = Srcname1Menu(parm=self.node.parm('srcname1'))
        self.parm_dstname1_menu = Dstname1Menu(parm=self.node.parm('dstname1'))


        # input vars:
        self.input_terrain_to_copy_layers_within = 0


# parm menu classes:
class Srcname1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.height = 0
        self.mask = 1


class Dstname1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.height = 0
        self.mask = 1



