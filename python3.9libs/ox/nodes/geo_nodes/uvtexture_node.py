from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class UvtextureNode(OXNode):
    node_type = 'texture'
    parm_lookup_dict = {'uvattrib': 'uvattrib', 'group': 'group', 'type': 'type', 'axis': 'axis', 'campath': 'campath', 'coord': 'coord', 'su': 'su', 'sv': 'sv', 'sw': 'sw', 'offsetu': 'offsetu', 'offsetv': 'offsetv', 'offsetw': 'offsetw', 'angle': 'angle', 'fixseams': 'fixseams'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_uvattrib = Parameter(parm=self.node.parm('uvattrib'))
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_campath = Parameter(parm=self.node.parm('campath'))
        self.parm_su = Parameter(parm=self.node.parm('su'))
        self.parm_sv = Parameter(parm=self.node.parm('sv'))
        self.parm_sw = Parameter(parm=self.node.parm('sw'))
        self.parm_offsetu = Parameter(parm=self.node.parm('offsetu'))
        self.parm_offsetv = Parameter(parm=self.node.parm('offsetv'))
        self.parm_offsetw = Parameter(parm=self.node.parm('offsetw'))
        self.parm_angle = Parameter(parm=self.node.parm('angle'))
        self.parm_fixseams = Parameter(parm=self.node.parm('fixseams'))

        
        # parm menu vars:
        self.parm_type = TypeMenu(parm=self.node.parm('type'))
        self.parm_axis = AxisMenu(parm=self.node.parm('axis'))
        self.parm_coord = CoordMenu(parm=self.node.parm('coord'))


        # input vars:
        self.input_texture_source = 'Texture source'


# parm menu classes:
class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_orthographic = ("texture", 0)
        self.menu_polar = ("polar", 1)
        self.menu_cylindrical = ("cylin", 2)
        self.menu_rows___columns = ("rowcol", 3)
        self.menu_face = ("face", 4)
        self.menu_modify_source = ("modify", 5)
        self.menu_uniform_spline = ("suniform", 6)
        self.menu_average_spline = ("saverage", 7)
        self.menu_arc_length_spline = ("sarclen", 8)
        self.menu_perspective_from_camera = ("persp", 9)


class AxisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_axis = ("x", 0)
        self.menu_y_axis = ("y", 1)
        self.menu_z_axis = ("z", 2)


class CoordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto_select = ("natural", 0)
        self.menu_point = ("point", 1)
        self.menu_vertex = ("vertex", 2)



