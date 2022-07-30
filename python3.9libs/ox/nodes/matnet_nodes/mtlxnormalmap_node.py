from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxnormalmapNode(OXNode):
    node_type = 'mtlxnormalmap'
    parm_lookup_dict = {'inx': 'inx', 'iny': 'iny', 'inz': 'inz', 'space': 'space', 'scale': 'scale', 'normalx': 'normalx', 'normaly': 'normaly', 'normalz': 'normalz', 'tangentx': 'tangentx', 'tangenty': 'tangenty', 'tangentz': 'tangentz'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_inx = Parameter(parm=self.node.parm('inx'))
        self.parm_iny = Parameter(parm=self.node.parm('iny'))
        self.parm_inz = Parameter(parm=self.node.parm('inz'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_normalx = Parameter(parm=self.node.parm('normalx'))
        self.parm_normaly = Parameter(parm=self.node.parm('normaly'))
        self.parm_normalz = Parameter(parm=self.node.parm('normalz'))
        self.parm_tangentx = Parameter(parm=self.node.parm('tangentx'))
        self.parm_tangenty = Parameter(parm=self.node.parm('tangenty'))
        self.parm_tangentz = Parameter(parm=self.node.parm('tangentz'))

        
        # parm menu vars:
        self.parm_space = SpaceMenu(parm=self.node.parm('space'))


        # input vars:
        self.input_input = 'Input'
        self.input_scale = 'Scale'
        self.input_normal = 'Normal'
        self.input_tangent = 'Tangent'


# parm menu classes:
class SpaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_tangent = "tangent"
        self.menu_object = "object"



