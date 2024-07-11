from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxdisplacementNode(OXNode):
    node_type = 'mtlxdisplacement'
    parm_lookup_dict = {'signature': 'signature', 'displacement': 'displacement', 'scale': 'scale', 'displacement_vector3x': 'displacement_vector3x', 'displacement_vector3y': 'displacement_vector3y', 'displacement_vector3z': 'displacement_vector3z'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_displacement = Parameter(parm=self.node.parm('displacement'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_displacement_vector3x = Parameter(parm=self.node.parm('displacement_vector3x'))
        self.parm_displacement_vector3y = Parameter(parm=self.node.parm('displacement_vector3y'))
        self.parm_displacement_vector3z = Parameter(parm=self.node.parm('displacement_vector3z'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))


        # input vars:
        self.input_displacement = 'Displacement'
        self.input_scale = 'Scale'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = ("default", 0)
        self.menu_vector_3 = ("vector3", 1)



