from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldVisualizeNode(OXNode):
    node_type = 'heightfield_visualize'
    parm_lookup_dict = {'folder0': 'folder0', 'updatetinting': 'updatetinting', 'heightvolume': 'heightvolume', 'cdvolume': 'cdvolume', 'computerange': 'computerange', 'cdrangeoverride': 'cdrangeoverride', 'cdrange1': 'cdrange1', 'cdrange2': 'cdrange2', 'cdrampmode': 'cdrampmode', 'cdpreset': 'cdpreset', 'cdramp': 'cdramp', 'folder1': 'folder1', 'updatematerial': 'updatematerial', 'vis_projection': 'vis_projection', 'computerange2': 'computerange2', 'vis_minelevation': 'vis_minelevation', 'vis_maxelevation': 'vis_maxelevation', 'vis_heightramp': 'vis_heightramp', 'vis_layer3': 'vis_layer3', 'vis_color3r': 'vis_color3r', 'vis_color3g': 'vis_color3g', 'vis_color3b': 'vis_color3b', 'vis_color3a': 'vis_color3a', 'vis_layer2': 'vis_layer2', 'vis_color2r': 'vis_color2r', 'vis_color2g': 'vis_color2g', 'vis_color2b': 'vis_color2b', 'vis_color2a': 'vis_color2a', 'vis_layer1': 'vis_layer1', 'vis_color1r': 'vis_color1r', 'vis_color1g': 'vis_color1g', 'vis_color1b': 'vis_color1b', 'vis_color1a': 'vis_color1a', 'cdramp1pos': 'cdramp1pos', 'cdramp1cr': 'cdramp1cr', 'cdramp1cg': 'cdramp1cg', 'cdramp1cb': 'cdramp1cb', 'cdramp1interp': 'cdramp1interp', 'cdramp2pos': 'cdramp2pos', 'cdramp2cr': 'cdramp2cr', 'cdramp2cg': 'cdramp2cg', 'cdramp2cb': 'cdramp2cb', 'cdramp2interp': 'cdramp2interp', 'vis_heightramp1pos': 'vis_heightramp1pos', 'vis_heightramp1cr': 'vis_heightramp1cr', 'vis_heightramp1cg': 'vis_heightramp1cg', 'vis_heightramp1cb': 'vis_heightramp1cb', 'vis_heightramp1interp': 'vis_heightramp1interp', 'vis_heightramp2pos': 'vis_heightramp2pos', 'vis_heightramp2cr': 'vis_heightramp2cr', 'vis_heightramp2cg': 'vis_heightramp2cg', 'vis_heightramp2cb': 'vis_heightramp2cb', 'vis_heightramp2interp': 'vis_heightramp2interp', 'vis_heightramp3pos': 'vis_heightramp3pos', 'vis_heightramp3cr': 'vis_heightramp3cr', 'vis_heightramp3cg': 'vis_heightramp3cg', 'vis_heightramp3cb': 'vis_heightramp3cb', 'vis_heightramp3interp': 'vis_heightramp3interp', 'vis_heightramp4pos': 'vis_heightramp4pos', 'vis_heightramp4cr': 'vis_heightramp4cr', 'vis_heightramp4cg': 'vis_heightramp4cg', 'vis_heightramp4cb': 'vis_heightramp4cb', 'vis_heightramp4interp': 'vis_heightramp4interp', 'vis_heightramp5pos': 'vis_heightramp5pos', 'vis_heightramp5cr': 'vis_heightramp5cr', 'vis_heightramp5cg': 'vis_heightramp5cg', 'vis_heightramp5cb': 'vis_heightramp5cb', 'vis_heightramp5interp': 'vis_heightramp5interp'}

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
        self.menu_no_change = 0
        self.menu_default_tinting = 1
        self.menu_custom_tinting = 2
        self.menu_remove_tinting = 3


class CdrampmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_ramp = 0
        self.menu_clamped_ramp = 1
        self.menu_periodic_ramp = 2


class CdpresetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_presets = 0
        self.menu_infra_red = 1
        self.menu_white_to_red = 2
        self.menu_grayscale = 3
        self.menu_black_body = 4
        self.menu_two_tone = 5


class UpdatematerialMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_change = 0
        self.menu_custom_material = 1
        self.menu_remove_material = 2


class VisProjectionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_y_up = 0
        self.menu_z_up = 1


class Cdramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class Cdramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class VisHeightramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class VisHeightramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class VisHeightramp3InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class VisHeightramp4InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6


class VisHeightramp5InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_linear = 1
        self.menu_catmull_rom = 2
        self.menu_monotone_cubic = 3
        self.menu_bezier = 4
        self.menu_b_spline = 5
        self.menu_hermite = 6



