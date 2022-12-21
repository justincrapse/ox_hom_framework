from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class MaterialNode(OXNode):
    node_type = "material"
    parm_lookup_dict = {
        "style": "style",
        "uselabels": "uselabels",
        "createstylesheets": "createstylesheets",
        "fullpath": "fullpath",
        "num_materials": "num_materials",
        "group1": "group1",
        "shop_materialpath1": "shop_materialpath1",
        "localvar1": "localvar1",
        "mergeoverride1": "mergeoverride1",
        "num_local1": "num_local1",
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
        self.parm_createstylesheets = Parameter(
            parm=self.node.parm("createstylesheets")
        )
        self.parm_fullpath = Parameter(parm=self.node.parm("fullpath"))
        self.parm_num_materials = Parameter(parm=self.node.parm("num_materials"))
        self.parm_group1 = Parameter(parm=self.node.parm("group1"))
        self.parm_shop_materialpath1 = Parameter(
            parm=self.node.parm("shop_materialpath1")
        )
        self.parm_localvar1 = Parameter(parm=self.node.parm("localvar1"))
        self.parm_mergeoverride1 = Parameter(parm=self.node.parm("mergeoverride1"))
        self.parm_num_local1 = Parameter(parm=self.node.parm("num_local1"))

        # parm menu vars:
        self.parm_style = StyleMenu(parm=self.node.parm("style"))
        self.parm_uselabels = UselabelsMenu(parm=self.node.parm("uselabels"))

        # input vars:
        self.input_source = "Source"


# parm menu classes:
class StyleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_point_attributes = ("point", 0)
        self.menu_primitive_attributes = ("primitive", 1)
        self.menu_detail_attribute = ("detail", 2)


class UselabelsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_use_parameter_labels_for_override_menu = ("uselabels", 0)
        self.menu_use_parameter_names_for_override_menu = ("usenames", 1)
