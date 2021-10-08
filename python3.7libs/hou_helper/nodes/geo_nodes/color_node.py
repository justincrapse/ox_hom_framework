from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu


class ColorNode(HHNode):
    node_type = 'color'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'deleteallcolorattribs': 'deleteallcolorattribs', 'class_alt': 'class', 'colortype': 'colortype', 'colorr': 'colorr', 'colorg': 'colorg', 'colorb': 'colorb', 'seed': 'seed', 'rampattribute': 'rampattribute', 'ramprange1': 'ramprange1', 'ramprange2': 'ramprange2', 'ramp': 'ramp', 'ramp1pos': 'ramp1pos', 'ramp1cr': 'ramp1cr', 'ramp1cg': 'ramp1cg', 'ramp1cb': 'ramp1cb', 'ramp1interp': 'ramp1interp', 'ramp2pos': 'ramp2pos', 'ramp2cr': 'ramp2cr', 'ramp2cg': 'ramp2cg', 'ramp2cb': 'ramp2cb', 'ramp2interp': 'ramp2interp'}

    def __init__(self, node=None, hh_parent_node=None, node_name=None):
        self.hh_parent_node = hh_parent_node
        if node:
            self.node = node
        else:
            self.node = self.hh_parent_node.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_deleteallcolorattribs = Parameter(parm=self.node.parm('deleteallcolorattribs'))
        self.parm_colorr = Parameter(parm=self.node.parm('colorr'))
        self.parm_colorg = Parameter(parm=self.node.parm('colorg'))
        self.parm_colorb = Parameter(parm=self.node.parm('colorb'))
        self.parm_seed = Parameter(parm=self.node.parm('seed'))
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
        self.parm_group_menu = GroupMenu(parm=self.node.parm('group'))
        self.parm_grouptype_menu = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_class_alt_menu = ClassAltMenu(parm=self.node.parm('class'))
        self.parm_colortype_menu = ColortypeMenu(parm=self.node.parm('colortype'))
        self.parm_rampattribute_menu = RampattributeMenu(parm=self.node.parm('rampattribute'))
        self.parm_ramp1interp_menu = Ramp1InterpMenu(parm=self.node.parm('ramp1interp'))
        self.parm_ramp2interp_menu = Ramp2InterpMenu(parm=self.node.parm('ramp2interp'))


        # input vars:
        self.input_geometry_to_color = 0


# parm menu classes:
class GroupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.__9857_var3_lod0 = 0


class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.guess_from_group = 0
        self.vertices = 1
        self.edges = 2
        self.points = 3
        self.primitives = 4


class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.detail = 0
        self.primitive = 1
        self.point = 2
        self.vertex = 3


class ColortypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.constant = 0
        self.bounding_box = 1
        self.random = 2
        self.ramp_from_attribute = 3
        self.random_from_attribute = 4


class RampattributeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.position____p_ = 0


class Ramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.constant = 0
        self.linear = 1
        self.catmull_rom = 2
        self.monotone_cubic = 3
        self.bezier = 4
        self.b_spline = 5
        self.hermite = 6


class Ramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.constant = 0
        self.linear = 1
        self.catmull_rom = 2
        self.monotone_cubic = 3
        self.bezier = 4
        self.b_spline = 5
        self.hermite = 6



