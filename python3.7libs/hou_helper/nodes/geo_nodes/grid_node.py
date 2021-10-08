from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class GridNode(HHNode):
    node_type = 'grid'
    parm_lookup_dict = {'type': 'type', 'surftype': 'surftype', 'orient': 'orient', 'sizex': 'sizex', 'sizey': 'sizey', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'rows': 'rows', 'cols': 'cols', 'orderu': 'orderu', 'orderv': 'orderv', 'interpu': 'interpu', 'interpv': 'interpv'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
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
        self.parm_type_menu = TypeMenu(parm=self.node.parm('type'))
        self.parm_surftype_menu = SurftypeMenu(parm=self.node.parm('surftype'))
        self.parm_orient_menu = OrientMenu(parm=self.node.parm('orient'))


        # input vars:


# parm menu classes:
class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.polygon = 0
        self.mesh = 1
        self.nurbs = 2
        self.bezier = 3
        self.points = 4
        self.polygon_soup = 5


class SurftypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.rows = 0
        self.columns = 1
        self.rows_and_columns = 2
        self.triangles = 3
        self.quadrilaterals = 4
        self.alternating_triangles = 5
        self.reverse_triangles = 6


class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.xy_plane = 0
        self.yz_plane = 1
        self.zx_plane = 2



