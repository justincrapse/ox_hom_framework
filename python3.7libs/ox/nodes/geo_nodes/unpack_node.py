from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class UnpackNode(OXNode):
    node_type = 'unpack'
    parm_lookup_dict = {'group': 'group', 'limit_iterations': 'limit_iterations', 'iterations': 'iterations', 'detail_attributes': 'detail_attributes', 'transfer_attributes': 'transfer_attributes', 'transfer_groups': 'transfer_groups', 'apply_style_sheets': 'apply_style_sheets', 'scene_style_sheet': 'scene_style_sheet', 'obj_style_sheet': 'obj_style_sheet'}

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
        self.parm_limit_iterations = Parameter(parm=self.node.parm('limit_iterations'))
        self.parm_iterations = Parameter(parm=self.node.parm('iterations'))
        self.parm_transfer_attributes = Parameter(parm=self.node.parm('transfer_attributes'))
        self.parm_transfer_groups = Parameter(parm=self.node.parm('transfer_groups'))
        self.parm_apply_style_sheets = Parameter(parm=self.node.parm('apply_style_sheets'))
        self.parm_scene_style_sheet = Parameter(parm=self.node.parm('scene_style_sheet'))
        self.parm_obj_style_sheet = Parameter(parm=self.node.parm('obj_style_sheet'))

        
        # parm menu vars:
        self.parm_detail_attributes = DetailAttributesMenu(parm=self.node.parm('detail_attributes'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class DetailAttributesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_promotion = 0
        self.menu_promote_to_primitive_attributes = 1
        self.menu_promote_to_point_attributes = 2
        self.menu_promote_to_vertex_attributes = 3



