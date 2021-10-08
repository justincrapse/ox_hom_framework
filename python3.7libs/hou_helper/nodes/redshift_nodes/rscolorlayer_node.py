from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class RscolorlayerNode(HHNode):
    node_type = 'redshift::RSColorLayer'
    parm_lookup_dict = {'advanced_mode': 'advanced_mode', 'base_layer_0': 'Base_Layer_0', 'base_colorr': 'base_colorr', 'base_colorg': 'base_colorg', 'base_colorb': 'base_colorb', 'base_colora': 'base_colora', 'base_color_premult': 'base_color_premult', 'layer_1_1': 'Layer_1_1', 'layer1_enable': 'layer1_enable', 'layer1_colorr': 'layer1_colorr', 'layer1_colorg': 'layer1_colorg', 'layer1_colorb': 'layer1_colorb', 'layer1_colora': 'layer1_colora', 'layer1_mask': 'layer1_mask', 'layer1_blend_mode': 'layer1_blend_mode', 'layer1_overlay_mode': 'layer1_overlay_mode', 'layer1_color_premult': 'layer1_color_premult', 'layer_2_2': 'Layer_2_2', 'layer2_enable': 'layer2_enable', 'layer2_colorr': 'layer2_colorr', 'layer2_colorg': 'layer2_colorg', 'layer2_colorb': 'layer2_colorb', 'layer2_colora': 'layer2_colora', 'layer2_mask': 'layer2_mask', 'layer2_blend_mode': 'layer2_blend_mode', 'layer2_overlay_mode': 'layer2_overlay_mode', 'layer2_color_premult': 'layer2_color_premult', 'layer_3_3': 'Layer_3_3', 'layer3_enable': 'layer3_enable', 'layer3_colorr': 'layer3_colorr', 'layer3_colorg': 'layer3_colorg', 'layer3_colorb': 'layer3_colorb', 'layer3_colora': 'layer3_colora', 'layer3_mask': 'layer3_mask', 'layer3_blend_mode': 'layer3_blend_mode', 'layer3_overlay_mode': 'layer3_overlay_mode', 'layer3_color_premult': 'layer3_color_premult', 'layer_4_4': 'Layer_4_4', 'layer4_enable': 'layer4_enable', 'layer4_colorr': 'layer4_colorr', 'layer4_colorg': 'layer4_colorg', 'layer4_colorb': 'layer4_colorb', 'layer4_colora': 'layer4_colora', 'layer4_mask': 'layer4_mask', 'layer4_blend_mode': 'layer4_blend_mode', 'layer4_overlay_mode': 'layer4_overlay_mode', 'layer4_color_premult': 'layer4_color_premult', 'layer_5_5': 'Layer_5_5', 'layer5_enable': 'layer5_enable', 'layer5_colorr': 'layer5_colorr', 'layer5_colorg': 'layer5_colorg', 'layer5_colorb': 'layer5_colorb', 'layer5_colora': 'layer5_colora', 'layer5_mask': 'layer5_mask', 'layer5_blend_mode': 'layer5_blend_mode', 'layer5_overlay_mode': 'layer5_overlay_mode', 'layer5_color_premult': 'layer5_color_premult', 'layer_6_6': 'Layer_6_6', 'layer6_enable': 'layer6_enable', 'layer6_colorr': 'layer6_colorr', 'layer6_colorg': 'layer6_colorg', 'layer6_colorb': 'layer6_colorb', 'layer6_colora': 'layer6_colora', 'layer6_mask': 'layer6_mask', 'layer6_blend_mode': 'layer6_blend_mode', 'layer6_overlay_mode': 'layer6_overlay_mode', 'layer6_color_premult': 'layer6_color_premult', 'layer_7_7': 'Layer_7_7', 'layer7_enable': 'layer7_enable', 'layer7_colorr': 'layer7_colorr', 'layer7_colorg': 'layer7_colorg', 'layer7_colorb': 'layer7_colorb', 'layer7_colora': 'layer7_colora', 'layer7_mask': 'layer7_mask', 'layer7_blend_mode': 'layer7_blend_mode', 'layer7_overlay_mode': 'layer7_overlay_mode', 'layer7_color_premult': 'layer7_color_premult'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_advanced_mode = Parameter(parm=self.node.parm('advanced_mode'))
        self.parm_base_layer_0 = Parameter(parm=self.node.parm('base_layer_0'))
        self.parm_base_colorr = Parameter(parm=self.node.parm('base_colorr'))
        self.parm_base_colorg = Parameter(parm=self.node.parm('base_colorg'))
        self.parm_base_colorb = Parameter(parm=self.node.parm('base_colorb'))
        self.parm_base_colora = Parameter(parm=self.node.parm('base_colora'))
        self.parm_base_color_premult = Parameter(parm=self.node.parm('base_color_premult'))
        self.parm_layer_1_1 = Parameter(parm=self.node.parm('layer_1_1'))
        self.parm_layer1_enable = Parameter(parm=self.node.parm('layer1_enable'))
        self.parm_layer1_colorr = Parameter(parm=self.node.parm('layer1_colorr'))
        self.parm_layer1_colorg = Parameter(parm=self.node.parm('layer1_colorg'))
        self.parm_layer1_colorb = Parameter(parm=self.node.parm('layer1_colorb'))
        self.parm_layer1_colora = Parameter(parm=self.node.parm('layer1_colora'))
        self.parm_layer1_mask = Parameter(parm=self.node.parm('layer1_mask'))
        self.parm_layer1_color_premult = Parameter(parm=self.node.parm('layer1_color_premult'))
        self.parm_layer_2_2 = Parameter(parm=self.node.parm('layer_2_2'))
        self.parm_layer2_enable = Parameter(parm=self.node.parm('layer2_enable'))
        self.parm_layer2_colorr = Parameter(parm=self.node.parm('layer2_colorr'))
        self.parm_layer2_colorg = Parameter(parm=self.node.parm('layer2_colorg'))
        self.parm_layer2_colorb = Parameter(parm=self.node.parm('layer2_colorb'))
        self.parm_layer2_colora = Parameter(parm=self.node.parm('layer2_colora'))
        self.parm_layer2_mask = Parameter(parm=self.node.parm('layer2_mask'))
        self.parm_layer2_color_premult = Parameter(parm=self.node.parm('layer2_color_premult'))
        self.parm_layer_3_3 = Parameter(parm=self.node.parm('layer_3_3'))
        self.parm_layer3_enable = Parameter(parm=self.node.parm('layer3_enable'))
        self.parm_layer3_colorr = Parameter(parm=self.node.parm('layer3_colorr'))
        self.parm_layer3_colorg = Parameter(parm=self.node.parm('layer3_colorg'))
        self.parm_layer3_colorb = Parameter(parm=self.node.parm('layer3_colorb'))
        self.parm_layer3_colora = Parameter(parm=self.node.parm('layer3_colora'))
        self.parm_layer3_mask = Parameter(parm=self.node.parm('layer3_mask'))
        self.parm_layer3_color_premult = Parameter(parm=self.node.parm('layer3_color_premult'))
        self.parm_layer_4_4 = Parameter(parm=self.node.parm('layer_4_4'))
        self.parm_layer4_enable = Parameter(parm=self.node.parm('layer4_enable'))
        self.parm_layer4_colorr = Parameter(parm=self.node.parm('layer4_colorr'))
        self.parm_layer4_colorg = Parameter(parm=self.node.parm('layer4_colorg'))
        self.parm_layer4_colorb = Parameter(parm=self.node.parm('layer4_colorb'))
        self.parm_layer4_colora = Parameter(parm=self.node.parm('layer4_colora'))
        self.parm_layer4_mask = Parameter(parm=self.node.parm('layer4_mask'))
        self.parm_layer4_color_premult = Parameter(parm=self.node.parm('layer4_color_premult'))
        self.parm_layer_5_5 = Parameter(parm=self.node.parm('layer_5_5'))
        self.parm_layer5_enable = Parameter(parm=self.node.parm('layer5_enable'))
        self.parm_layer5_colorr = Parameter(parm=self.node.parm('layer5_colorr'))
        self.parm_layer5_colorg = Parameter(parm=self.node.parm('layer5_colorg'))
        self.parm_layer5_colorb = Parameter(parm=self.node.parm('layer5_colorb'))
        self.parm_layer5_colora = Parameter(parm=self.node.parm('layer5_colora'))
        self.parm_layer5_mask = Parameter(parm=self.node.parm('layer5_mask'))
        self.parm_layer5_color_premult = Parameter(parm=self.node.parm('layer5_color_premult'))
        self.parm_layer_6_6 = Parameter(parm=self.node.parm('layer_6_6'))
        self.parm_layer6_enable = Parameter(parm=self.node.parm('layer6_enable'))
        self.parm_layer6_colorr = Parameter(parm=self.node.parm('layer6_colorr'))
        self.parm_layer6_colorg = Parameter(parm=self.node.parm('layer6_colorg'))
        self.parm_layer6_colorb = Parameter(parm=self.node.parm('layer6_colorb'))
        self.parm_layer6_colora = Parameter(parm=self.node.parm('layer6_colora'))
        self.parm_layer6_mask = Parameter(parm=self.node.parm('layer6_mask'))
        self.parm_layer6_color_premult = Parameter(parm=self.node.parm('layer6_color_premult'))
        self.parm_layer_7_7 = Parameter(parm=self.node.parm('layer_7_7'))
        self.parm_layer7_enable = Parameter(parm=self.node.parm('layer7_enable'))
        self.parm_layer7_colorr = Parameter(parm=self.node.parm('layer7_colorr'))
        self.parm_layer7_colorg = Parameter(parm=self.node.parm('layer7_colorg'))
        self.parm_layer7_colorb = Parameter(parm=self.node.parm('layer7_colorb'))
        self.parm_layer7_colora = Parameter(parm=self.node.parm('layer7_colora'))
        self.parm_layer7_mask = Parameter(parm=self.node.parm('layer7_mask'))
        self.parm_layer7_color_premult = Parameter(parm=self.node.parm('layer7_color_premult'))

        
        # parm menu vars:
        self.parm_layer1_blend_mode_menu = Layer1BlendModeMenu(parm=self.node.parm('layer1_blend_mode'))
        self.parm_layer1_overlay_mode_menu = Layer1OverlayModeMenu(parm=self.node.parm('layer1_overlay_mode'))
        self.parm_layer2_blend_mode_menu = Layer2BlendModeMenu(parm=self.node.parm('layer2_blend_mode'))
        self.parm_layer2_overlay_mode_menu = Layer2OverlayModeMenu(parm=self.node.parm('layer2_overlay_mode'))
        self.parm_layer3_blend_mode_menu = Layer3BlendModeMenu(parm=self.node.parm('layer3_blend_mode'))
        self.parm_layer3_overlay_mode_menu = Layer3OverlayModeMenu(parm=self.node.parm('layer3_overlay_mode'))
        self.parm_layer4_blend_mode_menu = Layer4BlendModeMenu(parm=self.node.parm('layer4_blend_mode'))
        self.parm_layer4_overlay_mode_menu = Layer4OverlayModeMenu(parm=self.node.parm('layer4_overlay_mode'))
        self.parm_layer5_blend_mode_menu = Layer5BlendModeMenu(parm=self.node.parm('layer5_blend_mode'))
        self.parm_layer5_overlay_mode_menu = Layer5OverlayModeMenu(parm=self.node.parm('layer5_overlay_mode'))
        self.parm_layer6_blend_mode_menu = Layer6BlendModeMenu(parm=self.node.parm('layer6_blend_mode'))
        self.parm_layer6_overlay_mode_menu = Layer6OverlayModeMenu(parm=self.node.parm('layer6_overlay_mode'))
        self.parm_layer7_blend_mode_menu = Layer7BlendModeMenu(parm=self.node.parm('layer7_blend_mode'))
        self.parm_layer7_overlay_mode_menu = Layer7OverlayModeMenu(parm=self.node.parm('layer7_overlay_mode'))


        # input vars:
        self.input_base_color = 0
        self.input_layer1_color = 1
        self.input_layer1_mask = 2
        self.input_layer2_color = 3
        self.input_layer2_mask = 4
        self.input_layer3_color = 5
        self.input_layer3_mask = 6
        self.input_layer4_color = 7
        self.input_layer4_mask = 8
        self.input_layer5_color = 9
        self.input_layer5_mask = 10
        self.input_layer6_color = 11
        self.input_layer6_mask = 12
        self.input_layer7_color = 13
        self.input_layer7_mask = 14


# parm menu classes:
class Layer1BlendModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.normal = 0
        self.average = 1
        self.add = 2
        self.subtract = 3
        self.multiply = 4
        self.difference = 5
        self.lighten = 6
        self.darken = 7
        self.screen = 8
        self.hardlight = 9
        self.softlight = 10
        self.burn = 11
        self.dodge = 12
        self.overlay = 13
        self.exclusion = 14
        self.divide = 15


class Layer1OverlayModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.src = 0
        self.atop = 1
        self.over = 2
        self.inside = 3
        self.out = 4
        self.dest = 5
        self.destatop = 6
        self.destover = 7
        self.destin = 8
        self.destout = 9
        self.clear = 10
        self.xor = 11


class Layer2BlendModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.normal = 0
        self.average = 1
        self.add = 2
        self.subtract = 3
        self.multiply = 4
        self.difference = 5
        self.lighten = 6
        self.darken = 7
        self.screen = 8
        self.hardlight = 9
        self.softlight = 10
        self.burn = 11
        self.dodge = 12
        self.overlay = 13
        self.exclusion = 14
        self.divide = 15


class Layer2OverlayModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.src = 0
        self.atop = 1
        self.over = 2
        self.inside = 3
        self.out = 4
        self.dest = 5
        self.destatop = 6
        self.destover = 7
        self.destin = 8
        self.destout = 9
        self.clear = 10
        self.xor = 11


class Layer3BlendModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.normal = 0
        self.average = 1
        self.add = 2
        self.subtract = 3
        self.multiply = 4
        self.difference = 5
        self.lighten = 6
        self.darken = 7
        self.screen = 8
        self.hardlight = 9
        self.softlight = 10
        self.burn = 11
        self.dodge = 12
        self.overlay = 13
        self.exclusion = 14
        self.divide = 15


class Layer3OverlayModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.src = 0
        self.atop = 1
        self.over = 2
        self.inside = 3
        self.out = 4
        self.dest = 5
        self.destatop = 6
        self.destover = 7
        self.destin = 8
        self.destout = 9
        self.clear = 10
        self.xor = 11


class Layer4BlendModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.normal = 0
        self.average = 1
        self.add = 2
        self.subtract = 3
        self.multiply = 4
        self.difference = 5
        self.lighten = 6
        self.darken = 7
        self.screen = 8
        self.hardlight = 9
        self.softlight = 10
        self.burn = 11
        self.dodge = 12
        self.overlay = 13
        self.exclusion = 14
        self.divide = 15


class Layer4OverlayModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.src = 0
        self.atop = 1
        self.over = 2
        self.inside = 3
        self.out = 4
        self.dest = 5
        self.destatop = 6
        self.destover = 7
        self.destin = 8
        self.destout = 9
        self.clear = 10
        self.xor = 11


class Layer5BlendModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.normal = 0
        self.average = 1
        self.add = 2
        self.subtract = 3
        self.multiply = 4
        self.difference = 5
        self.lighten = 6
        self.darken = 7
        self.screen = 8
        self.hardlight = 9
        self.softlight = 10
        self.burn = 11
        self.dodge = 12
        self.overlay = 13
        self.exclusion = 14
        self.divide = 15


class Layer5OverlayModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.src = 0
        self.atop = 1
        self.over = 2
        self.inside = 3
        self.out = 4
        self.dest = 5
        self.destatop = 6
        self.destover = 7
        self.destin = 8
        self.destout = 9
        self.clear = 10
        self.xor = 11


class Layer6BlendModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.normal = 0
        self.average = 1
        self.add = 2
        self.subtract = 3
        self.multiply = 4
        self.difference = 5
        self.lighten = 6
        self.darken = 7
        self.screen = 8
        self.hardlight = 9
        self.softlight = 10
        self.burn = 11
        self.dodge = 12
        self.overlay = 13
        self.exclusion = 14
        self.divide = 15


class Layer6OverlayModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.src = 0
        self.atop = 1
        self.over = 2
        self.inside = 3
        self.out = 4
        self.dest = 5
        self.destatop = 6
        self.destover = 7
        self.destin = 8
        self.destout = 9
        self.clear = 10
        self.xor = 11


class Layer7BlendModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.normal = 0
        self.average = 1
        self.add = 2
        self.subtract = 3
        self.multiply = 4
        self.difference = 5
        self.lighten = 6
        self.darken = 7
        self.screen = 8
        self.hardlight = 9
        self.softlight = 10
        self.burn = 11
        self.dodge = 12
        self.overlay = 13
        self.exclusion = 14
        self.divide = 15


class Layer7OverlayModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.src = 0
        self.atop = 1
        self.over = 2
        self.inside = 3
        self.out = 4
        self.dest = 5
        self.destatop = 6
        self.destover = 7
        self.destin = 8
        self.destout = 9
        self.clear = 10
        self.xor = 11



