from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class HfCombineMasksNode(OXNode):
    node_type = "labs::hf_combine_masks"
    parm_lookup_dict = {
        "bflood": "bFlood",
        "srcname1": "srcname1",
        "folder0": "folder0",
        "folder1": "folder1",
        "clampmin": "clampmin",
        "clampmax": "clampmax",
        "remap": "remap",
        "remap1pos": "remap1pos",
        "remap1value": "remap1value",
        "remap1interp": "remap1interp",
        "remap2pos": "remap2pos",
        "remap2value": "remap2value",
        "remap2interp": "remap2interp",
        "layername_1": "layername_1",
        "clamp_1": "clamp_1",
        "blend_1": "blend_1",
        "method_1": "method_1",
        "radius_1": "radius_1",
        "mode_1": "mode_1",
        "layername_2": "layername_2",
        "clamp_2": "clamp_2",
        "blend_2": "blend_2",
        "method_2": "method_2",
        "radius_2": "radius_2",
        "mode_2": "mode_2",
        "layername_3": "layername_3",
        "clamp_3": "clamp_3",
        "blend_3": "blend_3",
        "method_3": "method_3",
        "radius_3": "radius_3",
        "mode_3": "mode_3",
        "layername_4": "layername_4",
        "clamp_4": "clamp_4",
        "blend_4": "blend_4",
        "method_4": "method_4",
        "radius_4": "radius_4",
        "mode_4": "mode_4",
        "layername_5": "layername_5",
        "clamp_5": "clamp_5",
        "blend_5": "blend_5",
        "method_5": "method_5",
        "radius_5": "radius_5",
        "mode_5": "mode_5",
        "layername_6": "layername_6",
        "clamp_6": "clamp_6",
        "blend_6": "blend_6",
        "method_6": "method_6",
        "radius_6": "radius_6",
        "mode_6": "mode_6",
        "layername_7": "layername_7",
        "clamp_7": "clamp_7",
        "blend_7": "blend_7",
        "method_7": "method_7",
        "radius_7": "radius_7",
        "mode_7": "mode_7",
        "layername_8": "layername_8",
        "clamp_8": "clamp_8",
        "blend_8": "blend_8",
        "method_8": "method_8",
        "radius_8": "radius_8",
        "mode_8": "mode_8",
        "layername_9": "layername_9",
        "clamp_9": "clamp_9",
        "blend_9": "blend_9",
        "method_9": "method_9",
        "radius_9": "radius_9",
        "mode_9": "mode_9",
        "layername_10": "layername_10",
        "clamp_10": "clamp_10",
        "blend_10": "blend_10",
        "method_10": "method_10",
        "radius_10": "radius_10",
        "mode_10": "mode_10",
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
        self.parm_bflood = Parameter(parm=self.node.parm("bFlood"))
        self.parm_srcname1 = Parameter(parm=self.node.parm("srcname1"))
        self.parm_folder0 = Parameter(parm=self.node.parm("folder0"))
        self.parm_folder1 = Parameter(parm=self.node.parm("folder1"))
        self.parm_clampmin = Parameter(parm=self.node.parm("clampmin"))
        self.parm_clampmax = Parameter(parm=self.node.parm("clampmax"))
        self.parm_remap = Parameter(parm=self.node.parm("remap"))
        self.parm_remap1pos = Parameter(parm=self.node.parm("remap1pos"))
        self.parm_remap1value = Parameter(parm=self.node.parm("remap1value"))
        self.parm_remap2pos = Parameter(parm=self.node.parm("remap2pos"))
        self.parm_remap2value = Parameter(parm=self.node.parm("remap2value"))
        self.parm_layername_1 = Parameter(parm=self.node.parm("layername_1"))
        self.parm_clamp_1 = Parameter(parm=self.node.parm("clamp_1"))
        self.parm_blend_1 = Parameter(parm=self.node.parm("blend_1"))
        self.parm_radius_1 = Parameter(parm=self.node.parm("radius_1"))
        self.parm_layername_2 = Parameter(parm=self.node.parm("layername_2"))
        self.parm_clamp_2 = Parameter(parm=self.node.parm("clamp_2"))
        self.parm_blend_2 = Parameter(parm=self.node.parm("blend_2"))
        self.parm_radius_2 = Parameter(parm=self.node.parm("radius_2"))
        self.parm_layername_3 = Parameter(parm=self.node.parm("layername_3"))
        self.parm_clamp_3 = Parameter(parm=self.node.parm("clamp_3"))
        self.parm_blend_3 = Parameter(parm=self.node.parm("blend_3"))
        self.parm_radius_3 = Parameter(parm=self.node.parm("radius_3"))
        self.parm_layername_4 = Parameter(parm=self.node.parm("layername_4"))
        self.parm_clamp_4 = Parameter(parm=self.node.parm("clamp_4"))
        self.parm_blend_4 = Parameter(parm=self.node.parm("blend_4"))
        self.parm_radius_4 = Parameter(parm=self.node.parm("radius_4"))
        self.parm_layername_5 = Parameter(parm=self.node.parm("layername_5"))
        self.parm_clamp_5 = Parameter(parm=self.node.parm("clamp_5"))
        self.parm_blend_5 = Parameter(parm=self.node.parm("blend_5"))
        self.parm_radius_5 = Parameter(parm=self.node.parm("radius_5"))
        self.parm_layername_6 = Parameter(parm=self.node.parm("layername_6"))
        self.parm_clamp_6 = Parameter(parm=self.node.parm("clamp_6"))
        self.parm_blend_6 = Parameter(parm=self.node.parm("blend_6"))
        self.parm_radius_6 = Parameter(parm=self.node.parm("radius_6"))
        self.parm_layername_7 = Parameter(parm=self.node.parm("layername_7"))
        self.parm_clamp_7 = Parameter(parm=self.node.parm("clamp_7"))
        self.parm_blend_7 = Parameter(parm=self.node.parm("blend_7"))
        self.parm_radius_7 = Parameter(parm=self.node.parm("radius_7"))
        self.parm_layername_8 = Parameter(parm=self.node.parm("layername_8"))
        self.parm_clamp_8 = Parameter(parm=self.node.parm("clamp_8"))
        self.parm_blend_8 = Parameter(parm=self.node.parm("blend_8"))
        self.parm_radius_8 = Parameter(parm=self.node.parm("radius_8"))
        self.parm_layername_9 = Parameter(parm=self.node.parm("layername_9"))
        self.parm_clamp_9 = Parameter(parm=self.node.parm("clamp_9"))
        self.parm_blend_9 = Parameter(parm=self.node.parm("blend_9"))
        self.parm_radius_9 = Parameter(parm=self.node.parm("radius_9"))
        self.parm_layername_10 = Parameter(parm=self.node.parm("layername_10"))
        self.parm_clamp_10 = Parameter(parm=self.node.parm("clamp_10"))
        self.parm_blend_10 = Parameter(parm=self.node.parm("blend_10"))
        self.parm_radius_10 = Parameter(parm=self.node.parm("radius_10"))

        # parm menu vars:
        self.parm_remap1interp = Remap1InterpMenu(parm=self.node.parm("remap1interp"))
        self.parm_remap2interp = Remap2InterpMenu(parm=self.node.parm("remap2interp"))
        self.parm_method_1 = Method1Menu(parm=self.node.parm("method_1"))
        self.parm_mode_1 = Mode1Menu(parm=self.node.parm("mode_1"))
        self.parm_method_2 = Method2Menu(parm=self.node.parm("method_2"))
        self.parm_mode_2 = Mode2Menu(parm=self.node.parm("mode_2"))
        self.parm_method_3 = Method3Menu(parm=self.node.parm("method_3"))
        self.parm_mode_3 = Mode3Menu(parm=self.node.parm("mode_3"))
        self.parm_method_4 = Method4Menu(parm=self.node.parm("method_4"))
        self.parm_mode_4 = Mode4Menu(parm=self.node.parm("mode_4"))
        self.parm_method_5 = Method5Menu(parm=self.node.parm("method_5"))
        self.parm_mode_5 = Mode5Menu(parm=self.node.parm("mode_5"))
        self.parm_method_6 = Method6Menu(parm=self.node.parm("method_6"))
        self.parm_mode_6 = Mode6Menu(parm=self.node.parm("mode_6"))
        self.parm_method_7 = Method7Menu(parm=self.node.parm("method_7"))
        self.parm_mode_7 = Mode7Menu(parm=self.node.parm("mode_7"))
        self.parm_method_8 = Method8Menu(parm=self.node.parm("method_8"))
        self.parm_mode_8 = Mode8Menu(parm=self.node.parm("mode_8"))
        self.parm_method_9 = Method9Menu(parm=self.node.parm("method_9"))
        self.parm_mode_9 = Mode9Menu(parm=self.node.parm("mode_9"))
        self.parm_method_10 = Method10Menu(parm=self.node.parm("method_10"))
        self.parm_mode_10 = Mode10Menu(parm=self.node.parm("mode_10"))

        # input vars:
        self.input_heightfield = "Heightfield"


# parm menu classes:
class Remap1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_linear = ("linear", 1)
        self.menu_catmull_rom = ("catmull-rom", 2)
        self.menu_monotone_cubic = ("monotonecubic", 3)
        self.menu_bezier = ("bezier", 4)
        self.menu_b_spline = ("bspline", 5)
        self.menu_hermite = ("hermite", 6)


class Remap2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_linear = ("linear", 1)
        self.menu_catmull_rom = ("catmull-rom", 2)
        self.menu_monotone_cubic = ("monotonecubic", 3)
        self.menu_bezier = ("bezier", 4)
        self.menu_b_spline = ("bspline", 5)
        self.menu_hermite = ("hermite", 6)


class Method1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method6Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode6Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method7Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode7Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method8Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode8Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method9Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode9Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)


class Method10Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blur = ("blur", 0)
        self.menu_box_blur = ("boxblur", 1)
        self.menu_expand = ("expand", 2)
        self.menu_shrink = ("shrink", 3)


class Mode10Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = ("replace", 0)
        self.menu_add = ("add", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_difference = ("diff", 3)
        self.menu_multiply = ("multiply", 4)
        self.menu_maximum = ("max", 5)
        self.menu_minimum = ("min", 6)
        self.menu_blend = ("blend", 7)
