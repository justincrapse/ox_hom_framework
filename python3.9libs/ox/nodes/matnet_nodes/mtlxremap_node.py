from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class MtlxremapNode(OXNode):
    node_type = "mtlxremap"
    parm_lookup_dict = {
        "signature": "signature",
        "inside": "in",
        "inlow": "inlow",
        "inhigh": "inhigh",
        "outlow": "outlow",
        "outhigh": "outhigh",
        "in_color3r": "in_color3r",
        "in_color3g": "in_color3g",
        "in_color3b": "in_color3b",
        "inlow_color3r": "inlow_color3r",
        "inlow_color3g": "inlow_color3g",
        "inlow_color3b": "inlow_color3b",
        "inhigh_color3r": "inhigh_color3r",
        "inhigh_color3g": "inhigh_color3g",
        "inhigh_color3b": "inhigh_color3b",
        "outlow_color3r": "outlow_color3r",
        "outlow_color3g": "outlow_color3g",
        "outlow_color3b": "outlow_color3b",
        "outhigh_color3r": "outhigh_color3r",
        "outhigh_color3g": "outhigh_color3g",
        "outhigh_color3b": "outhigh_color3b",
        "in_color3far": "in_color3FAr",
        "in_color3fag": "in_color3FAg",
        "in_color3fab": "in_color3FAb",
        "in_color4r": "in_color4r",
        "in_color4g": "in_color4g",
        "in_color4b": "in_color4b",
        "in_color4a": "in_color4a",
        "inlow_color4r": "inlow_color4r",
        "inlow_color4g": "inlow_color4g",
        "inlow_color4b": "inlow_color4b",
        "inlow_color4a": "inlow_color4a",
        "inhigh_color4r": "inhigh_color4r",
        "inhigh_color4g": "inhigh_color4g",
        "inhigh_color4b": "inhigh_color4b",
        "inhigh_color4a": "inhigh_color4a",
        "outlow_color4r": "outlow_color4r",
        "outlow_color4g": "outlow_color4g",
        "outlow_color4b": "outlow_color4b",
        "outlow_color4a": "outlow_color4a",
        "outhigh_color4r": "outhigh_color4r",
        "outhigh_color4g": "outhigh_color4g",
        "outhigh_color4b": "outhigh_color4b",
        "outhigh_color4a": "outhigh_color4a",
        "in_color4far": "in_color4FAr",
        "in_color4fag": "in_color4FAg",
        "in_color4fab": "in_color4FAb",
        "in_color4faa": "in_color4FAa",
        "in_vector2x": "in_vector2x",
        "in_vector2y": "in_vector2y",
        "inlow_vector2x": "inlow_vector2x",
        "inlow_vector2y": "inlow_vector2y",
        "inhigh_vector2x": "inhigh_vector2x",
        "inhigh_vector2y": "inhigh_vector2y",
        "outlow_vector2x": "outlow_vector2x",
        "outlow_vector2y": "outlow_vector2y",
        "outhigh_vector2x": "outhigh_vector2x",
        "outhigh_vector2y": "outhigh_vector2y",
        "in_vector2fax": "in_vector2FAx",
        "in_vector2fay": "in_vector2FAy",
        "in_vector3x": "in_vector3x",
        "in_vector3y": "in_vector3y",
        "in_vector3z": "in_vector3z",
        "inlow_vector3x": "inlow_vector3x",
        "inlow_vector3y": "inlow_vector3y",
        "inlow_vector3z": "inlow_vector3z",
        "inhigh_vector3x": "inhigh_vector3x",
        "inhigh_vector3y": "inhigh_vector3y",
        "inhigh_vector3z": "inhigh_vector3z",
        "outlow_vector3x": "outlow_vector3x",
        "outlow_vector3y": "outlow_vector3y",
        "outlow_vector3z": "outlow_vector3z",
        "outhigh_vector3x": "outhigh_vector3x",
        "outhigh_vector3y": "outhigh_vector3y",
        "outhigh_vector3z": "outhigh_vector3z",
        "in_vector3fax": "in_vector3FAx",
        "in_vector3fay": "in_vector3FAy",
        "in_vector3faz": "in_vector3FAz",
        "in_vector4x": "in_vector4x",
        "in_vector4y": "in_vector4y",
        "in_vector4z": "in_vector4z",
        "in_vector4w": "in_vector4w",
        "inlow_vector4x": "inlow_vector4x",
        "inlow_vector4y": "inlow_vector4y",
        "inlow_vector4z": "inlow_vector4z",
        "inlow_vector4w": "inlow_vector4w",
        "inhigh_vector4x": "inhigh_vector4x",
        "inhigh_vector4y": "inhigh_vector4y",
        "inhigh_vector4z": "inhigh_vector4z",
        "inhigh_vector4w": "inhigh_vector4w",
        "outlow_vector4x": "outlow_vector4x",
        "outlow_vector4y": "outlow_vector4y",
        "outlow_vector4z": "outlow_vector4z",
        "outlow_vector4w": "outlow_vector4w",
        "outhigh_vector4x": "outhigh_vector4x",
        "outhigh_vector4y": "outhigh_vector4y",
        "outhigh_vector4z": "outhigh_vector4z",
        "outhigh_vector4w": "outhigh_vector4w",
        "in_vector4fax": "in_vector4FAx",
        "in_vector4fay": "in_vector4FAy",
        "in_vector4faz": "in_vector4FAz",
        "in_vector4faw": "in_vector4FAw",
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
        self.parm_inside = Parameter(parm=self.node.parm("in"))
        self.parm_inlow = Parameter(parm=self.node.parm("inlow"))
        self.parm_inhigh = Parameter(parm=self.node.parm("inhigh"))
        self.parm_outlow = Parameter(parm=self.node.parm("outlow"))
        self.parm_outhigh = Parameter(parm=self.node.parm("outhigh"))
        self.parm_in_color3r = Parameter(parm=self.node.parm("in_color3r"))
        self.parm_in_color3g = Parameter(parm=self.node.parm("in_color3g"))
        self.parm_in_color3b = Parameter(parm=self.node.parm("in_color3b"))
        self.parm_inlow_color3r = Parameter(parm=self.node.parm("inlow_color3r"))
        self.parm_inlow_color3g = Parameter(parm=self.node.parm("inlow_color3g"))
        self.parm_inlow_color3b = Parameter(parm=self.node.parm("inlow_color3b"))
        self.parm_inhigh_color3r = Parameter(parm=self.node.parm("inhigh_color3r"))
        self.parm_inhigh_color3g = Parameter(parm=self.node.parm("inhigh_color3g"))
        self.parm_inhigh_color3b = Parameter(parm=self.node.parm("inhigh_color3b"))
        self.parm_outlow_color3r = Parameter(parm=self.node.parm("outlow_color3r"))
        self.parm_outlow_color3g = Parameter(parm=self.node.parm("outlow_color3g"))
        self.parm_outlow_color3b = Parameter(parm=self.node.parm("outlow_color3b"))
        self.parm_outhigh_color3r = Parameter(parm=self.node.parm("outhigh_color3r"))
        self.parm_outhigh_color3g = Parameter(parm=self.node.parm("outhigh_color3g"))
        self.parm_outhigh_color3b = Parameter(parm=self.node.parm("outhigh_color3b"))
        self.parm_in_color3far = Parameter(parm=self.node.parm("in_color3FAr"))
        self.parm_in_color3fag = Parameter(parm=self.node.parm("in_color3FAg"))
        self.parm_in_color3fab = Parameter(parm=self.node.parm("in_color3FAb"))
        self.parm_in_color4r = Parameter(parm=self.node.parm("in_color4r"))
        self.parm_in_color4g = Parameter(parm=self.node.parm("in_color4g"))
        self.parm_in_color4b = Parameter(parm=self.node.parm("in_color4b"))
        self.parm_in_color4a = Parameter(parm=self.node.parm("in_color4a"))
        self.parm_inlow_color4r = Parameter(parm=self.node.parm("inlow_color4r"))
        self.parm_inlow_color4g = Parameter(parm=self.node.parm("inlow_color4g"))
        self.parm_inlow_color4b = Parameter(parm=self.node.parm("inlow_color4b"))
        self.parm_inlow_color4a = Parameter(parm=self.node.parm("inlow_color4a"))
        self.parm_inhigh_color4r = Parameter(parm=self.node.parm("inhigh_color4r"))
        self.parm_inhigh_color4g = Parameter(parm=self.node.parm("inhigh_color4g"))
        self.parm_inhigh_color4b = Parameter(parm=self.node.parm("inhigh_color4b"))
        self.parm_inhigh_color4a = Parameter(parm=self.node.parm("inhigh_color4a"))
        self.parm_outlow_color4r = Parameter(parm=self.node.parm("outlow_color4r"))
        self.parm_outlow_color4g = Parameter(parm=self.node.parm("outlow_color4g"))
        self.parm_outlow_color4b = Parameter(parm=self.node.parm("outlow_color4b"))
        self.parm_outlow_color4a = Parameter(parm=self.node.parm("outlow_color4a"))
        self.parm_outhigh_color4r = Parameter(parm=self.node.parm("outhigh_color4r"))
        self.parm_outhigh_color4g = Parameter(parm=self.node.parm("outhigh_color4g"))
        self.parm_outhigh_color4b = Parameter(parm=self.node.parm("outhigh_color4b"))
        self.parm_outhigh_color4a = Parameter(parm=self.node.parm("outhigh_color4a"))
        self.parm_in_color4far = Parameter(parm=self.node.parm("in_color4FAr"))
        self.parm_in_color4fag = Parameter(parm=self.node.parm("in_color4FAg"))
        self.parm_in_color4fab = Parameter(parm=self.node.parm("in_color4FAb"))
        self.parm_in_color4faa = Parameter(parm=self.node.parm("in_color4FAa"))
        self.parm_in_vector2x = Parameter(parm=self.node.parm("in_vector2x"))
        self.parm_in_vector2y = Parameter(parm=self.node.parm("in_vector2y"))
        self.parm_inlow_vector2x = Parameter(parm=self.node.parm("inlow_vector2x"))
        self.parm_inlow_vector2y = Parameter(parm=self.node.parm("inlow_vector2y"))
        self.parm_inhigh_vector2x = Parameter(parm=self.node.parm("inhigh_vector2x"))
        self.parm_inhigh_vector2y = Parameter(parm=self.node.parm("inhigh_vector2y"))
        self.parm_outlow_vector2x = Parameter(parm=self.node.parm("outlow_vector2x"))
        self.parm_outlow_vector2y = Parameter(parm=self.node.parm("outlow_vector2y"))
        self.parm_outhigh_vector2x = Parameter(parm=self.node.parm("outhigh_vector2x"))
        self.parm_outhigh_vector2y = Parameter(parm=self.node.parm("outhigh_vector2y"))
        self.parm_in_vector2fax = Parameter(parm=self.node.parm("in_vector2FAx"))
        self.parm_in_vector2fay = Parameter(parm=self.node.parm("in_vector2FAy"))
        self.parm_in_vector3x = Parameter(parm=self.node.parm("in_vector3x"))
        self.parm_in_vector3y = Parameter(parm=self.node.parm("in_vector3y"))
        self.parm_in_vector3z = Parameter(parm=self.node.parm("in_vector3z"))
        self.parm_inlow_vector3x = Parameter(parm=self.node.parm("inlow_vector3x"))
        self.parm_inlow_vector3y = Parameter(parm=self.node.parm("inlow_vector3y"))
        self.parm_inlow_vector3z = Parameter(parm=self.node.parm("inlow_vector3z"))
        self.parm_inhigh_vector3x = Parameter(parm=self.node.parm("inhigh_vector3x"))
        self.parm_inhigh_vector3y = Parameter(parm=self.node.parm("inhigh_vector3y"))
        self.parm_inhigh_vector3z = Parameter(parm=self.node.parm("inhigh_vector3z"))
        self.parm_outlow_vector3x = Parameter(parm=self.node.parm("outlow_vector3x"))
        self.parm_outlow_vector3y = Parameter(parm=self.node.parm("outlow_vector3y"))
        self.parm_outlow_vector3z = Parameter(parm=self.node.parm("outlow_vector3z"))
        self.parm_outhigh_vector3x = Parameter(parm=self.node.parm("outhigh_vector3x"))
        self.parm_outhigh_vector3y = Parameter(parm=self.node.parm("outhigh_vector3y"))
        self.parm_outhigh_vector3z = Parameter(parm=self.node.parm("outhigh_vector3z"))
        self.parm_in_vector3fax = Parameter(parm=self.node.parm("in_vector3FAx"))
        self.parm_in_vector3fay = Parameter(parm=self.node.parm("in_vector3FAy"))
        self.parm_in_vector3faz = Parameter(parm=self.node.parm("in_vector3FAz"))
        self.parm_in_vector4x = Parameter(parm=self.node.parm("in_vector4x"))
        self.parm_in_vector4y = Parameter(parm=self.node.parm("in_vector4y"))
        self.parm_in_vector4z = Parameter(parm=self.node.parm("in_vector4z"))
        self.parm_in_vector4w = Parameter(parm=self.node.parm("in_vector4w"))
        self.parm_inlow_vector4x = Parameter(parm=self.node.parm("inlow_vector4x"))
        self.parm_inlow_vector4y = Parameter(parm=self.node.parm("inlow_vector4y"))
        self.parm_inlow_vector4z = Parameter(parm=self.node.parm("inlow_vector4z"))
        self.parm_inlow_vector4w = Parameter(parm=self.node.parm("inlow_vector4w"))
        self.parm_inhigh_vector4x = Parameter(parm=self.node.parm("inhigh_vector4x"))
        self.parm_inhigh_vector4y = Parameter(parm=self.node.parm("inhigh_vector4y"))
        self.parm_inhigh_vector4z = Parameter(parm=self.node.parm("inhigh_vector4z"))
        self.parm_inhigh_vector4w = Parameter(parm=self.node.parm("inhigh_vector4w"))
        self.parm_outlow_vector4x = Parameter(parm=self.node.parm("outlow_vector4x"))
        self.parm_outlow_vector4y = Parameter(parm=self.node.parm("outlow_vector4y"))
        self.parm_outlow_vector4z = Parameter(parm=self.node.parm("outlow_vector4z"))
        self.parm_outlow_vector4w = Parameter(parm=self.node.parm("outlow_vector4w"))
        self.parm_outhigh_vector4x = Parameter(parm=self.node.parm("outhigh_vector4x"))
        self.parm_outhigh_vector4y = Parameter(parm=self.node.parm("outhigh_vector4y"))
        self.parm_outhigh_vector4z = Parameter(parm=self.node.parm("outhigh_vector4z"))
        self.parm_outhigh_vector4w = Parameter(parm=self.node.parm("outhigh_vector4w"))
        self.parm_in_vector4fax = Parameter(parm=self.node.parm("in_vector4FAx"))
        self.parm_in_vector4fay = Parameter(parm=self.node.parm("in_vector4FAy"))
        self.parm_in_vector4faz = Parameter(parm=self.node.parm("in_vector4FAz"))
        self.parm_in_vector4faw = Parameter(parm=self.node.parm("in_vector4FAw"))

        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm("signature"))

        # input vars:
        self.input_input = "Input"
        self.input_inlow = "Inlow"
        self.input_inhigh = "Inhigh"
        self.input_outlow = "Outlow"
        self.input_outhigh = "Outhigh"


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = ("default", 0)
