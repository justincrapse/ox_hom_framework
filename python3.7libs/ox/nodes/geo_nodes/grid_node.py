from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class GridNode(OXNode):
    node_type = 'grid'
    parm_lookup_dict = {'type': 'type', 'surftype': 'surftype', 'orient': 'orient', 'sizex': 'sizex', 'sizey': 'sizey', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'rows': 'rows', 'cols': 'cols', 'orderu': 'orderu', 'orderv': 'orderv', 'interpu': 'interpu', 'interpv': 'interpv'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_sizex = Parameter(parm=self.node.parm('sizex'))
        self.parm_sizey = Parameter(parm=self.node.parm('sizey'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_rows = Parameter(parm=self.node.parm('rows'))
        self.parm_cols = Parameter(parm=self.node.parm('cols'))
        self.parm_orderu = Parameter(parm=self.node.parm('orderu'))
        self.parm_orderv = Parameter(parm=self.node.parm('orderv'))
        self.parm_interpu = Parameter(parm=self.node.parm('interpu'))
        self.parm_interpv = Parameter(parm=self.node.parm('interpv'))

        
        # parm menu vars:
        self.parm_type = TypeMenu(parm=self.node.parm('type'))
        self.parm_surftype = SurftypeMenu(parm=self.node.parm('surftype'))
        self.parm_orient = OrientMenu(parm=self.node.parm('orient'))


        # input vars:


# parm menu classes:
class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_polygon = 0
        self.menu_mesh = 1
        self.menu_nurbs = 2
        self.menu_bezier = 3
        self.menu_points = 4
        self.menu_polygon_soup = 5


class SurftypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rows = 0
        self.menu_columns = 1
        self.menu_rows_and_columns = 2
        self.menu_triangles = 3
        self.menu_quadrilaterals = 4
        self.menu_alternating_triangles = 5
        self.menu_reverse_triangles = 6


class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_xy_plane = 0
        self.menu_yz_plane = 1
        self.menu_zx_plane = 2



