from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RasterizesetupNode(OXNode):
    node_type = 'rasterizesetup'
    parm_lookup_dict = {'space': 'space', 'orient': 'orient', 'fit': 'fit', 'refsizex': 'refsizex', 'refsizey': 'refsizey', 'refsizez': 'refsizez', 'refposx': 'refposx', 'refposy': 'refposy', 'refposz': 'refposz', 'targetposx': 'targetposx', 'targetposy': 'targetposy', 'targetposz': 'targetposz', 'targetsizex': 'targetsizex', 'targetsizey': 'targetsizey', 'targetsizez': 'targetsizez', 'doscale': 'doscale', 'dofitdepth': 'dofitdepth', 'fitdepthx': 'fitdepthx', 'fitdepthy': 'fitdepthy', 'uvattrib': 'uvattrib', 'addnormal': 'addnormal', 'adddepth': 'adddepth', 'depthattrib': 'depthattrib', 'origpattrib': 'origpattrib'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_refsizex = Parameter(parm=self.node.parm('refsizex'))
        self.parm_refsizey = Parameter(parm=self.node.parm('refsizey'))
        self.parm_refsizez = Parameter(parm=self.node.parm('refsizez'))
        self.parm_refposx = Parameter(parm=self.node.parm('refposx'))
        self.parm_refposy = Parameter(parm=self.node.parm('refposy'))
        self.parm_refposz = Parameter(parm=self.node.parm('refposz'))
        self.parm_targetposx = Parameter(parm=self.node.parm('targetposx'))
        self.parm_targetposy = Parameter(parm=self.node.parm('targetposy'))
        self.parm_targetposz = Parameter(parm=self.node.parm('targetposz'))
        self.parm_targetsizex = Parameter(parm=self.node.parm('targetsizex'))
        self.parm_targetsizey = Parameter(parm=self.node.parm('targetsizey'))
        self.parm_targetsizez = Parameter(parm=self.node.parm('targetsizez'))
        self.parm_doscale = Parameter(parm=self.node.parm('doscale'))
        self.parm_dofitdepth = Parameter(parm=self.node.parm('dofitdepth'))
        self.parm_fitdepthx = Parameter(parm=self.node.parm('fitdepthx'))
        self.parm_fitdepthy = Parameter(parm=self.node.parm('fitdepthy'))
        self.parm_uvattrib = Parameter(parm=self.node.parm('uvattrib'))
        self.parm_addnormal = Parameter(parm=self.node.parm('addnormal'))
        self.parm_adddepth = Parameter(parm=self.node.parm('adddepth'))
        self.parm_depthattrib = Parameter(parm=self.node.parm('depthattrib'))
        self.parm_origpattrib = Parameter(parm=self.node.parm('origpattrib'))

        
        # parm menu vars:
        self.parm_space = SpaceMenu(parm=self.node.parm('space'))
        self.parm_orient = OrientMenu(parm=self.node.parm('orient'))
        self.parm_fit = FitMenu(parm=self.node.parm('fit'))


        # input vars:
        self.input_source = 'source'


# parm menu classes:
class SpaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_position = ("pos", 0)
        self.menu_uvs = ("uv", 1)


class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_y_up = ("yup", 0)
        self.menu_z_up = ("zup", 1)


class FitMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_fitting = ("none", 0)
        self.menu_bounding_box = ("bbox", 1)
        self.menu_reference_box = ("refbox", 2)



