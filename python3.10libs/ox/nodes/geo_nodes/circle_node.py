from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CircleNode(OXNode):
    node_type = 'circle'
    parm_lookup_dict = {'type': 'type', 'orient': 'orient', 'radx': 'radx', 'rady': 'rady', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'scale': 'scale', 'order': 'order', 'divs': 'divs', 'arc': 'arc', 'beginangle': 'beginangle', 'endangle': 'endangle', 'imperfect': 'imperfect'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_radx = Parameter(parm=self.node.parm('radx'))
        self.parm_rady = Parameter(parm=self.node.parm('rady'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_order = Parameter(parm=self.node.parm('order'))
        self.parm_divs = Parameter(parm=self.node.parm('divs'))
        self.parm_beginangle = Parameter(parm=self.node.parm('beginangle'))
        self.parm_endangle = Parameter(parm=self.node.parm('endangle'))
        self.parm_imperfect = Parameter(parm=self.node.parm('imperfect'))

        
        # parm menu vars:
        self.parm_type = TypeMenu(parm=self.node.parm('type'))
        self.parm_orient = OrientMenu(parm=self.node.parm('orient'))
        self.parm_arc = ArcMenu(parm=self.node.parm('arc'))


        # input vars:


# parm menu classes:
class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitive = ("prim", 0)
        self.menu_polygon = ("poly", 1)
        self.menu_nurbs_curve = ("nurbs", 2)
        self.menu_bezier_curve = ("bezier", 3)


class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_xy_plane = ("xy", 0)
        self.menu_yz_plane = ("yz", 1)
        self.menu_zx_plane = ("zx", 2)


class ArcMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_closed = ("closed", 0)
        self.menu_open_arc = ("openarc", 1)
        self.menu_closed_arc = ("closedarc", 2)
        self.menu_sliced_arc = ("slicedarc", 3)



