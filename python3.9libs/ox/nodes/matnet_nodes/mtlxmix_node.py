from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class MtlxmixNode(OXNode):
    node_type = "mtlxmix"
    parm_lookup_dict = {
        "signature": "signature",
        "fg": "fg",
        "bg": "bg",
        "mix": "mix",
        "fg_bsdf": "fg_bsdf",
        "bg_bsdf": "bg_bsdf",
        "fg_color3r": "fg_color3r",
        "fg_color3g": "fg_color3g",
        "fg_color3b": "fg_color3b",
        "bg_color3r": "bg_color3r",
        "bg_color3g": "bg_color3g",
        "bg_color3b": "bg_color3b",
        "fg_color4r": "fg_color4r",
        "fg_color4g": "fg_color4g",
        "fg_color4b": "fg_color4b",
        "fg_color4a": "fg_color4a",
        "bg_color4r": "bg_color4r",
        "bg_color4g": "bg_color4g",
        "bg_color4b": "bg_color4b",
        "bg_color4a": "bg_color4a",
        "fg_displacementshader": "fg_displacementshader",
        "bg_displacementshader": "bg_displacementshader",
        "fg_edf": "fg_edf",
        "bg_edf": "bg_edf",
        "fg_surfaceshader": "fg_surfaceshader",
        "bg_surfaceshader": "bg_surfaceshader",
        "fg_vdf": "fg_vdf",
        "bg_vdf": "bg_vdf",
        "fg_vector2x": "fg_vector2x",
        "fg_vector2y": "fg_vector2y",
        "bg_vector2x": "bg_vector2x",
        "bg_vector2y": "bg_vector2y",
        "fg_vector3x": "fg_vector3x",
        "fg_vector3y": "fg_vector3y",
        "fg_vector3z": "fg_vector3z",
        "bg_vector3x": "bg_vector3x",
        "bg_vector3y": "bg_vector3y",
        "bg_vector3z": "bg_vector3z",
        "fg_vector4x": "fg_vector4x",
        "fg_vector4y": "fg_vector4y",
        "fg_vector4z": "fg_vector4z",
        "fg_vector4w": "fg_vector4w",
        "bg_vector4x": "bg_vector4x",
        "bg_vector4y": "bg_vector4y",
        "bg_vector4z": "bg_vector4z",
        "bg_vector4w": "bg_vector4w",
        "fg_volumeshader": "fg_volumeshader",
        "bg_volumeshader": "bg_volumeshader",
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
        self.parm_fg = Parameter(parm=self.node.parm("fg"))
        self.parm_bg = Parameter(parm=self.node.parm("bg"))
        self.parm_mix = Parameter(parm=self.node.parm("mix"))
        self.parm_fg_bsdf = Parameter(parm=self.node.parm("fg_bsdf"))
        self.parm_bg_bsdf = Parameter(parm=self.node.parm("bg_bsdf"))
        self.parm_fg_color3r = Parameter(parm=self.node.parm("fg_color3r"))
        self.parm_fg_color3g = Parameter(parm=self.node.parm("fg_color3g"))
        self.parm_fg_color3b = Parameter(parm=self.node.parm("fg_color3b"))
        self.parm_bg_color3r = Parameter(parm=self.node.parm("bg_color3r"))
        self.parm_bg_color3g = Parameter(parm=self.node.parm("bg_color3g"))
        self.parm_bg_color3b = Parameter(parm=self.node.parm("bg_color3b"))
        self.parm_fg_color4r = Parameter(parm=self.node.parm("fg_color4r"))
        self.parm_fg_color4g = Parameter(parm=self.node.parm("fg_color4g"))
        self.parm_fg_color4b = Parameter(parm=self.node.parm("fg_color4b"))
        self.parm_fg_color4a = Parameter(parm=self.node.parm("fg_color4a"))
        self.parm_bg_color4r = Parameter(parm=self.node.parm("bg_color4r"))
        self.parm_bg_color4g = Parameter(parm=self.node.parm("bg_color4g"))
        self.parm_bg_color4b = Parameter(parm=self.node.parm("bg_color4b"))
        self.parm_bg_color4a = Parameter(parm=self.node.parm("bg_color4a"))
        self.parm_fg_displacementshader = Parameter(
            parm=self.node.parm("fg_displacementshader")
        )
        self.parm_bg_displacementshader = Parameter(
            parm=self.node.parm("bg_displacementshader")
        )
        self.parm_fg_edf = Parameter(parm=self.node.parm("fg_edf"))
        self.parm_bg_edf = Parameter(parm=self.node.parm("bg_edf"))
        self.parm_fg_surfaceshader = Parameter(parm=self.node.parm("fg_surfaceshader"))
        self.parm_bg_surfaceshader = Parameter(parm=self.node.parm("bg_surfaceshader"))
        self.parm_fg_vdf = Parameter(parm=self.node.parm("fg_vdf"))
        self.parm_bg_vdf = Parameter(parm=self.node.parm("bg_vdf"))
        self.parm_fg_vector2x = Parameter(parm=self.node.parm("fg_vector2x"))
        self.parm_fg_vector2y = Parameter(parm=self.node.parm("fg_vector2y"))
        self.parm_bg_vector2x = Parameter(parm=self.node.parm("bg_vector2x"))
        self.parm_bg_vector2y = Parameter(parm=self.node.parm("bg_vector2y"))
        self.parm_fg_vector3x = Parameter(parm=self.node.parm("fg_vector3x"))
        self.parm_fg_vector3y = Parameter(parm=self.node.parm("fg_vector3y"))
        self.parm_fg_vector3z = Parameter(parm=self.node.parm("fg_vector3z"))
        self.parm_bg_vector3x = Parameter(parm=self.node.parm("bg_vector3x"))
        self.parm_bg_vector3y = Parameter(parm=self.node.parm("bg_vector3y"))
        self.parm_bg_vector3z = Parameter(parm=self.node.parm("bg_vector3z"))
        self.parm_fg_vector4x = Parameter(parm=self.node.parm("fg_vector4x"))
        self.parm_fg_vector4y = Parameter(parm=self.node.parm("fg_vector4y"))
        self.parm_fg_vector4z = Parameter(parm=self.node.parm("fg_vector4z"))
        self.parm_fg_vector4w = Parameter(parm=self.node.parm("fg_vector4w"))
        self.parm_bg_vector4x = Parameter(parm=self.node.parm("bg_vector4x"))
        self.parm_bg_vector4y = Parameter(parm=self.node.parm("bg_vector4y"))
        self.parm_bg_vector4z = Parameter(parm=self.node.parm("bg_vector4z"))
        self.parm_bg_vector4w = Parameter(parm=self.node.parm("bg_vector4w"))
        self.parm_fg_volumeshader = Parameter(parm=self.node.parm("fg_volumeshader"))
        self.parm_bg_volumeshader = Parameter(parm=self.node.parm("bg_volumeshader"))

        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm("signature"))

        # input vars:
        self.input_fg = "Fg"
        self.input_bg = "Bg"
        self.input_mix = "Mix"


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = ("default", 0)
