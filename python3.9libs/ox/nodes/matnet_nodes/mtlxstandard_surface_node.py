from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class MtlxstandardSurfaceNode(OXNode):
    node_type = 'mtlxstandard_surface'
    parm_lookup_dict = {'folder01': 'folder01', 'base': 'base', 'base_colorr': 'base_colorr', 'base_colorg': 'base_colorg', 'base_colorb': 'base_colorb', 'diffuse_roughness': 'diffuse_roughness', 'metalness': 'metalness', 'specular': 'specular', 'specular_colorr': 'specular_colorr', 'specular_colorg': 'specular_colorg', 'specular_colorb': 'specular_colorb', 'specular_roughness': 'specular_roughness', 'specular_ior': 'specular_IOR', 'specular_anisotropy': 'specular_anisotropy', 'specular_rotation': 'specular_rotation', 'transmission': 'transmission', 'transmission_colorr': 'transmission_colorr', 'transmission_colorg': 'transmission_colorg', 'transmission_colorb': 'transmission_colorb', 'transmission_depth': 'transmission_depth', 'transmission_scatterr': 'transmission_scatterr', 'transmission_scatterg': 'transmission_scatterg', 'transmission_scatterb': 'transmission_scatterb', 'transmission_scatter_anisotropy': 'transmission_scatter_anisotropy', 'transmission_dispersion': 'transmission_dispersion', 'transmission_extra_roughness': 'transmission_extra_roughness', 'subsurface': 'subsurface', 'subsurface_colorr': 'subsurface_colorr', 'subsurface_colorg': 'subsurface_colorg', 'subsurface_colorb': 'subsurface_colorb', 'subsurface_radiusr': 'subsurface_radiusr', 'subsurface_radiusg': 'subsurface_radiusg', 'subsurface_radiusb': 'subsurface_radiusb', 'subsurface_scale': 'subsurface_scale', 'subsurface_anisotropy': 'subsurface_anisotropy', 'sheen': 'sheen', 'sheen_colorr': 'sheen_colorr', 'sheen_colorg': 'sheen_colorg', 'sheen_colorb': 'sheen_colorb', 'sheen_roughness': 'sheen_roughness', 'coat': 'coat', 'coat_colorr': 'coat_colorr', 'coat_colorg': 'coat_colorg', 'coat_colorb': 'coat_colorb', 'coat_roughness': 'coat_roughness', 'coat_anisotropy': 'coat_anisotropy', 'coat_rotation': 'coat_rotation', 'coat_ior': 'coat_IOR', 'coat_normalx': 'coat_normalx', 'coat_normaly': 'coat_normaly', 'coat_normalz': 'coat_normalz', 'coat_affect_color': 'coat_affect_color', 'coat_affect_roughness': 'coat_affect_roughness', 'thin_film_thickness': 'thin_film_thickness', 'thin_film_ior': 'thin_film_IOR', 'emission': 'emission', 'emission_colorr': 'emission_colorr', 'emission_colorg': 'emission_colorg', 'emission_colorb': 'emission_colorb', 'opacityr': 'opacityr', 'opacityg': 'opacityg', 'opacityb': 'opacityb', 'thin_walled': 'thin_walled', 'normalx': 'normalx', 'normaly': 'normaly', 'normalz': 'normalz', 'tangentx': 'tangentx', 'tangenty': 'tangenty', 'tangentz': 'tangentz'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder01 = Parameter(parm=self.node.parm('folder01'))
        self.parm_base = Parameter(parm=self.node.parm('base'))
        self.parm_base_colorr = Parameter(parm=self.node.parm('base_colorr'))
        self.parm_base_colorg = Parameter(parm=self.node.parm('base_colorg'))
        self.parm_base_colorb = Parameter(parm=self.node.parm('base_colorb'))
        self.parm_diffuse_roughness = Parameter(parm=self.node.parm('diffuse_roughness'))
        self.parm_metalness = Parameter(parm=self.node.parm('metalness'))
        self.parm_specular = Parameter(parm=self.node.parm('specular'))
        self.parm_specular_colorr = Parameter(parm=self.node.parm('specular_colorr'))
        self.parm_specular_colorg = Parameter(parm=self.node.parm('specular_colorg'))
        self.parm_specular_colorb = Parameter(parm=self.node.parm('specular_colorb'))
        self.parm_specular_roughness = Parameter(parm=self.node.parm('specular_roughness'))
        self.parm_specular_ior = Parameter(parm=self.node.parm('specular_IOR'))
        self.parm_specular_anisotropy = Parameter(parm=self.node.parm('specular_anisotropy'))
        self.parm_specular_rotation = Parameter(parm=self.node.parm('specular_rotation'))
        self.parm_transmission = Parameter(parm=self.node.parm('transmission'))
        self.parm_transmission_colorr = Parameter(parm=self.node.parm('transmission_colorr'))
        self.parm_transmission_colorg = Parameter(parm=self.node.parm('transmission_colorg'))
        self.parm_transmission_colorb = Parameter(parm=self.node.parm('transmission_colorb'))
        self.parm_transmission_depth = Parameter(parm=self.node.parm('transmission_depth'))
        self.parm_transmission_scatterr = Parameter(parm=self.node.parm('transmission_scatterr'))
        self.parm_transmission_scatterg = Parameter(parm=self.node.parm('transmission_scatterg'))
        self.parm_transmission_scatterb = Parameter(parm=self.node.parm('transmission_scatterb'))
        self.parm_transmission_scatter_anisotropy = Parameter(parm=self.node.parm('transmission_scatter_anisotropy'))
        self.parm_transmission_dispersion = Parameter(parm=self.node.parm('transmission_dispersion'))
        self.parm_transmission_extra_roughness = Parameter(parm=self.node.parm('transmission_extra_roughness'))
        self.parm_subsurface = Parameter(parm=self.node.parm('subsurface'))
        self.parm_subsurface_colorr = Parameter(parm=self.node.parm('subsurface_colorr'))
        self.parm_subsurface_colorg = Parameter(parm=self.node.parm('subsurface_colorg'))
        self.parm_subsurface_colorb = Parameter(parm=self.node.parm('subsurface_colorb'))
        self.parm_subsurface_radiusr = Parameter(parm=self.node.parm('subsurface_radiusr'))
        self.parm_subsurface_radiusg = Parameter(parm=self.node.parm('subsurface_radiusg'))
        self.parm_subsurface_radiusb = Parameter(parm=self.node.parm('subsurface_radiusb'))
        self.parm_subsurface_scale = Parameter(parm=self.node.parm('subsurface_scale'))
        self.parm_subsurface_anisotropy = Parameter(parm=self.node.parm('subsurface_anisotropy'))
        self.parm_sheen = Parameter(parm=self.node.parm('sheen'))
        self.parm_sheen_colorr = Parameter(parm=self.node.parm('sheen_colorr'))
        self.parm_sheen_colorg = Parameter(parm=self.node.parm('sheen_colorg'))
        self.parm_sheen_colorb = Parameter(parm=self.node.parm('sheen_colorb'))
        self.parm_sheen_roughness = Parameter(parm=self.node.parm('sheen_roughness'))
        self.parm_coat = Parameter(parm=self.node.parm('coat'))
        self.parm_coat_colorr = Parameter(parm=self.node.parm('coat_colorr'))
        self.parm_coat_colorg = Parameter(parm=self.node.parm('coat_colorg'))
        self.parm_coat_colorb = Parameter(parm=self.node.parm('coat_colorb'))
        self.parm_coat_roughness = Parameter(parm=self.node.parm('coat_roughness'))
        self.parm_coat_anisotropy = Parameter(parm=self.node.parm('coat_anisotropy'))
        self.parm_coat_rotation = Parameter(parm=self.node.parm('coat_rotation'))
        self.parm_coat_ior = Parameter(parm=self.node.parm('coat_IOR'))
        self.parm_coat_normalx = Parameter(parm=self.node.parm('coat_normalx'))
        self.parm_coat_normaly = Parameter(parm=self.node.parm('coat_normaly'))
        self.parm_coat_normalz = Parameter(parm=self.node.parm('coat_normalz'))
        self.parm_coat_affect_color = Parameter(parm=self.node.parm('coat_affect_color'))
        self.parm_coat_affect_roughness = Parameter(parm=self.node.parm('coat_affect_roughness'))
        self.parm_thin_film_thickness = Parameter(parm=self.node.parm('thin_film_thickness'))
        self.parm_thin_film_ior = Parameter(parm=self.node.parm('thin_film_IOR'))
        self.parm_emission = Parameter(parm=self.node.parm('emission'))
        self.parm_emission_colorr = Parameter(parm=self.node.parm('emission_colorr'))
        self.parm_emission_colorg = Parameter(parm=self.node.parm('emission_colorg'))
        self.parm_emission_colorb = Parameter(parm=self.node.parm('emission_colorb'))
        self.parm_opacityr = Parameter(parm=self.node.parm('opacityr'))
        self.parm_opacityg = Parameter(parm=self.node.parm('opacityg'))
        self.parm_opacityb = Parameter(parm=self.node.parm('opacityb'))
        self.parm_thin_walled = Parameter(parm=self.node.parm('thin_walled'))
        self.parm_normalx = Parameter(parm=self.node.parm('normalx'))
        self.parm_normaly = Parameter(parm=self.node.parm('normaly'))
        self.parm_normalz = Parameter(parm=self.node.parm('normalz'))
        self.parm_tangentx = Parameter(parm=self.node.parm('tangentx'))
        self.parm_tangenty = Parameter(parm=self.node.parm('tangenty'))
        self.parm_tangentz = Parameter(parm=self.node.parm('tangentz'))

        
        # parm menu vars:


        # input vars:
        self.input_base = 'Base'
        self.input_base_color = 'Base Color'
        self.input_diffuse_roughness = 'Diffuse Roughness'
        self.input_metalness = 'Metalness'
        self.input_specular = 'Specular'
        self.input_specular_color = 'Specular Color'
        self.input_specular_roughness = 'Specular Roughness'
        self.input_index_of_refraction = 'Index of Refraction'
        self.input_specular_anisotropy = 'Specular Anisotropy'
        self.input_specular_rotation = 'Specular Rotation'
        self.input_transmission = 'Transmission'
        self.input_transmission_color = 'Transmission Color'
        self.input_transmission_depth = 'Transmission Depth'
        self.input_transmission_scatter = 'Transmission Scatter'
        self.input_transmission_anisotropy = 'Transmission Anisotropy'
        self.input_transmission_dispersion = 'Transmission Dispersion'
        self.input_transmission_roughness = 'Transmission Roughness'
        self.input_subsurface = 'Subsurface'
        self.input_subsurface_color = 'Subsurface Color'
        self.input_subsurface_radius = 'Subsurface Radius'
        self.input_subsurface_scale = 'Subsurface Scale'
        self.input_subsurface_anisotropy = 'Subsurface Anisotropy'
        self.input_sheen = 'Sheen'
        self.input_sheen_color = 'Sheen Color'
        self.input_sheen_roughness = 'Sheen Roughness'
        self.input_coat = 'Coat'
        self.input_coat_color = 'Coat Color'
        self.input_coat_roughness = 'Coat Roughness'
        self.input_coat_anisotropy = 'Coat Anisotropy'
        self.input_coat_rotation = 'Coat Rotation'
        self.input_coat_index_of_refraction = 'Coat Index of Refraction'
        self.input_coat_normal = 'Coat normal'
        self.input_coat_affect_color = 'Coat Affect Color'
        self.input_coat_affect_roughness = 'Coat Affect Roughness'
        self.input_thin_film_thickness = 'Thin Film Thickness'
        self.input_thin_film_index_of_refraction = 'Thin Film Index of Refraction'
        self.input_emission = 'Emission'
        self.input_emission_color = 'Emission Color'
        self.input_opacity = 'Opacity'
        self.input_thin_walled = 'Thin Walled'
        self.input_normal = 'Normal'
        self.input_tangent_input = 'Tangent Input'


# parm menu classes:

