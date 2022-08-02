from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MatchsizeNode(OXNode):
    node_type = 'matchsize'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'justifytarget': 'justifytarget', 'doboundgroup': 'doboundgroup', 'folder2': 'folder2', 'sourcegroup': 'sourcegroup', 'sourcegrouptype': 'sourcegrouptype', 'refgroup': 'refgroup', 'refgrouptype': 'refgrouptype', 'folder1': 'folder1', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'sizex': 'sizex', 'sizey': 'sizey', 'sizez': 'sizez', 'folder0': 'folder0', 'dotranslate': 'dotranslate', 'justify_x': 'justify_x', 'goal_x': 'goal_x', 'offset_x': 'offset_x', 'justify_y': 'justify_y', 'goal_y': 'goal_y', 'offset_y': 'offset_y', 'justify_z': 'justify_z', 'goal_z': 'goal_z', 'offset_z': 'offset_z', 'doscale': 'doscale', 'uniformscale': 'uniformscale', 'scale_axis': 'scale_axis', 'scale_x': 'scale_x', 'scale_y': 'scale_y', 'scale_z': 'scale_z', 'restorexform': 'restorexform', 'restoreattrib': 'restoreattrib', 'stashxform': 'stashxform', 'stashattrib': 'stashattrib', 'stashmerge': 'stashmerge'}

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
        self.parm_doboundgroup = Parameter(parm=self.node.parm('doboundgroup'))
        self.parm_folder2 = Parameter(parm=self.node.parm('folder2'))
        self.parm_sourcegroup = Parameter(parm=self.node.parm('sourcegroup'))
        self.parm_refgroup = Parameter(parm=self.node.parm('refgroup'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_sizex = Parameter(parm=self.node.parm('sizex'))
        self.parm_sizey = Parameter(parm=self.node.parm('sizey'))
        self.parm_sizez = Parameter(parm=self.node.parm('sizez'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_dotranslate = Parameter(parm=self.node.parm('dotranslate'))
        self.parm_offset_x = Parameter(parm=self.node.parm('offset_x'))
        self.parm_offset_y = Parameter(parm=self.node.parm('offset_y'))
        self.parm_offset_z = Parameter(parm=self.node.parm('offset_z'))
        self.parm_doscale = Parameter(parm=self.node.parm('doscale'))
        self.parm_uniformscale = Parameter(parm=self.node.parm('uniformscale'))
        self.parm_scale_x = Parameter(parm=self.node.parm('scale_x'))
        self.parm_scale_y = Parameter(parm=self.node.parm('scale_y'))
        self.parm_scale_z = Parameter(parm=self.node.parm('scale_z'))
        self.parm_restorexform = Parameter(parm=self.node.parm('restorexform'))
        self.parm_restoreattrib = Parameter(parm=self.node.parm('restoreattrib'))
        self.parm_stashxform = Parameter(parm=self.node.parm('stashxform'))
        self.parm_stashattrib = Parameter(parm=self.node.parm('stashattrib'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_justifytarget = JustifytargetMenu(parm=self.node.parm('justifytarget'))
        self.parm_sourcegrouptype = SourcegrouptypeMenu(parm=self.node.parm('sourcegrouptype'))
        self.parm_refgrouptype = RefgrouptypeMenu(parm=self.node.parm('refgrouptype'))
        self.parm_justify_x = JustifyXMenu(parm=self.node.parm('justify_x'))
        self.parm_goal_x = GoalXMenu(parm=self.node.parm('goal_x'))
        self.parm_justify_y = JustifyYMenu(parm=self.node.parm('justify_y'))
        self.parm_goal_y = GoalYMenu(parm=self.node.parm('goal_y'))
        self.parm_justify_z = JustifyZMenu(parm=self.node.parm('justify_z'))
        self.parm_goal_z = GoalZMenu(parm=self.node.parm('goal_z'))
        self.parm_scale_axis = ScaleAxisMenu(parm=self.node.parm('scale_axis'))
        self.parm_stashmerge = StashmergeMenu(parm=self.node.parm('stashmerge'))


        # input vars:
        self.input_geometry_to_move_and_resize = 'Geometry to move and resize'
        self.input_geometry_whose_bounding_box_is_to_be_matched = 'Geometry whose Bounding Box is to be matched'


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = "guess"
        self.menu_breakpoints = "breakpoints"
        self.menu_edges = "edges"
        self.menu_points = "points"
        self.menu_primitives = "prims"


class JustifytargetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_origin_and_unit_size = "origin"
        self.menu_second_input = "input"
        self.menu_location_and_size = "explicit"
        self.menu_input_if_wired = "auto"


class SourcegrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = "guess"
        self.menu_breakpoints = "breakpoints"
        self.menu_edges = "edges"
        self.menu_points = "points"
        self.menu_primitives = "prims"


class RefgrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = "guess"
        self.menu_breakpoints = "breakpoints"
        self.menu_edges = "edges"
        self.menu_points = "points"
        self.menu_primitives = "prims"


class JustifyXMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = "none"
        self.menu_min = "min"
        self.menu_center = "center"
        self.menu_max = "max"


class GoalXMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_same = "same"
        self.menu_min = "min"
        self.menu_center = "center"
        self.menu_max = "max"


class JustifyYMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = "none"
        self.menu_min = "min"
        self.menu_center = "center"
        self.menu_max = "max"


class GoalYMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_same = "same"
        self.menu_min = "min"
        self.menu_center = "center"
        self.menu_max = "max"


class JustifyZMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = "none"
        self.menu_min = "min"
        self.menu_center = "center"
        self.menu_max = "max"


class GoalZMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_same = "same"
        self.menu_min = "min"
        self.menu_center = "center"
        self.menu_max = "max"


class ScaleAxisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x = "x"
        self.menu_y = "y"
        self.menu_z = "z"
        self.menu_best_fit = "min"
        self.menu_perimeter = "perimeter"
        self.menu_area = "area"
        self.menu_volume = "volume"


class StashmergeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace_existing = "replace"
        self.menu_pre_multiply = "pre"
        self.menu_post_multiply = "post"



