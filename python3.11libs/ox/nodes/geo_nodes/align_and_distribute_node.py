from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AlignAndDistributeNode(OXNode):
    node_type = 'labs::align_and_distribute'
    parm_lookup_dict = {'folder1': 'folder1', 'split_by': 'split_by', 'attribname': 'attribname', 'sort_by': 'sort_by', 'bbox_relative': 'bbox_relative', 'offset': 'offset', 'axis_align': 'axis_align', 'x': 'x', 'y': 'y', 'z': 'z', 'fd_alignment': 'fd_alignment', 'malignmode': 'mAlignMode', 'fd_linear': 'fd_linear', 'axis': 'axis', 'alignment': 'alignment', 'fd_grid': 'fd_grid', 'orient': 'orient'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_attribname = Parameter(parm=self.node.parm('attribname'))
        self.parm_bbox_relative = Parameter(parm=self.node.parm('bbox_relative'))
        self.parm_offset = Parameter(parm=self.node.parm('offset'))
        self.parm_axis_align = Parameter(parm=self.node.parm('axis_align'))
        self.parm_fd_alignment = Parameter(parm=self.node.parm('fd_alignment'))
        self.parm_fd_linear = Parameter(parm=self.node.parm('fd_linear'))
        self.parm_fd_grid = Parameter(parm=self.node.parm('fd_grid'))

        
        # parm menu vars:
        self.parm_split_by = SplitByMenu(parm=self.node.parm('split_by'))
        self.parm_sort_by = SortByMenu(parm=self.node.parm('sort_by'))
        self.parm_x = XMenu(parm=self.node.parm('x'))
        self.parm_y = YMenu(parm=self.node.parm('y'))
        self.parm_z = ZMenu(parm=self.node.parm('z'))
        self.parm_malignmode = MalignmodeMenu(parm=self.node.parm('mAlignMode'))
        self.parm_axis = AxisMenu(parm=self.node.parm('axis'))
        self.parm_alignment = AlignmentMenu(parm=self.node.parm('alignment'))
        self.parm_orient = OrientMenu(parm=self.node.parm('orient'))


        # input vars:
        self.input_merged_meshes_to_align = 'Merged Meshes to Align'


# parm menu classes:
class SplitByMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_connectivity = ("0", 0)
        self.menu_piece_attribute = ("1", 1)


class SortByMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("0", 0)
        self.menu_size = ("1", 1)
        self.menu_polycount = ("2", 2)


class XMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_change = ("0", 0)
        self.menu_center = ("1", 1)
        self.menu_min = ("2", 2)
        self.menu_max = ("3", 3)


class YMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_change = ("0", 0)
        self.menu_center = ("1", 1)
        self.menu_min = ("2", 2)
        self.menu_max = ("3", 3)


class ZMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_change = ("0", 0)
        self.menu_center = ("1", 1)
        self.menu_min = ("2", 2)
        self.menu_max = ("3", 3)


class MalignmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear = ("0", 0)
        self.menu_grid = ("1", 1)


class AxisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x = ("0", 0)
        self.menu_y = ("1", 1)
        self.menu_z = ("2", 2)


class AlignmentMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_positive = ("0", 0)
        self.menu_center = ("1", 1)
        self.menu_negative = ("2", 2)


class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_xy_plane = ("xy", 0)
        self.menu_yz_plane = ("yz", 1)
        self.menu_zx_plane = ("zx", 2)



