from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxcolorcorrectNode(OXNode):
    node_type = 'mtlxcolorcorrect'
    parm_lookup_dict = {'signature': 'signature', 'inr': 'inr', 'ing': 'ing', 'inb': 'inb', 'in_color4r': 'in_color4r', 'in_color4g': 'in_color4g', 'in_color4b': 'in_color4b', 'in_color4a': 'in_color4a', 'hue': 'hue', 'saturation': 'saturation', 'gamma': 'gamma', 'lift': 'lift', 'gain': 'gain', 'contrast': 'contrast', 'contrastpivot': 'contrastpivot', 'exposure': 'exposure'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_inr = Parameter(parm=self.node.parm('inr'))
        self.parm_ing = Parameter(parm=self.node.parm('ing'))
        self.parm_inb = Parameter(parm=self.node.parm('inb'))
        self.parm_in_color4r = Parameter(parm=self.node.parm('in_color4r'))
        self.parm_in_color4g = Parameter(parm=self.node.parm('in_color4g'))
        self.parm_in_color4b = Parameter(parm=self.node.parm('in_color4b'))
        self.parm_in_color4a = Parameter(parm=self.node.parm('in_color4a'))
        self.parm_hue = Parameter(parm=self.node.parm('hue'))
        self.parm_saturation = Parameter(parm=self.node.parm('saturation'))
        self.parm_gamma = Parameter(parm=self.node.parm('gamma'))
        self.parm_lift = Parameter(parm=self.node.parm('lift'))
        self.parm_gain = Parameter(parm=self.node.parm('gain'))
        self.parm_contrast = Parameter(parm=self.node.parm('contrast'))
        self.parm_contrastpivot = Parameter(parm=self.node.parm('contrastpivot'))
        self.parm_exposure = Parameter(parm=self.node.parm('exposure'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))


        # input vars:
        self.input_input_color = 'Input Color'
        self.input_hue = 'Hue'
        self.input_saturation = 'Saturation'
        self.input_gamma = 'Gamma'
        self.input_lift = 'Lift'
        self.input_gain = 'Gain'
        self.input_contrast = 'Contrast'
        self.input_contrast_pivot = 'Contrast Pivot'
        self.input_exposure = 'Exposure'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_color = ("default", 0)
        self.menu_color_4 = ("color4", 1)



