from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class GroupsfromnameNode(OXNode):
    node_type = 'groupsfromname'
    parm_lookup_dict = {'attribname': 'attribname', 'class_alt': 'class', 'groupprefix': 'groupprefix', 'conflict': 'conflict', 'invalidnames': 'invalidnames'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_attribname = Parameter(parm=self.node.parm('attribname'))
        self.parm_groupprefix = Parameter(parm=self.node.parm('groupprefix'))

        
        # parm menu vars:
        self.parm_class_alt = ClassAltMenu(parm=self.node.parm('class'))
        self.parm_conflict = ConflictMenu(parm=self.node.parm('conflict'))
        self.parm_invalidnames = InvalidnamesMenu(parm=self.node.parm('invalidnames'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitive = ("primitive", 0)
        self.menu_point = ("point", 1)
        self.menu_vertex = ("vertex", 2)


class ConflictMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace_existing = ("replace", 0)
        self.menu_union_with_existing = ("union", 1)


class InvalidnamesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_ignore = ("ignore", 0)
        self.menu_force_valid = ("forcevalid", 1)
        self.menu_encode = ("encode", 2)



