from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SetpointtransformNode(OXNode):
    node_type = 'kinefx::setpointtransform'
    parm_lookup_dict = {'signature': 'signature', 'pt': 'pt', 'pt_n': 'pt_n', 'constrain': 'constrain', 'active': 'active'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_pt = Parameter(parm=self.node.parm('pt'))
        self.parm_pt_n = Parameter(parm=self.node.parm('pt_n'))
        self.parm_constrain = Parameter(parm=self.node.parm('constrain'))
        self.parm_active = Parameter(parm=self.node.parm('active'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))


        # input vars:
        self.input_point_number = 'Point Number'
        self.input_world_transform = 'World Transform'
        self.input_local_transform = 'Local Transform'
        self.input_effective_local_transform = 'Effective Local Transform'
        self.input_active = 'Active'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_by_point_number = ("default", 0)



