from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class MaterialblenderNode(OXNode):
    node_type = "redshift::MaterialBlender"
    parm_lookup_dict = {
        "base_material_0": "Base_Material_0",
        "basecolorr": "baseColorr",
        "basecolorg": "baseColorg",
        "basecolorb": "baseColorb",
        "layer_1_1": "Layer_1_1",
        "layercolor1r": "layerColor1r",
        "layercolor1g": "layerColor1g",
        "layercolor1b": "layerColor1b",
        "blendcolor1r": "blendColor1r",
        "blendcolor1g": "blendColor1g",
        "blendcolor1b": "blendColor1b",
        "additivemode1": "additiveMode1",
        "layer_2_2": "Layer_2_2",
        "layercolor2r": "layerColor2r",
        "layercolor2g": "layerColor2g",
        "layercolor2b": "layerColor2b",
        "blendcolor2r": "blendColor2r",
        "blendcolor2g": "blendColor2g",
        "blendcolor2b": "blendColor2b",
        "additivemode2": "additiveMode2",
        "layer_3_3": "Layer_3_3",
        "layercolor3r": "layerColor3r",
        "layercolor3g": "layerColor3g",
        "layercolor3b": "layerColor3b",
        "blendcolor3r": "blendColor3r",
        "blendcolor3g": "blendColor3g",
        "blendcolor3b": "blendColor3b",
        "additivemode3": "additiveMode3",
        "layer_4_4": "Layer_4_4",
        "layercolor4r": "layerColor4r",
        "layercolor4g": "layerColor4g",
        "layercolor4b": "layerColor4b",
        "blendcolor4r": "blendColor4r",
        "blendcolor4g": "blendColor4g",
        "blendcolor4b": "blendColor4b",
        "additivemode4": "additiveMode4",
        "layer_5_5": "Layer_5_5",
        "layercolor5r": "layerColor5r",
        "layercolor5g": "layerColor5g",
        "layercolor5b": "layerColor5b",
        "blendcolor5r": "blendColor5r",
        "blendcolor5g": "blendColor5g",
        "blendcolor5b": "blendColor5b",
        "additivemode5": "additiveMode5",
        "layer_6_6": "Layer_6_6",
        "layercolor6r": "layerColor6r",
        "layercolor6g": "layerColor6g",
        "layercolor6b": "layerColor6b",
        "blendcolor6r": "blendColor6r",
        "blendcolor6g": "blendColor6g",
        "blendcolor6b": "blendColor6b",
        "additivemode6": "additiveMode6",
        "shader_skipdefvalparms": "shader_skipdefvalparms",
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
        self.parm_base_material_0 = Parameter(parm=self.node.parm("Base_Material_0"))
        self.parm_basecolorr = Parameter(parm=self.node.parm("baseColorr"))
        self.parm_basecolorg = Parameter(parm=self.node.parm("baseColorg"))
        self.parm_basecolorb = Parameter(parm=self.node.parm("baseColorb"))
        self.parm_layer_1_1 = Parameter(parm=self.node.parm("Layer_1_1"))
        self.parm_layercolor1r = Parameter(parm=self.node.parm("layerColor1r"))
        self.parm_layercolor1g = Parameter(parm=self.node.parm("layerColor1g"))
        self.parm_layercolor1b = Parameter(parm=self.node.parm("layerColor1b"))
        self.parm_blendcolor1r = Parameter(parm=self.node.parm("blendColor1r"))
        self.parm_blendcolor1g = Parameter(parm=self.node.parm("blendColor1g"))
        self.parm_blendcolor1b = Parameter(parm=self.node.parm("blendColor1b"))
        self.parm_additivemode1 = Parameter(parm=self.node.parm("additiveMode1"))
        self.parm_layer_2_2 = Parameter(parm=self.node.parm("Layer_2_2"))
        self.parm_layercolor2r = Parameter(parm=self.node.parm("layerColor2r"))
        self.parm_layercolor2g = Parameter(parm=self.node.parm("layerColor2g"))
        self.parm_layercolor2b = Parameter(parm=self.node.parm("layerColor2b"))
        self.parm_blendcolor2r = Parameter(parm=self.node.parm("blendColor2r"))
        self.parm_blendcolor2g = Parameter(parm=self.node.parm("blendColor2g"))
        self.parm_blendcolor2b = Parameter(parm=self.node.parm("blendColor2b"))
        self.parm_additivemode2 = Parameter(parm=self.node.parm("additiveMode2"))
        self.parm_layer_3_3 = Parameter(parm=self.node.parm("Layer_3_3"))
        self.parm_layercolor3r = Parameter(parm=self.node.parm("layerColor3r"))
        self.parm_layercolor3g = Parameter(parm=self.node.parm("layerColor3g"))
        self.parm_layercolor3b = Parameter(parm=self.node.parm("layerColor3b"))
        self.parm_blendcolor3r = Parameter(parm=self.node.parm("blendColor3r"))
        self.parm_blendcolor3g = Parameter(parm=self.node.parm("blendColor3g"))
        self.parm_blendcolor3b = Parameter(parm=self.node.parm("blendColor3b"))
        self.parm_additivemode3 = Parameter(parm=self.node.parm("additiveMode3"))
        self.parm_layer_4_4 = Parameter(parm=self.node.parm("Layer_4_4"))
        self.parm_layercolor4r = Parameter(parm=self.node.parm("layerColor4r"))
        self.parm_layercolor4g = Parameter(parm=self.node.parm("layerColor4g"))
        self.parm_layercolor4b = Parameter(parm=self.node.parm("layerColor4b"))
        self.parm_blendcolor4r = Parameter(parm=self.node.parm("blendColor4r"))
        self.parm_blendcolor4g = Parameter(parm=self.node.parm("blendColor4g"))
        self.parm_blendcolor4b = Parameter(parm=self.node.parm("blendColor4b"))
        self.parm_additivemode4 = Parameter(parm=self.node.parm("additiveMode4"))
        self.parm_layer_5_5 = Parameter(parm=self.node.parm("Layer_5_5"))
        self.parm_layercolor5r = Parameter(parm=self.node.parm("layerColor5r"))
        self.parm_layercolor5g = Parameter(parm=self.node.parm("layerColor5g"))
        self.parm_layercolor5b = Parameter(parm=self.node.parm("layerColor5b"))
        self.parm_blendcolor5r = Parameter(parm=self.node.parm("blendColor5r"))
        self.parm_blendcolor5g = Parameter(parm=self.node.parm("blendColor5g"))
        self.parm_blendcolor5b = Parameter(parm=self.node.parm("blendColor5b"))
        self.parm_additivemode5 = Parameter(parm=self.node.parm("additiveMode5"))
        self.parm_layer_6_6 = Parameter(parm=self.node.parm("Layer_6_6"))
        self.parm_layercolor6r = Parameter(parm=self.node.parm("layerColor6r"))
        self.parm_layercolor6g = Parameter(parm=self.node.parm("layerColor6g"))
        self.parm_layercolor6b = Parameter(parm=self.node.parm("layerColor6b"))
        self.parm_blendcolor6r = Parameter(parm=self.node.parm("blendColor6r"))
        self.parm_blendcolor6g = Parameter(parm=self.node.parm("blendColor6g"))
        self.parm_blendcolor6b = Parameter(parm=self.node.parm("blendColor6b"))
        self.parm_additivemode6 = Parameter(parm=self.node.parm("additiveMode6"))
        self.parm_shader_skipdefvalparms = Parameter(
            parm=self.node.parm("shader_skipdefvalparms")
        )

        # parm menu vars:

        # input vars:
        self.input_basecolor = "baseColor"
        self.input_layercolor1 = "layerColor1"
        self.input_blendcolor1 = "blendColor1"
        self.input_layercolor2 = "layerColor2"
        self.input_blendcolor2 = "blendColor2"
        self.input_layercolor3 = "layerColor3"
        self.input_blendcolor3 = "blendColor3"
        self.input_layercolor4 = "layerColor4"
        self.input_blendcolor4 = "blendColor4"
        self.input_layercolor5 = "layerColor5"
        self.input_blendcolor5 = "blendColor5"
        self.input_layercolor6 = "layerColor6"
        self.input_blendcolor6 = "blendColor6"


# parm menu classes:
