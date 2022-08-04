from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class TorusNode(OXNode):
    node_type = 'torus'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'type': 'type', 'surftype': 'surftype', 'orient': 'orient', 'radx': 'radx', 'rady': 'rady', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'scale': 'scale', 'rows': 'rows', 'cols': 'cols', 'imperfect': 'imperfect', 'orderu': 'orderu', 'orderv': 'orderv', 'beginangleu': 'beginangleu', 'endangleu': 'endangleu', 'beginanglev': 'beginanglev', 'endanglev': 'endanglev', 'closeu': 'closeu', 'closev': 'closev', 'capu': 'capu', 'capv': 'capv'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_radx = Parameter(parm=self.node.parm('radx'))
        self.parm_rady = Parameter(parm=self.node.parm('rady'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_rows = Parameter(parm=self.node.parm('rows'))
        self.parm_cols = Parameter(parm=self.node.parm('cols'))
        self.parm_imperfect = Parameter(parm=self.node.parm('imperfect'))
        self.parm_orderu = Parameter(parm=self.node.parm('orderu'))
        self.parm_orderv = Parameter(parm=self.node.parm('orderv'))
        self.parm_beginangleu = Parameter(parm=self.node.parm('beginangleu'))
        self.parm_endangleu = Parameter(parm=self.node.parm('endangleu'))
        self.parm_beginanglev = Parameter(parm=self.node.parm('beginanglev'))
        self.parm_endanglev = Parameter(parm=self.node.parm('endanglev'))
        self.parm_closeu = Parameter(parm=self.node.parm('closeu'))
        self.parm_closev = Parameter(parm=self.node.parm('closev'))
        self.parm_capu = Parameter(parm=self.node.parm('capu'))
        self.parm_capv = Parameter(parm=self.node.parm('capv'))

        
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
        self.menu_polygon = "poly"
        self.menu_mesh = "mesh"
        self.menu_nurbs = "nurbs"
        self.menu_bezier = "bezier"
        self.menu_polygon_soup = "polysoup"


class SurftypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rows = "rows"
        self.menu_columns = "cols"
        self.menu_rows_and_columns = "rowcol"
        self.menu_triangles = "triangles"
        self.menu_quadrilaterals = "quads"
        self.menu_alternating_triangles = "alttriangles"
        self.menu_reverse_triangles = "revtriangles"


class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_axis = "x"
        self.menu_y_axis = "y"
        self.menu_z_axis = "z"



