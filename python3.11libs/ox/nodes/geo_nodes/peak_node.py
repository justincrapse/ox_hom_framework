from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class PeakNode(OXNode):
    node_type = 'peak'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'dist': 'dist', 'updatenmls': 'updatenmls'}

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
        self.parm_dist = Parameter(parm=self.node.parm('dist'))
        self.parm_updatenmls = Parameter(parm=self.node.parm('updatenmls'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))


        # input vars:
        self.input_points_to_displace = 'Points to displace'


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = ("guess", 0)
        self.menu_breakpoints = ("breakpoints", 1)
        self.menu_edges = ("edges", 2)
        self.menu_points = ("points", 3)
        self.menu_primitives = ("prims", 4)



