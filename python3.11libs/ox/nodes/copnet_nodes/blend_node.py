from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class BlendNode(OXNode):
    node_type = 'blend'
    parm_lookup_dict = {'signature': 'signature', 'mask': 'mask', 'scopergba': 'scopergba', 'mode': 'mode', 'alpha': 'alpha', 'swap': 'swap'}

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
        self.parm_alpha = Parameter(parm=self.node.parm('alpha'))
        self.parm_swap = Parameter(parm=self.node.parm('swap'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))
        self.parm_mode = ModeMenu(parm=self.node.parm('mode'))


        # input vars:
        self.input_bg = 'bg'
        self.input_fg = 'fg'
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


class ModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blend = ("blend", 0)
        self.menu___cop_over_over = ("over", 1)
        self.menu___cop_under_under = ("under", 2)
        self.menu___cop_add_add = ("add", 3)
        self.menu___cop_subtract_subtract = ("subtract", 4)
        self.menu___cop_multiply_multiply = ("multiply", 5)
        self.menu_divide = ("divide", 6)
        self.menu___cop_screen_screen = ("screen", 7)
        self.menu_hypot = ("hypot", 8)
        self.menu___cop_diff_difference = ("diff", 9)
        self.menu_exclusion = ("exclusion", 10)
        self.menu_sharpen = ("sharpen", 11)
        self.menu___cop_max_maximum = ("max", 12)
        self.menu___cop_min_minimum = ("min", 13)
        self.menu_overlay = ("overlay", 14)
        self.menu_softlight = ("softlight", 15)
        self.menu_hardlight = ("hardlight", 16)
        self.menu_dodge = ("dodge", 17)
        self.menu_burn = ("burn", 18)
        self.menu_hue = ("hue", 19)
        self.menu_saturation = ("sat", 20)
        self.menu_luminosity = ("lum", 21)
        self.menu_color = ("color", 22)



