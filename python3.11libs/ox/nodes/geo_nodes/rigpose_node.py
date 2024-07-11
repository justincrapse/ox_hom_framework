from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RigposeNode(OXNode):
    node_type = 'kinefx::rigpose'
    parm_lookup_dict = {'fbikhandles': 'fbikhandles', 'folder01': 'folder01', 'bake': 'bake', 'setalltodefault': 'setalltodefault', 'worldspace': 'worldspace', 'commands': 'commands', 'bakeall': 'bakeall', 'bakepose': 'bakepose', 'bakefromrestpose': 'bakefromrestpose', 'restattrib': 'restattrib', 'transformations': 'transformations', 'use_subnet_output': 'use_subnet_output', 'multithread': 'multithread', 'preserveshears': 'preserveshears', 'outputparmattribs': 'outputparmattribs', 'outputtrs_folder': 'outputtrs_folder', 'outputparmt': 'outputparmt', 'outputparmr': 'outputparmr', 'outputparms': 'outputparms', 'outputparmp': 'outputparmp', 'outputparmpr': 'outputparmpr', 'outputinternalattribs': 'outputinternalattribs', 'outputinternal_folder': 'outputinternal_folder', 'outputlocaltransform': 'outputlocaltransform', 'outputinputlocaltransform': 'outputinputlocaltransform', 'outputeffectivelocaltransform': 'outputeffectivelocaltransform', 'folder1': 'folder1', 'configurations': 'configurations', 'viewerrigs': 'viewerrigs', 'enable0': 'enable0', 'group0': 'group0', 'mode0': 'mode0', 'bake0': 'bake0', 'xord0': 'xOrd0', 'rord0': 'rOrd0', 't0x': 't0x', 't0y': 't0y', 't0z': 't0z', 'r0x': 'r0x', 'r0y': 'r0y', 'r0z': 'r0z', 's0x': 's0x', 's0y': 's0y', 's0z': 's0z', 'pivot0': 'pivot0', 'p0x': 'p0x', 'p0y': 'p0y', 'p0z': 'p0z', 'pivot_r0x': 'pivot_r0x', 'pivot_r0y': 'pivot_r0y', 'pivot_r0z': 'pivot_r0z'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_fbikhandles = Parameter(parm=self.node.parm('fbikhandles'))
        self.parm_folder01 = Parameter(parm=self.node.parm('folder01'))
        self.parm_bake = Parameter(parm=self.node.parm('bake'))
        self.parm_setalltodefault = Parameter(parm=self.node.parm('setalltodefault'))
        self.parm_worldspace = Parameter(parm=self.node.parm('worldspace'))
        self.parm_commands = Parameter(parm=self.node.parm('commands'))
        self.parm_bakeall = Parameter(parm=self.node.parm('bakeall'))
        self.parm_bakepose = Parameter(parm=self.node.parm('bakepose'))
        self.parm_bakefromrestpose = Parameter(parm=self.node.parm('bakefromrestpose'))
        self.parm_restattrib = Parameter(parm=self.node.parm('restattrib'))
        self.parm_transformations = Parameter(parm=self.node.parm('transformations'))
        self.parm_use_subnet_output = Parameter(parm=self.node.parm('use_subnet_output'))
        self.parm_multithread = Parameter(parm=self.node.parm('multithread'))
        self.parm_preserveshears = Parameter(parm=self.node.parm('preserveshears'))
        self.parm_outputparmattribs = Parameter(parm=self.node.parm('outputparmattribs'))
        self.parm_outputtrs_folder = Parameter(parm=self.node.parm('outputtrs_folder'))
        self.parm_outputparmt = Parameter(parm=self.node.parm('outputparmt'))
        self.parm_outputparmr = Parameter(parm=self.node.parm('outputparmr'))
        self.parm_outputparms = Parameter(parm=self.node.parm('outputparms'))
        self.parm_outputparmp = Parameter(parm=self.node.parm('outputparmp'))
        self.parm_outputparmpr = Parameter(parm=self.node.parm('outputparmpr'))
        self.parm_outputinternalattribs = Parameter(parm=self.node.parm('outputinternalattribs'))
        self.parm_outputinternal_folder = Parameter(parm=self.node.parm('outputinternal_folder'))
        self.parm_outputlocaltransform = Parameter(parm=self.node.parm('outputlocaltransform'))
        self.parm_outputinputlocaltransform = Parameter(parm=self.node.parm('outputinputlocaltransform'))
        self.parm_outputeffectivelocaltransform = Parameter(parm=self.node.parm('outputeffectivelocaltransform'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_configurations = Parameter(parm=self.node.parm('configurations'))
        self.parm_viewerrigs = Parameter(parm=self.node.parm('viewerrigs'))
        self.parm_enable0 = Parameter(parm=self.node.parm('enable0'))
        self.parm_bake0 = Parameter(parm=self.node.parm('bake0'))
        self.parm_t0x = Parameter(parm=self.node.parm('t0x'))
        self.parm_t0y = Parameter(parm=self.node.parm('t0y'))
        self.parm_t0z = Parameter(parm=self.node.parm('t0z'))
        self.parm_r0x = Parameter(parm=self.node.parm('r0x'))
        self.parm_r0y = Parameter(parm=self.node.parm('r0y'))
        self.parm_r0z = Parameter(parm=self.node.parm('r0z'))
        self.parm_s0x = Parameter(parm=self.node.parm('s0x'))
        self.parm_s0y = Parameter(parm=self.node.parm('s0y'))
        self.parm_s0z = Parameter(parm=self.node.parm('s0z'))
        self.parm_pivot0 = Parameter(parm=self.node.parm('pivot0'))
        self.parm_p0x = Parameter(parm=self.node.parm('p0x'))
        self.parm_p0y = Parameter(parm=self.node.parm('p0y'))
        self.parm_p0z = Parameter(parm=self.node.parm('p0z'))
        self.parm_pivot_r0x = Parameter(parm=self.node.parm('pivot_r0x'))
        self.parm_pivot_r0y = Parameter(parm=self.node.parm('pivot_r0y'))
        self.parm_pivot_r0z = Parameter(parm=self.node.parm('pivot_r0z'))

        
        # parm menu vars:
        self.parm_group0 = Group0Menu(parm=self.node.parm('group0'))
        self.parm_mode0 = Mode0Menu(parm=self.node.parm('mode0'))
        self.parm_xord0 = Xord0Menu(parm=self.node.parm('xOrd0'))
        self.parm_rord0 = Rord0Menu(parm=self.node.parm('rOrd0'))


        # input vars:
        self.input_skeleton = 'Skeleton'


# parm menu classes:
class Group0Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_arrowtip1_l = ("@name=ArrowTip1_L", 0)
        self.menu_arrowtip2_l = ("@name=ArrowTip2_L", 1)
        self.menu_arrowtip3_l = ("@name=ArrowTip3_L", 2)
        self.menu_arrowtip4_l = ("@name=ArrowTip4_L", 3)
        self.menu_cog = ("@name=COG", 4)
        self.menu_deformationsystem = ("@name=DeformationSystem", 5)
        self.menu_geometry = ("@name=Geometry", 6)
        self.menu_group = ("@name=Group", 7)
        self.menu_root_m = ("@name=Root_M", 8)
        self.menu_arrowfeather1_r = ("@name=arrowFeather1_R", 9)
        self.menu_arrowfeather2_r = ("@name=arrowFeather2_R", 10)
        self.menu_arrowfeather3_r = ("@name=arrowFeather3_R", 11)
        self.menu_cursed_crown_arrows1 = ("@name=cursed_crown_arrows1", 12)


class Mode0Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_pre_multiply = ("pre", 0)
        self.menu_post_multiply = ("post", 1)
        self.menu_override = ("override", 2)
        self.menu_from_rest_pose = ("restpose", 3)


class Xord0Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_rot_trans = ("srt", 0)
        self.menu_scale_trans_rot = ("str", 1)
        self.menu_rot_scale_trans = ("rst", 2)
        self.menu_rot_trans_scale = ("rts", 3)
        self.menu_trans_scale_rot = ("tsr", 4)
        self.menu_trans_rot_scale = ("trs", 5)


class Rord0Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rx_ry_rz = ("xyz", 0)
        self.menu_rx_rz_ry = ("xzy", 1)
        self.menu_ry_rx_rz = ("yxz", 2)
        self.menu_ry_rz_rx = ("yzx", 3)
        self.menu_rz_rx_ry = ("zxy", 4)
        self.menu_rz_ry_rx = ("zyx", 5)



