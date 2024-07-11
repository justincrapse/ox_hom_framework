from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class BonedeformNode(OXNode):
    node_type = 'bonedeform'
    parm_lookup_dict = {'group': 'group', 'skelrootpath': 'skelrootpath', 'method': 'method', 'dqblendattrib': 'dqblendattrib', 'bonetransformpath': 'bonetransformpath', 'bonetransformtargetpath': 'bonetransformtargetpath', 'bonetransformregionpath': 'bonetransformregionpath', 'otherattribs': 'otherattribs', 'donormal': 'donormal', 'deletecaptureattrib': 'deletecaptureattrib', 'deletepointtcolors': 'deletepointtcolors'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_skelrootpath = Parameter(parm=self.node.parm('skelrootpath'))
        self.parm_bonetransformpath = Parameter(parm=self.node.parm('bonetransformpath'))
        self.parm_bonetransformtargetpath = Parameter(parm=self.node.parm('bonetransformtargetpath'))
        self.parm_bonetransformregionpath = Parameter(parm=self.node.parm('bonetransformregionpath'))
        self.parm_donormal = Parameter(parm=self.node.parm('donormal'))
        self.parm_deletecaptureattrib = Parameter(parm=self.node.parm('deletecaptureattrib'))
        self.parm_deletepointtcolors = Parameter(parm=self.node.parm('deletepointtcolors'))

        
        # parm menu vars:
        self.parm_method = MethodMenu(parm=self.node.parm('method'))
        self.parm_dqblendattrib = DqblendattribMenu(parm=self.node.parm('dqblendattrib'))
        self.parm_otherattribs = OtherattribsMenu(parm=self.node.parm('otherattribs'))


        # input vars:
        self.input_geometry_to_deform = 'Geometry to Deform'
        self.input_rest_point_transforms = 'Rest Point Transforms'
        self.input_deform_point_transforms = 'Deform Point Transforms'


# parm menu classes:
class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear = ("linear", 0)
        self.menu_dual_quaternion = ("dualquat", 1)
        self.menu_blend_dual_quaternion_and_linear = ("blenddualquat", 2)
        self.menu_from_input_geometry = ("frominputgeo", 3)


class DqblendattribMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_position__p_ = ("P", 0)


class OtherattribsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_normal__n_ = ("N", 0)



