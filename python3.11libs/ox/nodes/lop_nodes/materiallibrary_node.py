from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class MateriallibraryNode(OXNode):
    node_type = "materiallibrary"
    parm_lookup_dict = {
        "genpreviewshaders": "genpreviewshaders",
        "allowparmanim": "allowparmanim",
        "referencerendervars": "referencerendervars",
        "parentprimtype": "parentprimtype",
        "matpathprefix": "matpathprefix",
        "fillgroup": "fillgroup",
        "matnet": "matnet",
        "containerpath": "containerpath",
        "fillmaterials": "fillmaterials",
        "materials": "materials",
        "enable1": "enable1",
        "matflag1": "matflag1",
        "matnode1": "matnode1",
        "matpath1": "matpath1",
        "assign1": "assign1",
        "geopath1": "geopath1",
        "tabmenufolder": "tabmenufolder",
        "tabmenumask": "tabmenumask",
        "fillgroup2": "fillgroup2",
    }

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)

        # parm vars:
        self.parm_genpreviewshaders = Parameter(parm=self.node.parm("genpreviewshaders"))
        self.parm_allowparmanim = Parameter(parm=self.node.parm("allowparmanim"))
        self.parm_referencerendervars = Parameter(parm=self.node.parm("referencerendervars"))
        self.parm_matpathprefix = Parameter(parm=self.node.parm("matpathprefix"))
        self.parm_fillgroup = Parameter(parm=self.node.parm("fillgroup"))
        self.parm_matnet = Parameter(parm=self.node.parm("matnet"))
        self.parm_containerpath = Parameter(parm=self.node.parm("containerpath"))
        self.parm_fillmaterials = Parameter(parm=self.node.parm("fillmaterials"))
        self.parm_materials = Parameter(parm=self.node.parm("materials"))
        self.parm_enable1 = Parameter(parm=self.node.parm("enable1"))
        self.parm_matflag1 = Parameter(parm=self.node.parm("matflag1"))
        self.parm_matnode1 = Parameter(parm=self.node.parm("matnode1"))
        self.parm_matpath1 = Parameter(parm=self.node.parm("matpath1"))
        self.parm_assign1 = Parameter(parm=self.node.parm("assign1"))
        self.parm_geopath1 = Parameter(parm=self.node.parm("geopath1"))
        self.parm_tabmenufolder = Parameter(parm=self.node.parm("tabmenufolder"))
        self.parm_tabmenumask = Parameter(parm=self.node.parm("tabmenumask"))
        self.parm_fillgroup2 = Parameter(parm=self.node.parm("fillgroup2"))

        # parm menu vars:
        self.parm_parentprimtype = ParentprimtypeMenu(parm=self.node.parm("parentprimtype"))

        # input vars:
        self.input_input_stage = "Input Stage"


# parm menu classes:
class ParentprimtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("", 0)
        self.menu_xform = ("UsdGeomXform", 1)
        self.menu_scope = ("UsdGeomScope", 2)
