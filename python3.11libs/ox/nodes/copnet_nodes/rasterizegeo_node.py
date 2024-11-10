from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RasterizegeoNode(OXNode):
    node_type = 'rasterizegeo'
    parm_lookup_dict = {'quicksetup': 'quicksetup', 'attributes': 'attributes', 'outtype1': 'outtype1', 'name1': 'name1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_attributes = Parameter(parm=self.node.parm('attributes'))
        self.parm_name1 = Parameter(parm=self.node.parm('name1'))

        
        # parm menu vars:
        self.parm_quicksetup = QuicksetupMenu(parm=self.node.parm('quicksetup'))
        self.parm_outtype1 = Outtype1Menu(parm=self.node.parm('outtype1'))


        # input vars:
        self.input_camera_ref = 'camera_ref'
        self.input_geometry = 'geometry'


# parm menu classes:
class QuicksetupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_quick_setups__ = ("menu", 0)
        self.menu_add_alpha = ("alpha", 1)
        self.menu_add_position = ("position", 2)
        self.menu_add_normal = ("normal", 3)
        self.menu_add_uv = ("uv", 4)
        self.menu_add_depth_from_eye = ("deptheye", 5)


class Outtype1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mono = ("float", 0)
        self.menu_uv = ("vector2", 1)
        self.menu_rgb = ("vector3", 2)
        self.menu_rgba = ("vector4", 3)
        self.menu_id = ("int", 4)



