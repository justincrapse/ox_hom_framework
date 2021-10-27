from ox.base_objects.ox_node import HHNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CleanNode(HHNode):
    node_type = 'clean'
    parm_lookup_dict = {'fusepts': 'fusepts', 'deldegengeo': 'deldegengeo', 'orientpoly': 'orientpoly', 'reversewinding': 'reversewinding', 'fixoverlap': 'fixoverlap', 'deleteoverlap': 'deleteoverlap', 'delunusedpts': 'delunusedpts', 'dodelattribs': 'dodelattribs', 'delattribs': 'delattribs', 'dodelgroups': 'dodelgroups', 'delgroups': 'delgroups', 'delnans': 'delnans', 'make_manifold': 'make_manifold', 'delete_small': 'delete_small', 'prim_count': 'prim_count'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_fusepts = Parameter(parm=self.node.parm('fusepts'))
        self.parm_deldegengeo = Parameter(parm=self.node.parm('deldegengeo'))
        self.parm_orientpoly = Parameter(parm=self.node.parm('orientpoly'))
        self.parm_reversewinding = Parameter(parm=self.node.parm('reversewinding'))
        self.parm_fixoverlap = Parameter(parm=self.node.parm('fixoverlap'))
        self.parm_deleteoverlap = Parameter(parm=self.node.parm('deleteoverlap'))
        self.parm_delunusedpts = Parameter(parm=self.node.parm('delunusedpts'))
        self.parm_dodelattribs = Parameter(parm=self.node.parm('dodelattribs'))
        self.parm_delattribs = Parameter(parm=self.node.parm('delattribs'))
        self.parm_dodelgroups = Parameter(parm=self.node.parm('dodelgroups'))
        self.parm_delgroups = Parameter(parm=self.node.parm('delgroups'))
        self.parm_delnans = Parameter(parm=self.node.parm('delnans'))
        self.parm_make_manifold = Parameter(parm=self.node.parm('make_manifold'))
        self.parm_delete_small = Parameter(parm=self.node.parm('delete_small'))
        self.parm_prim_count = Parameter(parm=self.node.parm('prim_count'))

        
        # parm menu vars:


        # input vars:
        self.input_geometry_to_clean = 0


# parm menu classes:

