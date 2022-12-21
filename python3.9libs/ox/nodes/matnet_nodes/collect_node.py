from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class CollectNode(OXNode):
    node_type = "collect"
    parm_lookup_dict = {
        "inputnum": "inputnum",
        "inputname1": "inputname1",
        "inputlabel1": "inputlabel1",
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
        self.parm_inputnum = Parameter(parm=self.node.parm("inputnum"))
        self.parm_inputname1 = Parameter(parm=self.node.parm("inputname1"))
        self.parm_inputlabel1 = Parameter(parm=self.node.parm("inputlabel1"))

        # parm menu vars:

        # input vars:
        self.input_input_1 = "Input 1"
        self.input_input_2 = "Input 2"


# parm menu classes:
