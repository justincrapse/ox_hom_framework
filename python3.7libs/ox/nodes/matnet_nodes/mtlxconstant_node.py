from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxconstantNode(OXNode):
    node_type = 'mtlxconstant'
    parm_lookup_dict = {'signature': 'signature', 'value': 'value', 'value_boolean': 'value_boolean', 'value_color3r': 'value_color3r', 'value_color3g': 'value_color3g', 'value_color3b': 'value_color3b', 'value_color4r': 'value_color4r', 'value_color4g': 'value_color4g', 'value_color4b': 'value_color4b', 'value_color4a': 'value_color4a', 'value_integer': 'value_integer', 'value_matrix331': 'value_matrix331', 'value_matrix332': 'value_matrix332', 'value_matrix333': 'value_matrix333', 'value_matrix334': 'value_matrix334', 'value_matrix335': 'value_matrix335', 'value_matrix336': 'value_matrix336', 'value_matrix337': 'value_matrix337', 'value_matrix338': 'value_matrix338', 'value_matrix339': 'value_matrix339', 'value_matrix441': 'value_matrix441', 'value_matrix442': 'value_matrix442', 'value_matrix443': 'value_matrix443', 'value_matrix444': 'value_matrix444', 'value_matrix445': 'value_matrix445', 'value_matrix446': 'value_matrix446', 'value_matrix447': 'value_matrix447', 'value_matrix448': 'value_matrix448', 'value_matrix449': 'value_matrix449', 'value_matrix4410': 'value_matrix4410', 'value_matrix4411': 'value_matrix4411', 'value_matrix4412': 'value_matrix4412', 'value_matrix4413': 'value_matrix4413', 'value_matrix4414': 'value_matrix4414', 'value_matrix4415': 'value_matrix4415', 'value_matrix4416': 'value_matrix4416', 'value_string': 'value_string', 'value_vector2x': 'value_vector2x', 'value_vector2y': 'value_vector2y', 'value_vector3x': 'value_vector3x', 'value_vector3y': 'value_vector3y', 'value_vector3z': 'value_vector3z', 'value_vector4x': 'value_vector4x', 'value_vector4y': 'value_vector4y', 'value_vector4z': 'value_vector4z', 'value_vector4w': 'value_vector4w', 'valuecolorspace_filename': 'valuecolorspace_filename', 'value_filename': 'value_filename'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_value = Parameter(parm=self.node.parm('value'))
        self.parm_value_boolean = Parameter(parm=self.node.parm('value_boolean'))
        self.parm_value_color3r = Parameter(parm=self.node.parm('value_color3r'))
        self.parm_value_color3g = Parameter(parm=self.node.parm('value_color3g'))
        self.parm_value_color3b = Parameter(parm=self.node.parm('value_color3b'))
        self.parm_value_color4r = Parameter(parm=self.node.parm('value_color4r'))
        self.parm_value_color4g = Parameter(parm=self.node.parm('value_color4g'))
        self.parm_value_color4b = Parameter(parm=self.node.parm('value_color4b'))
        self.parm_value_color4a = Parameter(parm=self.node.parm('value_color4a'))
        self.parm_value_integer = Parameter(parm=self.node.parm('value_integer'))
        self.parm_value_matrix331 = Parameter(parm=self.node.parm('value_matrix331'))
        self.parm_value_matrix332 = Parameter(parm=self.node.parm('value_matrix332'))
        self.parm_value_matrix333 = Parameter(parm=self.node.parm('value_matrix333'))
        self.parm_value_matrix334 = Parameter(parm=self.node.parm('value_matrix334'))
        self.parm_value_matrix335 = Parameter(parm=self.node.parm('value_matrix335'))
        self.parm_value_matrix336 = Parameter(parm=self.node.parm('value_matrix336'))
        self.parm_value_matrix337 = Parameter(parm=self.node.parm('value_matrix337'))
        self.parm_value_matrix338 = Parameter(parm=self.node.parm('value_matrix338'))
        self.parm_value_matrix339 = Parameter(parm=self.node.parm('value_matrix339'))
        self.parm_value_matrix441 = Parameter(parm=self.node.parm('value_matrix441'))
        self.parm_value_matrix442 = Parameter(parm=self.node.parm('value_matrix442'))
        self.parm_value_matrix443 = Parameter(parm=self.node.parm('value_matrix443'))
        self.parm_value_matrix444 = Parameter(parm=self.node.parm('value_matrix444'))
        self.parm_value_matrix445 = Parameter(parm=self.node.parm('value_matrix445'))
        self.parm_value_matrix446 = Parameter(parm=self.node.parm('value_matrix446'))
        self.parm_value_matrix447 = Parameter(parm=self.node.parm('value_matrix447'))
        self.parm_value_matrix448 = Parameter(parm=self.node.parm('value_matrix448'))
        self.parm_value_matrix449 = Parameter(parm=self.node.parm('value_matrix449'))
        self.parm_value_matrix4410 = Parameter(parm=self.node.parm('value_matrix4410'))
        self.parm_value_matrix4411 = Parameter(parm=self.node.parm('value_matrix4411'))
        self.parm_value_matrix4412 = Parameter(parm=self.node.parm('value_matrix4412'))
        self.parm_value_matrix4413 = Parameter(parm=self.node.parm('value_matrix4413'))
        self.parm_value_matrix4414 = Parameter(parm=self.node.parm('value_matrix4414'))
        self.parm_value_matrix4415 = Parameter(parm=self.node.parm('value_matrix4415'))
        self.parm_value_matrix4416 = Parameter(parm=self.node.parm('value_matrix4416'))
        self.parm_value_string = Parameter(parm=self.node.parm('value_string'))
        self.parm_value_vector2x = Parameter(parm=self.node.parm('value_vector2x'))
        self.parm_value_vector2y = Parameter(parm=self.node.parm('value_vector2y'))
        self.parm_value_vector3x = Parameter(parm=self.node.parm('value_vector3x'))
        self.parm_value_vector3y = Parameter(parm=self.node.parm('value_vector3y'))
        self.parm_value_vector3z = Parameter(parm=self.node.parm('value_vector3z'))
        self.parm_value_vector4x = Parameter(parm=self.node.parm('value_vector4x'))
        self.parm_value_vector4y = Parameter(parm=self.node.parm('value_vector4y'))
        self.parm_value_vector4z = Parameter(parm=self.node.parm('value_vector4z'))
        self.parm_value_vector4w = Parameter(parm=self.node.parm('value_vector4w'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))
        self.parm_valuecolorspace_filename = ValuecolorspaceFilenameMenu(parm=self.node.parm('valuecolorspace_filename'))
        self.parm_value_filename = ValueFilenameMenu(parm=self.node.parm('value_filename'))


        # input vars:
        self.input_value = 'Value'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = 'default'
        self.menu_boolean = 'boolean'
        self.menu_color = 'color3'
        self.menu_color_4 = 'color4'
        self.menu_integer = 'integer'
        self.menu_matrix_3x3 = 'matrix33'
        self.menu_matrix_4x4 = 'matrix44'
        self.menu_string = 'string'
        self.menu_vector_2 = 'vector2'
        self.menu_vector_3 = 'vector3'
        self.menu_vector_4 = 'vector4'
        self.menu_filename = 'filename'


class ValuecolorspaceFilenameMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear___rec_709 = 'lin_rec709'
        self.menu_linear_texture___srgb = 'srgb_texture'


class ValueFilenameMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_products____ic_basecolor_jpg = 'E:/ART/PRODUCTS/OX-MTLX/palmcube_quilted_moleskin_fabric/palmcube_quilted_moleskin_fabric_basecolor.jpg'
        self.menu__hip_hf_rendered___s_grass_mask_jpg = '$HIP/hf_rendered_layers/grass_mask.jpg'
        self.menu__hip_hf_rendered_layers_grass_mask = 'E:/ART/PRODUCTS/OX-Terrain_Textuers/hf_rendered_layers/grass_mask'
        self.menu_op__obj_hf_cop2n___ort1_grass_mask_ = 'op:/obj/hf/cop2net1/sopimport1{grass_mask}'
        self.menu_op__obj_cop2net1___ive1_base_color_ = 'op:/obj/cop2net1/sbs_archive1{Base Color}'
        self.menu_e__art_projects____oon_grass_4k_exr = 'E:/ART/PROJECTS/00_shared/hdri/noon_grass_4k.exr'
        self.menu_e__art_projects____quarry_02_4k_exr = 'E:/ART/PROJECTS/00_shared/hdri/quarry_02_4k.exr'
        self.menu_e__art_projects____anga_veld_4k_exr = 'E:/ART/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr'
        self.menu_e__art_projects____enheim_05_4k_exr = 'E:/ART/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr'
        self.menu_e__art_projects____ly_cloudy_4k_exr = 'E:/ART/PROJECTS/00_shared/hdri/kloofendal_48d_partly_cloudy_4k.exr'
        self.menu_e__art_projects____in_cellar_4k_exr = 'E:/ART/PROJECTS/00_shared/hdri/castle_zavelstein_cellar_4k.exr'
        self.menu_e__art_projects_____1d_clear_4k_exr = 'E:/ART/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr'



