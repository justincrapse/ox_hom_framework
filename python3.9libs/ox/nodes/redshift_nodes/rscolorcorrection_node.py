from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class RscolorcorrectionNode(OXNode):
    node_type = "redshift::RSColorCorrection"
    parm_lookup_dict = {
        "inputr": "inputr",
        "inputg": "inputg",
        "inputb": "inputb",
        "inputa": "inputa",
        "gamma": "gamma",
        "contrast": "contrast",
        "hue": "hue",
        "saturation": "saturation",
        "level": "level",
        "updatedmode": "updatedMode",
        "xsimode": "xsiMode",
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
        self.parm_inputr = Parameter(parm=self.node.parm("inputr"))
        self.parm_inputg = Parameter(parm=self.node.parm("inputg"))
        self.parm_inputb = Parameter(parm=self.node.parm("inputb"))
        self.parm_inputa = Parameter(parm=self.node.parm("inputa"))
        self.parm_gamma = Parameter(parm=self.node.parm("gamma"))
        self.parm_contrast = Parameter(parm=self.node.parm("contrast"))
        self.parm_hue = Parameter(parm=self.node.parm("hue"))
        self.parm_saturation = Parameter(parm=self.node.parm("saturation"))
        self.parm_level = Parameter(parm=self.node.parm("level"))
        self.parm_updatedmode = Parameter(parm=self.node.parm("updatedMode"))
        self.parm_xsimode = Parameter(parm=self.node.parm("xsiMode"))
        self.parm_shader_skipdefvalparms = Parameter(
            parm=self.node.parm("shader_skipdefvalparms")
        )

        # parm menu vars:

        # input vars:
        self.input_input = "input"
        self.input_gamma = "gamma"
        self.input_contrast = "contrast"
        self.input_hue = "hue"
        self.input_saturation = "saturation"
        self.input_level = "level"


# parm menu classes:
