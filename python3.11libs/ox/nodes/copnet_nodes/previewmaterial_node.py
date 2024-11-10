from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class PreviewmaterialNode(OXNode):
    node_type = 'previewmaterial'
    parm_lookup_dict = {'geotype': 'geotype', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'geoscale': 'geoscale', 'geouvscale': 'geouvscale', 'geores': 'geores', 'geowaviness': 'geowaviness', 'geobevel': 'geobevel', 'geobevelshape': 'geobevelshape', 'geobeveloffset': 'geobeveloffset', 'default_basecolorr': 'default_basecolorr', 'default_basecolorg': 'default_basecolorg', 'default_basecolorb': 'default_basecolorb', 'tintwithcdswitch': 'tintwithcdswitch', 'folder8': 'folder8', 'default_metalness': 'default_metalness', 'metalnessscale': 'metalnessscale', 'folder0': 'folder0', 'default_specular': 'default_specular', 'default_spec_colorr': 'default_spec_colorr', 'default_spec_colorg': 'default_spec_colorg', 'default_spec_colorb': 'default_spec_colorb', 'default_specular_roughness': 'default_specular_roughness', 'specularroughnessscale': 'specularroughnessscale', 'specular_ior': 'specular_IOR', 'folder1': 'folder1', 'default_coat_amount': 'default_coat_amount', 'default_coat_colorr': 'default_coat_colorr', 'default_coat_colorg': 'default_coat_colorg', 'default_coat_colorb': 'default_coat_colorb', 'default_coat_roughness': 'default_coat_roughness', 'coatroughnessscale': 'coatroughnessscale', 'folder2': 'folder2', 'default_sheen_amount': 'default_sheen_amount', 'default_sheen_colorr': 'default_sheen_colorr', 'default_sheen_colorg': 'default_sheen_colorg', 'default_sheen_colorb': 'default_sheen_colorb', 'default_sheen_roughness': 'default_sheen_roughness', 'sheenroughnessscale': 'sheenroughnessscale', 'folder3': 'folder3', 'default_emission_amount': 'default_emission_amount', 'emissionscale': 'emissionscale', 'default_emission_colorr': 'default_emission_colorr', 'default_emission_colorg': 'default_emission_colorg', 'default_emission_colorb': 'default_emission_colorb', 'folder7': 'folder7', 'normalmap_scale': 'normalmap_scale', 'heightscale': 'heightscale', 'folder5': 'folder5', 'default_transmission_amount': 'default_transmission_amount', 'default_transmission_colorr': 'default_transmission_colorr', 'default_transmission_colorg': 'default_transmission_colorg', 'default_transmission_colorb': 'default_transmission_colorb', 'folder4': 'folder4', 'default_sss_amount': 'default_sss_amount', 'default_sss_colorr': 'default_sss_colorr', 'default_sss_colorg': 'default_sss_colorg', 'default_sss_colorb': 'default_sss_colorb', 'default_sss_radiusr': 'default_sss_radiusr', 'default_sss_radiusg': 'default_sss_radiusg', 'default_sss_radiusb': 'default_sss_radiusb', 'sss_radius_scale': 'sss_radius_scale', 'folder6': 'folder6', 'default_opacity_amount': 'default_opacity_amount', 'opacityscale': 'opacityscale'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_geoscale = Parameter(parm=self.node.parm('geoscale'))
        self.parm_geouvscale = Parameter(parm=self.node.parm('geouvscale'))
        self.parm_geores = Parameter(parm=self.node.parm('geores'))
        self.parm_geowaviness = Parameter(parm=self.node.parm('geowaviness'))
        self.parm_geobevel = Parameter(parm=self.node.parm('geobevel'))
        self.parm_geobeveloffset = Parameter(parm=self.node.parm('geobeveloffset'))
        self.parm_default_basecolorr = Parameter(parm=self.node.parm('default_basecolorr'))
        self.parm_default_basecolorg = Parameter(parm=self.node.parm('default_basecolorg'))
        self.parm_default_basecolorb = Parameter(parm=self.node.parm('default_basecolorb'))
        self.parm_tintwithcdswitch = Parameter(parm=self.node.parm('tintwithcdswitch'))
        self.parm_folder8 = Parameter(parm=self.node.parm('folder8'))
        self.parm_default_metalness = Parameter(parm=self.node.parm('default_metalness'))
        self.parm_metalnessscale = Parameter(parm=self.node.parm('metalnessscale'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_default_specular = Parameter(parm=self.node.parm('default_specular'))
        self.parm_default_spec_colorr = Parameter(parm=self.node.parm('default_spec_colorr'))
        self.parm_default_spec_colorg = Parameter(parm=self.node.parm('default_spec_colorg'))
        self.parm_default_spec_colorb = Parameter(parm=self.node.parm('default_spec_colorb'))
        self.parm_default_specular_roughness = Parameter(parm=self.node.parm('default_specular_roughness'))
        self.parm_specularroughnessscale = Parameter(parm=self.node.parm('specularroughnessscale'))
        self.parm_specular_ior = Parameter(parm=self.node.parm('specular_IOR'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_default_coat_amount = Parameter(parm=self.node.parm('default_coat_amount'))
        self.parm_default_coat_colorr = Parameter(parm=self.node.parm('default_coat_colorr'))
        self.parm_default_coat_colorg = Parameter(parm=self.node.parm('default_coat_colorg'))
        self.parm_default_coat_colorb = Parameter(parm=self.node.parm('default_coat_colorb'))
        self.parm_default_coat_roughness = Parameter(parm=self.node.parm('default_coat_roughness'))
        self.parm_coatroughnessscale = Parameter(parm=self.node.parm('coatroughnessscale'))
        self.parm_folder2 = Parameter(parm=self.node.parm('folder2'))
        self.parm_default_sheen_amount = Parameter(parm=self.node.parm('default_sheen_amount'))
        self.parm_default_sheen_colorr = Parameter(parm=self.node.parm('default_sheen_colorr'))
        self.parm_default_sheen_colorg = Parameter(parm=self.node.parm('default_sheen_colorg'))
        self.parm_default_sheen_colorb = Parameter(parm=self.node.parm('default_sheen_colorb'))
        self.parm_default_sheen_roughness = Parameter(parm=self.node.parm('default_sheen_roughness'))
        self.parm_sheenroughnessscale = Parameter(parm=self.node.parm('sheenroughnessscale'))
        self.parm_folder3 = Parameter(parm=self.node.parm('folder3'))
        self.parm_default_emission_amount = Parameter(parm=self.node.parm('default_emission_amount'))
        self.parm_emissionscale = Parameter(parm=self.node.parm('emissionscale'))
        self.parm_default_emission_colorr = Parameter(parm=self.node.parm('default_emission_colorr'))
        self.parm_default_emission_colorg = Parameter(parm=self.node.parm('default_emission_colorg'))
        self.parm_default_emission_colorb = Parameter(parm=self.node.parm('default_emission_colorb'))
        self.parm_folder7 = Parameter(parm=self.node.parm('folder7'))
        self.parm_normalmap_scale = Parameter(parm=self.node.parm('normalmap_scale'))
        self.parm_heightscale = Parameter(parm=self.node.parm('heightscale'))
        self.parm_folder5 = Parameter(parm=self.node.parm('folder5'))
        self.parm_default_transmission_amount = Parameter(parm=self.node.parm('default_transmission_amount'))
        self.parm_default_transmission_colorr = Parameter(parm=self.node.parm('default_transmission_colorr'))
        self.parm_default_transmission_colorg = Parameter(parm=self.node.parm('default_transmission_colorg'))
        self.parm_default_transmission_colorb = Parameter(parm=self.node.parm('default_transmission_colorb'))
        self.parm_folder4 = Parameter(parm=self.node.parm('folder4'))
        self.parm_default_sss_amount = Parameter(parm=self.node.parm('default_sss_amount'))
        self.parm_default_sss_colorr = Parameter(parm=self.node.parm('default_sss_colorr'))
        self.parm_default_sss_colorg = Parameter(parm=self.node.parm('default_sss_colorg'))
        self.parm_default_sss_colorb = Parameter(parm=self.node.parm('default_sss_colorb'))
        self.parm_default_sss_radiusr = Parameter(parm=self.node.parm('default_sss_radiusr'))
        self.parm_default_sss_radiusg = Parameter(parm=self.node.parm('default_sss_radiusg'))
        self.parm_default_sss_radiusb = Parameter(parm=self.node.parm('default_sss_radiusb'))
        self.parm_sss_radius_scale = Parameter(parm=self.node.parm('sss_radius_scale'))
        self.parm_folder6 = Parameter(parm=self.node.parm('folder6'))
        self.parm_default_opacity_amount = Parameter(parm=self.node.parm('default_opacity_amount'))
        self.parm_opacityscale = Parameter(parm=self.node.parm('opacityscale'))

        
        # parm menu vars:
        self.parm_geotype = GeotypeMenu(parm=self.node.parm('geotype'))
        self.parm_geobevelshape = GeobevelshapeMenu(parm=self.node.parm('geobevelshape'))


        # input vars:
        self.input_geo = 'geo'
        self.input_basecolor = 'basecolor'
        self.input_metalness = 'metalness'
        self.input_specular = 'specular'
        self.input_spec_color = 'spec_color'
        self.input_roughness = 'roughness'
        self.input_coat = 'coat'
        self.input_coat_color = 'coat_color'
        self.input_coat_roughness = 'coat_roughness'
        self.input_sheen = 'sheen'
        self.input_sheen_color = 'sheen_color'
        self.input_sheen_roughness = 'sheen_roughness'
        self.input_emission = 'emission'
        self.input_emission_color = 'emission_color'
        self.input_opacity = 'opacity'
        self.input_normal = 'normal'
        self.input_height = 'height'
        self.input_transmission = 'transmission'
        self.input_transmission_color = 'transmission_color'
        self.input_sss_amount = 'sss_amount'
        self.input_sss_color = 'sss_color'
        self.input_sss_radius = 'sss_radius'


# parm menu classes:
class GeotypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_grid = ("grid", 0)
        self.menu_sphere = ("sphere", 1)
        self.menu_box = ("box", 2)
        self.menu_tube = ("tube", 3)
        self.menu_torus = ("torus", 4)
        self.menu_shader_ball = ("shaderball", 5)


class GeobevelshapeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_crease = ("crease", 0)
        self.menu_chamfer = ("chamfer", 1)
        self.menu_round = ("round", 2)



