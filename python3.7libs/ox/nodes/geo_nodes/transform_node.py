from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class TransformNode(OXNode):
    node_type = 'xform'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'shear1': 'shear1', 'shear2': 'shear2', 'shear3': 'shear3', 'scale': 'scale', 'parmgroup_pivotxform': 'parmgroup_pivotxform', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz', 'parmgroup_prexform': 'parmgroup_prexform', 'prexform_xord': 'prexform_xOrd', 'prexform_rord': 'prexform_rOrd', 'prexform_tx': 'prexform_tx', 'prexform_ty': 'prexform_ty', 'prexform_tz': 'prexform_tz', 'prexform_rx': 'prexform_rx', 'prexform_ry': 'prexform_ry', 'prexform_rz': 'prexform_rz', 'prexform_sx': 'prexform_sx', 'prexform_sy': 'prexform_sy', 'prexform_sz': 'prexform_sz', 'prexform_shear1': 'prexform_shear1', 'prexform_shear2': 'prexform_shear2', 'prexform_shear3': 'prexform_shear3', 'movecentroid': 'movecentroid', 'attribs': 'attribs', 'updatenmls': 'updatenmls', 'updateaffectednmls': 'updateaffectednmls', 'vlength': 'vlength', 'invertxform': 'invertxform', 'addattrib': 'addattrib', 'outputattrib': 'outputattrib', 'outputmerge': 'outputmerge'}

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
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_sx = Parameter(parm=self.node.parm('sx'))
        self.parm_sy = Parameter(parm=self.node.parm('sy'))
        self.parm_sz = Parameter(parm=self.node.parm('sz'))
        self.parm_shear1 = Parameter(parm=self.node.parm('shear1'))
        self.parm_shear2 = Parameter(parm=self.node.parm('shear2'))
        self.parm_shear3 = Parameter(parm=self.node.parm('shear3'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_parmgroup_pivotxform = Parameter(parm=self.node.parm('parmgroup_pivotxform'))
        self.parm_px = Parameter(parm=self.node.parm('px'))
        self.parm_py = Parameter(parm=self.node.parm('py'))
        self.parm_pz = Parameter(parm=self.node.parm('pz'))
        self.parm_prx = Parameter(parm=self.node.parm('prx'))
        self.parm_pry = Parameter(parm=self.node.parm('pry'))
        self.parm_prz = Parameter(parm=self.node.parm('prz'))
        self.parm_parmgroup_prexform = Parameter(parm=self.node.parm('parmgroup_prexform'))
        self.parm_prexform_tx = Parameter(parm=self.node.parm('prexform_tx'))
        self.parm_prexform_ty = Parameter(parm=self.node.parm('prexform_ty'))
        self.parm_prexform_tz = Parameter(parm=self.node.parm('prexform_tz'))
        self.parm_prexform_rx = Parameter(parm=self.node.parm('prexform_rx'))
        self.parm_prexform_ry = Parameter(parm=self.node.parm('prexform_ry'))
        self.parm_prexform_rz = Parameter(parm=self.node.parm('prexform_rz'))
        self.parm_prexform_sx = Parameter(parm=self.node.parm('prexform_sx'))
        self.parm_prexform_sy = Parameter(parm=self.node.parm('prexform_sy'))
        self.parm_prexform_sz = Parameter(parm=self.node.parm('prexform_sz'))
        self.parm_prexform_shear1 = Parameter(parm=self.node.parm('prexform_shear1'))
        self.parm_prexform_shear2 = Parameter(parm=self.node.parm('prexform_shear2'))
        self.parm_prexform_shear3 = Parameter(parm=self.node.parm('prexform_shear3'))
        self.parm_movecentroid = Parameter(parm=self.node.parm('movecentroid'))
        self.parm_attribs = Parameter(parm=self.node.parm('attribs'))
        self.parm_updatenmls = Parameter(parm=self.node.parm('updatenmls'))
        self.parm_updateaffectednmls = Parameter(parm=self.node.parm('updateaffectednmls'))
        self.parm_vlength = Parameter(parm=self.node.parm('vlength'))
        self.parm_invertxform = Parameter(parm=self.node.parm('invertxform'))
        self.parm_addattrib = Parameter(parm=self.node.parm('addattrib'))
        self.parm_outputattrib = Parameter(parm=self.node.parm('outputattrib'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))
        self.parm_prexform_xord = PrexformXordMenu(parm=self.node.parm('prexform_xOrd'))
        self.parm_prexform_rord = PrexformRordMenu(parm=self.node.parm('prexform_rOrd'))
        self.parm_outputmerge = OutputmergeMenu(parm=self.node.parm('outputmerge'))


        # input vars:
        self.input_transform_geometry = 'Transform geometry'


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


class XordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_rot_trans = "srt"
        self.menu_scale_trans_rot = "str"
        self.menu_rot_scale_trans = "rst"
        self.menu_rot_trans_scale = "rts"
        self.menu_trans_scale_rot = "tsr"
        self.menu_trans_rot_scale = "trs"


class RordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rx_ry_rz = "xyz"
        self.menu_rx_rz_ry = "xzy"
        self.menu_ry_rx_rz = "yxz"
        self.menu_ry_rz_rx = "yzx"
        self.menu_rz_rx_ry = "zxy"
        self.menu_rz_ry_rx = "zyx"


class PrexformXordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_rot_trans = "srt"
        self.menu_scale_trans_rot = "str"
        self.menu_rot_scale_trans = "rst"
        self.menu_rot_trans_scale = "rts"
        self.menu_trans_scale_rot = "tsr"
        self.menu_trans_rot_scale = "trs"


class PrexformRordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rx_ry_rz = "xyz"
        self.menu_rx_rz_ry = "xzy"
        self.menu_ry_rx_rz = "yxz"
        self.menu_ry_rz_rx = "yzx"
        self.menu_rz_rx_ry = "zxy"
        self.menu_rz_ry_rx = "zyx"


class OutputmergeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace_existing = "replace"
        self.menu_pre_multiply = "pre"
        self.menu_post_multiply = "post"



