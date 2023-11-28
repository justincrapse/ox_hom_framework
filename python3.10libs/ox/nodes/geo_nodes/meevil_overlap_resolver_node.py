from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MeevilOverlapResolverNode(OXNode):
    node_type = 'meevil_overlap_resolver'
    parm_lookup_dict = {}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:

        
        # parm menu vars:


        # input vars:
        self.input_in_body = 'IN-BODY'
        self.input_in_eyes = 'IN-EYES'
        self.input_in_legs = 'IN-LEGS'
        self.input_in_arms = 'IN-ARMS'
        self.input_in_mouth = 'IN-MOUTH'
        self.input_in_crown = 'IN-CROWN'


# parm menu classes:

