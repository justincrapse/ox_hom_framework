from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CopyNode(OXNode):
    node_type = 'copyxform'
    parm_lookup_dict = {'sourcegroup': 'sourcegroup', 'sourcegrouptype': 'sourcegrouptype', 'ncy': 'ncy', 'pack': 'pack', 'pivot': 'pivot', 'viewportlod': 'viewportlod', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'shear1': 'shear1', 'shear2': 'shear2', 'shear3': 'shear3', 'scale': 'scale', 'parmgroup_pivotxform': 'parmgroup_pivotxform', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz', 'newgroups': 'newgroups', 'newgroupprefix': 'newgroupprefix', 'docopyattrib': 'docopyattrib', 'copyattrib': 'copyattrib'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_sourcegroup = Parameter(parm=self.node.parm('sourcegroup'))
        self.parm_ncy = Parameter(parm=self.node.parm('ncy'))
        self.parm_pack = Parameter(parm=self.node.parm('pack'))
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
        self.parm_newgroups = Parameter(parm=self.node.parm('newgroups'))
        self.parm_newgroupprefix = Parameter(parm=self.node.parm('newgroupprefix'))
        self.parm_docopyattrib = Parameter(parm=self.node.parm('docopyattrib'))
        self.parm_copyattrib = Parameter(parm=self.node.parm('copyattrib'))

        
        # parm menu vars:
        self.parm_sourcegrouptype = SourcegrouptypeMenu(parm=self.node.parm('sourcegrouptype'))
        self.parm_pivot = PivotMenu(parm=self.node.parm('pivot'))
        self.parm_viewportlod = ViewportlodMenu(parm=self.node.parm('viewportlod'))
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))


        # input vars:
        self.input_primitives_to_copy = 'Primitives to Copy'


# parm menu classes:
class SourcegrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = ("guess", 0)
        self.menu_primitives = ("prims", 1)
        self.menu_points = ("points", 2)


class PivotMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_origin = ("origin", 0)
        self.menu_centroid = ("centroid", 1)


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = ("full", 0)
        self.menu_point_cloud = ("points", 1)
        self.menu_bounding_box = ("box", 2)
        self.menu_centroid = ("centroid", 3)
        self.menu_hidden = ("hidden", 4)


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



