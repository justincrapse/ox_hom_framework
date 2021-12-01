from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class NormalNode(OXNode):
    node_type = 'normal'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'overridenormal': 'overridenormal', 'normalattrib': 'normalattrib', 'construct': 'construct', 'docompute': 'docompute', 'type': 'type', 'cuspangle': 'cuspangle', 'method': 'method', 'origifzero': 'origifzero', 'modify': 'modify', 'normalize': 'normalize', 'reverse': 'reverse'}

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
        self.parm_overridenormal = Parameter(parm=self.node.parm('overridenormal'))
        self.parm_normalattrib = Parameter(parm=self.node.parm('normalattrib'))
        self.parm_construct = Parameter(parm=self.node.parm('construct'))
        self.parm_docompute = Parameter(parm=self.node.parm('docompute'))
        self.parm_cuspangle = Parameter(parm=self.node.parm('cuspangle'))
        self.parm_origifzero = Parameter(parm=self.node.parm('origifzero'))
        self.parm_modify = Parameter(parm=self.node.parm('modify'))
        self.parm_normalize = Parameter(parm=self.node.parm('normalize'))
        self.parm_reverse = Parameter(parm=self.node.parm('reverse'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_type = TypeMenu(parm=self.node.parm('type'))
        self.parm_method = MethodMenu(parm=self.node.parm('method'))


        # input vars:
        self.input_geometry_to_add_normals_to = 'Geometry to add normals to'


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = 0
        self.menu_vertices = 1
        self.menu_edges = 2
        self.menu_points = 3
        self.menu_primitives = 4


class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_points = 0
        self.menu_vertices = 1
        self.menu_primitives = 2
        self.menu_detail = 3


class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_each_vertex_equally = 0
        self.menu_by_vertex_angle = 1
        self.menu_by_face_area = 2



