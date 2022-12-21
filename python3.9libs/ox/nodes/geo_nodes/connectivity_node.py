from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class ConnectivityNode(OXNode):
    node_type = "connectivity"
    parm_lookup_dict = {
        "connecttype": "connecttype",
        "attribname": "attribname",
        "attribtype": "attribtype",
        "prefix": "prefix",
        "createvarmap": "createvarmap",
        "varname": "varname",
        "seamgroup": "seamgroup",
        "byuv": "byuv",
        "uvattrib": "uvattrib",
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
        self.parm_attribname = Parameter(parm=self.node.parm("attribname"))
        self.parm_prefix = Parameter(parm=self.node.parm("prefix"))
        self.parm_createvarmap = Parameter(parm=self.node.parm("createvarmap"))
        self.parm_varname = Parameter(parm=self.node.parm("varname"))
        self.parm_seamgroup = Parameter(parm=self.node.parm("seamgroup"))
        self.parm_byuv = Parameter(parm=self.node.parm("byuv"))
        self.parm_uvattrib = Parameter(parm=self.node.parm("uvattrib"))

        # parm menu vars:
        self.parm_connecttype = ConnecttypeMenu(parm=self.node.parm("connecttype"))
        self.parm_attribtype = AttribtypeMenu(parm=self.node.parm("attribtype"))

        # input vars:
        self.input_input_1 = "Input 1"


# parm menu classes:
class ConnecttypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_point = ("point", 0)
        self.menu_primitive = ("prim", 1)


class AttribtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_integer = ("int", 0)
        self.menu_string = ("string", 1)
