from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SubnetNode(OXNode):
    node_type = 'subnet'
    parm_lookup_dict = {'inputs': 'inputs', 'outputs': 'outputs', 'inputlabel1': 'inputlabel1', 'inputtype1': 'inputtype1', 'outputlabel1': 'outputlabel1', 'outputtype1': 'outputtype1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_inputs = Parameter(parm=self.node.parm('inputs'))
        self.parm_outputs = Parameter(parm=self.node.parm('outputs'))
        self.parm_inputlabel1 = Parameter(parm=self.node.parm('inputlabel1'))
        self.parm_outputlabel1 = Parameter(parm=self.node.parm('outputlabel1'))

        
        # parm menu vars:
        self.parm_inputtype1 = Inputtype1Menu(parm=self.node.parm('inputtype1'))
        self.parm_outputtype1 = Outputtype1Menu(parm=self.node.parm('outputtype1'))


        # input vars:
        self.input_src = 'src'


# parm menu classes:
class Inputtype1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_id = ("int", 0)
        self.menu_mono = ("float", 1)
        self.menu_uv = ("vector2", 2)
        self.menu_rgb = ("vector", 3)
        self.menu_rgba = ("vector4", 4)
        self.menu_geometry = ("geo", 5)


class Outputtype1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_id = ("int", 0)
        self.menu_mono = ("float", 1)
        self.menu_uv = ("vector2", 2)
        self.menu_rgb = ("vector", 3)
        self.menu_rgba = ("vector4", 4)
        self.menu_geometry = ("geo", 5)



