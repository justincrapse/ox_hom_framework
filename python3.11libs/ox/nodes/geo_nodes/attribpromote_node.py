from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AttribpromoteNode(OXNode):
    node_type = 'attribpromote'
    parm_lookup_dict = {'inname': 'inname', 'inclass': 'inclass', 'outclass': 'outclass', 'usepieceattrib': 'usepieceattrib', 'pieceattrib': 'pieceattrib', 'method': 'method', 'useoutname': 'useoutname', 'outname': 'outname', 'deletein': 'deletein'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_usepieceattrib = Parameter(parm=self.node.parm('usepieceattrib'))
        self.parm_useoutname = Parameter(parm=self.node.parm('useoutname'))
        self.parm_outname = Parameter(parm=self.node.parm('outname'))
        self.parm_deletein = Parameter(parm=self.node.parm('deletein'))

        
        # parm menu vars:
        self.parm_inname = InnameMenu(parm=self.node.parm('inname'))
        self.parm_inclass = InclassMenu(parm=self.node.parm('inclass'))
        self.parm_outclass = OutclassMenu(parm=self.node.parm('outclass'))
        self.parm_pieceattrib = PieceattribMenu(parm=self.node.parm('pieceattrib'))
        self.parm_method = MethodMenu(parm=self.node.parm('method'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class InnameMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_color__cd_ = ("Cd", 0)
        self.menu_position__p_ = ("P", 1)
        self.menu_cog_index = ("cog_index", 2)
        self.menu_fbx_custom_attributes = ("fbx_custom_attributes", 3)
        self.menu_name = ("name", 4)
        self.menu_path = ("path", 5)
        self.menu_scaleinheritance = ("scaleinheritance", 6)
        self.menu_start_pos = ("start_pos", 7)
        self.menu_transform = ("transform", 8)
        self.menu_y_offset = ("y_offset", 9)


class InclassMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_detail = ("detail", 0)
        self.menu_primitive = ("primitive", 1)
        self.menu_point = ("point", 2)
        self.menu_vertex = ("vertex", 3)


class OutclassMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_detail = ("detail", 0)
        self.menu_primitive = ("primitive", 1)
        self.menu_point = ("point", 2)
        self.menu_vertex = ("vertex", 3)


class PieceattribMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_clipinfo = ("clipinfo", 0)
        self.menu_cog_index = ("cog_index", 1)


class MethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_maximum = ("max", 0)
        self.menu_minimum = ("min", 1)
        self.menu_average = ("mean", 2)
        self.menu_mode = ("mode", 3)
        self.menu_median = ("median", 4)
        self.menu_sum = ("sum", 5)
        self.menu_sum_of_squares = ("sumsquare", 6)
        self.menu_root_mean_square = ("rms", 7)
        self.menu_first_match = ("first", 8)
        self.menu_last_match = ("last", 9)
        self.menu_array_of_all = ("array", 10)



