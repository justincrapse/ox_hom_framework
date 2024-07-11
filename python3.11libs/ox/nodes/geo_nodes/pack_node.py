from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class PackNode(OXNode):
    node_type = 'pack'
    parm_lookup_dict = {'viewportlod': 'viewportlod', 'createpath': 'createpath', 'path': 'path', 'packbyname': 'packbyname', 'nameattribute': 'nameattribute', 'packedfragments': 'packedfragments', 'pivot': 'pivot', 'transfer_attributes': 'transfer_attributes', 'transfer_groups': 'transfer_groups'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_createpath = Parameter(parm=self.node.parm('createpath'))
        self.parm_path = Parameter(parm=self.node.parm('path'))
        self.parm_packbyname = Parameter(parm=self.node.parm('packbyname'))
        self.parm_nameattribute = Parameter(parm=self.node.parm('nameattribute'))
        self.parm_packedfragments = Parameter(parm=self.node.parm('packedfragments'))
        self.parm_transfer_groups = Parameter(parm=self.node.parm('transfer_groups'))

        
        # parm menu vars:
        self.parm_viewportlod = ViewportlodMenu(parm=self.node.parm('viewportlod'))
        self.parm_pivot = PivotMenu(parm=self.node.parm('pivot'))
        self.parm_transfer_attributes = TransferAttributesMenu(parm=self.node.parm('transfer_attributes'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = ("full", 0)
        self.menu_point_cloud = ("points", 1)
        self.menu_bounding_box = ("box", 2)
        self.menu_centroid = ("centroid", 3)
        self.menu_hidden = ("hidden", 4)


class PivotMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_origin = ("origin", 0)
        self.menu_centroid = ("centroid", 1)


class TransferAttributesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_alpha = ("Alpha", 0)
        self.menu_cd = ("Cd", 1)
        self.menu_n = ("N", 2)
        self.menu_class_alt = ("class", 3)
        self.menu_name = ("name", 4)
        self.menu_shop_materialpath = ("shop_materialpath", 5)
        self.menu_uv = ("uv", 6)
        self.menu_uv2 = ("uv2", 7)



