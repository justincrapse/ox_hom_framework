from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class BoxNode(OXNode):
    node_type = "box"
    parm_lookup_dict = {
        "type": "type",
        "surftype": "surftype",
        "consolidatepts": "consolidatepts",
        "sizex": "sizex",
        "sizey": "sizey",
        "sizez": "sizez",
        "tx": "tx",
        "ty": "ty",
        "tz": "tz",
        "rx": "rx",
        "ry": "ry",
        "rz": "rz",
        "scale": "scale",
        "divrate1": "divrate1",
        "divrate2": "divrate2",
        "divrate3": "divrate3",
        "orderrate1": "orderrate1",
        "orderrate2": "orderrate2",
        "orderrate3": "orderrate3",
        "dodivs": "dodivs",
        "divsx": "divsx",
        "divsy": "divsy",
        "divsz": "divsz",
        "rebar": "rebar",
        "orientedbbox": "orientedbbox",
        "vertexnormals": "vertexnormals",
    }

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(
                node_type_name=self.node_type, node_name=node_name
            )
        self.node_name = self.node.name()
        super().__init__(node=self.node)

        # parm vars:
        self.parm_consolidatepts = Parameter(parm=self.node.parm("consolidatepts"))
        self.parm_sizex = Parameter(parm=self.node.parm("sizex"))
        self.parm_sizey = Parameter(parm=self.node.parm("sizey"))
        self.parm_sizez = Parameter(parm=self.node.parm("sizez"))
        self.parm_tx = Parameter(parm=self.node.parm("tx"))
        self.parm_ty = Parameter(parm=self.node.parm("ty"))
        self.parm_tz = Parameter(parm=self.node.parm("tz"))
        self.parm_rx = Parameter(parm=self.node.parm("rx"))
        self.parm_ry = Parameter(parm=self.node.parm("ry"))
        self.parm_rz = Parameter(parm=self.node.parm("rz"))
        self.parm_scale = Parameter(parm=self.node.parm("scale"))
        self.parm_divrate1 = Parameter(parm=self.node.parm("divrate1"))
        self.parm_divrate2 = Parameter(parm=self.node.parm("divrate2"))
        self.parm_divrate3 = Parameter(parm=self.node.parm("divrate3"))
        self.parm_orderrate1 = Parameter(parm=self.node.parm("orderrate1"))
        self.parm_orderrate2 = Parameter(parm=self.node.parm("orderrate2"))
        self.parm_orderrate3 = Parameter(parm=self.node.parm("orderrate3"))
        self.parm_dodivs = Parameter(parm=self.node.parm("dodivs"))
        self.parm_divsx = Parameter(parm=self.node.parm("divsx"))
        self.parm_divsy = Parameter(parm=self.node.parm("divsy"))
        self.parm_divsz = Parameter(parm=self.node.parm("divsz"))
        self.parm_rebar = Parameter(parm=self.node.parm("rebar"))
        self.parm_orientedbbox = Parameter(parm=self.node.parm("orientedbbox"))
        self.parm_vertexnormals = Parameter(parm=self.node.parm("vertexnormals"))

        # parm menu vars:
        self.parm_type = TypeMenu(parm=self.node.parm("type"))
        self.parm_surftype = SurftypeMenu(parm=self.node.parm("surftype"))

        # input vars:
        self.input_bounding_source = "Bounding Source"


# parm menu classes:
class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_polygon = ("poly", 0)
        self.menu_polygon_mesh = ("polymesh", 1)
        self.menu_mesh = ("mesh", 2)
        self.menu_nurbs = ("nurbs", 3)
        self.menu_bezier = ("bezier", 4)
        self.menu_points = ("points", 5)
        self.menu_primitive = ("prim", 6)


class SurftypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rows = ("rows", 0)
        self.menu_columns = ("cols", 1)
        self.menu_rows_and_columns = ("rowcol", 2)
        self.menu_triangles = ("triangles", 3)
        self.menu_quadrilaterals = ("quads", 4)
        self.menu_alternating_triangles = ("alttriangles", 5)
        self.menu_reverse_triangles = ("revtriangles", 6)
