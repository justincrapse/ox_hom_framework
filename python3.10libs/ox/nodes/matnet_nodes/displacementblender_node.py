from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class DisplacementblenderNode(OXNode):
    node_type = 'redshift::DisplacementBlender'
    parm_lookup_dict = {'additive': 'additive', 'base_0': 'Base_0', 'baseinput1': 'baseInput1', 'baseinput2': 'baseInput2', 'baseinput3': 'baseInput3', 'layer_0_1': 'Layer_0_1', 'displaceinput01': 'displaceInput01', 'displaceinput02': 'displaceInput02', 'displaceinput03': 'displaceInput03', 'displaceweight0': 'displaceWeight0', 'layer_1_2': 'Layer_1_2', 'displaceinput11': 'displaceInput11', 'displaceinput12': 'displaceInput12', 'displaceinput13': 'displaceInput13', 'displaceweight1': 'displaceWeight1', 'layer_2_3': 'Layer_2_3', 'displaceinput21': 'displaceInput21', 'displaceinput22': 'displaceInput22', 'displaceinput23': 'displaceInput23', 'displaceweight2': 'displaceWeight2', 'shader_skipdefvalparms': 'shader_skipdefvalparms'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_additive = Parameter(parm=self.node.parm('additive'))
        self.parm_base_0 = Parameter(parm=self.node.parm('Base_0'))
        self.parm_baseinput1 = Parameter(parm=self.node.parm('baseInput1'))
        self.parm_baseinput2 = Parameter(parm=self.node.parm('baseInput2'))
        self.parm_baseinput3 = Parameter(parm=self.node.parm('baseInput3'))
        self.parm_layer_0_1 = Parameter(parm=self.node.parm('Layer_0_1'))
        self.parm_displaceinput01 = Parameter(parm=self.node.parm('displaceInput01'))
        self.parm_displaceinput02 = Parameter(parm=self.node.parm('displaceInput02'))
        self.parm_displaceinput03 = Parameter(parm=self.node.parm('displaceInput03'))
        self.parm_displaceweight0 = Parameter(parm=self.node.parm('displaceWeight0'))
        self.parm_layer_1_2 = Parameter(parm=self.node.parm('Layer_1_2'))
        self.parm_displaceinput11 = Parameter(parm=self.node.parm('displaceInput11'))
        self.parm_displaceinput12 = Parameter(parm=self.node.parm('displaceInput12'))
        self.parm_displaceinput13 = Parameter(parm=self.node.parm('displaceInput13'))
        self.parm_displaceweight1 = Parameter(parm=self.node.parm('displaceWeight1'))
        self.parm_layer_2_3 = Parameter(parm=self.node.parm('Layer_2_3'))
        self.parm_displaceinput21 = Parameter(parm=self.node.parm('displaceInput21'))
        self.parm_displaceinput22 = Parameter(parm=self.node.parm('displaceInput22'))
        self.parm_displaceinput23 = Parameter(parm=self.node.parm('displaceInput23'))
        self.parm_displaceweight2 = Parameter(parm=self.node.parm('displaceWeight2'))
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))

        
        # parm menu vars:


        # input vars:
        self.input_baseinput = 'baseInput'
        self.input_displaceinput0 = 'displaceInput0'
        self.input_displaceweight0 = 'displaceWeight0'
        self.input_displaceinput1 = 'displaceInput1'
        self.input_displaceweight1 = 'displaceWeight1'
        self.input_displaceinput2 = 'displaceInput2'
        self.input_displaceweight2 = 'displaceWeight2'


# parm menu classes:

