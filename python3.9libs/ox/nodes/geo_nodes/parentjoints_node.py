from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class ParentjointsNode(OXNode):
    node_type = 'kinefx::parentjoints'
    parm_lookup_dict = {'unparentoncycle': 'unparentoncycle', 'reparent': 'reparent', 'enable1': 'enable1', 'joint1': 'joint1', 'parent1': 'parent1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_unparentoncycle = Parameter(parm=self.node.parm('unparentoncycle'))
        self.parm_reparent = Parameter(parm=self.node.parm('reparent'))
        self.parm_enable1 = Parameter(parm=self.node.parm('enable1'))

        
        # parm menu vars:
        self.parm_joint1 = Joint1Menu(parm=self.node.parm('joint1'))
        self.parm_parent1 = Parent1Menu(parm=self.node.parm('parent1'))


        # input vars:
        self.input_skeleton = 'Skeleton'


# parm menu classes:
class Joint1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_arrowtip1_l = ("@name=ArrowTip1_L", 0)
        self.menu_arrowtip2_l = ("@name=ArrowTip2_L", 1)
        self.menu_arrowtip3_l = ("@name=ArrowTip3_L", 2)
        self.menu_arrowtip4_l = ("@name=ArrowTip4_L", 3)
        self.menu_cog = ("@name=COG", 4)
        self.menu_deformationsystem = ("@name=DeformationSystem", 5)
        self.menu_geometry = ("@name=Geometry", 6)
        self.menu_group = ("@name=Group", 7)
        self.menu_root_m = ("@name=Root_M", 8)
        self.menu_arrowfeather1_r = ("@name=arrowFeather1_R", 9)
        self.menu_arrowfeather2_r = ("@name=arrowFeather2_R", 10)
        self.menu_arrowfeather3_r = ("@name=arrowFeather3_R", 11)
        self.menu_cursed_crown_arrows1 = ("@name=cursed_crown_arrows1", 12)


class Parent1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_arrowtip1_l = ("@name=ArrowTip1_L", 0)
        self.menu_arrowtip2_l = ("@name=ArrowTip2_L", 1)
        self.menu_arrowtip3_l = ("@name=ArrowTip3_L", 2)
        self.menu_arrowtip4_l = ("@name=ArrowTip4_L", 3)
        self.menu_cog = ("@name=COG", 4)
        self.menu_deformationsystem = ("@name=DeformationSystem", 5)
        self.menu_geometry = ("@name=Geometry", 6)
        self.menu_group = ("@name=Group", 7)
        self.menu_root_m = ("@name=Root_M", 8)
        self.menu_arrowfeather1_r = ("@name=arrowFeather1_R", 9)
        self.menu_arrowfeather2_r = ("@name=arrowFeather2_R", 10)
        self.menu_arrowfeather3_r = ("@name=arrowFeather3_R", 11)
        self.menu_cursed_crown_arrows1 = ("@name=cursed_crown_arrows1", 12)



