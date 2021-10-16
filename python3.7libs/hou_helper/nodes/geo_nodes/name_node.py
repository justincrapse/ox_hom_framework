from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class NameNode(HHNode):
    node_type = 'name'
    parm_lookup_dict = {'attribname': 'attribname', 'class_alt': 'class', 'donamefromgroup': 'donamefromgroup', 'namefromgroupmask': 'namefromgroupmask', 'numnames': 'numnames', 'numrenames': 'numrenames', 'group1': 'group1', 'name1': 'name1'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
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
        self.parm_class_alt_menu = ClassAltMenu(parm=self.node.parm('class'))


        # input vars:
        self.input_input_1 = 0


# parm menu classes:
class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.primitive = 0
        self.point = 1



