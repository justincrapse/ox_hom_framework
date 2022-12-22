from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RenameNode(OXNode):
    node_type = 'rename'
    parm_lookup_dict = {'stdswitcher': 'stdswitcher', 'from': 'from', 'to': 'to'}

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
        self.parm_from = Parameter(parm=self.node.parm('from'))
        self.parm_to = Parameter(parm=self.node.parm('to'))

        
        # parm menu vars:


        # input vars:
        self.input_planes_to_rename = 'Planes to Rename'


# parm menu classes:

