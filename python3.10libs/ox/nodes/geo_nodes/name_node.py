from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class NameNode(OXNode):
    node_type = 'name'
    parm_lookup_dict = {'attribname': 'attribname', 'class_alt': 'class', 'donamefromgroup': 'donamefromgroup', 'namefromgroupmask': 'namefromgroupmask', 'numnames': 'numnames', 'numrenames': 'numrenames', 'group1': 'group1', 'name1': 'name1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_attribname = Parameter(parm=self.node.parm('attribname'))
        self.parm_donamefromgroup = Parameter(parm=self.node.parm('donamefromgroup'))
        self.parm_namefromgroupmask = Parameter(parm=self.node.parm('namefromgroupmask'))
        self.parm_numnames = Parameter(parm=self.node.parm('numnames'))
        self.parm_numrenames = Parameter(parm=self.node.parm('numrenames'))
        self.parm_group1 = Parameter(parm=self.node.parm('group1'))
        self.parm_name1 = Parameter(parm=self.node.parm('name1'))

        
        # parm menu vars:
        self.parm_class_alt = ClassAltMenu(parm=self.node.parm('class'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitive = ("primitive", 0)
        self.menu_point = ("point", 1)
        self.menu_vertex = ("vertex", 2)



