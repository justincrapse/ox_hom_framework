from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RigattribvopNode(OXNode):
    node_type = 'kinefx::rigattribvop'
    parm_lookup_dict = {'bindgroup': 'bindgroup', 'bindgrouptype': 'bindgrouptype', 'bindclass': 'bindclass', 'vex_numcount': 'vex_numcount', 'vex_threadjobsize': 'vex_threadjobsize', 'stdswitcher1': 'stdswitcher1', 'vexsrc': 'vexsrc', 'shoppath': 'shoppath', 'script': 'script', 'clear': 'clear', 'vexsnippet': 'vexsnippet', 'vex_strict': 'vex_strict', 'vex_exportlist': 'vex_exportlist', 'vop_compiler': 'vop_compiler', 'vop_forcecompile': 'vop_forcecompile', 'vex_cwdpath': 'vex_cwdpath', 'vex_outputmask': 'vex_outputmask', 'vex_multithread': 'vex_multithread', 'vex_precision': 'vex_precision', 'autobind': 'autobind', 'bindings': 'bindings', 'groupautobind': 'groupautobind', 'groupbindings': 'groupbindings', 'vex_updatenmls': 'vex_updatenmls', 'vex_matchattrib': 'vex_matchattrib', 'vex_inplace': 'vex_inplace', 'vex_selectiongroup': 'vex_selectiongroup', 'viewerstate': 'viewerstate', 'compute': 'compute', 'compute1': 'compute1', 'compute2': 'compute2', 'compute3': 'compute3', 'compute4': 'compute4'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_bindgroup = Parameter(parm=self.node.parm('bindgroup'))
        self.parm_vex_numcount = Parameter(parm=self.node.parm('vex_numcount'))
        self.parm_vex_threadjobsize = Parameter(parm=self.node.parm('vex_threadjobsize'))
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_shoppath = Parameter(parm=self.node.parm('shoppath'))
        self.parm_script = Parameter(parm=self.node.parm('script'))
        self.parm_clear = Parameter(parm=self.node.parm('clear'))
        self.parm_vexsnippet = Parameter(parm=self.node.parm('vexsnippet'))
        self.parm_vex_strict = Parameter(parm=self.node.parm('vex_strict'))
        self.parm_vex_exportlist = Parameter(parm=self.node.parm('vex_exportlist'))
        self.parm_vop_compiler = Parameter(parm=self.node.parm('vop_compiler'))
        self.parm_vop_forcecompile = Parameter(parm=self.node.parm('vop_forcecompile'))
        self.parm_vex_cwdpath = Parameter(parm=self.node.parm('vex_cwdpath'))
        self.parm_vex_outputmask = Parameter(parm=self.node.parm('vex_outputmask'))
        self.parm_vex_multithread = Parameter(parm=self.node.parm('vex_multithread'))
        self.parm_autobind = Parameter(parm=self.node.parm('autobind'))
        self.parm_bindings = Parameter(parm=self.node.parm('bindings'))
        self.parm_groupautobind = Parameter(parm=self.node.parm('groupautobind'))
        self.parm_groupbindings = Parameter(parm=self.node.parm('groupbindings'))
        self.parm_vex_updatenmls = Parameter(parm=self.node.parm('vex_updatenmls'))
        self.parm_vex_matchattrib = Parameter(parm=self.node.parm('vex_matchattrib'))
        self.parm_vex_inplace = Parameter(parm=self.node.parm('vex_inplace'))
        self.parm_vex_selectiongroup = Parameter(parm=self.node.parm('vex_selectiongroup'))
        self.parm_viewerstate = Parameter(parm=self.node.parm('viewerstate'))
        self.parm_compute = Parameter(parm=self.node.parm('compute'))
        self.parm_compute1 = Parameter(parm=self.node.parm('compute1'))
        self.parm_compute2 = Parameter(parm=self.node.parm('compute2'))
        self.parm_compute3 = Parameter(parm=self.node.parm('compute3'))
        self.parm_compute4 = Parameter(parm=self.node.parm('compute4'))

        
        # parm menu vars:
        self.parm_bindgrouptype = BindgrouptypeMenu(parm=self.node.parm('bindgrouptype'))
        self.parm_bindclass = BindclassMenu(parm=self.node.parm('bindclass'))
        self.parm_vexsrc = VexsrcMenu(parm=self.node.parm('vexsrc'))
        self.parm_vex_precision = VexPrecisionMenu(parm=self.node.parm('vex_precision'))


        # input vars:
        self.input_input_1 = 'Input 1'
        self.input_input_2 = 'Input 2'
        self.input_input_3 = 'Input 3'
        self.input_input_4 = 'Input 4'


# parm menu classes:
class BindgrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = ("guess", 0)
        self.menu_vertices = ("vertices", 1)
        self.menu_edges = ("edges", 2)
        self.menu_points = ("points", 3)
        self.menu_primitives = ("prims", 4)


class BindclassMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_detail__only_once_ = ("detail", 0)
        self.menu_primitives = ("primitive", 1)
        self.menu_points = ("point", 2)
        self.menu_vertices = ("vertex", 3)
        self.menu_numbers = ("number", 4)


class VexsrcMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_myself = ("myself", 0)
        self.menu_shop = ("shop", 1)
        self.menu_script = ("script", 2)
        self.menu_snippet = ("snippet", 3)


class VexPrecisionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = ("auto", 0)
        self.menu_bit_32 = ("32", 1)
        self.menu_bit_64 = ("64", 2)



