from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CopyandtransformNode(OXNode):
    node_type = 'duplicate'
    parm_lookup_dict = {'sourceprims': 'sourceprims', 'modifysource': 'modifysource', 'ncy': 'ncy', 'separatesource': 'separatesource', 'destinationprims': 'destinationprims', 'duplicatename': 'duplicatename', 'primitivedefinitiongroup': 'primitivedefinitiongroup', 'reftype': 'reftype', 'makeinstances': 'makeinstances', 'primkind': 'primkind', 'parentprimtype': 'parentprimtype', 'collectionsgroup': 'collectionsgroup', 'collectionpath': 'collectionpath', 'collectionname': 'collectionname', 'promotecollections': 'promotecollections', 'promotesourcecollections': 'promotesourcecollections', 'xformcumulative': 'xformcumulative', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'shear1': 'shear1', 'shear2': 'shear2', 'shear3': 'shear3', 'scale': 'scale', 'parmgroup_pivotxform': 'parmgroup_pivotxform', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_sourceprims = Parameter(parm=self.node.parm('sourceprims'))
        self.parm_ncy = Parameter(parm=self.node.parm('ncy'))
        self.parm_separatesource = Parameter(parm=self.node.parm('separatesource'))
        self.parm_destinationprims = Parameter(parm=self.node.parm('destinationprims'))
        self.parm_duplicatename = Parameter(parm=self.node.parm('duplicatename'))
        self.parm_primitivedefinitiongroup = Parameter(parm=self.node.parm('primitivedefinitiongroup'))
        self.parm_makeinstances = Parameter(parm=self.node.parm('makeinstances'))
        self.parm_collectionsgroup = Parameter(parm=self.node.parm('collectionsgroup'))
        self.parm_collectionpath = Parameter(parm=self.node.parm('collectionpath'))
        self.parm_collectionname = Parameter(parm=self.node.parm('collectionname'))
        self.parm_promotecollections = Parameter(parm=self.node.parm('promotecollections'))
        self.parm_promotesourcecollections = Parameter(parm=self.node.parm('promotesourcecollections'))
        self.parm_xformcumulative = Parameter(parm=self.node.parm('xformcumulative'))
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

        
        # parm menu vars:
        self.parm_modifysource = ModifysourceMenu(parm=self.node.parm('modifysource'))
        self.parm_reftype = ReftypeMenu(parm=self.node.parm('reftype'))
        self.parm_primkind = PrimkindMenu(parm=self.node.parm('primkind'))
        self.parm_parentprimtype = ParentprimtypeMenu(parm=self.node.parm('parentprimtype'))
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))


        # input vars:
        self.input_input_stage = 'Input Stage'


# parm menu classes:
class ModifysourceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_deactivate_source_primitives = ("deactivate", 0)
        self.menu_hide_source_primitives = ("hide", 1)
        self.menu_source_primitives_are_first_duplicates = ("", 2)
        self.menu_source_primitives_are_classes = ("class", 3)
        self.menu_source_primitives_are_deactivated = ("deactivated", 4)
        self.menu_source_primitives_are_hidden = ("hidden", 5)


class ReftypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_reference = ("prim", 0)
        self.menu_inherit = ("inherit", 1)
        self.menu_specialize = ("specialize", 2)
        self.menu_copy = ("copy", 3)


class PrimkindMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("", 0)
        self.menu_automatic = ("__automatic__", 1)
        self.menu_assembly = ("assembly", 2)
        self.menu_group = ("group", 3)
        self.menu_component = ("component", 4)
        self.menu_subcomponent = ("subcomponent", 5)


class ParentprimtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("", 0)
        self.menu_xform = ("UsdGeomXform", 1)
        self.menu_scope = ("UsdGeomScope", 2)


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



