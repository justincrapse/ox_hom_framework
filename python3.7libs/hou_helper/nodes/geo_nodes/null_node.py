from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class NullNode(HHNode):
    node_type = 'null'
    parm_lookup_dict = {'copyinput': 'copyinput', 'cacheinput': 'cacheinput'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_copyinput = Parameter(parm=self.node.parm('copyinput'))
        self.parm_cacheinput = Parameter(parm=self.node.parm('cacheinput'))

        
        # parm menu vars:


        # input vars:
        self.input_input_1 = 0


# parm menu classes:
