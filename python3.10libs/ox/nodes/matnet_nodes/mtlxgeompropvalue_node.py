from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxgeompropvalueNode(OXNode):
    node_type = 'mtlxgeompropvalue'
    parm_lookup_dict = {'signature': 'signature', 'geomprop': 'geomprop', 'default': 'default', 'default_boolean': 'default_boolean', 'default_color3r': 'default_color3r', 'default_color3g': 'default_color3g', 'default_color3b': 'default_color3b', 'default_color4r': 'default_color4r', 'default_color4g': 'default_color4g', 'default_color4b': 'default_color4b', 'default_color4a': 'default_color4a', 'default_integer': 'default_integer', 'default_string': 'default_string', 'default_vector2x': 'default_vector2x', 'default_vector2y': 'default_vector2y', 'default_vector3x': 'default_vector3x', 'default_vector3y': 'default_vector3y', 'default_vector3z': 'default_vector3z', 'default_vector4x': 'default_vector4x', 'default_vector4y': 'default_vector4y', 'default_vector4z': 'default_vector4z', 'default_vector4w': 'default_vector4w'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_geomprop = Parameter(parm=self.node.parm('geomprop'))
        self.parm_default = Parameter(parm=self.node.parm('default'))
        self.parm_default_boolean = Parameter(parm=self.node.parm('default_boolean'))
        self.parm_default_color3r = Parameter(parm=self.node.parm('default_color3r'))
        self.parm_default_color3g = Parameter(parm=self.node.parm('default_color3g'))
        self.parm_default_color3b = Parameter(parm=self.node.parm('default_color3b'))
        self.parm_default_color4r = Parameter(parm=self.node.parm('default_color4r'))
        self.parm_default_color4g = Parameter(parm=self.node.parm('default_color4g'))
        self.parm_default_color4b = Parameter(parm=self.node.parm('default_color4b'))
        self.parm_default_color4a = Parameter(parm=self.node.parm('default_color4a'))
        self.parm_default_integer = Parameter(parm=self.node.parm('default_integer'))
        self.parm_default_string = Parameter(parm=self.node.parm('default_string'))
        self.parm_default_vector2x = Parameter(parm=self.node.parm('default_vector2x'))
        self.parm_default_vector2y = Parameter(parm=self.node.parm('default_vector2y'))
        self.parm_default_vector3x = Parameter(parm=self.node.parm('default_vector3x'))
        self.parm_default_vector3y = Parameter(parm=self.node.parm('default_vector3y'))
        self.parm_default_vector3z = Parameter(parm=self.node.parm('default_vector3z'))
        self.parm_default_vector4x = Parameter(parm=self.node.parm('default_vector4x'))
        self.parm_default_vector4y = Parameter(parm=self.node.parm('default_vector4y'))
        self.parm_default_vector4z = Parameter(parm=self.node.parm('default_vector4z'))
        self.parm_default_vector4w = Parameter(parm=self.node.parm('default_vector4w'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))


        # input vars:
        self.input_default = 'Default'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = ("default", 0)
        self.menu_boolean = ("boolean", 1)
        self.menu_color = ("color3", 2)
        self.menu_color_4 = ("color4", 3)
        self.menu_integer = ("integer", 4)
        self.menu_string = ("string", 5)
        self.menu_vector_2 = ("vector2", 6)
        self.menu_vector_3 = ("vector3", 7)
        self.menu_vector_4 = ("vector4", 8)



