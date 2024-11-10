from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class TransformDNode(OXNode):
    node_type = 'xform2d'
    parm_lookup_dict = {'signature': 'signature', 'border': 'border', 'filter': 'filter', 'mask': 'mask', 'xord': 'xOrd', 'tx': 'tx', 'ty': 'ty', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'shear1': 'shear1', 'scale': 'scale', 'px': 'px', 'py': 'py', 'invertxform': 'invertxform', 'rasterize': 'rasterize'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_mask = Parameter(parm=self.node.parm('mask'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_sx = Parameter(parm=self.node.parm('sx'))
        self.parm_sy = Parameter(parm=self.node.parm('sy'))
        self.parm_shear1 = Parameter(parm=self.node.parm('shear1'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_px = Parameter(parm=self.node.parm('px'))
        self.parm_py = Parameter(parm=self.node.parm('py'))
        self.parm_invertxform = Parameter(parm=self.node.parm('invertxform'))
        self.parm_rasterize = Parameter(parm=self.node.parm('rasterize'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))
        self.parm_border = BorderMenu(parm=self.node.parm('border'))
        self.parm_filter = FilterMenu(parm=self.node.parm('filter'))
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))


        # input vars:
        self.input_source = 'source'
        self.input_mask = 'mask'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_select_automatically = ("auto", 0)
        self.menu_mono = ("f1", 1)
        self.menu_uv = ("f2", 2)
        self.menu_rgb = ("f3", 3)
        self.menu_rgba = ("f4", 4)
        self.menu_id = ("i", 5)


class BorderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = ("auto", 0)
        self.menu_constant = ("constant", 1)
        self.menu_clamp = ("clamp", 2)
        self.menu_mirror = ("mirror", 3)
        self.menu_wrap = ("wrap", 4)
        self.menu_clip = ("clip", 5)


class FilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_point = ("point", 0)
        self.menu_bilinear = ("bilinear", 1)
        self.menu_box = ("box", 2)
        self.menu_bartlett = ("triangle", 3)
        self.menu_catmull_rom = ("cubic", 4)
        self.menu_mitchell = ("mitchell", 5)
        self.menu_b_spline = ("bspline", 6)


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



