from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CreepNode(OXNode):
    node_type = 'creep'
    parm_lookup_dict = {'group': 'group', 'path': 'path', 'stdswitcher1': 'stdswitcher1', 'initialize': 'Initialize', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'px': 'px', 'py': 'py', 'pz': 'pz', 'douv': 'douv', 'uvname': 'uvname', 'doattr': 'doattr', '_label_1': '_label_1', '_label_2': '_label_2', '_label_3': '_label_3', '_label_4': '_label_4', 'setpt': 'setpt', 'mulpt': 'mulpt', 'addpt': 'addpt', 'subpt': 'subpt', 'setprim': 'setprim', 'mulprim': 'mulprim', 'addprim': 'addprim', 'subprim': 'subprim', 'setvtx': 'setvtx', 'mulvtx': 'mulvtx', 'addvtx': 'addvtx', 'subvtx': 'subvtx'}

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
        self.parm_path = Parameter(parm=self.node.parm('path'))
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_sx = Parameter(parm=self.node.parm('sx'))
        self.parm_sy = Parameter(parm=self.node.parm('sy'))
        self.parm_sz = Parameter(parm=self.node.parm('sz'))
        self.parm_px = Parameter(parm=self.node.parm('px'))
        self.parm_py = Parameter(parm=self.node.parm('py'))
        self.parm_pz = Parameter(parm=self.node.parm('pz'))
        self.parm_douv = Parameter(parm=self.node.parm('douv'))
        self.parm_uvname = Parameter(parm=self.node.parm('uvname'))
        self.parm_doattr = Parameter(parm=self.node.parm('doattr'))
        self.parm__label_1 = Parameter(parm=self.node.parm('_label_1'))
        self.parm__label_2 = Parameter(parm=self.node.parm('_label_2'))
        self.parm__label_3 = Parameter(parm=self.node.parm('_label_3'))
        self.parm__label_4 = Parameter(parm=self.node.parm('_label_4'))
        self.parm_setpt = Parameter(parm=self.node.parm('setpt'))
        self.parm_mulpt = Parameter(parm=self.node.parm('mulpt'))
        self.parm_addpt = Parameter(parm=self.node.parm('addpt'))
        self.parm_subpt = Parameter(parm=self.node.parm('subpt'))
        self.parm_setprim = Parameter(parm=self.node.parm('setprim'))
        self.parm_mulprim = Parameter(parm=self.node.parm('mulprim'))
        self.parm_addprim = Parameter(parm=self.node.parm('addprim'))
        self.parm_subprim = Parameter(parm=self.node.parm('subprim'))
        self.parm_setvtx = Parameter(parm=self.node.parm('setvtx'))
        self.parm_mulvtx = Parameter(parm=self.node.parm('mulvtx'))
        self.parm_addvtx = Parameter(parm=self.node.parm('addvtx'))
        self.parm_subvtx = Parameter(parm=self.node.parm('subvtx'))

        
        # parm menu vars:
        self.parm_initialize = InitializeMenu(parm=self.node.parm('Initialize'))


        # input vars:
        self.input_geometry_to_project = 'Geometry To Project'
        self.input_geometry_to_project_onto = 'Geometry To Project Onto'


# parm menu classes:
class InitializeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_fill_path = ("initfill", 0)
        self.menu_keep_proportions = ("initundistort", 1)



