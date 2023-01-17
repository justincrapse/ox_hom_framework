from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ParticleattributelookupNode(OXNode):
    node_type = 'redshift::ParticleAttributeLookup'
    parm_lookup_dict = {'attribute': 'attribute', 'shader_skipdefvalparms': 'shader_skipdefvalparms'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_attribute = Parameter(parm=self.node.parm('attribute'))
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))

        
        # parm menu vars:


        # input vars:


# parm menu classes:

