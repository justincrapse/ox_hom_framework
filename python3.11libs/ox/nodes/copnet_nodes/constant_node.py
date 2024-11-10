from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ConstantNode(OXNode):
    node_type = 'constant'
    parm_lookup_dict = {'signature': 'signature', 'mask': 'mask', 'scopergba': 'scopergba', 'f1': 'f1', 'f21': 'f21', 'f22': 'f22', 'f3r': 'f3r', 'f3g': 'f3g', 'f3b': 'f3b', 'f4r': 'f4r', 'f4g': 'f4g', 'f4b': 'f4b', 'f4a': 'f4a'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_mask = Parameter(parm=self.node.parm('mask'))
        self.parm_scopergba = Parameter(parm=self.node.parm('scopergba'))
        self.parm_f1 = Parameter(parm=self.node.parm('f1'))
        self.parm_f21 = Parameter(parm=self.node.parm('f21'))
        self.parm_f22 = Parameter(parm=self.node.parm('f22'))
        self.parm_f3r = Parameter(parm=self.node.parm('f3r'))
        self.parm_f3g = Parameter(parm=self.node.parm('f3g'))
        self.parm_f3b = Parameter(parm=self.node.parm('f3b'))
        self.parm_f4r = Parameter(parm=self.node.parm('f4r'))
        self.parm_f4g = Parameter(parm=self.node.parm('f4g'))
        self.parm_f4b = Parameter(parm=self.node.parm('f4b'))
        self.parm_f4a = Parameter(parm=self.node.parm('f4a'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))


        # input vars:
        self.input_source = 'source'
        self.input_mask = 'mask'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_select_automatically = ("auto", 0)
        self.menu_mono = ("f1", 1)
        self.menu_uv = ("f2", 2)
        self.menu_rgb = ("f3", 3)
        self.menu_rgba = ("f4", 4)



