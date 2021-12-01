from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AttribtransferNode(OXNode):
    node_type = 'attribtransfer'
    parm_lookup_dict = {'srcgroups': 'srcgroups', 'srcgrouptype': 'srcgrouptype', 'dstgroups': 'dstgroups', 'dstgrouptype': 'dstgrouptype', 'cardswitcher1': 'cardswitcher1', 'detailattribs': 'detailattribs', 'detailattriblist': 'detailattriblist', 'primitiveattribs': 'primitiveattribs', 'primattriblist': 'primattriblist', 'pointattribs': 'pointattribs', 'pointattriblist': 'pointattriblist', 'vertexattribs': 'vertexattribs', 'vertexattriblist': 'vertexattriblist', 'copyvariable': 'copyvariable', 'matchpattrib': 'matchpattrib', 'kernel': 'kernel', 'kernelradius': 'kernelradius', 'maxsamplecount': 'maxsamplecount', 'threshold': 'threshold', 'thresholddist': 'thresholddist', 'blendwidth': 'blendwidth', 'uniformbias': 'uniformbias'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_dstgroups = Parameter(parm=self.node.parm('dstgroups'))
        self.parm_cardswitcher1 = Parameter(parm=self.node.parm('cardswitcher1'))
        self.parm_detailattribs = Parameter(parm=self.node.parm('detailattribs'))
        self.parm_primitiveattribs = Parameter(parm=self.node.parm('primitiveattribs'))
        self.parm_pointattribs = Parameter(parm=self.node.parm('pointattribs'))
        self.parm_vertexattribs = Parameter(parm=self.node.parm('vertexattribs'))
        self.parm_copyvariable = Parameter(parm=self.node.parm('copyvariable'))
        self.parm_matchpattrib = Parameter(parm=self.node.parm('matchpattrib'))
        self.parm_kernelradius = Parameter(parm=self.node.parm('kernelradius'))
        self.parm_maxsamplecount = Parameter(parm=self.node.parm('maxsamplecount'))
        self.parm_threshold = Parameter(parm=self.node.parm('threshold'))
        self.parm_thresholddist = Parameter(parm=self.node.parm('thresholddist'))
        self.parm_blendwidth = Parameter(parm=self.node.parm('blendwidth'))
        self.parm_uniformbias = Parameter(parm=self.node.parm('uniformbias'))

        
        # parm menu vars:
        self.parm_srcgroups = SrcgroupsMenu(parm=self.node.parm('srcgroups'))
        self.parm_srcgrouptype = SrcgrouptypeMenu(parm=self.node.parm('srcgrouptype'))
        self.parm_dstgrouptype = DstgrouptypeMenu(parm=self.node.parm('dstgrouptype'))
        self.parm_detailattriblist = DetailattriblistMenu(parm=self.node.parm('detailattriblist'))
        self.parm_primattriblist = PrimattriblistMenu(parm=self.node.parm('primattriblist'))
        self.parm_pointattriblist = PointattriblistMenu(parm=self.node.parm('pointattriblist'))
        self.parm_vertexattriblist = VertexattriblistMenu(parm=self.node.parm('vertexattriblist'))
        self.parm_kernel = KernelMenu(parm=self.node.parm('kernel'))


        # input vars:
        self.input_geometry_to_transfer_attributes_to = 'Geometry to transfer attributes to'
        self.input_geometry_to_transfer_attributes_from = 'Geometry to transfer attributes from'


# parm menu classes:
class SrcgroupsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__var1_lod0 = 0


class SrcgrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = 0
        self.menu_points = 1


class DstgrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = 0
        self.menu_points = 1


class DetailattriblistMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_varmap = 0


class PrimattriblistMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_material____shop_materialpath_ = 0
        self.menu_currentuvset = 1
        self.menu_name = 2


class PointattriblistMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_color____cd_ = 0
        self.menu_normal____n_ = 1
        self.menu_position____p_ = 2


class VertexattriblistMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_alpha = 0
        self.menu_texture____uv_ = 1
        self.menu_uv2 = 2


class KernelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_wyvill_model = 0
        self.menu_elendt_model = 1
        self.menu_blinn_model = 2
        self.menu_links_model = 3
        self.menu_renderman_model = 4
        self.menu_hart_model = 5
        self.menu_exponential_bump = 6
        self.menu_uniform_model = 7



