from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldNode(OXNode):
    node_type = 'heightfield'
    parm_lookup_dict = {'orient': 'orient', 'sampling': 'sampling', 'initialheight': 'initialheight', 'initialmask': 'initialmask', 'divisionmode': 'divisionmode', 'gridspacing': 'gridspacing', 'gridsamples': 'gridsamples', 'scale': 'scale', 'sizex': 'sizex', 'sizey': 'sizey', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_initialheight = Parameter(parm=self.node.parm('initialheight'))
        self.parm_initialmask = Parameter(parm=self.node.parm('initialmask'))
        self.parm_gridspacing = Parameter(parm=self.node.parm('gridspacing'))
        self.parm_gridsamples = Parameter(parm=self.node.parm('gridsamples'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_sizex = Parameter(parm=self.node.parm('sizex'))
        self.parm_sizey = Parameter(parm=self.node.parm('sizey'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))

        
        # parm menu vars:
        self.parm_orient = OrientMenu(parm=self.node.parm('orient'))
        self.parm_sampling = SamplingMenu(parm=self.node.parm('sampling'))
        self.parm_divisionmode = DivisionmodeMenu(parm=self.node.parm('divisionmode'))


        # input vars:


# parm menu classes:
class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_xy = ("xy", 0)
        self.menu_yz = ("yz", 1)
        self.menu_zx = ("zx", 2)


class SamplingMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_center = ("center", 0)
        self.menu_corner = ("corner", 1)


class DivisionmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_by_axis = ("maxaxis", 0)
        self.menu_by_size = ("size", 1)



