from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class Getpointtransform(OXNode):
    node_type = 'kinefx::getpointtransform'
    parm_lookup_dict = {'signature': 'signature', 'file': 'file', 'oppath': 'oppath', 'pt': 'pt', 'pt_n': 'pt_n', '_srcstr': '_srcstr'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_oppath = Parameter(parm=self.node.parm('oppath'))
        self.parm_pt = Parameter(parm=self.node.parm('pt'))
        self.parm_pt_n = Parameter(parm=self.node.parm('pt_n'))
        self.parm__srcstr = Parameter(parm=self.node.parm('_srcstr'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))
        self.parm_file = FileMenu(parm=self.node.parm('file'))


        # input vars:
        self.input_file = 'File'
        self.input_point_number = 'Point Number'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_by_point_number = ("default", 0)
        self.menu_by_name = ("n", 1)


class FileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_operator_path = ("oppath", 0)
        self.menu_first_input = ("opinput:0", 1)
        self.menu_second_input = ("opinput:1", 2)
        self.menu_third_input = ("opinput:2", 3)
        self.menu_fourth_input = ("opinput:3", 4)



