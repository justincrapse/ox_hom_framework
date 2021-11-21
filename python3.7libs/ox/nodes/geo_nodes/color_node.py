from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ColorNode(OXNode):
    node_type = 'color'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'deleteallcolorattribs': 'deleteallcolorattribs', 'class_alt': 'class', 'colortype': 'colortype', 'colorr': 'colorr', 'colorg': 'colorg', 'colorb': 'colorb', 'seed': 'seed', 'rampattribute': 'rampattribute', 'ramprange1': 'ramprange1', 'ramprange2': 'ramprange2', 'ramp': 'ramp', 'ramp1pos': 'ramp1pos', 'ramp1cr': 'ramp1cr', 'ramp1cg': 'ramp1cg', 'ramp1cb': 'ramp1cb', 'ramp1interp': 'ramp1interp', 'ramp2pos': 'ramp2pos', 'ramp2cr': 'ramp2cr', 'ramp2cg': 'ramp2cg', 'ramp2cb': 'ramp2cb', 'ramp2interp': 'ramp2interp'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_deleteallcolorattribs = Parameter(parm=self.node.parm('deleteallcolorattribs'))
        self.parm_colorr = Parameter(parm=self.node.parm('colorr'))
        self.parm_colorg = Parameter(parm=self.node.parm('colorg'))
        self.parm_colorb = Parameter(parm=self.node.parm('colorb'))
        self.parm_seed = Parameter(parm=self.node.parm('seed'))
        self.parm_rampattribute = Parameter(parm=self.node.parm('rampattribute'))
        self.parm_ramprange1 = Parameter(parm=self.node.parm('ramprange1'))
        self.parm_ramprange2 = Parameter(parm=self.node.parm('ramprange2'))
        self.parm_ramp = Parameter(parm=self.node.parm('ramp'))
        self.parm_ramp1pos = Parameter(parm=self.node.parm('ramp1pos'))
        self.parm_ramp1cr = Parameter(parm=self.node.parm('ramp1cr'))
        self.parm_ramp1cg = Parameter(parm=self.node.parm('ramp1cg'))
        self.parm_ramp1cb = Parameter(parm=self.node.parm('ramp1cb'))
        self.parm_ramp2pos = Parameter(parm=self.node.parm('ramp2pos'))
        self.parm_ramp2cr = Parameter(parm=self.node.parm('ramp2cr'))
        self.parm_ramp2cg = Parameter(parm=self.node.parm('ramp2cg'))
        self.parm_ramp2cb = Parameter(parm=self.node.parm('ramp2cb'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_class_alt = ClassAltMenu(parm=self.node.parm('class'))
        self.parm_colortype = ColortypeMenu(parm=self.node.parm('colortype'))
        self.parm_ramp1interp = Ramp1InterpMenu(parm=self.node.parm('ramp1interp'))
        self.parm_ramp2interp = Ramp2InterpMenu(parm=self.node.parm('ramp2interp'))


        # input vars:
        self.input_geometry_to_color = 'Geometry to Color'


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = 0
        self.menu_vertices = 1
        self.menu_edges = 2
        self.menu_points = 3
        self.menu_primitives = 4


class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_detail = 0
        self.menu_primitive = 1
        self.menu_point = 2
        self.menu_vertex = 3


class ColortypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = 0
        self.menu_bounding_box = 1
        self.menu_random = 2
        self.menu_ramp_from_attribute = 3
        self.menu_random_from_attribute = 4


class Ramp1InterpMenu(Menu):
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


class Ramp2InterpMenu(Menu):
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



