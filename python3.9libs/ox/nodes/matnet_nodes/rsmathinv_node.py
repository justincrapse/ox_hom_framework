from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RsmathinvNode(OXNode):
    node_type = 'redshift::RSMathInv'
    parm_lookup_dict = {'input': 'input', 'math_op': 'math_op', 'shader_skipdefvalparms': 'shader_skipdefvalparms'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_input = Parameter(parm=self.node.parm('input'))
        self.parm_math_op = Parameter(parm=self.node.parm('math_op'))
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))

        
        # parm menu vars:


        # input vars:
        self.input_input = 'input'


# parm menu classes:

