from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class UvtransformNode(OXNode):
    node_type = 'uvtransform::2.0'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'uvattrib': 'uvattrib', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'shear1': 'shear1', 'shear2': 'shear2', 'shear3': 'shear3', 'px': 'px', 'py': 'py', 'pz': 'pz', 'softparmsgrouper': 'softparmsgrouper', 'rad': 'rad', 'type': 'type', 'begintandeg': 'begintandeg', 'endtandeg': 'endtandeg', 'kernel': 'kernel', 'metric': 'metric', 'global': 'global', 'uvglobal': 'uvglobal', 'visualizefalloff': 'visualizefalloff'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
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
        self.parm_px = Parameter(parm=self.node.parm('px'))
        self.parm_py = Parameter(parm=self.node.parm('py'))
        self.parm_pz = Parameter(parm=self.node.parm('pz'))
        self.parm_softparmsgrouper = Parameter(parm=self.node.parm('softparmsgrouper'))
        self.parm_rad = Parameter(parm=self.node.parm('rad'))
        self.parm_begintandeg = Parameter(parm=self.node.parm('begintandeg'))
        self.parm_endtandeg = Parameter(parm=self.node.parm('endtandeg'))
        self.parm_kernel = Parameter(parm=self.node.parm('kernel'))
        self.parm_global = Parameter(parm=self.node.parm('global'))
        self.parm_uvglobal = Parameter(parm=self.node.parm('uvglobal'))

        
        # parm menu vars:
        self.parm_group = GroupMenu(parm=self.node.parm('group'))
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_uvattrib = UvattribMenu(parm=self.node.parm('uvattrib'))
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))
        self.parm_type = TypeMenu(parm=self.node.parm('type'))
        self.parm_metric = MetricMenu(parm=self.node.parm('metric'))
        self.parm_visualizefalloff = VisualizefalloffMenu(parm=self.node.parm('visualizefalloff'))


        # input vars:
        self.input_uvs_to_transform = 'UVs to Transform'


# parm menu classes:
class GroupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bottom = ("bottom", 0)
        self.menu_hf_group = ("hf_group", 1)
        self.menu__separator_ = ("_separator_", 2)
        self.menu__name = ("", 3)
        self.menu_height = ("@name=height", 4)
        self.menu__separator_ = ("_separator_", 5)
        self.menu__shop_materialpath = ("", 6)
        self.menu__obj_limestone_cli___liff_rock_rs_vopnet = ("@shop_materialpath=/obj/limestone_cliff_rock/limestone_cliff_rock_RS_VOPnet", 7)


class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = ("guess", 0)
        self.menu_vertices = ("vertices", 1)
        self.menu_edges = ("edges", 2)
        self.menu_points = ("points", 3)
        self.menu_primitives = ("prims", 4)


class UvattribMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_texture__uv_ = ("uv", 0)


class XordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_rot_trans = ("srt", 0)
        self.menu_scale_trans_rot = ("str", 1)
        self.menu_rot_scale_trans = ("rst", 2)
        self.menu_rot_trans_scale = ("rts", 3)
        self.menu_trans_scale_rot = ("tsr", 4)
        self.menu_trans_rot_scale = ("trs", 5)


class RordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rx_ry_rz = ("xyz", 0)
        self.menu_rx_rz_ry = ("xzy", 1)
        self.menu_ry_rx_rz = ("yxz", 2)
        self.menu_ry_rz_rx = ("yzx", 3)
        self.menu_rz_rx_ry = ("zxy", 4)
        self.menu_rz_ry_rx = ("zyx", 5)


class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear = ("linear", 0)
        self.menu_quadratic = ("quadratic", 1)
        self.menu_cubic = ("cubic", 2)
        self.menu_meta_ball = ("meta", 3)


class MetricMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uv = ("uv", 0)
        self.menu_uvw = ("uvw", 1)
        self.menu_xyz = ("xyz", 2)


class VisualizefalloffMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_never = ("never", 0)
        self.menu_always = ("always", 1)
        self.menu_when_viewport_tool_is_active = ("state", 2)



