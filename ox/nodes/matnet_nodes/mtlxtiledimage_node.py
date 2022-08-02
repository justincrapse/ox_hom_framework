from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxtiledimageNode(OXNode):
    node_type = 'mtlxtiledimage'
    parm_lookup_dict = {'signature': 'signature', 'file': 'file', 'filecolorspace': 'filecolorspace', 'default': 'default', 'texcoordx': 'texcoordx', 'texcoordy': 'texcoordy', 'uvtilingx': 'uvtilingx', 'uvtilingy': 'uvtilingy', 'uvoffsetx': 'uvoffsetx', 'uvoffsety': 'uvoffsety', 'realworldimagesizex': 'realworldimagesizex', 'realworldimagesizey': 'realworldimagesizey', 'realworldtilesizex': 'realworldtilesizex', 'realworldtilesizey': 'realworldtilesizey', 'filtertype': 'filtertype', 'framerange': 'framerange', 'frameoffset': 'frameoffset', 'frameendaction': 'frameendaction', 'default_color3r': 'default_color3r', 'default_color3g': 'default_color3g', 'default_color3b': 'default_color3b', 'default_color4r': 'default_color4r', 'default_color4g': 'default_color4g', 'default_color4b': 'default_color4b', 'default_color4a': 'default_color4a', 'default_vector2x': 'default_vector2x', 'default_vector2y': 'default_vector2y', 'default_vector3x': 'default_vector3x', 'default_vector3y': 'default_vector3y', 'default_vector3z': 'default_vector3z', 'default_vector4x': 'default_vector4x', 'default_vector4y': 'default_vector4y', 'default_vector4z': 'default_vector4z', 'default_vector4w': 'default_vector4w'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_file = Parameter(parm=self.node.parm('file'))
        self.parm_default = Parameter(parm=self.node.parm('default'))
        self.parm_texcoordx = Parameter(parm=self.node.parm('texcoordx'))
        self.parm_texcoordy = Parameter(parm=self.node.parm('texcoordy'))
        self.parm_uvtilingx = Parameter(parm=self.node.parm('uvtilingx'))
        self.parm_uvtilingy = Parameter(parm=self.node.parm('uvtilingy'))
        self.parm_uvoffsetx = Parameter(parm=self.node.parm('uvoffsetx'))
        self.parm_uvoffsety = Parameter(parm=self.node.parm('uvoffsety'))
        self.parm_realworldimagesizex = Parameter(parm=self.node.parm('realworldimagesizex'))
        self.parm_realworldimagesizey = Parameter(parm=self.node.parm('realworldimagesizey'))
        self.parm_realworldtilesizex = Parameter(parm=self.node.parm('realworldtilesizex'))
        self.parm_realworldtilesizey = Parameter(parm=self.node.parm('realworldtilesizey'))
        self.parm_framerange = Parameter(parm=self.node.parm('framerange'))
        self.parm_frameoffset = Parameter(parm=self.node.parm('frameoffset'))
        self.parm_default_color3r = Parameter(parm=self.node.parm('default_color3r'))
        self.parm_default_color3g = Parameter(parm=self.node.parm('default_color3g'))
        self.parm_default_color3b = Parameter(parm=self.node.parm('default_color3b'))
        self.parm_default_color4r = Parameter(parm=self.node.parm('default_color4r'))
        self.parm_default_color4g = Parameter(parm=self.node.parm('default_color4g'))
        self.parm_default_color4b = Parameter(parm=self.node.parm('default_color4b'))
        self.parm_default_color4a = Parameter(parm=self.node.parm('default_color4a'))
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
        self.parm_filecolorspace = FilecolorspaceMenu(parm=self.node.parm('filecolorspace'))
        self.parm_filtertype = FiltertypeMenu(parm=self.node.parm('filtertype'))
        self.parm_frameendaction = FrameendactionMenu(parm=self.node.parm('frameendaction'))


        # input vars:
        self.input_default = 'Default'
        self.input_texcoord = 'Texcoord'
        self.input_uvtiling = 'Uvtiling'
        self.input_uvoffset = 'Uvoffset'
        self.input_realworldimagesize = 'Realworldimagesize'
        self.input_realworldtilesize = 'Realworldtilesize'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = "default"
        self.menu_color = "color3"
        self.menu_color_4 = "color4"
        self.menu_vector_2 = "vector2"
        self.menu_vector_3 = "vector3"
        self.menu_vector_4 = "vector4"


class FilecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear___rec_709 = "lin_rec709"
        self.menu_linear_texture___srgb = "srgb_texture"


class FiltertypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_closest = "closest"
        self.menu_linear = "linear"
        self.menu_cubic = "cubic"


class FrameendactionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_clamp = "clamp"
        self.menu_periodic = "periodic"
        self.menu_mirror = "mirror"



