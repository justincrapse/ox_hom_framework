from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class DeletejointsNode(OXNode):
    node_type = 'kinefx::deletejoints'
    parm_lookup_dict = {'group': 'group', 'negate': 'negate', 'delete': 'delete', 'children': 'children'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_delete = Parameter(parm=self.node.parm('delete'))
        self.parm_children = Parameter(parm=self.node.parm('children'))

        
        # parm menu vars:
        self.parm_group = GroupMenu(parm=self.node.parm('group'))
        self.parm_negate = NegateMenu(parm=self.node.parm('negate'))


        # input vars:
        self.input_skeleton = 'Skeleton'


# parm menu classes:
class GroupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_deformationsystem = ("@name=DeformationSystem", 0)
        self.menu_geometry = ("@name=Geometry", 1)
        self.menu_group = ("@name=Group", 2)
        self.menu_root_m = ("@name=Root_M", 3)
        self.menu_cursed_body_base1 = ("@name=cursed_body_base1", 4)


class NegateMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_delete_selected = ("dele", 0)
        self.menu_delete_non_selected = ("keep", 1)



