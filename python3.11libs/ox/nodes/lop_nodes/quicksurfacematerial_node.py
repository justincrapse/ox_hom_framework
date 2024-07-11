from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class QuicksurfacematerialNode(OXNode):
    node_type = 'editmaterialproperties'
    parm_lookup_dict = {'sample_group': 'sample_group', 'sample_behavior': 'sample_behavior', 'sample_f1': 'sample_f1', 'sample_f2': 'sample_f2', 'sample_f3': 'sample_f3', 'sample_subframeenable': 'sample_subframeenable', 'sample_subframegroup': 'sample_subframegroup', 'sample_shuttermode': 'sample_shuttermode', 'sample_shutterrange1': 'sample_shutterrange1', 'sample_shutterrange2': 'sample_shutterrange2', 'sample_cameraprim': 'sample_cameraprim', 'sample_count': 'sample_count', 'sample_includeframe': 'sample_includeframe', 'reftype': 'reftype', 'classancestor': 'classancestor', 'reload': 'reload', 'reffilepath': 'reffilepath', 'primpattern': 'primpattern', 'classprimpath': 'classprimpath', 'createparms': 'createparms', 'createoutputparms': 'createoutputparms', 'initforedit': 'initforedit', 'destinationprim_group': 'destinationprim_group', 'refparentmat': 'refparentmat', 'instanceable': 'instanceable', 'primpath': 'primpath', 'parentprimtype': 'parentprimtype', 'sample_group2': 'sample_group2', 'sample_subframegroup2': 'sample_subframegroup2', 'folder0': 'folder0', 'quickmaterialrefresh': 'quickmaterialrefresh', 'destinationprim_group2': 'destinationprim_group2', 'folder0_0': 'folder0_0', 'base_control': 'base_control', 'base': 'base', 'base_color_control': 'base_color_control', 'base_colorr': 'base_colorr', 'base_colorg': 'base_colorg', 'base_colorb': 'base_colorb', 'base_color_file_control': 'base_color_file_control', 'base_color_file': 'base_color_file', 'base_color_primvar_control': 'base_color_primvar_control', 'base_color_primvar': 'base_color_primvar', 'metalness_control': 'metalness_control', 'metalness': 'metalness', 'metalness_file_control': 'metalness_file_control', 'metalness_file': 'metalness_file', 'folder0_1': 'folder0_1', 'specular_control': 'specular_control', 'specular': 'specular', 'specular_color_control': 'specular_color_control', 'specular_colorr': 'specular_colorr', 'specular_colorg': 'specular_colorg', 'specular_colorb': 'specular_colorb', 'specular_color_file_control': 'specular_color_file_control', 'specular_color_file': 'specular_color_file', 'specular_roughness_control': 'specular_roughness_control', 'specular_roughness': 'specular_roughness', 'specular_roughness_file_control': 'specular_roughness_file_control', 'specular_roughness_file': 'specular_roughness_file', 'roughness_primvar_control': 'roughness_primvar_control', 'roughness_primvar': 'roughness_primvar', 'specular_ior_control': 'specular_IOR_control', 'specular_ior': 'specular_IOR', 'specular_anisotropy_control': 'specular_anisotropy_control', 'specular_anisotropy': 'specular_anisotropy', 'specular_rotation_control': 'specular_rotation_control', 'specular_rotation': 'specular_rotation', 'folder0_5': 'folder0_5', 'coat_control': 'coat_control', 'coat': 'coat', 'coat_color_control': 'coat_color_control', 'coat_colorr': 'coat_colorr', 'coat_colorg': 'coat_colorg', 'coat_colorb': 'coat_colorb', 'coat_color_file_control': 'coat_color_file_control', 'coat_color_file': 'coat_color_file', 'coat_roughness_control': 'coat_roughness_control', 'coat_roughness': 'coat_roughness', 'coat_roughness_file_control': 'coat_roughness_file_control', 'coat_roughness_file': 'coat_roughness_file', 'folder0_2': 'folder0_2', 'transmission_control': 'transmission_control', 'transmission': 'transmission', 'transmission_color_control': 'transmission_color_control', 'transmission_colorr': 'transmission_colorr', 'transmission_colorg': 'transmission_colorg', 'transmission_colorb': 'transmission_colorb', 'transmission_color_file_control': 'transmission_color_file_control', 'transmission_color_file': 'transmission_color_file', 'transmission_color_primvar_control': 'transmission_color_primvar_control', 'transmission_color_primvar': 'transmission_color_primvar', 'transmission_depth_control': 'transmission_depth_control', 'transmission_depth': 'transmission_depth', 'transmission_dispersion_control': 'transmission_dispersion_control', 'transmission_dispersion': 'transmission_dispersion', 'folder0_4': 'folder0_4', 'sheen_control': 'sheen_control', 'sheen': 'sheen', 'sheen_color_control': 'sheen_color_control', 'sheen_colorr': 'sheen_colorr', 'sheen_colorg': 'sheen_colorg', 'sheen_colorb': 'sheen_colorb', 'sheen_color_file_control': 'sheen_color_file_control', 'sheen_color_file': 'sheen_color_file', 'sheen_roughness_control': 'sheen_roughness_control', 'sheen_roughness': 'sheen_roughness', 'sheen_roughness_file_control': 'sheen_roughness_file_control', 'sheen_roughness_file': 'sheen_roughness_file', 'folder0_3': 'folder0_3', 'subsurface_control': 'subsurface_control', 'subsurface': 'subsurface', 'subsurface_color_control': 'subsurface_color_control', 'subsurface_colorr': 'subsurface_colorr', 'subsurface_colorg': 'subsurface_colorg', 'subsurface_colorb': 'subsurface_colorb', 'subsurface_color_file_control': 'subsurface_color_file_control', 'subsurface_color_file': 'subsurface_color_file', 'subsurface_color_primvar_control': 'subsurface_color_primvar_control', 'subsurface_color_primvar': 'subsurface_color_primvar', 'subsurface_radius_control': 'subsurface_radius_control', 'subsurface_radiusr': 'subsurface_radiusr', 'subsurface_radiusg': 'subsurface_radiusg', 'subsurface_radiusb': 'subsurface_radiusb', 'subsurface_scale_control': 'subsurface_scale_control', 'subsurface_scale': 'subsurface_scale', 'subsurface_scale_file_control': 'subsurface_scale_file_control', 'subsurface_scale_file': 'subsurface_scale_file', 'folder0_7': 'folder0_7', 'emission_control': 'emission_control', 'emission': 'emission', 'emission_color_control': 'emission_color_control', 'emission_colorr': 'emission_colorr', 'emission_colorg': 'emission_colorg', 'emission_colorb': 'emission_colorb', 'emission_color_file_control': 'emission_color_file_control', 'emission_color_file': 'emission_color_file', 'emission_color_primvar_control': 'emission_color_primvar_control', 'emission_color_primvar': 'emission_color_primvar', 'folder3_1': 'folder3_1', 'bump_style_control': 'bump_style_control', 'bump_style': 'bump_style', 'bump_height_file_control': 'bump_height_file_control', 'bump_height_file': 'bump_height_file', 'bump_normal_file_control': 'bump_normal_file_control', 'bump_normal_file': 'bump_normal_file', 'bump_scale_control': 'bump_scale_control', 'bump_scale': 'bump_scale', 'true_displacements_control': 'true_displacements_control', 'true_displacements': 'true_displacements', 'folder0_6': 'folder0_6', 'thin_film_ior_control': 'thin_film_IOR_control', 'thin_film_ior': 'thin_film_IOR', 'thin_film_thickness_control': 'thin_film_thickness_control', 'thin_film_thickness': 'thin_film_thickness', 'thin_film_thickness_primvar_control': 'thin_film_thickness_primvar_control', 'thin_film_thickness_primvar': 'thin_film_thickness_primvar', 'thin_film_thickness_file_control': 'thin_film_thickness_file_control', 'thin_film_thickness_file': 'thin_film_thickness_file', 'folder0_8': 'folder0_8', 'thin_walled_control': 'thin_walled_control', 'thin_walled': 'thin_walled', 'opacity_control': 'opacity_control', 'opacityr': 'opacityr', 'opacityg': 'opacityg', 'opacityb': 'opacityb', 'opacity_file_control': 'opacity_file_control', 'opacity_file': 'opacity_file', 'opacity_primvar_control': 'opacity_primvar_control', 'opacity_primvar': 'opacity_primvar', 'folder0_9': 'folder0_9', 'filtertype_control': 'filtertype_control', 'filtertype': 'filtertype', 'projection_control': 'projection_control', 'projection': 'projection', 'uv_offset_control': 'uv_offset_control', 'uv_offset1': 'uv_offset1', 'uv_offset2': 'uv_offset2', 'uv_scale_control': 'uv_scale_control', 'uv_scale1': 'uv_scale1', 'uv_scale2': 'uv_scale2', 'uv_primvar_control': 'uv_primvar_control', 'uv_primvar': 'uv_primvar', 'triplanar_blend_control': 'triplanar_blend_control', 'triplanar_blend': 'triplanar_blend', 'triplanar_upaxis_control': 'triplanar_upaxis_control', 'triplanar_upaxis': 'triplanar_upaxis', 'displacement_control': 'displacement_control', 'displacement': 'displacement', 'maps_copnet': 'maps_copnet'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_sample_group = Parameter(parm=self.node.parm('sample_group'))
        self.parm_sample_f1 = Parameter(parm=self.node.parm('sample_f1'))
        self.parm_sample_f2 = Parameter(parm=self.node.parm('sample_f2'))
        self.parm_sample_f3 = Parameter(parm=self.node.parm('sample_f3'))
        self.parm_sample_subframeenable = Parameter(parm=self.node.parm('sample_subframeenable'))
        self.parm_sample_subframegroup = Parameter(parm=self.node.parm('sample_subframegroup'))
        self.parm_sample_shutterrange1 = Parameter(parm=self.node.parm('sample_shutterrange1'))
        self.parm_sample_shutterrange2 = Parameter(parm=self.node.parm('sample_shutterrange2'))
        self.parm_sample_cameraprim = Parameter(parm=self.node.parm('sample_cameraprim'))
        self.parm_sample_count = Parameter(parm=self.node.parm('sample_count'))
        self.parm_sample_includeframe = Parameter(parm=self.node.parm('sample_includeframe'))
        self.parm_classancestor = Parameter(parm=self.node.parm('classancestor'))
        self.parm_reload = Parameter(parm=self.node.parm('reload'))
        self.parm_reffilepath = Parameter(parm=self.node.parm('reffilepath'))
        self.parm_primpattern = Parameter(parm=self.node.parm('primpattern'))
        self.parm_classprimpath = Parameter(parm=self.node.parm('classprimpath'))
        self.parm_createparms = Parameter(parm=self.node.parm('createparms'))
        self.parm_createoutputparms = Parameter(parm=self.node.parm('createoutputparms'))
        self.parm_destinationprim_group = Parameter(parm=self.node.parm('destinationprim_group'))
        self.parm_refparentmat = Parameter(parm=self.node.parm('refparentmat'))
        self.parm_instanceable = Parameter(parm=self.node.parm('instanceable'))
        self.parm_primpath = Parameter(parm=self.node.parm('primpath'))
        self.parm_sample_group2 = Parameter(parm=self.node.parm('sample_group2'))
        self.parm_sample_subframegroup2 = Parameter(parm=self.node.parm('sample_subframegroup2'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_quickmaterialrefresh = Parameter(parm=self.node.parm('quickmaterialrefresh'))
        self.parm_destinationprim_group2 = Parameter(parm=self.node.parm('destinationprim_group2'))
        self.parm_folder0_0 = Parameter(parm=self.node.parm('folder0_0'))
        self.parm_base_control = Parameter(parm=self.node.parm('base_control'))
        self.parm_base = Parameter(parm=self.node.parm('base'))
        self.parm_base_color_control = Parameter(parm=self.node.parm('base_color_control'))
        self.parm_base_colorr = Parameter(parm=self.node.parm('base_colorr'))
        self.parm_base_colorg = Parameter(parm=self.node.parm('base_colorg'))
        self.parm_base_colorb = Parameter(parm=self.node.parm('base_colorb'))
        self.parm_base_color_file_control = Parameter(parm=self.node.parm('base_color_file_control'))
        self.parm_base_color_file = Parameter(parm=self.node.parm('base_color_file'))
        self.parm_base_color_primvar_control = Parameter(parm=self.node.parm('base_color_primvar_control'))
        self.parm_base_color_primvar = Parameter(parm=self.node.parm('base_color_primvar'))
        self.parm_metalness_control = Parameter(parm=self.node.parm('metalness_control'))
        self.parm_metalness = Parameter(parm=self.node.parm('metalness'))
        self.parm_metalness_file_control = Parameter(parm=self.node.parm('metalness_file_control'))
        self.parm_metalness_file = Parameter(parm=self.node.parm('metalness_file'))
        self.parm_folder0_1 = Parameter(parm=self.node.parm('folder0_1'))
        self.parm_specular_control = Parameter(parm=self.node.parm('specular_control'))
        self.parm_specular = Parameter(parm=self.node.parm('specular'))
        self.parm_specular_color_control = Parameter(parm=self.node.parm('specular_color_control'))
        self.parm_specular_colorr = Parameter(parm=self.node.parm('specular_colorr'))
        self.parm_specular_colorg = Parameter(parm=self.node.parm('specular_colorg'))
        self.parm_specular_colorb = Parameter(parm=self.node.parm('specular_colorb'))
        self.parm_specular_color_file_control = Parameter(parm=self.node.parm('specular_color_file_control'))
        self.parm_specular_color_file = Parameter(parm=self.node.parm('specular_color_file'))
        self.parm_specular_roughness_control = Parameter(parm=self.node.parm('specular_roughness_control'))
        self.parm_specular_roughness = Parameter(parm=self.node.parm('specular_roughness'))
        self.parm_specular_roughness_file_control = Parameter(parm=self.node.parm('specular_roughness_file_control'))
        self.parm_specular_roughness_file = Parameter(parm=self.node.parm('specular_roughness_file'))
        self.parm_roughness_primvar_control = Parameter(parm=self.node.parm('roughness_primvar_control'))
        self.parm_roughness_primvar = Parameter(parm=self.node.parm('roughness_primvar'))
        self.parm_specular_ior_control = Parameter(parm=self.node.parm('specular_IOR_control'))
        self.parm_specular_ior = Parameter(parm=self.node.parm('specular_IOR'))
        self.parm_specular_anisotropy_control = Parameter(parm=self.node.parm('specular_anisotropy_control'))
        self.parm_specular_anisotropy = Parameter(parm=self.node.parm('specular_anisotropy'))
        self.parm_specular_rotation_control = Parameter(parm=self.node.parm('specular_rotation_control'))
        self.parm_specular_rotation = Parameter(parm=self.node.parm('specular_rotation'))
        self.parm_folder0_5 = Parameter(parm=self.node.parm('folder0_5'))
        self.parm_coat_control = Parameter(parm=self.node.parm('coat_control'))
        self.parm_coat = Parameter(parm=self.node.parm('coat'))
        self.parm_coat_color_control = Parameter(parm=self.node.parm('coat_color_control'))
        self.parm_coat_colorr = Parameter(parm=self.node.parm('coat_colorr'))
        self.parm_coat_colorg = Parameter(parm=self.node.parm('coat_colorg'))
        self.parm_coat_colorb = Parameter(parm=self.node.parm('coat_colorb'))
        self.parm_coat_color_file_control = Parameter(parm=self.node.parm('coat_color_file_control'))
        self.parm_coat_color_file = Parameter(parm=self.node.parm('coat_color_file'))
        self.parm_coat_roughness_control = Parameter(parm=self.node.parm('coat_roughness_control'))
        self.parm_coat_roughness = Parameter(parm=self.node.parm('coat_roughness'))
        self.parm_coat_roughness_file_control = Parameter(parm=self.node.parm('coat_roughness_file_control'))
        self.parm_coat_roughness_file = Parameter(parm=self.node.parm('coat_roughness_file'))
        self.parm_folder0_2 = Parameter(parm=self.node.parm('folder0_2'))
        self.parm_transmission_control = Parameter(parm=self.node.parm('transmission_control'))
        self.parm_transmission = Parameter(parm=self.node.parm('transmission'))
        self.parm_transmission_color_control = Parameter(parm=self.node.parm('transmission_color_control'))
        self.parm_transmission_colorr = Parameter(parm=self.node.parm('transmission_colorr'))
        self.parm_transmission_colorg = Parameter(parm=self.node.parm('transmission_colorg'))
        self.parm_transmission_colorb = Parameter(parm=self.node.parm('transmission_colorb'))
        self.parm_transmission_color_file_control = Parameter(parm=self.node.parm('transmission_color_file_control'))
        self.parm_transmission_color_file = Parameter(parm=self.node.parm('transmission_color_file'))
        self.parm_transmission_color_primvar_control = Parameter(parm=self.node.parm('transmission_color_primvar_control'))
        self.parm_transmission_color_primvar = Parameter(parm=self.node.parm('transmission_color_primvar'))
        self.parm_transmission_depth_control = Parameter(parm=self.node.parm('transmission_depth_control'))
        self.parm_transmission_depth = Parameter(parm=self.node.parm('transmission_depth'))
        self.parm_transmission_dispersion_control = Parameter(parm=self.node.parm('transmission_dispersion_control'))
        self.parm_transmission_dispersion = Parameter(parm=self.node.parm('transmission_dispersion'))
        self.parm_folder0_4 = Parameter(parm=self.node.parm('folder0_4'))
        self.parm_sheen_control = Parameter(parm=self.node.parm('sheen_control'))
        self.parm_sheen = Parameter(parm=self.node.parm('sheen'))
        self.parm_sheen_color_control = Parameter(parm=self.node.parm('sheen_color_control'))
        self.parm_sheen_colorr = Parameter(parm=self.node.parm('sheen_colorr'))
        self.parm_sheen_colorg = Parameter(parm=self.node.parm('sheen_colorg'))
        self.parm_sheen_colorb = Parameter(parm=self.node.parm('sheen_colorb'))
        self.parm_sheen_color_file_control = Parameter(parm=self.node.parm('sheen_color_file_control'))
        self.parm_sheen_color_file = Parameter(parm=self.node.parm('sheen_color_file'))
        self.parm_sheen_roughness_control = Parameter(parm=self.node.parm('sheen_roughness_control'))
        self.parm_sheen_roughness = Parameter(parm=self.node.parm('sheen_roughness'))
        self.parm_sheen_roughness_file_control = Parameter(parm=self.node.parm('sheen_roughness_file_control'))
        self.parm_sheen_roughness_file = Parameter(parm=self.node.parm('sheen_roughness_file'))
        self.parm_folder0_3 = Parameter(parm=self.node.parm('folder0_3'))
        self.parm_subsurface_control = Parameter(parm=self.node.parm('subsurface_control'))
        self.parm_subsurface = Parameter(parm=self.node.parm('subsurface'))
        self.parm_subsurface_color_control = Parameter(parm=self.node.parm('subsurface_color_control'))
        self.parm_subsurface_colorr = Parameter(parm=self.node.parm('subsurface_colorr'))
        self.parm_subsurface_colorg = Parameter(parm=self.node.parm('subsurface_colorg'))
        self.parm_subsurface_colorb = Parameter(parm=self.node.parm('subsurface_colorb'))
        self.parm_subsurface_color_file_control = Parameter(parm=self.node.parm('subsurface_color_file_control'))
        self.parm_subsurface_color_file = Parameter(parm=self.node.parm('subsurface_color_file'))
        self.parm_subsurface_color_primvar_control = Parameter(parm=self.node.parm('subsurface_color_primvar_control'))
        self.parm_subsurface_color_primvar = Parameter(parm=self.node.parm('subsurface_color_primvar'))
        self.parm_subsurface_radius_control = Parameter(parm=self.node.parm('subsurface_radius_control'))
        self.parm_subsurface_radiusr = Parameter(parm=self.node.parm('subsurface_radiusr'))
        self.parm_subsurface_radiusg = Parameter(parm=self.node.parm('subsurface_radiusg'))
        self.parm_subsurface_radiusb = Parameter(parm=self.node.parm('subsurface_radiusb'))
        self.parm_subsurface_scale_control = Parameter(parm=self.node.parm('subsurface_scale_control'))
        self.parm_subsurface_scale = Parameter(parm=self.node.parm('subsurface_scale'))
        self.parm_subsurface_scale_file_control = Parameter(parm=self.node.parm('subsurface_scale_file_control'))
        self.parm_subsurface_scale_file = Parameter(parm=self.node.parm('subsurface_scale_file'))
        self.parm_folder0_7 = Parameter(parm=self.node.parm('folder0_7'))
        self.parm_emission_control = Parameter(parm=self.node.parm('emission_control'))
        self.parm_emission = Parameter(parm=self.node.parm('emission'))
        self.parm_emission_color_control = Parameter(parm=self.node.parm('emission_color_control'))
        self.parm_emission_colorr = Parameter(parm=self.node.parm('emission_colorr'))
        self.parm_emission_colorg = Parameter(parm=self.node.parm('emission_colorg'))
        self.parm_emission_colorb = Parameter(parm=self.node.parm('emission_colorb'))
        self.parm_emission_color_file_control = Parameter(parm=self.node.parm('emission_color_file_control'))
        self.parm_emission_color_file = Parameter(parm=self.node.parm('emission_color_file'))
        self.parm_emission_color_primvar_control = Parameter(parm=self.node.parm('emission_color_primvar_control'))
        self.parm_emission_color_primvar = Parameter(parm=self.node.parm('emission_color_primvar'))
        self.parm_folder3_1 = Parameter(parm=self.node.parm('folder3_1'))
        self.parm_bump_style_control = Parameter(parm=self.node.parm('bump_style_control'))
        self.parm_bump_height_file_control = Parameter(parm=self.node.parm('bump_height_file_control'))
        self.parm_bump_height_file = Parameter(parm=self.node.parm('bump_height_file'))
        self.parm_bump_normal_file_control = Parameter(parm=self.node.parm('bump_normal_file_control'))
        self.parm_bump_normal_file = Parameter(parm=self.node.parm('bump_normal_file'))
        self.parm_bump_scale_control = Parameter(parm=self.node.parm('bump_scale_control'))
        self.parm_bump_scale = Parameter(parm=self.node.parm('bump_scale'))
        self.parm_true_displacements_control = Parameter(parm=self.node.parm('true_displacements_control'))
        self.parm_true_displacements = Parameter(parm=self.node.parm('true_displacements'))
        self.parm_folder0_6 = Parameter(parm=self.node.parm('folder0_6'))
        self.parm_thin_film_ior_control = Parameter(parm=self.node.parm('thin_film_IOR_control'))
        self.parm_thin_film_ior = Parameter(parm=self.node.parm('thin_film_IOR'))
        self.parm_thin_film_thickness_control = Parameter(parm=self.node.parm('thin_film_thickness_control'))
        self.parm_thin_film_thickness = Parameter(parm=self.node.parm('thin_film_thickness'))
        self.parm_thin_film_thickness_primvar_control = Parameter(parm=self.node.parm('thin_film_thickness_primvar_control'))
        self.parm_thin_film_thickness_primvar = Parameter(parm=self.node.parm('thin_film_thickness_primvar'))
        self.parm_thin_film_thickness_file_control = Parameter(parm=self.node.parm('thin_film_thickness_file_control'))
        self.parm_thin_film_thickness_file = Parameter(parm=self.node.parm('thin_film_thickness_file'))
        self.parm_folder0_8 = Parameter(parm=self.node.parm('folder0_8'))
        self.parm_thin_walled_control = Parameter(parm=self.node.parm('thin_walled_control'))
        self.parm_thin_walled = Parameter(parm=self.node.parm('thin_walled'))
        self.parm_opacity_control = Parameter(parm=self.node.parm('opacity_control'))
        self.parm_opacityr = Parameter(parm=self.node.parm('opacityr'))
        self.parm_opacityg = Parameter(parm=self.node.parm('opacityg'))
        self.parm_opacityb = Parameter(parm=self.node.parm('opacityb'))
        self.parm_opacity_file_control = Parameter(parm=self.node.parm('opacity_file_control'))
        self.parm_opacity_file = Parameter(parm=self.node.parm('opacity_file'))
        self.parm_opacity_primvar_control = Parameter(parm=self.node.parm('opacity_primvar_control'))
        self.parm_opacity_primvar = Parameter(parm=self.node.parm('opacity_primvar'))
        self.parm_folder0_9 = Parameter(parm=self.node.parm('folder0_9'))
        self.parm_filtertype_control = Parameter(parm=self.node.parm('filtertype_control'))
        self.parm_projection_control = Parameter(parm=self.node.parm('projection_control'))
        self.parm_uv_offset_control = Parameter(parm=self.node.parm('uv_offset_control'))
        self.parm_uv_offset1 = Parameter(parm=self.node.parm('uv_offset1'))
        self.parm_uv_offset2 = Parameter(parm=self.node.parm('uv_offset2'))
        self.parm_uv_scale_control = Parameter(parm=self.node.parm('uv_scale_control'))
        self.parm_uv_scale1 = Parameter(parm=self.node.parm('uv_scale1'))
        self.parm_uv_scale2 = Parameter(parm=self.node.parm('uv_scale2'))
        self.parm_uv_primvar_control = Parameter(parm=self.node.parm('uv_primvar_control'))
        self.parm_uv_primvar = Parameter(parm=self.node.parm('uv_primvar'))
        self.parm_triplanar_blend_control = Parameter(parm=self.node.parm('triplanar_blend_control'))
        self.parm_triplanar_blend = Parameter(parm=self.node.parm('triplanar_blend'))
        self.parm_triplanar_upaxis_control = Parameter(parm=self.node.parm('triplanar_upaxis_control'))
        self.parm_displacement_control = Parameter(parm=self.node.parm('displacement_control'))
        self.parm_displacement = Parameter(parm=self.node.parm('displacement'))
        self.parm_maps_copnet = Parameter(parm=self.node.parm('maps_copnet'))

        
        # parm menu vars:
        self.parm_sample_behavior = SampleBehaviorMenu(parm=self.node.parm('sample_behavior'))
        self.parm_sample_shuttermode = SampleShuttermodeMenu(parm=self.node.parm('sample_shuttermode'))
        self.parm_reftype = ReftypeMenu(parm=self.node.parm('reftype'))
        self.parm_initforedit = InitforeditMenu(parm=self.node.parm('initforedit'))
        self.parm_parentprimtype = ParentprimtypeMenu(parm=self.node.parm('parentprimtype'))
        self.parm_bump_style = BumpStyleMenu(parm=self.node.parm('bump_style'))
        self.parm_filtertype = FiltertypeMenu(parm=self.node.parm('filtertype'))
        self.parm_projection = ProjectionMenu(parm=self.node.parm('projection'))
        self.parm_triplanar_upaxis = TriplanarUpaxisMenu(parm=self.node.parm('triplanar_upaxis'))


        # input vars:
        self.input_input_stage = 'Input Stage'


# parm menu classes:
class SampleBehaviorMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_sample_current_frame = ("single", 0)
        self.menu_sample_frame_range_if_input_is_not_time_dependent = ("timedep", 1)
        self.menu_sample_frame_range = ("multi", 2)


class SampleShuttermodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_use_camera_prim = ("cameraprim", 0)
        self.menu_specify_manually = ("manual", 1)


class ReftypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("none", 0)
        self.menu_reference = ("reference", 1)
        self.menu_inherit = ("inherit", 2)
        self.menu_specialize = ("specialize", 3)
        self.menu_reference_file = ("reffile", 4)
        self.menu_create_class = ("createclass", 5)


class InitforeditMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_set_all_parameters_to_do_nothing = ("setdonothing", 0)
        self.menu_set_all_parameters_to_set_or_create = ("setsetorcreate", 1)
        self.menu_set__do_nothing__parameter_values_from_usd_primitive = ("initdonothingfromprim", 2)
        self.menu_set_all_parameter_values_from_usd_primitive = ("initallfromprim", 3)


class ParentprimtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("", 0)
        self.menu_xform = ("UsdGeomXform", 1)
        self.menu_scope = ("UsdGeomScope", 2)


class BumpStyleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_height = ("0", 0)
        self.menu_normal = ("1", 1)


class FiltertypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_closest = ("closest", 0)
        self.menu_linear = ("linear", 1)
        self.menu_cubic = ("cubic", 2)


class ProjectionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uv = ("0", 0)
        self.menu_tri_planar = ("1", 1)


class TriplanarUpaxisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x = ("0", 0)
        self.menu_y = ("1", 1)
        self.menu_z = ("2", 2)



