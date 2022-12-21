from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class BumpblenderNode(OXNode):
    node_type = "redshift::BumpBlender"
    parm_lookup_dict = {
        "additive": "additive",
        "base_0": "Base_0",
        "baseinput1": "baseInput1",
        "baseinput2": "baseInput2",
        "baseinput3": "baseInput3",
        "layer_0_1": "Layer_0_1",
        "bumpinput01": "bumpInput01",
        "bumpinput02": "bumpInput02",
        "bumpinput03": "bumpInput03",
        "bumpweight0": "bumpWeight0",
        "layer_1_2": "Layer_1_2",
        "bumpinput11": "bumpInput11",
        "bumpinput12": "bumpInput12",
        "bumpinput13": "bumpInput13",
        "bumpweight1": "bumpWeight1",
        "layer_2_3": "Layer_2_3",
        "bumpinput21": "bumpInput21",
        "bumpinput22": "bumpInput22",
        "bumpinput23": "bumpInput23",
        "bumpweight2": "bumpWeight2",
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
        self.parm_additive = Parameter(parm=self.node.parm("additive"))
        self.parm_base_0 = Parameter(parm=self.node.parm("Base_0"))
        self.parm_baseinput1 = Parameter(parm=self.node.parm("baseInput1"))
        self.parm_baseinput2 = Parameter(parm=self.node.parm("baseInput2"))
        self.parm_baseinput3 = Parameter(parm=self.node.parm("baseInput3"))
        self.parm_layer_0_1 = Parameter(parm=self.node.parm("Layer_0_1"))
        self.parm_bumpinput01 = Parameter(parm=self.node.parm("bumpInput01"))
        self.parm_bumpinput02 = Parameter(parm=self.node.parm("bumpInput02"))
        self.parm_bumpinput03 = Parameter(parm=self.node.parm("bumpInput03"))
        self.parm_bumpweight0 = Parameter(parm=self.node.parm("bumpWeight0"))
        self.parm_layer_1_2 = Parameter(parm=self.node.parm("Layer_1_2"))
        self.parm_bumpinput11 = Parameter(parm=self.node.parm("bumpInput11"))
        self.parm_bumpinput12 = Parameter(parm=self.node.parm("bumpInput12"))
        self.parm_bumpinput13 = Parameter(parm=self.node.parm("bumpInput13"))
        self.parm_bumpweight1 = Parameter(parm=self.node.parm("bumpWeight1"))
        self.parm_layer_2_3 = Parameter(parm=self.node.parm("Layer_2_3"))
        self.parm_bumpinput21 = Parameter(parm=self.node.parm("bumpInput21"))
        self.parm_bumpinput22 = Parameter(parm=self.node.parm("bumpInput22"))
        self.parm_bumpinput23 = Parameter(parm=self.node.parm("bumpInput23"))
        self.parm_bumpweight2 = Parameter(parm=self.node.parm("bumpWeight2"))
        self.parm_shader_skipdefvalparms = Parameter(
            parm=self.node.parm("shader_skipdefvalparms")
        )

        # parm menu vars:

        # input vars:
        self.input_baseinput = "baseInput"
        self.input_bumpinput0 = "bumpInput0"
        self.input_bumpweight0 = "bumpWeight0"
        self.input_bumpinput1 = "bumpInput1"
        self.input_bumpweight1 = "bumpWeight1"
        self.input_bumpinput2 = "bumpInput2"
        self.input_bumpweight2 = "bumpWeight2"


# parm menu classes:
