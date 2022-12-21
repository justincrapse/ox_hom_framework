from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class ConvertheightfieldNode(OXNode):
    node_type = "convertheightfield"
    parm_lookup_dict = {
        "layer": "layer",
        "conversion": "conversion",
        "surftype": "surftype",
        "lod": "lod",
        "bakecd": "bakecd",
        "folder0": "folder0",
        "doextrude": "doextrude",
        "depth": "depth",
        "basenormalx": "basenormalx",
        "basenormaly": "basenormaly",
        "basenormalz": "basenormalz",
        "flat": "flat",
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
        self.parm_layer = Parameter(parm=self.node.parm("layer"))
        self.parm_lod = Parameter(parm=self.node.parm("lod"))
        self.parm_bakecd = Parameter(parm=self.node.parm("bakecd"))
        self.parm_folder0 = Parameter(parm=self.node.parm("folder0"))
        self.parm_doextrude = Parameter(parm=self.node.parm("doextrude"))
        self.parm_depth = Parameter(parm=self.node.parm("depth"))
        self.parm_basenormalx = Parameter(parm=self.node.parm("basenormalx"))
        self.parm_basenormaly = Parameter(parm=self.node.parm("basenormaly"))
        self.parm_basenormalz = Parameter(parm=self.node.parm("basenormalz"))
        self.parm_flat = Parameter(parm=self.node.parm("flat"))

        # parm menu vars:
        self.parm_conversion = ConversionMenu(parm=self.node.parm("conversion"))
        self.parm_surftype = SurftypeMenu(parm=self.node.parm("surftype"))

        # input vars:
        self.input_terrain = "Terrain"


# parm menu classes:
class ConversionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_polygon = ("poly", 0)
        self.menu_polygon_soup = ("polysoup", 1)
        self.menu_vdb = ("vdb", 2)


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
