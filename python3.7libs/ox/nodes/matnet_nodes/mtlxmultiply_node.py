from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxmultiplyNode(OXNode):
    node_type = 'mtlxmultiply'
    parm_lookup_dict = {'signature': 'signature', 'in1': 'in1', 'in2': 'in2', 'in1_bsdfc': 'in1_bsdfC', 'in2_bsdfcr': 'in2_bsdfCr', 'in2_bsdfcg': 'in2_bsdfCg', 'in2_bsdfcb': 'in2_bsdfCb', 'in1_bsdff': 'in1_bsdfF', 'in1_color3r': 'in1_color3r', 'in1_color3g': 'in1_color3g', 'in1_color3b': 'in1_color3b', 'in2_color3r': 'in2_color3r', 'in2_color3g': 'in2_color3g', 'in2_color3b': 'in2_color3b', 'in1_color3far': 'in1_color3FAr', 'in1_color3fag': 'in1_color3FAg', 'in1_color3fab': 'in1_color3FAb', 'in1_color4r': 'in1_color4r', 'in1_color4g': 'in1_color4g', 'in1_color4b': 'in1_color4b', 'in1_color4a': 'in1_color4a', 'in2_color4r': 'in2_color4r', 'in2_color4g': 'in2_color4g', 'in2_color4b': 'in2_color4b', 'in2_color4a': 'in2_color4a', 'in1_color4far': 'in1_color4FAr', 'in1_color4fag': 'in1_color4FAg', 'in1_color4fab': 'in1_color4FAb', 'in1_color4faa': 'in1_color4FAa', 'in1_displacementshaderf': 'in1_displacementshaderF', 'in1_displacementshaderv': 'in1_displacementshaderV', 'in2_displacementshadervx': 'in2_displacementshaderVx', 'in2_displacementshadervy': 'in2_displacementshaderVy', 'in2_displacementshadervz': 'in2_displacementshaderVz', 'in1_edfc': 'in1_edfC', 'in2_edfcr': 'in2_edfCr', 'in2_edfcg': 'in2_edfCg', 'in2_edfcb': 'in2_edfCb', 'in1_edff': 'in1_edfF', 'in1_matrix331': 'in1_matrix331', 'in1_matrix332': 'in1_matrix332', 'in1_matrix333': 'in1_matrix333', 'in1_matrix334': 'in1_matrix334', 'in1_matrix335': 'in1_matrix335', 'in1_matrix336': 'in1_matrix336', 'in1_matrix337': 'in1_matrix337', 'in1_matrix338': 'in1_matrix338', 'in1_matrix339': 'in1_matrix339', 'in2_matrix331': 'in2_matrix331', 'in2_matrix332': 'in2_matrix332', 'in2_matrix333': 'in2_matrix333', 'in2_matrix334': 'in2_matrix334', 'in2_matrix335': 'in2_matrix335', 'in2_matrix336': 'in2_matrix336', 'in2_matrix337': 'in2_matrix337', 'in2_matrix338': 'in2_matrix338', 'in2_matrix339': 'in2_matrix339', 'in1_matrix441': 'in1_matrix441', 'in1_matrix442': 'in1_matrix442', 'in1_matrix443': 'in1_matrix443', 'in1_matrix444': 'in1_matrix444', 'in1_matrix445': 'in1_matrix445', 'in1_matrix446': 'in1_matrix446', 'in1_matrix447': 'in1_matrix447', 'in1_matrix448': 'in1_matrix448', 'in1_matrix449': 'in1_matrix449', 'in1_matrix4410': 'in1_matrix4410', 'in1_matrix4411': 'in1_matrix4411', 'in1_matrix4412': 'in1_matrix4412', 'in1_matrix4413': 'in1_matrix4413', 'in1_matrix4414': 'in1_matrix4414', 'in1_matrix4415': 'in1_matrix4415', 'in1_matrix4416': 'in1_matrix4416', 'in2_matrix441': 'in2_matrix441', 'in2_matrix442': 'in2_matrix442', 'in2_matrix443': 'in2_matrix443', 'in2_matrix444': 'in2_matrix444', 'in2_matrix445': 'in2_matrix445', 'in2_matrix446': 'in2_matrix446', 'in2_matrix447': 'in2_matrix447', 'in2_matrix448': 'in2_matrix448', 'in2_matrix449': 'in2_matrix449', 'in2_matrix4410': 'in2_matrix4410', 'in2_matrix4411': 'in2_matrix4411', 'in2_matrix4412': 'in2_matrix4412', 'in2_matrix4413': 'in2_matrix4413', 'in2_matrix4414': 'in2_matrix4414', 'in2_matrix4415': 'in2_matrix4415', 'in2_matrix4416': 'in2_matrix4416', 'in1_surfaceshaderc': 'in1_surfaceshaderC', 'in2_surfaceshadercr': 'in2_surfaceshaderCr', 'in2_surfaceshadercg': 'in2_surfaceshaderCg', 'in2_surfaceshadercb': 'in2_surfaceshaderCb', 'in1_surfaceshaderf': 'in1_surfaceshaderF', 'in1_vdfc': 'in1_vdfC', 'in2_vdfcr': 'in2_vdfCr', 'in2_vdfcg': 'in2_vdfCg', 'in2_vdfcb': 'in2_vdfCb', 'in1_vdff': 'in1_vdfF', 'in1_vector2x': 'in1_vector2x', 'in1_vector2y': 'in1_vector2y', 'in2_vector2x': 'in2_vector2x', 'in2_vector2y': 'in2_vector2y', 'in1_vector2fax': 'in1_vector2FAx', 'in1_vector2fay': 'in1_vector2FAy', 'in1_vector3x': 'in1_vector3x', 'in1_vector3y': 'in1_vector3y', 'in1_vector3z': 'in1_vector3z', 'in2_vector3x': 'in2_vector3x', 'in2_vector3y': 'in2_vector3y', 'in2_vector3z': 'in2_vector3z', 'in1_vector3fax': 'in1_vector3FAx', 'in1_vector3fay': 'in1_vector3FAy', 'in1_vector3faz': 'in1_vector3FAz', 'in1_vector4x': 'in1_vector4x', 'in1_vector4y': 'in1_vector4y', 'in1_vector4z': 'in1_vector4z', 'in1_vector4w': 'in1_vector4w', 'in2_vector4x': 'in2_vector4x', 'in2_vector4y': 'in2_vector4y', 'in2_vector4z': 'in2_vector4z', 'in2_vector4w': 'in2_vector4w', 'in1_vector4fax': 'in1_vector4FAx', 'in1_vector4fay': 'in1_vector4FAy', 'in1_vector4faz': 'in1_vector4FAz', 'in1_vector4faw': 'in1_vector4FAw', 'in1_volumeshaderc': 'in1_volumeshaderC', 'in2_volumeshadercr': 'in2_volumeshaderCr', 'in2_volumeshadercg': 'in2_volumeshaderCg', 'in2_volumeshadercb': 'in2_volumeshaderCb', 'in1_volumeshaderf': 'in1_volumeshaderF'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_in1 = Parameter(parm=self.node.parm('in1'))
        self.parm_in2 = Parameter(parm=self.node.parm('in2'))
        self.parm_in1_bsdfc = Parameter(parm=self.node.parm('in1_bsdfC'))
        self.parm_in2_bsdfcr = Parameter(parm=self.node.parm('in2_bsdfCr'))
        self.parm_in2_bsdfcg = Parameter(parm=self.node.parm('in2_bsdfCg'))
        self.parm_in2_bsdfcb = Parameter(parm=self.node.parm('in2_bsdfCb'))
        self.parm_in1_bsdff = Parameter(parm=self.node.parm('in1_bsdfF'))
        self.parm_in1_color3r = Parameter(parm=self.node.parm('in1_color3r'))
        self.parm_in1_color3g = Parameter(parm=self.node.parm('in1_color3g'))
        self.parm_in1_color3b = Parameter(parm=self.node.parm('in1_color3b'))
        self.parm_in2_color3r = Parameter(parm=self.node.parm('in2_color3r'))
        self.parm_in2_color3g = Parameter(parm=self.node.parm('in2_color3g'))
        self.parm_in2_color3b = Parameter(parm=self.node.parm('in2_color3b'))
        self.parm_in1_color3far = Parameter(parm=self.node.parm('in1_color3FAr'))
        self.parm_in1_color3fag = Parameter(parm=self.node.parm('in1_color3FAg'))
        self.parm_in1_color3fab = Parameter(parm=self.node.parm('in1_color3FAb'))
        self.parm_in1_color4r = Parameter(parm=self.node.parm('in1_color4r'))
        self.parm_in1_color4g = Parameter(parm=self.node.parm('in1_color4g'))
        self.parm_in1_color4b = Parameter(parm=self.node.parm('in1_color4b'))
        self.parm_in1_color4a = Parameter(parm=self.node.parm('in1_color4a'))
        self.parm_in2_color4r = Parameter(parm=self.node.parm('in2_color4r'))
        self.parm_in2_color4g = Parameter(parm=self.node.parm('in2_color4g'))
        self.parm_in2_color4b = Parameter(parm=self.node.parm('in2_color4b'))
        self.parm_in2_color4a = Parameter(parm=self.node.parm('in2_color4a'))
        self.parm_in1_color4far = Parameter(parm=self.node.parm('in1_color4FAr'))
        self.parm_in1_color4fag = Parameter(parm=self.node.parm('in1_color4FAg'))
        self.parm_in1_color4fab = Parameter(parm=self.node.parm('in1_color4FAb'))
        self.parm_in1_color4faa = Parameter(parm=self.node.parm('in1_color4FAa'))
        self.parm_in1_displacementshaderf = Parameter(parm=self.node.parm('in1_displacementshaderF'))
        self.parm_in1_displacementshaderv = Parameter(parm=self.node.parm('in1_displacementshaderV'))
        self.parm_in2_displacementshadervx = Parameter(parm=self.node.parm('in2_displacementshaderVx'))
        self.parm_in2_displacementshadervy = Parameter(parm=self.node.parm('in2_displacementshaderVy'))
        self.parm_in2_displacementshadervz = Parameter(parm=self.node.parm('in2_displacementshaderVz'))
        self.parm_in1_edfc = Parameter(parm=self.node.parm('in1_edfC'))
        self.parm_in2_edfcr = Parameter(parm=self.node.parm('in2_edfCr'))
        self.parm_in2_edfcg = Parameter(parm=self.node.parm('in2_edfCg'))
        self.parm_in2_edfcb = Parameter(parm=self.node.parm('in2_edfCb'))
        self.parm_in1_edff = Parameter(parm=self.node.parm('in1_edfF'))
        self.parm_in1_matrix331 = Parameter(parm=self.node.parm('in1_matrix331'))
        self.parm_in1_matrix332 = Parameter(parm=self.node.parm('in1_matrix332'))
        self.parm_in1_matrix333 = Parameter(parm=self.node.parm('in1_matrix333'))
        self.parm_in1_matrix334 = Parameter(parm=self.node.parm('in1_matrix334'))
        self.parm_in1_matrix335 = Parameter(parm=self.node.parm('in1_matrix335'))
        self.parm_in1_matrix336 = Parameter(parm=self.node.parm('in1_matrix336'))
        self.parm_in1_matrix337 = Parameter(parm=self.node.parm('in1_matrix337'))
        self.parm_in1_matrix338 = Parameter(parm=self.node.parm('in1_matrix338'))
        self.parm_in1_matrix339 = Parameter(parm=self.node.parm('in1_matrix339'))
        self.parm_in2_matrix331 = Parameter(parm=self.node.parm('in2_matrix331'))
        self.parm_in2_matrix332 = Parameter(parm=self.node.parm('in2_matrix332'))
        self.parm_in2_matrix333 = Parameter(parm=self.node.parm('in2_matrix333'))
        self.parm_in2_matrix334 = Parameter(parm=self.node.parm('in2_matrix334'))
        self.parm_in2_matrix335 = Parameter(parm=self.node.parm('in2_matrix335'))
        self.parm_in2_matrix336 = Parameter(parm=self.node.parm('in2_matrix336'))
        self.parm_in2_matrix337 = Parameter(parm=self.node.parm('in2_matrix337'))
        self.parm_in2_matrix338 = Parameter(parm=self.node.parm('in2_matrix338'))
        self.parm_in2_matrix339 = Parameter(parm=self.node.parm('in2_matrix339'))
        self.parm_in1_matrix441 = Parameter(parm=self.node.parm('in1_matrix441'))
        self.parm_in1_matrix442 = Parameter(parm=self.node.parm('in1_matrix442'))
        self.parm_in1_matrix443 = Parameter(parm=self.node.parm('in1_matrix443'))
        self.parm_in1_matrix444 = Parameter(parm=self.node.parm('in1_matrix444'))
        self.parm_in1_matrix445 = Parameter(parm=self.node.parm('in1_matrix445'))
        self.parm_in1_matrix446 = Parameter(parm=self.node.parm('in1_matrix446'))
        self.parm_in1_matrix447 = Parameter(parm=self.node.parm('in1_matrix447'))
        self.parm_in1_matrix448 = Parameter(parm=self.node.parm('in1_matrix448'))
        self.parm_in1_matrix449 = Parameter(parm=self.node.parm('in1_matrix449'))
        self.parm_in1_matrix4410 = Parameter(parm=self.node.parm('in1_matrix4410'))
        self.parm_in1_matrix4411 = Parameter(parm=self.node.parm('in1_matrix4411'))
        self.parm_in1_matrix4412 = Parameter(parm=self.node.parm('in1_matrix4412'))
        self.parm_in1_matrix4413 = Parameter(parm=self.node.parm('in1_matrix4413'))
        self.parm_in1_matrix4414 = Parameter(parm=self.node.parm('in1_matrix4414'))
        self.parm_in1_matrix4415 = Parameter(parm=self.node.parm('in1_matrix4415'))
        self.parm_in1_matrix4416 = Parameter(parm=self.node.parm('in1_matrix4416'))
        self.parm_in2_matrix441 = Parameter(parm=self.node.parm('in2_matrix441'))
        self.parm_in2_matrix442 = Parameter(parm=self.node.parm('in2_matrix442'))
        self.parm_in2_matrix443 = Parameter(parm=self.node.parm('in2_matrix443'))
        self.parm_in2_matrix444 = Parameter(parm=self.node.parm('in2_matrix444'))
        self.parm_in2_matrix445 = Parameter(parm=self.node.parm('in2_matrix445'))
        self.parm_in2_matrix446 = Parameter(parm=self.node.parm('in2_matrix446'))
        self.parm_in2_matrix447 = Parameter(parm=self.node.parm('in2_matrix447'))
        self.parm_in2_matrix448 = Parameter(parm=self.node.parm('in2_matrix448'))
        self.parm_in2_matrix449 = Parameter(parm=self.node.parm('in2_matrix449'))
        self.parm_in2_matrix4410 = Parameter(parm=self.node.parm('in2_matrix4410'))
        self.parm_in2_matrix4411 = Parameter(parm=self.node.parm('in2_matrix4411'))
        self.parm_in2_matrix4412 = Parameter(parm=self.node.parm('in2_matrix4412'))
        self.parm_in2_matrix4413 = Parameter(parm=self.node.parm('in2_matrix4413'))
        self.parm_in2_matrix4414 = Parameter(parm=self.node.parm('in2_matrix4414'))
        self.parm_in2_matrix4415 = Parameter(parm=self.node.parm('in2_matrix4415'))
        self.parm_in2_matrix4416 = Parameter(parm=self.node.parm('in2_matrix4416'))
        self.parm_in1_surfaceshaderc = Parameter(parm=self.node.parm('in1_surfaceshaderC'))
        self.parm_in2_surfaceshadercr = Parameter(parm=self.node.parm('in2_surfaceshaderCr'))
        self.parm_in2_surfaceshadercg = Parameter(parm=self.node.parm('in2_surfaceshaderCg'))
        self.parm_in2_surfaceshadercb = Parameter(parm=self.node.parm('in2_surfaceshaderCb'))
        self.parm_in1_surfaceshaderf = Parameter(parm=self.node.parm('in1_surfaceshaderF'))
        self.parm_in1_vdfc = Parameter(parm=self.node.parm('in1_vdfC'))
        self.parm_in2_vdfcr = Parameter(parm=self.node.parm('in2_vdfCr'))
        self.parm_in2_vdfcg = Parameter(parm=self.node.parm('in2_vdfCg'))
        self.parm_in2_vdfcb = Parameter(parm=self.node.parm('in2_vdfCb'))
        self.parm_in1_vdff = Parameter(parm=self.node.parm('in1_vdfF'))
        self.parm_in1_vector2x = Parameter(parm=self.node.parm('in1_vector2x'))
        self.parm_in1_vector2y = Parameter(parm=self.node.parm('in1_vector2y'))
        self.parm_in2_vector2x = Parameter(parm=self.node.parm('in2_vector2x'))
        self.parm_in2_vector2y = Parameter(parm=self.node.parm('in2_vector2y'))
        self.parm_in1_vector2fax = Parameter(parm=self.node.parm('in1_vector2FAx'))
        self.parm_in1_vector2fay = Parameter(parm=self.node.parm('in1_vector2FAy'))
        self.parm_in1_vector3x = Parameter(parm=self.node.parm('in1_vector3x'))
        self.parm_in1_vector3y = Parameter(parm=self.node.parm('in1_vector3y'))
        self.parm_in1_vector3z = Parameter(parm=self.node.parm('in1_vector3z'))
        self.parm_in2_vector3x = Parameter(parm=self.node.parm('in2_vector3x'))
        self.parm_in2_vector3y = Parameter(parm=self.node.parm('in2_vector3y'))
        self.parm_in2_vector3z = Parameter(parm=self.node.parm('in2_vector3z'))
        self.parm_in1_vector3fax = Parameter(parm=self.node.parm('in1_vector3FAx'))
        self.parm_in1_vector3fay = Parameter(parm=self.node.parm('in1_vector3FAy'))
        self.parm_in1_vector3faz = Parameter(parm=self.node.parm('in1_vector3FAz'))
        self.parm_in1_vector4x = Parameter(parm=self.node.parm('in1_vector4x'))
        self.parm_in1_vector4y = Parameter(parm=self.node.parm('in1_vector4y'))
        self.parm_in1_vector4z = Parameter(parm=self.node.parm('in1_vector4z'))
        self.parm_in1_vector4w = Parameter(parm=self.node.parm('in1_vector4w'))
        self.parm_in2_vector4x = Parameter(parm=self.node.parm('in2_vector4x'))
        self.parm_in2_vector4y = Parameter(parm=self.node.parm('in2_vector4y'))
        self.parm_in2_vector4z = Parameter(parm=self.node.parm('in2_vector4z'))
        self.parm_in2_vector4w = Parameter(parm=self.node.parm('in2_vector4w'))
        self.parm_in1_vector4fax = Parameter(parm=self.node.parm('in1_vector4FAx'))
        self.parm_in1_vector4fay = Parameter(parm=self.node.parm('in1_vector4FAy'))
        self.parm_in1_vector4faz = Parameter(parm=self.node.parm('in1_vector4FAz'))
        self.parm_in1_vector4faw = Parameter(parm=self.node.parm('in1_vector4FAw'))
        self.parm_in1_volumeshaderc = Parameter(parm=self.node.parm('in1_volumeshaderC'))
        self.parm_in2_volumeshadercr = Parameter(parm=self.node.parm('in2_volumeshaderCr'))
        self.parm_in2_volumeshadercg = Parameter(parm=self.node.parm('in2_volumeshaderCg'))
        self.parm_in2_volumeshadercb = Parameter(parm=self.node.parm('in2_volumeshaderCb'))
        self.parm_in1_volumeshaderf = Parameter(parm=self.node.parm('in1_volumeshaderF'))

        
        # parm menu vars:
        self.parm_signature = SignatureMenu(parm=self.node.parm('signature'))


        # input vars:
        self.input_input_1 = 'Input 1'
        self.input_input_2 = 'Input 2'


# parm menu classes:
class SignatureMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_float = "default"



