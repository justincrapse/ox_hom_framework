from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AttribcreateNode(OXNode):
    node_type = 'attribcreate::2.0'
    parm_lookup_dict = {'group': 'group', 'grouptype': 'grouptype', 'encodenames': 'encodenames', 'numattr': 'numattr', 'enable1': 'enable1', 'name1': 'name1', 'existing1': 'existing1', 'createvarmap1': 'createvarmap1', 'varname1': 'varname1', 'class1': 'class1', 'savetoinfo1': 'savetoinfo1', 'type1': 'type1', 'typeinfo1': 'typeinfo1', 'precision1': 'precision1', 'size1': 'size1', 'default1v1': 'default1v1', 'default1v2': 'default1v2', 'default1v3': 'default1v3', 'default1v4': 'default1v4', 'writevalues1': 'writevalues1', 'uselocal1': 'uselocal1', 'value1v1': 'value1v1', 'value1v2': 'value1v2', 'value1v3': 'value1v3', 'value1v4': 'value1v4', 'string1': 'string1'}

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
        self.parm_encodenames = Parameter(parm=self.node.parm('encodenames'))
        self.parm_numattr = Parameter(parm=self.node.parm('numattr'))
        self.parm_enable1 = Parameter(parm=self.node.parm('enable1'))
        self.parm_name1 = Parameter(parm=self.node.parm('name1'))
        self.parm_createvarmap1 = Parameter(parm=self.node.parm('createvarmap1'))
        self.parm_varname1 = Parameter(parm=self.node.parm('varname1'))
        self.parm_savetoinfo1 = Parameter(parm=self.node.parm('savetoinfo1'))
        self.parm_size1 = Parameter(parm=self.node.parm('size1'))
        self.parm_default1v1 = Parameter(parm=self.node.parm('default1v1'))
        self.parm_default1v2 = Parameter(parm=self.node.parm('default1v2'))
        self.parm_default1v3 = Parameter(parm=self.node.parm('default1v3'))
        self.parm_default1v4 = Parameter(parm=self.node.parm('default1v4'))
        self.parm_writevalues1 = Parameter(parm=self.node.parm('writevalues1'))
        self.parm_uselocal1 = Parameter(parm=self.node.parm('uselocal1'))
        self.parm_value1v1 = Parameter(parm=self.node.parm('value1v1'))
        self.parm_value1v2 = Parameter(parm=self.node.parm('value1v2'))
        self.parm_value1v3 = Parameter(parm=self.node.parm('value1v3'))
        self.parm_value1v4 = Parameter(parm=self.node.parm('value1v4'))
        self.parm_string1 = Parameter(parm=self.node.parm('string1'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_existing1 = Existing1Menu(parm=self.node.parm('existing1'))
        self.parm_class1 = Class1Menu(parm=self.node.parm('class1'))
        self.parm_type1 = Type1Menu(parm=self.node.parm('type1'))
        self.parm_typeinfo1 = Typeinfo1Menu(parm=self.node.parm('typeinfo1'))
        self.parm_precision1 = Precision1Menu(parm=self.node.parm('precision1'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = "guess"
        self.menu_vertices = "vertices"
        self.menu_edges = "edges"
        self.menu_points = "points"
        self.menu_primitives = "prims"


class Existing1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_generate_error_on_mis_matched_attribute = "error"
        self.menu_generate_warning_on_mis_matched_attribute = "warn"
        self.menu_replace_existing_attribute = "replace"
        self.menu_use_the_better_type__size_and_precision = "better"


class Class1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_detail = "detail"
        self.menu_primitive = "primitive"
        self.menu_point = "point"
        self.menu_vertex = "vertex"


class Type1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = "float"
        self.menu_integer = "int"
        self.menu_vector = "vector"
        self.menu_string = "index"
        self.menu_float_array = "floatarray"
        self.menu_integer_array = "intarray"
        self.menu_string_array = "stringarray"
        self.menu_dictionary = "dict"
        self.menu_dictionary_array = "dictarray"


class Typeinfo1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_name = "guess"
        self.menu_none = "none"
        self.menu_position = "point"
        self.menu_vector = "vector"
        self.menu_normal = "normal"
        self.menu_color = "color"
        self.menu_quaternion = "quaternion"
        self.menu_transform_matrix = "tranform"
        self.menu_texture_coordinate = "texturecoord"


class Precision1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bit_8 = "8"
        self.menu_bit_16 = "16"
        self.menu_bit_32 = "32"
        self.menu_bit_64 = "64"
        self.menu_auto = "auto"



