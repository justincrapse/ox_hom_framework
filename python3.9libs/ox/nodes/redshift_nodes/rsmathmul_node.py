from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class RsmathmulNode(OXNode):
    node_type = "redshift::RSMathMul"
    parm_lookup_dict = {
        "input1": "input1",
        "input2": "input2",
        "math_op": "math_op",
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
        self.parm_input1 = Parameter(parm=self.node.parm("input1"))
        self.parm_input2 = Parameter(parm=self.node.parm("input2"))
        self.parm_math_op = Parameter(parm=self.node.parm("math_op"))
        self.parm_shader_skipdefvalparms = Parameter(
            parm=self.node.parm("shader_skipdefvalparms")
        )

        # parm menu vars:

        # input vars:
        self.input_input1 = "input1"
        self.input_input2 = "input2"


# parm menu classes:
