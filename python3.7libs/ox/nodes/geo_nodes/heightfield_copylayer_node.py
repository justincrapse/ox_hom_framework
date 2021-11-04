from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldCopylayerNode(OXNode):
    node_type = 'heightfield_copylayer'
    parm_lookup_dict = {'numcopy': 'numcopy', 'srcname1': 'srcname1', 'dstname1': 'dstname1', 'copysrc1': 'copysrc1', 'replacedst1': 'replacedst1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_numcopy = Parameter(parm=self.node.parm('numcopy'))
        self.parm_srcname1 = Parameter(parm=self.node.parm('srcname1'))
        self.parm_dstname1 = Parameter(parm=self.node.parm('dstname1'))
        self.parm_copysrc1 = Parameter(parm=self.node.parm('copysrc1'))
        self.parm_replacedst1 = Parameter(parm=self.node.parm('replacedst1'))

        
        # parm menu vars:


        # input vars:
        self.input_terrain_to_copy_layers_within = 0


# parm menu classes:

