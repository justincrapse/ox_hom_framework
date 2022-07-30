from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class DeleteNode(OXNode):
    node_type = 'delete'
    parm_lookup_dict = {'stdswitcher': 'stdswitcher', 'delete': 'delete', 'scope': 'scope'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_stdswitcher = Parameter(parm=self.node.parm('stdswitcher'))

        
        # parm menu vars:
        self.parm_delete = DeleteMenu(parm=self.node.parm('delete'))
        self.parm_scope = ScopeMenu(parm=self.node.parm('scope'))


        # input vars:
        self.input_planes_to_delete = 'Planes to Delete'
        self.input_reference_planes_to_keep = 'Reference Planes to Keep'


# parm menu classes:
class DeleteMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scoped_planes___components = "scoped"
        self.menu_non_scoped_planes___components = "nonscoped"


class ScopeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = "*"



