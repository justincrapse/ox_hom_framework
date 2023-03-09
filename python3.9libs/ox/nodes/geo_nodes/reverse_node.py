from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ReverseNode(OXNode):
    node_type = 'reverse'
    parm_lookup_dict = {'group': 'group', 'vtxsort': 'vtxsort', 'vtxuoff': 'vtxuoff', 'vtxvoff': 'vtxvoff'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_vtxuoff = Parameter(parm=self.node.parm('vtxuoff'))
        self.parm_vtxvoff = Parameter(parm=self.node.parm('vtxvoff'))

        
        # parm menu vars:
        self.parm_vtxsort = VtxsortMenu(parm=self.node.parm('vtxsort'))


        # input vars:
        self.input_source_geometry = 'Source Geometry'


# parm menu classes:
class VtxsortMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_change = ("samevertex", 0)
        self.menu_reverse = ("reverse", 1)
        self.menu_reverse_u = ("reverseu", 2)
        self.menu_reverse_v = ("reversev", 3)
        self.menu_swap_u_and_v = ("swapuv", 4)
        self.menu_shift = ("shift", 5)



