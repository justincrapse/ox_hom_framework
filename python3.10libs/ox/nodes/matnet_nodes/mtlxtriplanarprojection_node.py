from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxtriplanarprojectionNode(OXNode):
    node_type = 'mtlxtriplanarprojection'
    parm_lookup_dict = {'signature': 'signature', 'filex': 'filex', 'filexcolorspace': 'filexcolorspace', 'filey': 'filey', 'fileycolorspace': 'fileycolorspace', 'filez': 'filez', 'filezcolorspace': 'filezcolorspace', 'layerx': 'layerx', 'layery': 'layery', 'layerz': 'layerz', 'default': 'default', 'default_color3r': 'default_color3r', 'default_color3g': 'default_color3g', 'default_color3b': 'default_color3b', 'default_color4r': 'default_color4r', 'default_color4g': 'default_color4g', 'default_color4b': 'default_color4b', 'default_color4a': 'default_color4a', 'default_vector2x': 'default_vector2x', 'default_vector2y': 'default_vector2y', 'default_vector3x': 'default_vector3x', 'default_vector3y': 'default_vector3y', 'default_vector3z': 'default_vector3z', 'default_vector4x': 'default_vector4x', 'default_vector4y': 'default_vector4y', 'default_vector4z': 'default_vector4z', 'default_vector4w': 'default_vector4w', 'positionx': 'positionx', 'positiony': 'positiony', 'positionz': 'positionz', 'normalx': 'normalx', 'normaly': 'normaly', 'normalz': 'normalz', 'upaxis': 'upaxis', 'blend': 'blend', 'filtertype': 'filtertype', 'framerange': 'framerange', 'frameoffset': 'frameoffset', 'frameendaction': 'frameendaction'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_layerx = Parameter(parm=self.node.parm('layerx'))
        self.parm_layery = Parameter(parm=self.node.parm('layery'))
        self.parm_layerz = Parameter(parm=self.node.parm('layerz'))
        self.parm_default = Parameter(parm=self.node.parm('default'))
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
        self.parm_positionx = Parameter(parm=self.node.parm('positionx'))
        self.parm_positiony = Parameter(parm=self.node.parm('positiony'))
        self.parm_positionz = Parameter(parm=self.node.parm('positionz'))
        self.parm_normalx = Parameter(parm=self.node.parm('normalx'))
        self.parm_normaly = Parameter(parm=self.node.parm('normaly'))
        self.parm_normalz = Parameter(parm=self.node.parm('normalz'))
        self.parm_blend = Parameter(parm=self.node.parm('blend'))
        self.parm_framerange = Parameter(parm=self.node.parm('framerange'))
        self.parm_frameoffset = Parameter(parm=self.node.parm('frameoffset'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))
        self.parm_filex = FilexMenu(parm=self.node.parm('filex'))
        self.parm_filexcolorspace = FilexcolorspaceMenu(parm=self.node.parm('filexcolorspace'))
        self.parm_filey = FileyMenu(parm=self.node.parm('filey'))
        self.parm_fileycolorspace = FileycolorspaceMenu(parm=self.node.parm('fileycolorspace'))
        self.parm_filez = FilezMenu(parm=self.node.parm('filez'))
        self.parm_filezcolorspace = FilezcolorspaceMenu(parm=self.node.parm('filezcolorspace'))
        self.parm_upaxis = UpaxisMenu(parm=self.node.parm('upaxis'))
        self.parm_filtertype = FiltertypeMenu(parm=self.node.parm('filtertype'))
        self.parm_frameendaction = FrameendactionMenu(parm=self.node.parm('frameendaction'))


        # input vars:
        self.input_filex = 'Filex'
        self.input_filey = 'Filey'
        self.input_filez = 'Filez'
        self.input_layerx = 'Layerx'
        self.input_layery = 'Layery'
        self.input_layerz = 'Layerz'
        self.input_default = 'Default'
        self.input_position = 'Position'
        self.input_normal = 'Normal'
        self.input_upaxis = 'Upaxis'
        self.input_blend = 'Blend'
        self.input_filtertype = 'Filtertype'
        self.input_framerange = 'Framerange'
        self.input_frameoffset = 'Frameoffset'
        self.input_frameendaction = 'Frameendaction'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = ("default", 0)
        self.menu_color = ("color3", 1)
        self.menu_color_4 = ("color4", 2)
        self.menu_vector_2 = ("vector2", 3)
        self.menu_vector_3 = ("vector3", 4)
        self.menu_vector_4 = ("vector4", 5)


class FilexMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_op__obj_cop2net1_out_roughness = ("op:/obj/cop2net1/OUT_Roughness", 0)
        self.menu_op__obj_cop2net1_out_ = ("op:/obj/cop2net1/OUT_", 1)
        self.menu_op__obj_cop2net1_out_normal = ("op:/obj/cop2net1/OUT_Normal", 2)
        self.menu_op__obj_cop2net1_out_metallic = ("op:/obj/cop2net1/OUT_Metallic", 3)
        self.menu_op__obj_cop2net1_out_height = ("op:/obj/cop2net1/OUT_Height", 4)
        self.menu_op__obj_cop2net1_out_glossiness = ("op:/obj/cop2net1/OUT_Glossiness", 5)
        self.menu_op__obj_cop2net1_out_specular = ("op:/obj/cop2net1/OUT_Specular", 6)
        self.menu_op__obj_cop2net1_out_diffuse = ("op:/obj/cop2net1/OUT_Diffuse", 7)
        self.menu_op__obj_cop2net1_out_diffuse_ = ("op:/obj/cop2net1/OUT_Diffuse/", 8)
        self.menu_op__obj_cop2net1_out = ("op:/obj/cop2net1/OUT", 9)
        self.menu_op__obj_cop2net1___channel_diffuse_ = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_diffuse/", 10)
        self.menu_op__obj_cop2net1____channel_diffuse = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_diffuse", 11)
        self.menu_op__obj_cop2net1_out_ = ("op:/obj/cop2net1/OUT/", 12)
        self.menu_op__obj_cop2net1___ode_out_diffuse_ = ("op:/obj/cop2net1/limestone_cliff_rock_cop2net_node/OUT_Diffuse/", 13)
        self.menu_op__obj_cop2net1_out_c = ("op:/obj/cop2net1/OUT/C", 14)
        self.menu_op__obj_cop2net2____channel_diffuse = ("op:/obj/cop2net2/sbs_archive1/sbs_channel_diffuse", 15)
        self.menu_op__obj_cop2net1___s_channel_normal = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_normal", 16)
        self.menu_op__obj_cop2net1___hannel_basecolor = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_basecolor", 17)
        self.menu_op__obj_cop2net1___node_out_diffuse = ("op:/obj/cop2net1/limestone_cliff_rock_cop2net_node/OUT_Diffuse", 18)
        self.menu_op__obj_cop2net1_sbs_archive1_ = ("op:/obj/cop2net1/sbs_archive1/", 19)
        self.menu_op__obj_ = ("op:/obj/", 20)
        self.menu_op__obj_cop2net1_sbs_archive1 = ("op:/obj/cop2net1/sbs_archive1", 21)


class FilexcolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_srgb___texture = ("srgb_tx", 0)
        self.menu_acescg = ("ACEScg", 1)
        self.menu_linear_rec_709__srgb_ = ("lin_rec709", 2)
        self.menu_raw = ("Raw", 3)


class FileyMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_op__obj_cop2net1_out_roughness = ("op:/obj/cop2net1/OUT_Roughness", 0)
        self.menu_op__obj_cop2net1_out_ = ("op:/obj/cop2net1/OUT_", 1)
        self.menu_op__obj_cop2net1_out_normal = ("op:/obj/cop2net1/OUT_Normal", 2)
        self.menu_op__obj_cop2net1_out_metallic = ("op:/obj/cop2net1/OUT_Metallic", 3)
        self.menu_op__obj_cop2net1_out_height = ("op:/obj/cop2net1/OUT_Height", 4)
        self.menu_op__obj_cop2net1_out_glossiness = ("op:/obj/cop2net1/OUT_Glossiness", 5)
        self.menu_op__obj_cop2net1_out_specular = ("op:/obj/cop2net1/OUT_Specular", 6)
        self.menu_op__obj_cop2net1_out_diffuse = ("op:/obj/cop2net1/OUT_Diffuse", 7)
        self.menu_op__obj_cop2net1_out_diffuse_ = ("op:/obj/cop2net1/OUT_Diffuse/", 8)
        self.menu_op__obj_cop2net1_out = ("op:/obj/cop2net1/OUT", 9)
        self.menu_op__obj_cop2net1___channel_diffuse_ = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_diffuse/", 10)
        self.menu_op__obj_cop2net1____channel_diffuse = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_diffuse", 11)
        self.menu_op__obj_cop2net1_out_ = ("op:/obj/cop2net1/OUT/", 12)
        self.menu_op__obj_cop2net1___ode_out_diffuse_ = ("op:/obj/cop2net1/limestone_cliff_rock_cop2net_node/OUT_Diffuse/", 13)
        self.menu_op__obj_cop2net1_out_c = ("op:/obj/cop2net1/OUT/C", 14)
        self.menu_op__obj_cop2net2____channel_diffuse = ("op:/obj/cop2net2/sbs_archive1/sbs_channel_diffuse", 15)
        self.menu_op__obj_cop2net1___s_channel_normal = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_normal", 16)
        self.menu_op__obj_cop2net1___hannel_basecolor = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_basecolor", 17)
        self.menu_op__obj_cop2net1___node_out_diffuse = ("op:/obj/cop2net1/limestone_cliff_rock_cop2net_node/OUT_Diffuse", 18)
        self.menu_op__obj_cop2net1_sbs_archive1_ = ("op:/obj/cop2net1/sbs_archive1/", 19)
        self.menu_op__obj_ = ("op:/obj/", 20)
        self.menu_op__obj_cop2net1_sbs_archive1 = ("op:/obj/cop2net1/sbs_archive1", 21)


class FileycolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_srgb___texture = ("srgb_tx", 0)
        self.menu_acescg = ("ACEScg", 1)
        self.menu_linear_rec_709__srgb_ = ("lin_rec709", 2)
        self.menu_raw = ("Raw", 3)


class FilezMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_op__obj_cop2net1_out_roughness = ("op:/obj/cop2net1/OUT_Roughness", 0)
        self.menu_op__obj_cop2net1_out_ = ("op:/obj/cop2net1/OUT_", 1)
        self.menu_op__obj_cop2net1_out_normal = ("op:/obj/cop2net1/OUT_Normal", 2)
        self.menu_op__obj_cop2net1_out_metallic = ("op:/obj/cop2net1/OUT_Metallic", 3)
        self.menu_op__obj_cop2net1_out_height = ("op:/obj/cop2net1/OUT_Height", 4)
        self.menu_op__obj_cop2net1_out_glossiness = ("op:/obj/cop2net1/OUT_Glossiness", 5)
        self.menu_op__obj_cop2net1_out_specular = ("op:/obj/cop2net1/OUT_Specular", 6)
        self.menu_op__obj_cop2net1_out_diffuse = ("op:/obj/cop2net1/OUT_Diffuse", 7)
        self.menu_op__obj_cop2net1_out_diffuse_ = ("op:/obj/cop2net1/OUT_Diffuse/", 8)
        self.menu_op__obj_cop2net1_out = ("op:/obj/cop2net1/OUT", 9)
        self.menu_op__obj_cop2net1___channel_diffuse_ = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_diffuse/", 10)
        self.menu_op__obj_cop2net1____channel_diffuse = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_diffuse", 11)
        self.menu_op__obj_cop2net1_out_ = ("op:/obj/cop2net1/OUT/", 12)
        self.menu_op__obj_cop2net1___ode_out_diffuse_ = ("op:/obj/cop2net1/limestone_cliff_rock_cop2net_node/OUT_Diffuse/", 13)
        self.menu_op__obj_cop2net1_out_c = ("op:/obj/cop2net1/OUT/C", 14)
        self.menu_op__obj_cop2net2____channel_diffuse = ("op:/obj/cop2net2/sbs_archive1/sbs_channel_diffuse", 15)
        self.menu_op__obj_cop2net1___s_channel_normal = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_normal", 16)
        self.menu_op__obj_cop2net1___hannel_basecolor = ("op:/obj/cop2net1/sbs_archive1/sbs_channel_basecolor", 17)
        self.menu_op__obj_cop2net1___node_out_diffuse = ("op:/obj/cop2net1/limestone_cliff_rock_cop2net_node/OUT_Diffuse", 18)
        self.menu_op__obj_cop2net1_sbs_archive1_ = ("op:/obj/cop2net1/sbs_archive1/", 19)
        self.menu_op__obj_ = ("op:/obj/", 20)
        self.menu_op__obj_cop2net1_sbs_archive1 = ("op:/obj/cop2net1/sbs_archive1", 21)


class FilezcolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_srgb___texture = ("srgb_tx", 0)
        self.menu_acescg = ("ACEScg", 1)
        self.menu_linear_rec_709__srgb_ = ("lin_rec709", 2)
        self.menu_raw = ("Raw", 3)


class UpaxisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x = ("0", 0)
        self.menu_y = ("1", 1)
        self.menu_z = ("2", 2)


class FiltertypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_closest = ("closest", 0)
        self.menu_linear = ("linear", 1)
        self.menu_cubic = ("cubic", 2)


class FrameendactionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_clamp = ("clamp", 1)
        self.menu_periodic = ("periodic", 2)
        self.menu_mirror = ("mirror", 3)



