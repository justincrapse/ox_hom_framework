from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AddNode(OXNode):
    node_type = 'add'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'keep': 'keep', 'points': 'points', 'remove': 'remove', 'switcher1': 'switcher1', 'prims': 'prims', 'group': 'group', 'add': 'add', 'inc': 'inc', 'attrname': 'attrname', 'closedall': 'closedall', 'addparticlesystem': 'addparticlesystem', 'particlegroup': 'particlegroup', 'appendunusedtoparticlesystem': 'appendunusedtoparticlesystem', 'prim0': 'prim0', 'closed0': 'closed0', 'usept0': 'usept0', 'pt0x': 'pt0x', 'pt0y': 'pt0y', 'pt0z': 'pt0z', 'weight0': 'weight0'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_keep = Parameter(parm=self.node.parm('keep'))
        self.parm_points = Parameter(parm=self.node.parm('points'))
        self.parm_remove = Parameter(parm=self.node.parm('remove'))
        self.parm_switcher1 = Parameter(parm=self.node.parm('switcher1'))
        self.parm_prims = Parameter(parm=self.node.parm('prims'))
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_inc = Parameter(parm=self.node.parm('inc'))
        self.parm_attrname = Parameter(parm=self.node.parm('attrname'))
        self.parm_closedall = Parameter(parm=self.node.parm('closedall'))
        self.parm_addparticlesystem = Parameter(parm=self.node.parm('addparticlesystem'))
        self.parm_particlegroup = Parameter(parm=self.node.parm('particlegroup'))
        self.parm_appendunusedtoparticlesystem = Parameter(parm=self.node.parm('appendunusedtoparticlesystem'))
        self.parm_prim0 = Parameter(parm=self.node.parm('prim0'))
        self.parm_closed0 = Parameter(parm=self.node.parm('closed0'))
        self.parm_usept0 = Parameter(parm=self.node.parm('usept0'))
        self.parm_pt0x = Parameter(parm=self.node.parm('pt0x'))
        self.parm_pt0y = Parameter(parm=self.node.parm('pt0y'))
        self.parm_pt0z = Parameter(parm=self.node.parm('pt0z'))
        self.parm_weight0 = Parameter(parm=self.node.parm('weight0'))

        
        # parm menu vars:
        self.parm_add = AddMenu(parm=self.node.parm('add'))


        # input vars:
        self.input_source = 'Source'


# parm menu classes:
class AddMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_points = ("all", 0)
        self.menu_groups_of_n_points = ("group", 1)
        self.menu_skip_every_nth_point = ("skip", 2)
        self.menu_each_group_separately = ("sep", 3)
        self.menu_by_attribute = ("attribute", 4)



