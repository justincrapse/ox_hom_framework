from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class NormalmapNode(OXNode):
    node_type = 'redshift::NormalMap'
    parm_lookup_dict = {'rs_shadernodemainswitcher1': 'RS_shaderNodeMainSwitcher1', 'texture_0': 'Texture_0', 'tex0': 'tex0', 'tspace_id': 'tspace_id', 'unbiasednormalmap': 'unbiasedNormalMap', 'flipy': 'flipY', 'scale': 'scale', 'tangents_1': 'Tangents_1', 'tangents': 'tangents', 'legacynormalmap': 'legacyNormalMap', 'elliptical_filtering_2': 'Elliptical_Filtering_2', 'eccmax': 'eccmax', 'alternate_3': 'Alternate_3', 'alt_x': 'alt_x', 'alt_y': 'alt_y', 'repeats_4': 'Repeats_4', 'repeats1': 'repeats1', 'repeats2': 'repeats2', 'wrapu': 'wrapU', 'wrapv': 'wrapV', 'uv_remap_5': 'UV_Remap_5', 'min_uv1': 'min_uv1', 'min_uv2': 'min_uv2', 'max_uv1': 'max_uv1', 'max_uv2': 'max_uv2', 'shader_skipdefvalparms': 'shader_skipdefvalparms'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_rs_shadernodemainswitcher1 = Parameter(parm=self.node.parm('RS_shaderNodeMainSwitcher1'))
        self.parm_texture_0 = Parameter(parm=self.node.parm('Texture_0'))
        self.parm_tex0 = Parameter(parm=self.node.parm('tex0'))
        self.parm_tspace_id = Parameter(parm=self.node.parm('tspace_id'))
        self.parm_unbiasednormalmap = Parameter(parm=self.node.parm('unbiasedNormalMap'))
        self.parm_flipy = Parameter(parm=self.node.parm('flipY'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_tangents_1 = Parameter(parm=self.node.parm('Tangents_1'))
        self.parm_tangents = Parameter(parm=self.node.parm('tangents'))
        self.parm_legacynormalmap = Parameter(parm=self.node.parm('legacyNormalMap'))
        self.parm_elliptical_filtering_2 = Parameter(parm=self.node.parm('Elliptical_Filtering_2'))
        self.parm_eccmax = Parameter(parm=self.node.parm('eccmax'))
        self.parm_alternate_3 = Parameter(parm=self.node.parm('Alternate_3'))
        self.parm_alt_x = Parameter(parm=self.node.parm('alt_x'))
        self.parm_alt_y = Parameter(parm=self.node.parm('alt_y'))
        self.parm_repeats_4 = Parameter(parm=self.node.parm('Repeats_4'))
        self.parm_repeats1 = Parameter(parm=self.node.parm('repeats1'))
        self.parm_repeats2 = Parameter(parm=self.node.parm('repeats2'))
        self.parm_wrapu = Parameter(parm=self.node.parm('wrapU'))
        self.parm_wrapv = Parameter(parm=self.node.parm('wrapV'))
        self.parm_uv_remap_5 = Parameter(parm=self.node.parm('UV_Remap_5'))
        self.parm_min_uv1 = Parameter(parm=self.node.parm('min_uv1'))
        self.parm_min_uv2 = Parameter(parm=self.node.parm('min_uv2'))
        self.parm_max_uv1 = Parameter(parm=self.node.parm('max_uv1'))
        self.parm_max_uv2 = Parameter(parm=self.node.parm('max_uv2'))
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))

        
        # parm menu vars:


        # input vars:
        self.input_min_uv = 'min_uv'
        self.input_max_uv = 'max_uv'


# parm menu classes:

