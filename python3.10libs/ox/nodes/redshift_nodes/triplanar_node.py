from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class TriplanarNode(OXNode):
    node_type = 'redshift::TriPlanar'
    parm_lookup_dict = {'islefthanded': 'isLeftHanded', 'yisup': 'yIsUp', 'texture_0': 'Texture_0', 'sameimageoneachaxis': 'sameImageOnEachAxis', 'imagexr': 'imageXr', 'imagexg': 'imageXg', 'imagexb': 'imageXb', 'imagexa': 'imageXa', 'imageyr': 'imageYr', 'imageyg': 'imageYg', 'imageyb': 'imageYb', 'imageya': 'imageYa', 'imagezr': 'imageZr', 'imagezg': 'imageZg', 'imagezb': 'imageZb', 'imageza': 'imageZa', 'blendamount': 'blendAmount', 'blendcurve': 'blendCurve', 'coordinates_1': 'Coordinates_1', 'scale1': 'scale1', 'scale2': 'scale2', 'scale3': 'scale3', 'offset1': 'offset1', 'offset2': 'offset2', 'offset3': 'offset3', 'rotation1': 'rotation1', 'rotation2': 'rotation2', 'rotation3': 'rotation3', 'projspacetype': 'projSpaceType', 'shader_skipdefvalparms': 'shader_skipdefvalparms'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_islefthanded = Parameter(parm=self.node.parm('isLeftHanded'))
        self.parm_yisup = Parameter(parm=self.node.parm('yIsUp'))
        self.parm_texture_0 = Parameter(parm=self.node.parm('Texture_0'))
        self.parm_sameimageoneachaxis = Parameter(parm=self.node.parm('sameImageOnEachAxis'))
        self.parm_imagexr = Parameter(parm=self.node.parm('imageXr'))
        self.parm_imagexg = Parameter(parm=self.node.parm('imageXg'))
        self.parm_imagexb = Parameter(parm=self.node.parm('imageXb'))
        self.parm_imagexa = Parameter(parm=self.node.parm('imageXa'))
        self.parm_imageyr = Parameter(parm=self.node.parm('imageYr'))
        self.parm_imageyg = Parameter(parm=self.node.parm('imageYg'))
        self.parm_imageyb = Parameter(parm=self.node.parm('imageYb'))
        self.parm_imageya = Parameter(parm=self.node.parm('imageYa'))
        self.parm_imagezr = Parameter(parm=self.node.parm('imageZr'))
        self.parm_imagezg = Parameter(parm=self.node.parm('imageZg'))
        self.parm_imagezb = Parameter(parm=self.node.parm('imageZb'))
        self.parm_imageza = Parameter(parm=self.node.parm('imageZa'))
        self.parm_blendamount = Parameter(parm=self.node.parm('blendAmount'))
        self.parm_blendcurve = Parameter(parm=self.node.parm('blendCurve'))
        self.parm_coordinates_1 = Parameter(parm=self.node.parm('Coordinates_1'))
        self.parm_scale1 = Parameter(parm=self.node.parm('scale1'))
        self.parm_scale2 = Parameter(parm=self.node.parm('scale2'))
        self.parm_scale3 = Parameter(parm=self.node.parm('scale3'))
        self.parm_offset1 = Parameter(parm=self.node.parm('offset1'))
        self.parm_offset2 = Parameter(parm=self.node.parm('offset2'))
        self.parm_offset3 = Parameter(parm=self.node.parm('offset3'))
        self.parm_rotation1 = Parameter(parm=self.node.parm('rotation1'))
        self.parm_rotation2 = Parameter(parm=self.node.parm('rotation2'))
        self.parm_rotation3 = Parameter(parm=self.node.parm('rotation3'))
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))

        
        # parm menu vars:
        self.parm_projspacetype = ProjspacetypeMenu(parm=self.node.parm('projSpaceType'))


        # input vars:
        self.input_imagex = 'imageX'
        self.input_imagey = 'imageY'
        self.input_imagez = 'imageZ'
        self.input_blendamount = 'blendAmount'
        self.input_scale = 'scale'
        self.input_offset = 'offset'
        self.input_rotation = 'rotation'


# parm menu classes:
class ProjspacetypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_world = ("0", 0)
        self.menu_object = ("1", 1)
        self.menu_reference = ("2", 2)



