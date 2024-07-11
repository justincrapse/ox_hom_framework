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
        self.parm_srcgroups = Parameter(parm=self.node.parm('srcgroups'))
        self.parm_dstgroups = Parameter(parm=self.node.parm('dstgroups'))
        self.parm_cardswitcher1 = Parameter(parm=self.node.parm('cardswitcher1'))
        self.parm_detailattribs = Parameter(parm=self.node.parm('detailattribs'))
        self.parm_detailattriblist = Parameter(parm=self.node.parm('detailattriblist'))
        self.parm_primitiveattribs = Parameter(parm=self.node.parm('primitiveattribs'))
        self.parm_primattriblist = Parameter(parm=self.node.parm('primattriblist'))
        self.parm_pointattribs = Parameter(parm=self.node.parm('pointattribs'))
        self.parm_pointattriblist = Parameter(parm=self.node.parm('pointattriblist'))
        self.parm_vertexattribs = Parameter(parm=self.node.parm('vertexattribs'))
        self.parm_vertexattriblist = Parameter(parm=self.node.parm('vertexattriblist'))
        self.parm_copyvariable = Parameter(parm=self.node.parm('copyvariable'))
        self.parm_matchpattrib = Parameter(parm=self.node.parm('matchpattrib'))
        self.parm_kernelradius = Parameter(parm=self.node.parm('kernelradius'))
        self.parm_maxsamplecount = Parameter(parm=self.node.parm('maxsamplecount'))
        self.parm_threshold = Parameter(parm=self.node.parm('threshold'))
        self.parm_thresholddist = Parameter(parm=self.node.parm('thresholddist'))
        self.parm_blendwidth = Parameter(parm=self.node.parm('blendwidth'))
        self.parm_uniformbias = Parameter(parm=self.node.parm('uniformbias'))

        
        # parm menu vars:
        self.parm_srcgrouptype = SrcgrouptypeMenu(parm=self.node.parm('srcgrouptype'))
        self.parm_dstgrouptype = DstgrouptypeMenu(parm=self.node.parm('dstgrouptype'))
        self.parm_kernel = KernelMenu(parm=self.node.parm('kernel'))


        # input vars:
        self.input_geometry_to_transfer_attributes_to = 'Geometry to transfer attributes to'
        self.input_geometry_to_transfer_attributes_from = 'Geometry to transfer attributes from'


# parm menu classes:
class SrcgrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = ("primitive", 0)
        self.menu_points = ("point", 1)


class DstgrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = ("primitive", 0)
        self.menu_points = ("point", 1)


class KernelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_wyvill_model = ("wyvill", 0)
        self.menu_elendt_model = ("elendt", 1)
        self.menu_blinn_model = ("blinn", 2)
        self.menu_links_model = ("links", 3)
        self.menu_renderman_model = ("prman", 4)
        self.menu_hart_model = ("hart", 5)
        self.menu_exponential_bump = ("xpbump", 6)
        self.menu_uniform_model = ("uniform", 7)



