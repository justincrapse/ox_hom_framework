from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldVisualizeNode(OXNode):
    node_type = 'heightfield_visualize'
    parm_lookup_dict = {'folder0': 'folder0', 'updatetinting': 'updatetinting', 'heightvolume': 'heightvolume', 'cdvolume': 'cdvolume', 'computerange': 'computerange', 'cdrangeoverride': 'cdrangeoverride', 'cdrange1': 'cdrange1', 'cdrange2': 'cdrange2', 'cdrampmode': 'cdrampmode', 'cdpreset': 'cdpreset', 'cdramp': 'cdramp', 'folder1': 'folder1', 'updatematerial': 'updatematerial', 'vis_projection': 'vis_projection', 'computerange2': 'computerange2', 'vis_minelevation': 'vis_minelevation', 'vis_maxelevation': 'vis_maxelevation', 'vis_heightramp': 'vis_heightramp', 'vis_layer9': 'vis_layer9', 'vis_color9r': 'vis_color9r', 'vis_color9g': 'vis_color9g', 'vis_color9b': 'vis_color9b', 'vis_color9a': 'vis_color9a', 'vis_layer8': 'vis_layer8', 'vis_color8r': 'vis_color8r', 'vis_color8g': 'vis_color8g', 'vis_color8b': 'vis_color8b', 'vis_color8a': 'vis_color8a', 'vis_layer7': 'vis_layer7', 'vis_color7r': 'vis_color7r', 'vis_color7g': 'vis_color7g', 'vis_color7b': 'vis_color7b', 'vis_color7a': 'vis_color7a', 'vis_layer6': 'vis_layer6', 'vis_color6r': 'vis_color6r', 'vis_color6g': 'vis_color6g', 'vis_color6b': 'vis_color6b', 'vis_color6a': 'vis_color6a', 'vis_layer5': 'vis_layer5', 'vis_color5r': 'vis_color5r', 'vis_color5g': 'vis_color5g', 'vis_color5b': 'vis_color5b', 'vis_color5a': 'vis_color5a', 'vis_layer4': 'vis_layer4', 'vis_color4r': 'vis_color4r', 'vis_color4g': 'vis_color4g', 'vis_color4b': 'vis_color4b', 'vis_color4a': 'vis_color4a', 'vis_layer3': 'vis_layer3', 'vis_color3r': 'vis_color3r', 'vis_color3g': 'vis_color3g', 'vis_color3b': 'vis_color3b', 'vis_color3a': 'vis_color3a', 'vis_layer2': 'vis_layer2', 'vis_color2r': 'vis_color2r', 'vis_color2g': 'vis_color2g', 'vis_color2b': 'vis_color2b', 'vis_color2a': 'vis_color2a', 'vis_layer1': 'vis_layer1', 'vis_color1r': 'vis_color1r', 'vis_color1g': 'vis_color1g', 'vis_color1b': 'vis_color1b', 'vis_color1a': 'vis_color1a', 'cdramp1pos': 'cdramp1pos', 'cdramp1cr': 'cdramp1cr', 'cdramp1cg': 'cdramp1cg', 'cdramp1cb': 'cdramp1cb', 'cdramp1interp': 'cdramp1interp', 'cdramp2pos': 'cdramp2pos', 'cdramp2cr': 'cdramp2cr', 'cdramp2cg': 'cdramp2cg', 'cdramp2cb': 'cdramp2cb', 'cdramp2interp': 'cdramp2interp', 'vis_heightramp1pos': 'vis_heightramp1pos', 'vis_heightramp1cr': 'vis_heightramp1cr', 'vis_heightramp1cg': 'vis_heightramp1cg', 'vis_heightramp1cb': 'vis_heightramp1cb', 'vis_heightramp1interp': 'vis_heightramp1interp', 'vis_heightramp2pos': 'vis_heightramp2pos', 'vis_heightramp2cr': 'vis_heightramp2cr', 'vis_heightramp2cg': 'vis_heightramp2cg', 'vis_heightramp2cb': 'vis_heightramp2cb', 'vis_heightramp2interp': 'vis_heightramp2interp', 'vis_heightramp3pos': 'vis_heightramp3pos', 'vis_heightramp3cr': 'vis_heightramp3cr', 'vis_heightramp3cg': 'vis_heightramp3cg', 'vis_heightramp3cb': 'vis_heightramp3cb', 'vis_heightramp3interp': 'vis_heightramp3interp', 'vis_heightramp4pos': 'vis_heightramp4pos', 'vis_heightramp4cr': 'vis_heightramp4cr', 'vis_heightramp4cg': 'vis_heightramp4cg', 'vis_heightramp4cb': 'vis_heightramp4cb', 'vis_heightramp4interp': 'vis_heightramp4interp', 'vis_heightramp5pos': 'vis_heightramp5pos', 'vis_heightramp5cr': 'vis_heightramp5cr', 'vis_heightramp5cg': 'vis_heightramp5cg', 'vis_heightramp5cb': 'vis_heightramp5cb', 'vis_heightramp5interp': 'vis_heightramp5interp'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_heightvolume = Parameter(parm=self.node.parm('heightvolume'))
        self.parm_cdvolume = Parameter(parm=self.node.parm('cdvolume'))
        self.parm_computerange = Parameter(parm=self.node.parm('computerange'))
        self.parm_cdrangeoverride = Parameter(parm=self.node.parm('cdrangeoverride'))
        self.parm_cdrange1 = Parameter(parm=self.node.parm('cdrange1'))
        self.parm_cdrange2 = Parameter(parm=self.node.parm('cdrange2'))
        self.parm_cdramp = Parameter(parm=self.node.parm('cdramp'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_computerange2 = Parameter(parm=self.node.parm('computerange2'))
        self.parm_vis_minelevation = Parameter(parm=self.node.parm('vis_minelevation'))
        self.parm_vis_maxelevation = Parameter(parm=self.node.parm('vis_maxelevation'))
        self.parm_vis_heightramp = Parameter(parm=self.node.parm('vis_heightramp'))
        self.parm_vis_layer9 = Parameter(parm=self.node.parm('vis_layer9'))
        self.parm_vis_color9r = Parameter(parm=self.node.parm('vis_color9r'))
        self.parm_vis_color9g = Parameter(parm=self.node.parm('vis_color9g'))
        self.parm_vis_color9b = Parameter(parm=self.node.parm('vis_color9b'))
        self.parm_vis_color9a = Parameter(parm=self.node.parm('vis_color9a'))
        self.parm_vis_layer8 = Parameter(parm=self.node.parm('vis_layer8'))
        self.parm_vis_color8r = Parameter(parm=self.node.parm('vis_color8r'))
        self.parm_vis_color8g = Parameter(parm=self.node.parm('vis_color8g'))
        self.parm_vis_color8b = Parameter(parm=self.node.parm('vis_color8b'))
        self.parm_vis_color8a = Parameter(parm=self.node.parm('vis_color8a'))
        self.parm_vis_layer7 = Parameter(parm=self.node.parm('vis_layer7'))
        self.parm_vis_color7r = Parameter(parm=self.node.parm('vis_color7r'))
        self.parm_vis_color7g = Parameter(parm=self.node.parm('vis_color7g'))
        self.parm_vis_color7b = Parameter(parm=self.node.parm('vis_color7b'))
        self.parm_vis_color7a = Parameter(parm=self.node.parm('vis_color7a'))
        self.parm_vis_layer6 = Parameter(parm=self.node.parm('vis_layer6'))
        self.parm_vis_color6r = Parameter(parm=self.node.parm('vis_color6r'))
        self.parm_vis_color6g = Parameter(parm=self.node.parm('vis_color6g'))
        self.parm_vis_color6b = Parameter(parm=self.node.parm('vis_color6b'))
        self.parm_vis_color6a = Parameter(parm=self.node.parm('vis_color6a'))
        self.parm_vis_layer5 = Parameter(parm=self.node.parm('vis_layer5'))
        self.parm_vis_color5r = Parameter(parm=self.node.parm('vis_color5r'))
        self.parm_vis_color5g = Parameter(parm=self.node.parm('vis_color5g'))
        self.parm_vis_color5b = Parameter(parm=self.node.parm('vis_color5b'))
        self.parm_vis_color5a = Parameter(parm=self.node.parm('vis_color5a'))
        self.parm_vis_layer4 = Parameter(parm=self.node.parm('vis_layer4'))
        self.parm_vis_color4r = Parameter(parm=self.node.parm('vis_color4r'))
        self.parm_vis_color4g = Parameter(parm=self.node.parm('vis_color4g'))
        self.parm_vis_color4b = Parameter(parm=self.node.parm('vis_color4b'))
        self.parm_vis_color4a = Parameter(parm=self.node.parm('vis_color4a'))
        self.parm_vis_layer3 = Parameter(parm=self.node.parm('vis_layer3'))
        self.parm_vis_color3r = Parameter(parm=self.node.parm('vis_color3r'))
        self.parm_vis_color3g = Parameter(parm=self.node.parm('vis_color3g'))
        self.parm_vis_color3b = Parameter(parm=self.node.parm('vis_color3b'))
        self.parm_vis_color3a = Parameter(parm=self.node.parm('vis_color3a'))
        self.parm_vis_layer2 = Parameter(parm=self.node.parm('vis_layer2'))
        self.parm_vis_color2r = Parameter(parm=self.node.parm('vis_color2r'))
        self.parm_vis_color2g = Parameter(parm=self.node.parm('vis_color2g'))
        self.parm_vis_color2b = Parameter(parm=self.node.parm('vis_color2b'))
        self.parm_vis_color2a = Parameter(parm=self.node.parm('vis_color2a'))
        self.parm_vis_layer1 = Parameter(parm=self.node.parm('vis_layer1'))
        self.parm_vis_color1r = Parameter(parm=self.node.parm('vis_color1r'))
        self.parm_vis_color1g = Parameter(parm=self.node.parm('vis_color1g'))
        self.parm_vis_color1b = Parameter(parm=self.node.parm('vis_color1b'))
        self.parm_vis_color1a = Parameter(parm=self.node.parm('vis_color1a'))
        self.parm_cdramp1pos = Parameter(parm=self.node.parm('cdramp1pos'))
        self.parm_cdramp1cr = Parameter(parm=self.node.parm('cdramp1cr'))
        self.parm_cdramp1cg = Parameter(parm=self.node.parm('cdramp1cg'))
        self.parm_cdramp1cb = Parameter(parm=self.node.parm('cdramp1cb'))
        self.parm_cdramp2pos = Parameter(parm=self.node.parm('cdramp2pos'))
        self.parm_cdramp2cr = Parameter(parm=self.node.parm('cdramp2cr'))
        self.parm_cdramp2cg = Parameter(parm=self.node.parm('cdramp2cg'))
        self.parm_cdramp2cb = Parameter(parm=self.node.parm('cdramp2cb'))
        self.parm_vis_heightramp1pos = Parameter(parm=self.node.parm('vis_heightramp1pos'))
        self.parm_vis_heightramp1cr = Parameter(parm=self.node.parm('vis_heightramp1cr'))
        self.parm_vis_heightramp1cg = Parameter(parm=self.node.parm('vis_heightramp1cg'))
        self.parm_vis_heightramp1cb = Parameter(parm=self.node.parm('vis_heightramp1cb'))
        self.parm_vis_heightramp2pos = Parameter(parm=self.node.parm('vis_heightramp2pos'))
        self.parm_vis_heightramp2cr = Parameter(parm=self.node.parm('vis_heightramp2cr'))
        self.parm_vis_heightramp2cg = Parameter(parm=self.node.parm('vis_heightramp2cg'))
        self.parm_vis_heightramp2cb = Parameter(parm=self.node.parm('vis_heightramp2cb'))
        self.parm_vis_heightramp3pos = Parameter(parm=self.node.parm('vis_heightramp3pos'))
        self.parm_vis_heightramp3cr = Parameter(parm=self.node.parm('vis_heightramp3cr'))
        self.parm_vis_heightramp3cg = Parameter(parm=self.node.parm('vis_heightramp3cg'))
        self.parm_vis_heightramp3cb = Parameter(parm=self.node.parm('vis_heightramp3cb'))
        self.parm_vis_heightramp4pos = Parameter(parm=self.node.parm('vis_heightramp4pos'))
        self.parm_vis_heightramp4cr = Parameter(parm=self.node.parm('vis_heightramp4cr'))
        self.parm_vis_heightramp4cg = Parameter(parm=self.node.parm('vis_heightramp4cg'))
        self.parm_vis_heightramp4cb = Parameter(parm=self.node.parm('vis_heightramp4cb'))
        self.parm_vis_heightramp5pos = Parameter(parm=self.node.parm('vis_heightramp5pos'))
        self.parm_vis_heightramp5cr = Parameter(parm=self.node.parm('vis_heightramp5cr'))
        self.parm_vis_heightramp5cg = Parameter(parm=self.node.parm('vis_heightramp5cg'))
        self.parm_vis_heightramp5cb = Parameter(parm=self.node.parm('vis_heightramp5cb'))

        
        # parm menu vars:
        self.parm_updatetinting = UpdatetintingMenu(parm=self.node.parm('updatetinting'))
        self.parm_cdrampmode = CdrampmodeMenu(parm=self.node.parm('cdrampmode'))
        self.parm_cdpreset = CdpresetMenu(parm=self.node.parm('cdpreset'))
        self.parm_updatematerial = UpdatematerialMenu(parm=self.node.parm('updatematerial'))
        self.parm_vis_projection = VisProjectionMenu(parm=self.node.parm('vis_projection'))
        self.parm_cdramp1interp = Cdramp1InterpMenu(parm=self.node.parm('cdramp1interp'))
        self.parm_cdramp2interp = Cdramp2InterpMenu(parm=self.node.parm('cdramp2interp'))
        self.parm_vis_heightramp1interp = VisHeightramp1InterpMenu(parm=self.node.parm('vis_heightramp1interp'))
        self.parm_vis_heightramp2interp = VisHeightramp2InterpMenu(parm=self.node.parm('vis_heightramp2interp'))
        self.parm_vis_heightramp3interp = VisHeightramp3InterpMenu(parm=self.node.parm('vis_heightramp3interp'))
        self.parm_vis_heightramp4interp = VisHeightramp4InterpMenu(parm=self.node.parm('vis_heightramp4interp'))
        self.parm_vis_heightramp5interp = VisHeightramp5InterpMenu(parm=self.node.parm('vis_heightramp5interp'))


        # input vars:
        self.input_terrain = 'Terrain'


# parm menu classes:
class UpdatetintingMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_change = ("unchanged", 0)
        self.menu_default_tinting = ("default", 1)
        self.menu_custom_tinting = ("custom", 2)
        self.menu_remove_tinting = ("none", 3)


class CdrampmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_ramp = ("none", 0)
        self.menu_clamped_ramp = ("clamp", 1)
        self.menu_periodic_ramp = ("periodic", 2)


class CdpresetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_presets = ("none", 0)
        self.menu_infra_red = ("false", 1)
        self.menu_white_to_red = ("pink", 2)
        self.menu_grayscale = ("mono", 3)
        self.menu_blackbody = ("blackbody", 4)
        self.menu_two_tone = ("bipartite", 5)


class UpdatematerialMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_change = ("unchanged", 0)
        self.menu_custom_material = ("custom", 1)
        self.menu_remove_material = ("none", 2)


class VisProjectionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_y_up = ("y", 0)
        self.menu_z_up = ("z", 1)


class Cdramp1InterpMenu(Menu):
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


class Cdramp2InterpMenu(Menu):
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


class VisHeightramp1InterpMenu(Menu):
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


class VisHeightramp2InterpMenu(Menu):
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


class VisHeightramp3InterpMenu(Menu):
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


class VisHeightramp4InterpMenu(Menu):
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


class VisHeightramp5InterpMenu(Menu):
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



