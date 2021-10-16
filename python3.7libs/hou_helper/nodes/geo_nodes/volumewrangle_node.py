from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class VolumewrangleNode(HHNode):
    node_type = 'volumewrangle'
    parm_lookup_dict = {'folder01': 'folder01', 'group': 'group', 'bindeach': 'bindeach', 'snippet': 'snippet', 'exportlist': 'exportlist', 'vex_strict': 'vex_strict', 'autobind': 'autobind', 'bindings': 'bindings', 'vex_geometrygenerator': 'vex_geometrygenerator', 'vdb_signedflood': 'vdb_signedflood', 'vex_cwdpath': 'vex_cwdpath', 'vex_outputmask': 'vex_outputmask', 'vex_precision': 'vex_precision'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder01 = Parameter(parm=self.node.parm('folder01'))
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_bindeach = Parameter(parm=self.node.parm('bindeach'))
        self.parm_exportlist = Parameter(parm=self.node.parm('exportlist'))
        self.parm_vex_strict = Parameter(parm=self.node.parm('vex_strict'))
        self.parm_autobind = Parameter(parm=self.node.parm('autobind'))
        self.parm_bindings = Parameter(parm=self.node.parm('bindings'))
        self.parm_vex_geometrygenerator = Parameter(parm=self.node.parm('vex_geometrygenerator'))
        self.parm_vdb_signedflood = Parameter(parm=self.node.parm('vdb_signedflood'))
        self.parm_vex_cwdpath = Parameter(parm=self.node.parm('vex_cwdpath'))
        self.parm_vex_outputmask = Parameter(parm=self.node.parm('vex_outputmask'))

        
        # parm menu vars:
        self.parm_snippet_menu = SnippetMenu(parm=self.node.parm('snippet'))
        self.parm_vex_precision_menu = VexPrecisionMenu(parm=self.node.parm('vex_precision'))


        # input vars:
        self.input_volumes_to_process_with_wrangle = 0
        self.input_auxillary_input_1__access_with_volumesample_1______ = 1
        self.input_auxillary_input_2__access_with_volumesample_2______ = 2
        self.input_auxillary_input_3__access_with_volumesample_3______ = 3


# parm menu classes:
class SnippetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.create_points_where_positive = 0


class VexPrecisionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.auto = 0
        self._32 = 1
        self._64 = 2



