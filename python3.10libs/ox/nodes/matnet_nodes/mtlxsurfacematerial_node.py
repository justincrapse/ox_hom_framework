from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxsurfacematerialNode(OXNode):
    node_type = 'mtlxsurfacematerial'
    parm_lookup_dict = {'surfaceshader': 'surfaceshader', 'displacementshader': 'displacementshader'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_surfaceshader = Parameter(parm=self.node.parm('surfaceshader'))
        self.parm_displacementshader = Parameter(parm=self.node.parm('displacementshader'))

        
        # parm menu vars:


        # input vars:
        self.input_surfaceshader = 'Surfaceshader'
        self.input_displacementshader = 'Displacementshader'


# parm menu classes:

