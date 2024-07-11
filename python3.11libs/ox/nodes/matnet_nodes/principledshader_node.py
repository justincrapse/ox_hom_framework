from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class PrincipledshaderNode(OXNode):
    node_type = 'principledshader::2.0'
    parm_lookup_dict = {'specmodel': 'specmodel', 'coatspecmodel': 'coatspecmodel', 'specular_tint': 'specular_tint', 'diffuse_folder_151': 'diffuse_folder_151', 'folder7': 'folder7', 'basecolorr': 'basecolorr', 'basecolorg': 'basecolorg', 'basecolorb': 'basecolorb', 'albedomult': 'albedomult', 'basecolor_usepointcolor': 'basecolor_usePointColor', 'basecolor_usepackedcolor': 'basecolor_usePackedColor', 'frontface': 'frontface', 'folder4': 'folder4', 'ior': 'ior', 'rough': 'rough', 'aniso': 'aniso', 'anisodir': 'anisodir', 'folder12': 'folder12', 'metallic': 'metallic', 'reflect': 'reflect', 'reflecttint': 'reflecttint', 'coat': 'coat', 'coatrough': 'coatrough', 'folder13': 'folder13', 'transparency': 'transparency', 'transcolorr': 'transcolorr', 'transcolorg': 'transcolorg', 'transcolorb': 'transcolorb', 'transdist': 'transdist', 'dispersion': 'dispersion', 'priority': 'priority', 'transcolor_usepointcolor': 'transcolor_usePointColor', 'folder8': 'folder8', 'sss': 'sss', 'ssscolorr': 'ssscolorr', 'ssscolorg': 'ssscolorg', 'ssscolorb': 'ssscolorb', 'sssmodel': 'sssmodel', 'sssdist': 'sssdist', 'sssphase': 'sssphase', 'ssscolor_usepointcolor': 'ssscolor_usePointColor', 'folder11': 'folder11', 'sheen': 'sheen', 'sheentint': 'sheentint', 'folder9': 'folder9', 'emitint': 'emitint', 'emitcolorr': 'emitcolorr', 'emitcolorg': 'emitcolorg', 'emitcolorb': 'emitcolorb', 'emitcolor_usepointcolor': 'emitcolor_usePointColor', 'emitillum': 'emitillum', 'folder15': 'folder15', 'opac': 'opac', 'opaccolorr': 'opaccolorr', 'opaccolorg': 'opaccolorg', 'opaccolorb': 'opaccolorb', 'opacpointalpha': 'opacpointalpha', 'opacpackedalpha': 'opacpackedalpha', 'folder6': 'folder6', 'fakecausticsenabled': 'fakecausticsenabled', 'fakecausticstransmit': 'fakecausticstransmit', 'fakecausticsshadow': 'fakecausticsshadow', 'fakecausticsopacity': 'fakecausticsopacity', 'folder17': 'folder17', 'alphablendmode': 'alphablendmode', 'alphacutoff': 'alphacutoff', 'folder54': 'folder54', 'basecolor_usetexture': 'basecolor_useTexture', 'basecolor_texture': 'basecolor_texture', 'basecolor_textureintensity': 'basecolor_textureIntensity', 'basecolor_texturewrap': 'basecolor_textureWrap', 'basecolor_texturecolorspace': 'basecolor_textureColorSpace', 'basecolor_usetexturealpha': 'basecolor_useTextureAlpha', 'folder1': 'folder1', 'ior_usetexture': 'ior_useTexture', 'ior_texture': 'ior_texture', 'ior_monochannel': 'ior_monoChannel', 'ior_texturewrap': 'ior_textureWrap', 'ior_texturecolorspace': 'ior_textureColorSpace', 'folder227': 'folder227', 'rough_usetexture': 'rough_useTexture', 'rough_texture': 'rough_texture', 'rough_monochannel': 'rough_monoChannel', 'rough_texturewrap': 'rough_textureWrap', 'rough_texturecolorspace': 'rough_textureColorSpace', 'folder228': 'folder228', 'aniso_usetexture': 'aniso_useTexture', 'aniso_texture': 'aniso_texture', 'aniso_monochannel': 'aniso_monoChannel', 'aniso_texturewrap': 'aniso_textureWrap', 'aniso_texturecolorspace': 'aniso_textureColorSpace', 'folder229': 'folder229', 'anisodir_usetexture': 'anisodir_useTexture', 'anisodir_texture': 'anisodir_texture', 'anisodir_monochannel': 'anisodir_monoChannel', 'anisodir_texturewrap': 'anisodir_textureWrap', 'anisodir_texturecolorspace': 'anisodir_textureColorSpace', 'anisodir_texturefilter': 'anisodir_textureFilter', 'folder55': 'folder55', 'metallic_usetexture': 'metallic_useTexture', 'metallic_texture': 'metallic_texture', 'metallic_monochannel': 'metallic_monoChannel', 'metallic_texturewrap': 'metallic_textureWrap', 'metallic_texturecolorspace': 'metallic_textureColorSpace', 'folder16': 'folder16', 'reflect_usetexture': 'reflect_useTexture', 'reflect_texture': 'reflect_texture', 'reflect_monochannel': 'reflect_monoChannel', 'reflect_texturewrap': 'reflect_textureWrap', 'reflect_texturecolorspace': 'reflect_textureColorSpace', 'folder226': 'folder226', 'reflecttint_usetexture': 'reflecttint_useTexture', 'reflecttint_texture': 'reflecttint_texture', 'reflecttint_monochannel': 'reflecttint_monoChannel', 'reflecttint_texturewrap': 'reflecttint_textureWrap', 'reflecttint_texturecolorspace': 'reflecttint_textureColorSpace', 'folder233': 'folder233', 'coat_usetexture': 'coat_useTexture', 'coat_texture': 'coat_texture', 'coat_monochannel': 'coat_monoChannel', 'coat_texturewrap': 'coat_textureWrap', 'coat_texturecolorspace': 'coat_textureColorSpace', 'folder234': 'folder234', 'coatrough_usetexture': 'coatrough_useTexture', 'coatrough_texture': 'coatrough_texture', 'coatrough_monochannel': 'coatrough_monoChannel', 'coatrough_texturewrap': 'coatrough_textureWrap', 'coatrough_texturecolorspace': 'coatrough_textureColorSpace', 'folder2': 'folder2', 'transparency_usetexture': 'transparency_useTexture', 'transparency_texture': 'transparency_texture', 'transparency_monochannel': 'transparency_monoChannel', 'transparency_texturewrap': 'transparency_textureWrap', 'transparency_texturecolorspace': 'transparency_textureColorSpace', 'folder5': 'folder5', 'transcolor_usetexture': 'transcolor_useTexture', 'transcolor_texture': 'transcolor_texture', 'transcolor_textureintensity': 'transcolor_textureIntensity', 'transcolor_texturewrap': 'transcolor_textureWrap', 'transcolor_texturecolorspace': 'transcolor_textureColorSpace', 'folder5_1': 'folder5_1', 'transdist_usetexture': 'transdist_useTexture', 'transdist_texture': 'transdist_texture', 'transdist_monochannel': 'transdist_monoChannel', 'transdist_texturewrap': 'transdist_textureWrap', 'transdist_texturecolorspace': 'transdist_textureColorSpace', 'folder5_2': 'folder5_2', 'dispersion_usetexture': 'dispersion_useTexture', 'dispersion_texture': 'dispersion_texture', 'dispersion_monochannel': 'dispersion_monoChannel', 'dispersion_texturewrap': 'dispersion_textureWrap', 'dispersion_texturecolorspace': 'dispersion_textureColorSpace', 'folder230': 'folder230', 'sss_usetexture': 'sss_useTexture', 'sss_texture': 'sss_texture', 'sss_monochannel': 'sss_monoChannel', 'sss_texturewrap': 'sss_textureWrap', 'sss_texturecolorspace': 'sss_textureColorSpace', 'folder3': 'folder3', 'sssdist_usetexture': 'sssdist_useTexture', 'sssdist_texture': 'sssdist_texture', 'sssdist_monochannel': 'sssdist_monoChannel', 'sssdist_texturewrap': 'sssdist_textureWrap', 'sssdist_texturecolorspace': 'sssdist_textureColorSpace', 'folder3_1': 'folder3_1', 'ssscolor_usetexture': 'ssscolor_useTexture', 'ssscolor_texture': 'ssscolor_texture', 'ssscolor_texturewrap': 'ssscolor_textureWrap', 'ssscolor_texturecolorspace': 'ssscolor_textureColorSpace', 'folder231': 'folder231', 'sheen_usetexture': 'sheen_useTexture', 'sheen_texture': 'sheen_texture', 'sheen_monochannel': 'sheen_monoChannel', 'sheen_texturewrap': 'sheen_textureWrap', 'sheen_texturecolorspace': 'sheen_textureColorSpace', 'folder232': 'folder232', 'sheentint_usetexture': 'sheentint_useTexture', 'sheentint_texture': 'sheentint_texture', 'sheentint_monochannel': 'sheentint_monoChannel', 'sheentint_texturewrap': 'sheentint_textureWrap', 'sheentint_texturecolorspace': 'sheentint_textureColorSpace', 'diffuse_folder_14_3': 'diffuse_folder_14_3', 'emitcolor_usetexture': 'emitcolor_useTexture', 'emitcolor_texture': 'emitcolor_texture', 'emitcolor_textureintensity': 'emitcolor_textureIntensity', 'emitcolor_texturewrap': 'emitcolor_textureWrap', 'emitcolor_texturecolorspace': 'emitcolor_textureColorSpace', 'folder14': 'folder14', 'opaccolor_usetexture': 'opaccolor_useTexture', 'opaccolor_texture': 'opaccolor_texture', 'opaccolor_texturewrap': 'opaccolor_textureWrap', 'opaccolor_textureintensity': 'opaccolor_textureIntensity', 'opaccolor_texturecolorspace': 'opaccolor_textureColorSpace', 'folder18': 'folder18', 'occlusion_usetexture': 'occlusion_useTexture', 'occlusion_texture': 'occlusion_texture', 'occlusion_texturewrap': 'occlusion_textureWrap', 'occlusion_textureintensity': 'occlusion_textureIntensity', 'occlusion_texturecolorspace': 'occlusion_textureColorSpace', 'folder235': 'folder235', 'surface_texturefilter': 'surface_textureFilter', 'surface_texturefilterwidth': 'surface_textureFilterWidth', 'roundededge_enable': 'roundedEdge_enable', 'roundededge_radius': 'roundedEdge_radius', 'roundededge_mode': 'roundedEdge_mode', 'shading_161': 'shading_161', 'basebumpandnormal_enable': 'baseBumpAndNormal_enable', 'basebumpandnormal_type': 'baseBumpAndNormal_type', 'basebump_colorspace': 'baseBump_colorSpace', 'basebump_bumpscale': 'baseBump_bumpScale', 'basebump_bumptexture': 'baseBump_bumpTexture', 'basebump_wrap': 'baseBump_wrap', 'basebump_filter': 'baseBump_filter', 'basebump_filterwidth': 'baseBump_filterWidth', 'basebump_channel': 'baseBump_channel', 'basebump_imageplane': 'baseBump_imagePlane', 'basenormal_colorspace': 'baseNormal_colorspace', 'basenormal_vectorspace': 'baseNormal_vectorSpace', 'basenormal_scale': 'baseNormal_scale', 'basenormal_texture': 'baseNormal_texture', 'basenormal_wrap': 'baseNormal_wrap', 'basenormal_filter': 'baseNormal_filter', 'basenormal_filterwidth': 'baseNormal_filterWidth', 'basenormal_channel': 'baseNormal_channel', 'basenormal_imageplane': 'baseNormal_imagePlane', 'basenormal_space': 'baseNormal_space', 'basenormal_flipx': 'baseNormal_flipX', 'basenormal_flipy': 'baseNormal_flipY', 'basebump_usetexture': 'baseBump_useTexture', 'basenormal_usetexture': 'baseNormal_useTexture', 'separatecoatnormals': 'separateCoatNormals', 'coatbumpandnormal_enable': 'coatBumpAndNormal_enable', 'coatbumpandnormal_type': 'coatBumpAndNormal_type', 'coatbump_colorspace': 'coatBump_colorSpace', 'coatbump_bumpscale': 'coatBump_bumpScale', 'coatbump_bumptexture': 'coatBump_bumpTexture', 'coatbump_wrap': 'coatBump_wrap', 'coatbump_filter': 'coatBump_filter', 'coatbump_filterwidth': 'coatBump_filterWidth', 'coatbump_channel': 'coatBump_channel', 'coatbump_imageplane': 'coatBump_imagePlane', 'coatnormal_colorspace': 'coatNormal_colorspace', 'coatnormal_vectorspace': 'coatNormal_vectorSpace', 'coatnormal_scale': 'coatNormal_scale', 'coatnormal_texture': 'coatNormal_texture', 'coatnormal_wrap': 'coatNormal_wrap', 'coatnormal_filter': 'coatNormal_filter', 'coatnormal_filterwidth': 'coatNormal_filterWidth', 'coatnormal_channel': 'coatNormal_channel', 'coatnormal_imageplane': 'coatNormal_imagePlane', 'coatnormal_space': 'coatNormal_space', 'coatnormal_flipx': 'coatNormal_flipX', 'coatnormal_flipy': 'coatNormal_flipY', 'shop_disable_displace_shader': 'shop_disable_displace_shader', 'folder236': 'folder236', 'vm_displacebound': 'vm_displacebound', 'vm_truedisplace': 'vm_truedisplace', 'vm_bumpraydisplace': 'vm_bumpraydisplace', 'folder10': 'folder10', 'dispinput_enable': 'dispInput_enable', 'dispinput_max': 'dispInput_max', 'dispinput_vectorspace': 'dispInput_vectorspace', 'folder237': 'folder237', 'disptex_enable': 'dispTex_enable', 'disptex_type': 'dispTex_type', 'disptex_colorspace': 'dispTex_colorSpace', 'disptex_vectorspace': 'dispTex_vectorSpace', 'disptex_channelorder': 'dispTex_channelOrder', 'disptex_offset': 'dispTex_offset', 'disptex_scale': 'dispTex_scale', 'disptex_texture': 'dispTex_texture', 'disptex_channel': 'dispTex_channel', 'disptex_wrap': 'dispTex_wrap', 'disptex_filter': 'dispTex_filter', 'disptex_filterwidth': 'dispTex_filterWidth', 'folder238': 'folder238', 'dispnoise_enable': 'dispNoise_enable', 'dispnoise_type': 'dispNoise_type', 'dispnoise_freq1': 'dispNoise_freq1', 'dispnoise_freq2': 'dispNoise_freq2', 'dispnoise_freq3': 'dispNoise_freq3', 'dispnoise_offset1': 'dispNoise_offset1', 'dispnoise_offset2': 'dispNoise_offset2', 'dispnoise_offset3': 'dispNoise_offset3', 'dispnoise_amp': 'dispNoise_amp', 'dispnoise_rough': 'dispNoise_rough', 'dispnoise_atten': 'dispNoise_atten', 'dispnoise_turb': 'dispNoise_turb', 'folder239': 'folder239', 'difflabel': 'difflabel', 'refllabel': 'refllabel', 'refractlabel': 'refractlabel', 'coatlabel': 'coatlabel', 'ssslabel': 'ssslabel', 'folder0': 'folder0', 'uvtrans1': 'uvtrans1', 'uvtrans2': 'uvtrans2', 'uvrot': 'uvrot', 'uvscale1': 'uvscale1', 'uvscale2': 'uvscale2', 'cdr': 'Cdr', 'cdg': 'Cdg', 'cdb': 'Cdb', 'alpha': 'Alpha', 'layer': 'layer', 'direct1': 'direct1', 'direct2': 'direct2', 'direct3': 'direct3', 'indirect1': 'indirect1', 'indirect2': 'indirect2', 'indirect3': 'indirect3', 'ce1': 'Ce1', 'ce2': 'Ce2', 'ce3': 'Ce3', 'direct_emission1': 'direct_emission1', 'direct_emission2': 'direct_emission2', 'direct_emission3': 'direct_emission3', 'all_emission1': 'all_emission1', 'all_emission2': 'all_emission2', 'all_emission3': 'all_emission3', 'all1': 'all1', 'all2': 'all2', 'all3': 'all3', 'indirect_emission1': 'indirect_emission1', 'indirect_emission2': 'indirect_emission2', 'indirect_emission3': 'indirect_emission3', 'direct_comp': 'direct_comp', 'indirect_comp': 'indirect_comp', 'all_comp': 'all_comp', 'direct_noshadow1': 'direct_noshadow1', 'direct_noshadow2': 'direct_noshadow2', 'direct_noshadow3': 'direct_noshadow3', 'direct_shadow1': 'direct_shadow1', 'direct_shadow2': 'direct_shadow2', 'direct_shadow3': 'direct_shadow3', 'indirect_noshadow1': 'indirect_noshadow1', 'indirect_noshadow2': 'indirect_noshadow2', 'indirect_noshadow3': 'indirect_noshadow3', 'indirect_shadow1': 'indirect_shadow1', 'indirect_shadow2': 'indirect_shadow2', 'indirect_shadow3': 'indirect_shadow3', 'level': 'level', 'diffuselevel': 'diffuselevel', 'specularlevel': 'specularlevel', 'volumelevel': 'volumelevel', 'direct_samples': 'direct_samples', 'indirect_samples': 'indirect_samples', 'nlights': 'nlights', 'direct_noshadow_comp': 'direct_noshadow_comp', 'indirect_noshadow_comp': 'indirect_noshadow_comp', 'nddispersion': 'nddispersion', 'ndpriority': 'ndpriority', 'ndior': 'ndior', 'absorption1': 'absorption1', 'absorption2': 'absorption2', 'absorption3': 'absorption3', 'oc1': 'Oc1', 'oc2': 'Oc2', 'oc3': 'Oc3', 'cv1': 'Cv1', 'cv2': 'Cv2', 'cv3': 'Cv3', 'th1': 'Th1', 'th2': 'Th2', 'th3': 'Th3', 'ab1': 'Ab1', 'ab2': 'Ab2', 'ab3': 'Ab3', 'cu1': 'Cu1', 'cu2': 'Cu2', 'cu3': 'Cu3', 'vd1': 'Vd1', 'vd2': 'Vd2', 'vd3': 'Vd3', 'nt1': 'Nt1', 'nt2': 'Nt2', 'nt3': 'Nt3', 'ds1': 'Ds1', 'ds2': 'Ds2', 'ds3': 'Ds3', 'pre_disp_p1': 'pre_disp_P1', 'pre_disp_p2': 'pre_disp_P2', 'pre_disp_p3': 'pre_disp_P3', 'pre_disp_utan1': 'pre_disp_utan1', 'pre_disp_utan2': 'pre_disp_utan2', 'pre_disp_utan3': 'pre_disp_utan3', 'pre_disp_vtan1': 'pre_disp_vtan1', 'pre_disp_vtan2': 'pre_disp_vtan2', 'pre_disp_vtan3': 'pre_disp_vtan3', 'pre_disp_n1': 'pre_disp_N1', 'pre_disp_n2': 'pre_disp_N2', 'pre_disp_n3': 'pre_disp_N3', 'disp': 'disp', 'vdisp1': 'vdisp1', 'vdisp2': 'vdisp2', 'vdisp3': 'vdisp3', 'dt1': 'Dt1', 'dt2': 'Dt2', 'dt3': 'Dt3', 'vdt1': 'Vdt1', 'vdt2': 'Vdt2', 'vdt3': 'Vdt3', 'basen1': 'baseN1', 'basen2': 'baseN2', 'basen3': 'baseN3', 'coatn1': 'coatN1', 'coatn2': 'coatN2', 'coatn3': 'coatN3', 'speccolorr': 'speccolorr', 'speccolorg': 'speccolorg', 'speccolorb': 'speccolorb', 'displaycolorr': 'displayColorr', 'displaycolorg': 'displayColorg', 'displaycolorb': 'displayColorb', 'st1': 'st1', 'st2': 'st2', 'displayopacity': 'displayOpacity'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_specmodel = Parameter(parm=self.node.parm('specmodel'))
        self.parm_coatspecmodel = Parameter(parm=self.node.parm('coatspecmodel'))
        self.parm_specular_tint = Parameter(parm=self.node.parm('specular_tint'))
        self.parm_diffuse_folder_151 = Parameter(parm=self.node.parm('diffuse_folder_151'))
        self.parm_folder7 = Parameter(parm=self.node.parm('folder7'))
        self.parm_basecolorr = Parameter(parm=self.node.parm('basecolorr'))
        self.parm_basecolorg = Parameter(parm=self.node.parm('basecolorg'))
        self.parm_basecolorb = Parameter(parm=self.node.parm('basecolorb'))
        self.parm_albedomult = Parameter(parm=self.node.parm('albedomult'))
        self.parm_basecolor_usepointcolor = Parameter(parm=self.node.parm('basecolor_usePointColor'))
        self.parm_basecolor_usepackedcolor = Parameter(parm=self.node.parm('basecolor_usePackedColor'))
        self.parm_frontface = Parameter(parm=self.node.parm('frontface'))
        self.parm_folder4 = Parameter(parm=self.node.parm('folder4'))
        self.parm_ior = Parameter(parm=self.node.parm('ior'))
        self.parm_rough = Parameter(parm=self.node.parm('rough'))
        self.parm_aniso = Parameter(parm=self.node.parm('aniso'))
        self.parm_anisodir = Parameter(parm=self.node.parm('anisodir'))
        self.parm_folder12 = Parameter(parm=self.node.parm('folder12'))
        self.parm_metallic = Parameter(parm=self.node.parm('metallic'))
        self.parm_reflect = Parameter(parm=self.node.parm('reflect'))
        self.parm_reflecttint = Parameter(parm=self.node.parm('reflecttint'))
        self.parm_coat = Parameter(parm=self.node.parm('coat'))
        self.parm_coatrough = Parameter(parm=self.node.parm('coatrough'))
        self.parm_folder13 = Parameter(parm=self.node.parm('folder13'))
        self.parm_transparency = Parameter(parm=self.node.parm('transparency'))
        self.parm_transcolorr = Parameter(parm=self.node.parm('transcolorr'))
        self.parm_transcolorg = Parameter(parm=self.node.parm('transcolorg'))
        self.parm_transcolorb = Parameter(parm=self.node.parm('transcolorb'))
        self.parm_transdist = Parameter(parm=self.node.parm('transdist'))
        self.parm_dispersion = Parameter(parm=self.node.parm('dispersion'))
        self.parm_priority = Parameter(parm=self.node.parm('priority'))
        self.parm_transcolor_usepointcolor = Parameter(parm=self.node.parm('transcolor_usePointColor'))
        self.parm_folder8 = Parameter(parm=self.node.parm('folder8'))
        self.parm_sss = Parameter(parm=self.node.parm('sss'))
        self.parm_ssscolorr = Parameter(parm=self.node.parm('ssscolorr'))
        self.parm_ssscolorg = Parameter(parm=self.node.parm('ssscolorg'))
        self.parm_ssscolorb = Parameter(parm=self.node.parm('ssscolorb'))
        self.parm_sssdist = Parameter(parm=self.node.parm('sssdist'))
        self.parm_sssphase = Parameter(parm=self.node.parm('sssphase'))
        self.parm_ssscolor_usepointcolor = Parameter(parm=self.node.parm('ssscolor_usePointColor'))
        self.parm_folder11 = Parameter(parm=self.node.parm('folder11'))
        self.parm_sheen = Parameter(parm=self.node.parm('sheen'))
        self.parm_sheentint = Parameter(parm=self.node.parm('sheentint'))
        self.parm_folder9 = Parameter(parm=self.node.parm('folder9'))
        self.parm_emitint = Parameter(parm=self.node.parm('emitint'))
        self.parm_emitcolorr = Parameter(parm=self.node.parm('emitcolorr'))
        self.parm_emitcolorg = Parameter(parm=self.node.parm('emitcolorg'))
        self.parm_emitcolorb = Parameter(parm=self.node.parm('emitcolorb'))
        self.parm_emitcolor_usepointcolor = Parameter(parm=self.node.parm('emitcolor_usePointColor'))
        self.parm_emitillum = Parameter(parm=self.node.parm('emitillum'))
        self.parm_folder15 = Parameter(parm=self.node.parm('folder15'))
        self.parm_opac = Parameter(parm=self.node.parm('opac'))
        self.parm_opaccolorr = Parameter(parm=self.node.parm('opaccolorr'))
        self.parm_opaccolorg = Parameter(parm=self.node.parm('opaccolorg'))
        self.parm_opaccolorb = Parameter(parm=self.node.parm('opaccolorb'))
        self.parm_opacpointalpha = Parameter(parm=self.node.parm('opacpointalpha'))
        self.parm_opacpackedalpha = Parameter(parm=self.node.parm('opacpackedalpha'))
        self.parm_folder6 = Parameter(parm=self.node.parm('folder6'))
        self.parm_fakecausticsenabled = Parameter(parm=self.node.parm('fakecausticsenabled'))
        self.parm_fakecausticstransmit = Parameter(parm=self.node.parm('fakecausticstransmit'))
        self.parm_fakecausticsshadow = Parameter(parm=self.node.parm('fakecausticsshadow'))
        self.parm_fakecausticsopacity = Parameter(parm=self.node.parm('fakecausticsopacity'))
        self.parm_folder17 = Parameter(parm=self.node.parm('folder17'))
        self.parm_alphacutoff = Parameter(parm=self.node.parm('alphacutoff'))
        self.parm_folder54 = Parameter(parm=self.node.parm('folder54'))
        self.parm_basecolor_usetexture = Parameter(parm=self.node.parm('basecolor_useTexture'))
        self.parm_basecolor_texture = Parameter(parm=self.node.parm('basecolor_texture'))
        self.parm_basecolor_textureintensity = Parameter(parm=self.node.parm('basecolor_textureIntensity'))
        self.parm_basecolor_usetexturealpha = Parameter(parm=self.node.parm('basecolor_useTextureAlpha'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_ior_usetexture = Parameter(parm=self.node.parm('ior_useTexture'))
        self.parm_ior_texture = Parameter(parm=self.node.parm('ior_texture'))
        self.parm_folder227 = Parameter(parm=self.node.parm('folder227'))
        self.parm_rough_usetexture = Parameter(parm=self.node.parm('rough_useTexture'))
        self.parm_rough_texture = Parameter(parm=self.node.parm('rough_texture'))
        self.parm_folder228 = Parameter(parm=self.node.parm('folder228'))
        self.parm_aniso_usetexture = Parameter(parm=self.node.parm('aniso_useTexture'))
        self.parm_aniso_texture = Parameter(parm=self.node.parm('aniso_texture'))
        self.parm_folder229 = Parameter(parm=self.node.parm('folder229'))
        self.parm_anisodir_usetexture = Parameter(parm=self.node.parm('anisodir_useTexture'))
        self.parm_anisodir_texture = Parameter(parm=self.node.parm('anisodir_texture'))
        self.parm_folder55 = Parameter(parm=self.node.parm('folder55'))
        self.parm_metallic_usetexture = Parameter(parm=self.node.parm('metallic_useTexture'))
        self.parm_metallic_texture = Parameter(parm=self.node.parm('metallic_texture'))
        self.parm_folder16 = Parameter(parm=self.node.parm('folder16'))
        self.parm_reflect_usetexture = Parameter(parm=self.node.parm('reflect_useTexture'))
        self.parm_reflect_texture = Parameter(parm=self.node.parm('reflect_texture'))
        self.parm_folder226 = Parameter(parm=self.node.parm('folder226'))
        self.parm_reflecttint_usetexture = Parameter(parm=self.node.parm('reflecttint_useTexture'))
        self.parm_reflecttint_texture = Parameter(parm=self.node.parm('reflecttint_texture'))
        self.parm_folder233 = Parameter(parm=self.node.parm('folder233'))
        self.parm_coat_usetexture = Parameter(parm=self.node.parm('coat_useTexture'))
        self.parm_coat_texture = Parameter(parm=self.node.parm('coat_texture'))
        self.parm_folder234 = Parameter(parm=self.node.parm('folder234'))
        self.parm_coatrough_usetexture = Parameter(parm=self.node.parm('coatrough_useTexture'))
        self.parm_coatrough_texture = Parameter(parm=self.node.parm('coatrough_texture'))
        self.parm_folder2 = Parameter(parm=self.node.parm('folder2'))
        self.parm_transparency_usetexture = Parameter(parm=self.node.parm('transparency_useTexture'))
        self.parm_transparency_texture = Parameter(parm=self.node.parm('transparency_texture'))
        self.parm_folder5 = Parameter(parm=self.node.parm('folder5'))
        self.parm_transcolor_usetexture = Parameter(parm=self.node.parm('transcolor_useTexture'))
        self.parm_transcolor_texture = Parameter(parm=self.node.parm('transcolor_texture'))
        self.parm_transcolor_textureintensity = Parameter(parm=self.node.parm('transcolor_textureIntensity'))
        self.parm_folder5_1 = Parameter(parm=self.node.parm('folder5_1'))
        self.parm_transdist_usetexture = Parameter(parm=self.node.parm('transdist_useTexture'))
        self.parm_transdist_texture = Parameter(parm=self.node.parm('transdist_texture'))
        self.parm_folder5_2 = Parameter(parm=self.node.parm('folder5_2'))
        self.parm_dispersion_usetexture = Parameter(parm=self.node.parm('dispersion_useTexture'))
        self.parm_dispersion_texture = Parameter(parm=self.node.parm('dispersion_texture'))
        self.parm_folder230 = Parameter(parm=self.node.parm('folder230'))
        self.parm_sss_usetexture = Parameter(parm=self.node.parm('sss_useTexture'))
        self.parm_sss_texture = Parameter(parm=self.node.parm('sss_texture'))
        self.parm_folder3 = Parameter(parm=self.node.parm('folder3'))
        self.parm_sssdist_usetexture = Parameter(parm=self.node.parm('sssdist_useTexture'))
        self.parm_sssdist_texture = Parameter(parm=self.node.parm('sssdist_texture'))
        self.parm_folder3_1 = Parameter(parm=self.node.parm('folder3_1'))
        self.parm_ssscolor_usetexture = Parameter(parm=self.node.parm('ssscolor_useTexture'))
        self.parm_ssscolor_texture = Parameter(parm=self.node.parm('ssscolor_texture'))
        self.parm_folder231 = Parameter(parm=self.node.parm('folder231'))
        self.parm_sheen_usetexture = Parameter(parm=self.node.parm('sheen_useTexture'))
        self.parm_sheen_texture = Parameter(parm=self.node.parm('sheen_texture'))
        self.parm_folder232 = Parameter(parm=self.node.parm('folder232'))
        self.parm_sheentint_usetexture = Parameter(parm=self.node.parm('sheentint_useTexture'))
        self.parm_sheentint_texture = Parameter(parm=self.node.parm('sheentint_texture'))
        self.parm_diffuse_folder_14_3 = Parameter(parm=self.node.parm('diffuse_folder_14_3'))
        self.parm_emitcolor_usetexture = Parameter(parm=self.node.parm('emitcolor_useTexture'))
        self.parm_emitcolor_texture = Parameter(parm=self.node.parm('emitcolor_texture'))
        self.parm_emitcolor_textureintensity = Parameter(parm=self.node.parm('emitcolor_textureIntensity'))
        self.parm_folder14 = Parameter(parm=self.node.parm('folder14'))
        self.parm_opaccolor_usetexture = Parameter(parm=self.node.parm('opaccolor_useTexture'))
        self.parm_opaccolor_texture = Parameter(parm=self.node.parm('opaccolor_texture'))
        self.parm_opaccolor_textureintensity = Parameter(parm=self.node.parm('opaccolor_textureIntensity'))
        self.parm_folder18 = Parameter(parm=self.node.parm('folder18'))
        self.parm_occlusion_usetexture = Parameter(parm=self.node.parm('occlusion_useTexture'))
        self.parm_occlusion_texture = Parameter(parm=self.node.parm('occlusion_texture'))
        self.parm_occlusion_textureintensity = Parameter(parm=self.node.parm('occlusion_textureIntensity'))
        self.parm_folder235 = Parameter(parm=self.node.parm('folder235'))
        self.parm_surface_texturefilterwidth = Parameter(parm=self.node.parm('surface_textureFilterWidth'))
        self.parm_roundededge_enable = Parameter(parm=self.node.parm('roundedEdge_enable'))
        self.parm_roundededge_radius = Parameter(parm=self.node.parm('roundedEdge_radius'))
        self.parm_shading_161 = Parameter(parm=self.node.parm('shading_161'))
        self.parm_basebumpandnormal_enable = Parameter(parm=self.node.parm('baseBumpAndNormal_enable'))
        self.parm_basebump_bumpscale = Parameter(parm=self.node.parm('baseBump_bumpScale'))
        self.parm_basebump_bumptexture = Parameter(parm=self.node.parm('baseBump_bumpTexture'))
        self.parm_basebump_filterwidth = Parameter(parm=self.node.parm('baseBump_filterWidth'))
        self.parm_basebump_imageplane = Parameter(parm=self.node.parm('baseBump_imagePlane'))
        self.parm_basenormal_scale = Parameter(parm=self.node.parm('baseNormal_scale'))
        self.parm_basenormal_texture = Parameter(parm=self.node.parm('baseNormal_texture'))
        self.parm_basenormal_filterwidth = Parameter(parm=self.node.parm('baseNormal_filterWidth'))
        self.parm_basenormal_imageplane = Parameter(parm=self.node.parm('baseNormal_imagePlane'))
        self.parm_basenormal_flipx = Parameter(parm=self.node.parm('baseNormal_flipX'))
        self.parm_basenormal_flipy = Parameter(parm=self.node.parm('baseNormal_flipY'))
        self.parm_basebump_usetexture = Parameter(parm=self.node.parm('baseBump_useTexture'))
        self.parm_basenormal_usetexture = Parameter(parm=self.node.parm('baseNormal_useTexture'))
        self.parm_separatecoatnormals = Parameter(parm=self.node.parm('separateCoatNormals'))
        self.parm_coatbumpandnormal_enable = Parameter(parm=self.node.parm('coatBumpAndNormal_enable'))
        self.parm_coatbump_bumpscale = Parameter(parm=self.node.parm('coatBump_bumpScale'))
        self.parm_coatbump_bumptexture = Parameter(parm=self.node.parm('coatBump_bumpTexture'))
        self.parm_coatbump_filterwidth = Parameter(parm=self.node.parm('coatBump_filterWidth'))
        self.parm_coatbump_imageplane = Parameter(parm=self.node.parm('coatBump_imagePlane'))
        self.parm_coatnormal_scale = Parameter(parm=self.node.parm('coatNormal_scale'))
        self.parm_coatnormal_texture = Parameter(parm=self.node.parm('coatNormal_texture'))
        self.parm_coatnormal_filterwidth = Parameter(parm=self.node.parm('coatNormal_filterWidth'))
        self.parm_coatnormal_imageplane = Parameter(parm=self.node.parm('coatNormal_imagePlane'))
        self.parm_coatnormal_flipx = Parameter(parm=self.node.parm('coatNormal_flipX'))
        self.parm_coatnormal_flipy = Parameter(parm=self.node.parm('coatNormal_flipY'))
        self.parm_shop_disable_displace_shader = Parameter(parm=self.node.parm('shop_disable_displace_shader'))
        self.parm_folder236 = Parameter(parm=self.node.parm('folder236'))
        self.parm_vm_displacebound = Parameter(parm=self.node.parm('vm_displacebound'))
        self.parm_vm_truedisplace = Parameter(parm=self.node.parm('vm_truedisplace'))
        self.parm_vm_bumpraydisplace = Parameter(parm=self.node.parm('vm_bumpraydisplace'))
        self.parm_folder10 = Parameter(parm=self.node.parm('folder10'))
        self.parm_dispinput_enable = Parameter(parm=self.node.parm('dispInput_enable'))
        self.parm_dispinput_max = Parameter(parm=self.node.parm('dispInput_max'))
        self.parm_folder237 = Parameter(parm=self.node.parm('folder237'))
        self.parm_disptex_enable = Parameter(parm=self.node.parm('dispTex_enable'))
        self.parm_disptex_offset = Parameter(parm=self.node.parm('dispTex_offset'))
        self.parm_disptex_scale = Parameter(parm=self.node.parm('dispTex_scale'))
        self.parm_disptex_texture = Parameter(parm=self.node.parm('dispTex_texture'))
        self.parm_disptex_filterwidth = Parameter(parm=self.node.parm('dispTex_filterWidth'))
        self.parm_folder238 = Parameter(parm=self.node.parm('folder238'))
        self.parm_dispnoise_enable = Parameter(parm=self.node.parm('dispNoise_enable'))
        self.parm_dispnoise_freq1 = Parameter(parm=self.node.parm('dispNoise_freq1'))
        self.parm_dispnoise_freq2 = Parameter(parm=self.node.parm('dispNoise_freq2'))
        self.parm_dispnoise_freq3 = Parameter(parm=self.node.parm('dispNoise_freq3'))
        self.parm_dispnoise_offset1 = Parameter(parm=self.node.parm('dispNoise_offset1'))
        self.parm_dispnoise_offset2 = Parameter(parm=self.node.parm('dispNoise_offset2'))
        self.parm_dispnoise_offset3 = Parameter(parm=self.node.parm('dispNoise_offset3'))
        self.parm_dispnoise_amp = Parameter(parm=self.node.parm('dispNoise_amp'))
        self.parm_dispnoise_rough = Parameter(parm=self.node.parm('dispNoise_rough'))
        self.parm_dispnoise_atten = Parameter(parm=self.node.parm('dispNoise_atten'))
        self.parm_dispnoise_turb = Parameter(parm=self.node.parm('dispNoise_turb'))
        self.parm_folder239 = Parameter(parm=self.node.parm('folder239'))
        self.parm_difflabel = Parameter(parm=self.node.parm('difflabel'))
        self.parm_refllabel = Parameter(parm=self.node.parm('refllabel'))
        self.parm_refractlabel = Parameter(parm=self.node.parm('refractlabel'))
        self.parm_coatlabel = Parameter(parm=self.node.parm('coatlabel'))
        self.parm_ssslabel = Parameter(parm=self.node.parm('ssslabel'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_uvtrans1 = Parameter(parm=self.node.parm('uvtrans1'))
        self.parm_uvtrans2 = Parameter(parm=self.node.parm('uvtrans2'))
        self.parm_uvrot = Parameter(parm=self.node.parm('uvrot'))
        self.parm_uvscale1 = Parameter(parm=self.node.parm('uvscale1'))
        self.parm_uvscale2 = Parameter(parm=self.node.parm('uvscale2'))
        self.parm_cdr = Parameter(parm=self.node.parm('Cdr'))
        self.parm_cdg = Parameter(parm=self.node.parm('Cdg'))
        self.parm_cdb = Parameter(parm=self.node.parm('Cdb'))
        self.parm_alpha = Parameter(parm=self.node.parm('Alpha'))
        self.parm_layer = Parameter(parm=self.node.parm('layer'))
        self.parm_direct1 = Parameter(parm=self.node.parm('direct1'))
        self.parm_direct2 = Parameter(parm=self.node.parm('direct2'))
        self.parm_direct3 = Parameter(parm=self.node.parm('direct3'))
        self.parm_indirect1 = Parameter(parm=self.node.parm('indirect1'))
        self.parm_indirect2 = Parameter(parm=self.node.parm('indirect2'))
        self.parm_indirect3 = Parameter(parm=self.node.parm('indirect3'))
        self.parm_ce1 = Parameter(parm=self.node.parm('Ce1'))
        self.parm_ce2 = Parameter(parm=self.node.parm('Ce2'))
        self.parm_ce3 = Parameter(parm=self.node.parm('Ce3'))
        self.parm_direct_emission1 = Parameter(parm=self.node.parm('direct_emission1'))
        self.parm_direct_emission2 = Parameter(parm=self.node.parm('direct_emission2'))
        self.parm_direct_emission3 = Parameter(parm=self.node.parm('direct_emission3'))
        self.parm_all_emission1 = Parameter(parm=self.node.parm('all_emission1'))
        self.parm_all_emission2 = Parameter(parm=self.node.parm('all_emission2'))
        self.parm_all_emission3 = Parameter(parm=self.node.parm('all_emission3'))
        self.parm_all1 = Parameter(parm=self.node.parm('all1'))
        self.parm_all2 = Parameter(parm=self.node.parm('all2'))
        self.parm_all3 = Parameter(parm=self.node.parm('all3'))
        self.parm_indirect_emission1 = Parameter(parm=self.node.parm('indirect_emission1'))
        self.parm_indirect_emission2 = Parameter(parm=self.node.parm('indirect_emission2'))
        self.parm_indirect_emission3 = Parameter(parm=self.node.parm('indirect_emission3'))
        self.parm_direct_comp = Parameter(parm=self.node.parm('direct_comp'))
        self.parm_indirect_comp = Parameter(parm=self.node.parm('indirect_comp'))
        self.parm_all_comp = Parameter(parm=self.node.parm('all_comp'))
        self.parm_direct_noshadow1 = Parameter(parm=self.node.parm('direct_noshadow1'))
        self.parm_direct_noshadow2 = Parameter(parm=self.node.parm('direct_noshadow2'))
        self.parm_direct_noshadow3 = Parameter(parm=self.node.parm('direct_noshadow3'))
        self.parm_direct_shadow1 = Parameter(parm=self.node.parm('direct_shadow1'))
        self.parm_direct_shadow2 = Parameter(parm=self.node.parm('direct_shadow2'))
        self.parm_direct_shadow3 = Parameter(parm=self.node.parm('direct_shadow3'))
        self.parm_indirect_noshadow1 = Parameter(parm=self.node.parm('indirect_noshadow1'))
        self.parm_indirect_noshadow2 = Parameter(parm=self.node.parm('indirect_noshadow2'))
        self.parm_indirect_noshadow3 = Parameter(parm=self.node.parm('indirect_noshadow3'))
        self.parm_indirect_shadow1 = Parameter(parm=self.node.parm('indirect_shadow1'))
        self.parm_indirect_shadow2 = Parameter(parm=self.node.parm('indirect_shadow2'))
        self.parm_indirect_shadow3 = Parameter(parm=self.node.parm('indirect_shadow3'))
        self.parm_level = Parameter(parm=self.node.parm('level'))
        self.parm_diffuselevel = Parameter(parm=self.node.parm('diffuselevel'))
        self.parm_specularlevel = Parameter(parm=self.node.parm('specularlevel'))
        self.parm_volumelevel = Parameter(parm=self.node.parm('volumelevel'))
        self.parm_direct_samples = Parameter(parm=self.node.parm('direct_samples'))
        self.parm_indirect_samples = Parameter(parm=self.node.parm('indirect_samples'))
        self.parm_nlights = Parameter(parm=self.node.parm('nlights'))
        self.parm_direct_noshadow_comp = Parameter(parm=self.node.parm('direct_noshadow_comp'))
        self.parm_indirect_noshadow_comp = Parameter(parm=self.node.parm('indirect_noshadow_comp'))
        self.parm_nddispersion = Parameter(parm=self.node.parm('nddispersion'))
        self.parm_ndpriority = Parameter(parm=self.node.parm('ndpriority'))
        self.parm_ndior = Parameter(parm=self.node.parm('ndior'))
        self.parm_absorption1 = Parameter(parm=self.node.parm('absorption1'))
        self.parm_absorption2 = Parameter(parm=self.node.parm('absorption2'))
        self.parm_absorption3 = Parameter(parm=self.node.parm('absorption3'))
        self.parm_oc1 = Parameter(parm=self.node.parm('Oc1'))
        self.parm_oc2 = Parameter(parm=self.node.parm('Oc2'))
        self.parm_oc3 = Parameter(parm=self.node.parm('Oc3'))
        self.parm_cv1 = Parameter(parm=self.node.parm('Cv1'))
        self.parm_cv2 = Parameter(parm=self.node.parm('Cv2'))
        self.parm_cv3 = Parameter(parm=self.node.parm('Cv3'))
        self.parm_th1 = Parameter(parm=self.node.parm('Th1'))
        self.parm_th2 = Parameter(parm=self.node.parm('Th2'))
        self.parm_th3 = Parameter(parm=self.node.parm('Th3'))
        self.parm_ab1 = Parameter(parm=self.node.parm('Ab1'))
        self.parm_ab2 = Parameter(parm=self.node.parm('Ab2'))
        self.parm_ab3 = Parameter(parm=self.node.parm('Ab3'))
        self.parm_cu1 = Parameter(parm=self.node.parm('Cu1'))
        self.parm_cu2 = Parameter(parm=self.node.parm('Cu2'))
        self.parm_cu3 = Parameter(parm=self.node.parm('Cu3'))
        self.parm_vd1 = Parameter(parm=self.node.parm('Vd1'))
        self.parm_vd2 = Parameter(parm=self.node.parm('Vd2'))
        self.parm_vd3 = Parameter(parm=self.node.parm('Vd3'))
        self.parm_nt1 = Parameter(parm=self.node.parm('Nt1'))
        self.parm_nt2 = Parameter(parm=self.node.parm('Nt2'))
        self.parm_nt3 = Parameter(parm=self.node.parm('Nt3'))
        self.parm_ds1 = Parameter(parm=self.node.parm('Ds1'))
        self.parm_ds2 = Parameter(parm=self.node.parm('Ds2'))
        self.parm_ds3 = Parameter(parm=self.node.parm('Ds3'))
        self.parm_pre_disp_p1 = Parameter(parm=self.node.parm('pre_disp_P1'))
        self.parm_pre_disp_p2 = Parameter(parm=self.node.parm('pre_disp_P2'))
        self.parm_pre_disp_p3 = Parameter(parm=self.node.parm('pre_disp_P3'))
        self.parm_pre_disp_utan1 = Parameter(parm=self.node.parm('pre_disp_utan1'))
        self.parm_pre_disp_utan2 = Parameter(parm=self.node.parm('pre_disp_utan2'))
        self.parm_pre_disp_utan3 = Parameter(parm=self.node.parm('pre_disp_utan3'))
        self.parm_pre_disp_vtan1 = Parameter(parm=self.node.parm('pre_disp_vtan1'))
        self.parm_pre_disp_vtan2 = Parameter(parm=self.node.parm('pre_disp_vtan2'))
        self.parm_pre_disp_vtan3 = Parameter(parm=self.node.parm('pre_disp_vtan3'))
        self.parm_pre_disp_n1 = Parameter(parm=self.node.parm('pre_disp_N1'))
        self.parm_pre_disp_n2 = Parameter(parm=self.node.parm('pre_disp_N2'))
        self.parm_pre_disp_n3 = Parameter(parm=self.node.parm('pre_disp_N3'))
        self.parm_disp = Parameter(parm=self.node.parm('disp'))
        self.parm_vdisp1 = Parameter(parm=self.node.parm('vdisp1'))
        self.parm_vdisp2 = Parameter(parm=self.node.parm('vdisp2'))
        self.parm_vdisp3 = Parameter(parm=self.node.parm('vdisp3'))
        self.parm_dt1 = Parameter(parm=self.node.parm('Dt1'))
        self.parm_dt2 = Parameter(parm=self.node.parm('Dt2'))
        self.parm_dt3 = Parameter(parm=self.node.parm('Dt3'))
        self.parm_vdt1 = Parameter(parm=self.node.parm('Vdt1'))
        self.parm_vdt2 = Parameter(parm=self.node.parm('Vdt2'))
        self.parm_vdt3 = Parameter(parm=self.node.parm('Vdt3'))
        self.parm_basen1 = Parameter(parm=self.node.parm('baseN1'))
        self.parm_basen2 = Parameter(parm=self.node.parm('baseN2'))
        self.parm_basen3 = Parameter(parm=self.node.parm('baseN3'))
        self.parm_coatn1 = Parameter(parm=self.node.parm('coatN1'))
        self.parm_coatn2 = Parameter(parm=self.node.parm('coatN2'))
        self.parm_coatn3 = Parameter(parm=self.node.parm('coatN3'))
        self.parm_speccolorr = Parameter(parm=self.node.parm('speccolorr'))
        self.parm_speccolorg = Parameter(parm=self.node.parm('speccolorg'))
        self.parm_speccolorb = Parameter(parm=self.node.parm('speccolorb'))
        self.parm_displaycolorr = Parameter(parm=self.node.parm('displayColorr'))
        self.parm_displaycolorg = Parameter(parm=self.node.parm('displayColorg'))
        self.parm_displaycolorb = Parameter(parm=self.node.parm('displayColorb'))
        self.parm_st1 = Parameter(parm=self.node.parm('st1'))
        self.parm_st2 = Parameter(parm=self.node.parm('st2'))
        self.parm_displayopacity = Parameter(parm=self.node.parm('displayOpacity'))

        
        # parm menu vars:
        self.parm_sssmodel = SssmodelMenu(parm=self.node.parm('sssmodel'))
        self.parm_alphablendmode = AlphablendmodeMenu(parm=self.node.parm('alphablendmode'))
        self.parm_basecolor_texturewrap = BasecolorTexturewrapMenu(parm=self.node.parm('basecolor_textureWrap'))
        self.parm_basecolor_texturecolorspace = BasecolorTexturecolorspaceMenu(parm=self.node.parm('basecolor_textureColorSpace'))
        self.parm_ior_monochannel = IorMonochannelMenu(parm=self.node.parm('ior_monoChannel'))
        self.parm_ior_texturewrap = IorTexturewrapMenu(parm=self.node.parm('ior_textureWrap'))
        self.parm_ior_texturecolorspace = IorTexturecolorspaceMenu(parm=self.node.parm('ior_textureColorSpace'))
        self.parm_rough_monochannel = RoughMonochannelMenu(parm=self.node.parm('rough_monoChannel'))
        self.parm_rough_texturewrap = RoughTexturewrapMenu(parm=self.node.parm('rough_textureWrap'))
        self.parm_rough_texturecolorspace = RoughTexturecolorspaceMenu(parm=self.node.parm('rough_textureColorSpace'))
        self.parm_aniso_monochannel = AnisoMonochannelMenu(parm=self.node.parm('aniso_monoChannel'))
        self.parm_aniso_texturewrap = AnisoTexturewrapMenu(parm=self.node.parm('aniso_textureWrap'))
        self.parm_aniso_texturecolorspace = AnisoTexturecolorspaceMenu(parm=self.node.parm('aniso_textureColorSpace'))
        self.parm_anisodir_monochannel = AnisodirMonochannelMenu(parm=self.node.parm('anisodir_monoChannel'))
        self.parm_anisodir_texturewrap = AnisodirTexturewrapMenu(parm=self.node.parm('anisodir_textureWrap'))
        self.parm_anisodir_texturecolorspace = AnisodirTexturecolorspaceMenu(parm=self.node.parm('anisodir_textureColorSpace'))
        self.parm_anisodir_texturefilter = AnisodirTexturefilterMenu(parm=self.node.parm('anisodir_textureFilter'))
        self.parm_metallic_monochannel = MetallicMonochannelMenu(parm=self.node.parm('metallic_monoChannel'))
        self.parm_metallic_texturewrap = MetallicTexturewrapMenu(parm=self.node.parm('metallic_textureWrap'))
        self.parm_metallic_texturecolorspace = MetallicTexturecolorspaceMenu(parm=self.node.parm('metallic_textureColorSpace'))
        self.parm_reflect_monochannel = ReflectMonochannelMenu(parm=self.node.parm('reflect_monoChannel'))
        self.parm_reflect_texturewrap = ReflectTexturewrapMenu(parm=self.node.parm('reflect_textureWrap'))
        self.parm_reflect_texturecolorspace = ReflectTexturecolorspaceMenu(parm=self.node.parm('reflect_textureColorSpace'))
        self.parm_reflecttint_monochannel = ReflecttintMonochannelMenu(parm=self.node.parm('reflecttint_monoChannel'))
        self.parm_reflecttint_texturewrap = ReflecttintTexturewrapMenu(parm=self.node.parm('reflecttint_textureWrap'))
        self.parm_reflecttint_texturecolorspace = ReflecttintTexturecolorspaceMenu(parm=self.node.parm('reflecttint_textureColorSpace'))
        self.parm_coat_monochannel = CoatMonochannelMenu(parm=self.node.parm('coat_monoChannel'))
        self.parm_coat_texturewrap = CoatTexturewrapMenu(parm=self.node.parm('coat_textureWrap'))
        self.parm_coat_texturecolorspace = CoatTexturecolorspaceMenu(parm=self.node.parm('coat_textureColorSpace'))
        self.parm_coatrough_monochannel = CoatroughMonochannelMenu(parm=self.node.parm('coatrough_monoChannel'))
        self.parm_coatrough_texturewrap = CoatroughTexturewrapMenu(parm=self.node.parm('coatrough_textureWrap'))
        self.parm_coatrough_texturecolorspace = CoatroughTexturecolorspaceMenu(parm=self.node.parm('coatrough_textureColorSpace'))
        self.parm_transparency_monochannel = TransparencyMonochannelMenu(parm=self.node.parm('transparency_monoChannel'))
        self.parm_transparency_texturewrap = TransparencyTexturewrapMenu(parm=self.node.parm('transparency_textureWrap'))
        self.parm_transparency_texturecolorspace = TransparencyTexturecolorspaceMenu(parm=self.node.parm('transparency_textureColorSpace'))
        self.parm_transcolor_texturewrap = TranscolorTexturewrapMenu(parm=self.node.parm('transcolor_textureWrap'))
        self.parm_transcolor_texturecolorspace = TranscolorTexturecolorspaceMenu(parm=self.node.parm('transcolor_textureColorSpace'))
        self.parm_transdist_monochannel = TransdistMonochannelMenu(parm=self.node.parm('transdist_monoChannel'))
        self.parm_transdist_texturewrap = TransdistTexturewrapMenu(parm=self.node.parm('transdist_textureWrap'))
        self.parm_transdist_texturecolorspace = TransdistTexturecolorspaceMenu(parm=self.node.parm('transdist_textureColorSpace'))
        self.parm_dispersion_monochannel = DispersionMonochannelMenu(parm=self.node.parm('dispersion_monoChannel'))
        self.parm_dispersion_texturewrap = DispersionTexturewrapMenu(parm=self.node.parm('dispersion_textureWrap'))
        self.parm_dispersion_texturecolorspace = DispersionTexturecolorspaceMenu(parm=self.node.parm('dispersion_textureColorSpace'))
        self.parm_sss_monochannel = SssMonochannelMenu(parm=self.node.parm('sss_monoChannel'))
        self.parm_sss_texturewrap = SssTexturewrapMenu(parm=self.node.parm('sss_textureWrap'))
        self.parm_sss_texturecolorspace = SssTexturecolorspaceMenu(parm=self.node.parm('sss_textureColorSpace'))
        self.parm_sssdist_monochannel = SssdistMonochannelMenu(parm=self.node.parm('sssdist_monoChannel'))
        self.parm_sssdist_texturewrap = SssdistTexturewrapMenu(parm=self.node.parm('sssdist_textureWrap'))
        self.parm_sssdist_texturecolorspace = SssdistTexturecolorspaceMenu(parm=self.node.parm('sssdist_textureColorSpace'))
        self.parm_ssscolor_texturewrap = SsscolorTexturewrapMenu(parm=self.node.parm('ssscolor_textureWrap'))
        self.parm_ssscolor_texturecolorspace = SsscolorTexturecolorspaceMenu(parm=self.node.parm('ssscolor_textureColorSpace'))
        self.parm_sheen_monochannel = SheenMonochannelMenu(parm=self.node.parm('sheen_monoChannel'))
        self.parm_sheen_texturewrap = SheenTexturewrapMenu(parm=self.node.parm('sheen_textureWrap'))
        self.parm_sheen_texturecolorspace = SheenTexturecolorspaceMenu(parm=self.node.parm('sheen_textureColorSpace'))
        self.parm_sheentint_monochannel = SheentintMonochannelMenu(parm=self.node.parm('sheentint_monoChannel'))
        self.parm_sheentint_texturewrap = SheentintTexturewrapMenu(parm=self.node.parm('sheentint_textureWrap'))
        self.parm_sheentint_texturecolorspace = SheentintTexturecolorspaceMenu(parm=self.node.parm('sheentint_textureColorSpace'))
        self.parm_emitcolor_texturewrap = EmitcolorTexturewrapMenu(parm=self.node.parm('emitcolor_textureWrap'))
        self.parm_emitcolor_texturecolorspace = EmitcolorTexturecolorspaceMenu(parm=self.node.parm('emitcolor_textureColorSpace'))
        self.parm_opaccolor_texturewrap = OpaccolorTexturewrapMenu(parm=self.node.parm('opaccolor_textureWrap'))
        self.parm_opaccolor_texturecolorspace = OpaccolorTexturecolorspaceMenu(parm=self.node.parm('opaccolor_textureColorSpace'))
        self.parm_occlusion_texturewrap = OcclusionTexturewrapMenu(parm=self.node.parm('occlusion_textureWrap'))
        self.parm_occlusion_texturecolorspace = OcclusionTexturecolorspaceMenu(parm=self.node.parm('occlusion_textureColorSpace'))
        self.parm_surface_texturefilter = SurfaceTexturefilterMenu(parm=self.node.parm('surface_textureFilter'))
        self.parm_roundededge_mode = RoundededgeModeMenu(parm=self.node.parm('roundedEdge_mode'))
        self.parm_basebumpandnormal_type = BasebumpandnormalTypeMenu(parm=self.node.parm('baseBumpAndNormal_type'))
        self.parm_basebump_colorspace = BasebumpColorspaceMenu(parm=self.node.parm('baseBump_colorSpace'))
        self.parm_basebump_wrap = BasebumpWrapMenu(parm=self.node.parm('baseBump_wrap'))
        self.parm_basebump_filter = BasebumpFilterMenu(parm=self.node.parm('baseBump_filter'))
        self.parm_basebump_channel = BasebumpChannelMenu(parm=self.node.parm('baseBump_channel'))
        self.parm_basenormal_colorspace = BasenormalColorspaceMenu(parm=self.node.parm('baseNormal_colorspace'))
        self.parm_basenormal_vectorspace = BasenormalVectorspaceMenu(parm=self.node.parm('baseNormal_vectorSpace'))
        self.parm_basenormal_wrap = BasenormalWrapMenu(parm=self.node.parm('baseNormal_wrap'))
        self.parm_basenormal_filter = BasenormalFilterMenu(parm=self.node.parm('baseNormal_filter'))
        self.parm_basenormal_channel = BasenormalChannelMenu(parm=self.node.parm('baseNormal_channel'))
        self.parm_basenormal_space = BasenormalSpaceMenu(parm=self.node.parm('baseNormal_space'))
        self.parm_coatbumpandnormal_type = CoatbumpandnormalTypeMenu(parm=self.node.parm('coatBumpAndNormal_type'))
        self.parm_coatbump_colorspace = CoatbumpColorspaceMenu(parm=self.node.parm('coatBump_colorSpace'))
        self.parm_coatbump_wrap = CoatbumpWrapMenu(parm=self.node.parm('coatBump_wrap'))
        self.parm_coatbump_filter = CoatbumpFilterMenu(parm=self.node.parm('coatBump_filter'))
        self.parm_coatbump_channel = CoatbumpChannelMenu(parm=self.node.parm('coatBump_channel'))
        self.parm_coatnormal_colorspace = CoatnormalColorspaceMenu(parm=self.node.parm('coatNormal_colorspace'))
        self.parm_coatnormal_vectorspace = CoatnormalVectorspaceMenu(parm=self.node.parm('coatNormal_vectorSpace'))
        self.parm_coatnormal_wrap = CoatnormalWrapMenu(parm=self.node.parm('coatNormal_wrap'))
        self.parm_coatnormal_filter = CoatnormalFilterMenu(parm=self.node.parm('coatNormal_filter'))
        self.parm_coatnormal_channel = CoatnormalChannelMenu(parm=self.node.parm('coatNormal_channel'))
        self.parm_coatnormal_space = CoatnormalSpaceMenu(parm=self.node.parm('coatNormal_space'))
        self.parm_dispinput_vectorspace = DispinputVectorspaceMenu(parm=self.node.parm('dispInput_vectorspace'))
        self.parm_disptex_type = DisptexTypeMenu(parm=self.node.parm('dispTex_type'))
        self.parm_disptex_colorspace = DisptexColorspaceMenu(parm=self.node.parm('dispTex_colorSpace'))
        self.parm_disptex_vectorspace = DisptexVectorspaceMenu(parm=self.node.parm('dispTex_vectorSpace'))
        self.parm_disptex_channelorder = DisptexChannelorderMenu(parm=self.node.parm('dispTex_channelOrder'))
        self.parm_disptex_channel = DisptexChannelMenu(parm=self.node.parm('dispTex_channel'))
        self.parm_disptex_wrap = DisptexWrapMenu(parm=self.node.parm('dispTex_wrap'))
        self.parm_disptex_filter = DisptexFilterMenu(parm=self.node.parm('dispTex_filter'))
        self.parm_dispnoise_type = DispnoiseTypeMenu(parm=self.node.parm('dispNoise_type'))


        # input vars:
        self.input_uv_coordinates = 'UV Coordinates'
        self.input_base_color = 'Base Color'
        self.input_albedo_multiplier = 'Albedo Multiplier'
        self.input_use_point_color = 'Use Point Color'
        self.input_use_packed_color = 'Use Packed Color'
        self.input_shade_both_sides_as_front = 'Shade Both Sides As Front'
        self.input_ior = 'IOR'
        self.input_roughness = 'Roughness'
        self.input_anisotropy = 'Anisotropy'
        self.input_anisotropy_direction = 'Anisotropy Direction'
        self.input_metallic = 'Metallic'
        self.input_reflectivity = 'Reflectivity'
        self.input_reflect_tint = 'Reflect Tint'
        self.input_coat = 'Coat'
        self.input_coat_roughness = 'Coat Roughness'
        self.input_transparency = 'Transparency'
        self.input_transmission_color = 'Transmission Color'
        self.input_at_distance = 'At Distance'
        self.input_dispersion = 'Dispersion'
        self.input_surface_priority = 'Surface Priority'
        self.input_subsurface = 'Subsurface'
        self.input_sss_mode = 'SSS Mode'
        self.input_subsurface_distance = 'Subsurface Distance'
        self.input_subsurface_color = 'Subsurface Color'
        self.input_scattering_phase = 'Scattering Phase'
        self.input_sheen = 'Sheen'
        self.input_sheen_tint = 'Sheen Tint'
        self.input_emission_color = 'Emission Color'
        self.input_emission_intensity = 'Emission Intensity'
        self.input_emission_illuminates_objects = 'Emission Illuminates Objects'
        self.input_opacity_scale = 'Opacity Scale'
        self.input_opacity_color = 'Opacity Color'
        self.input_enable = 'Enable'
        self.input_transmission_tint = 'Transmission Tint'
        self.input_shadow_contour = 'Shadow Contour'
        self.input_shadow_opacity = 'Shadow Opacity'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_tint_intensity = 'Tint Intensity'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_tint_intensity = 'Tint Intensity'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_filter_type = 'Filter Type'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_map = 'Map'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_tint_intensity = 'Tint Intensity'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_wrap = 'Wrap'
        self.input_tint_intensity = 'Tint Intensity'
        self.input_source_color_space = 'Source Color Space'
        self.input_filter = 'Filter'
        self.input_filter_width = 'Filter Width'
        self.input_enable = 'Enable'
        self.input_texture_type = 'Texture Type'
        self.input_texture_color_space = 'Texture Color Space'
        self.input_effect_scale = 'Effect Scale'
        self.input_texture_path = 'Texture Path'
        self.input_wrap = 'Wrap'
        self.input_filter = 'Filter'
        self.input_filter_width = 'Filter Width'
        self.input_channel = 'Channel'
        self.input_image_plane = 'Image Plane'
        self.input_texture_color_space = 'Texture Color Space'
        self.input_vector_space = 'Vector Space'
        self.input_effect_scale = 'Effect Scale'
        self.input_texture_path = 'Texture Path'
        self.input_wrap = 'Wrap'
        self.input_filter = 'Filter'
        self.input_filter_width = 'Filter Width'
        self.input_channel = 'Channel'
        self.input_image_plane = 'Image Plane'
        self.input_normal_space = 'Normal Space'
        self.input_flip_x = 'Flip X'
        self.input_flip_y = 'Flip Y'
        self.input_separate_coat_normals = 'Separate Coat Normals'
        self.input_enable = 'Enable'
        self.input_texture_type = 'Texture Type'
        self.input_texture_color_space = 'Texture Color Space'
        self.input_effect_scale = 'Effect Scale'
        self.input_texture_path = 'Texture Path'
        self.input_wrap = 'Wrap'
        self.input_filter = 'Filter'
        self.input_filter_width = 'Filter Width'
        self.input_channel = 'Channel'
        self.input_image_plane = 'Image Plane'
        self.input_texture_color_space = 'Texture Color Space'
        self.input_vector_space = 'Vector Space'
        self.input_effect_scale = 'Effect Scale'
        self.input_texture_path = 'Texture Path'
        self.input_wrap = 'Wrap'
        self.input_filter = 'Filter'
        self.input_filter_width = 'Filter Width'
        self.input_channel = 'Channel'
        self.input_image_plane = 'Image Plane'
        self.input_normal_space = 'Normal Space'
        self.input_flip_x = 'Flip X'
        self.input_flip_y = 'Flip Y'
        self.input_enable_input_displacement = 'Enable Input Displacement'
        self.input_maximum_displacement = 'Maximum Displacement'
        self.input_vector_space = 'Vector Space'
        self.input_enable_texture_displacement = 'Enable Texture Displacement'
        self.input_texture_type = 'Texture Type'
        self.input_texture_color_space = 'Texture Color Space'
        self.input_vector_space = 'Vector Space'
        self.input_channel_order = 'Channel Order'
        self.input_offset = 'Offset'
        self.input_effect_scale = 'Effect Scale'
        self.input_texture_path = 'Texture Path'
        self.input_channel = 'Channel'
        self.input_wrap = 'Wrap'
        self.input_filter = 'Filter'
        self.input_filter_width = 'Filter Width'
        self.input_enable_noise_displacement = 'Enable Noise Displacement'
        self.input_noise_type = 'Noise Type'
        self.input_frequency = 'Frequency'
        self.input_offset = 'Offset'
        self.input_amplitude = 'Amplitude'
        self.input_roughness = 'Roughness'
        self.input_attenuation = 'Attenuation'
        self.input_turbulence = 'Turbulence'
        self.input_diffuse = 'Diffuse'
        self.input_reflection = 'Reflection'
        self.input_refraction = 'Refraction'
        self.input_coat_reflection = 'Coat Reflection'
        self.input_subsurface = 'Subsurface'
        self.input_translate = 'Translate'
        self.input_rotate = 'Rotate'
        self.input_scale = 'Scale'
        self.input_wala = ''
        self.input_wala = ''
        self.input_normal_displacement = 'Normal Displacement'
        self.input_vector_displacement = 'Vector Displacement'
        self.input_use_point_alpha = 'Use Point Alpha'
        self.input_wala = ''
        self.input_round_edge_radius = 'Round Edge Radius'
        self.input_round_edge_mode = 'Round Edge Mode'
        self.input_use_packed_alpha = 'Use Packed Alpha'
        self.input_wala = ''
        self.input_use_texture_alpha = 'Use Texture Alpha'
        self.input_use_texture = 'Use Texture'
        self.input_texture = 'Texture'
        self.input_tint_intensity = 'Tint Intensity'
        self.input_wrap = 'Wrap'
        self.input_source_color_space = 'Source Color Space'
        self.input_alpha_mode = 'Alpha Mode'
        self.input_alpha_cutoff = 'Alpha Cutoff'
        self.input_use_point_color = 'Use Point Color'
        self.input_use_point_color = 'Use Point Color'
        self.input_use_point_color = 'Use Point Color'


# parm menu classes:
class SssmodelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_subsurface_scattering = ("pbrsss", 0)
        self.menu_single_scattering = ("pbrsingles", 1)
        self.menu_random_walk__karma_ = ("pbrrwalksss", 2)


class AlphablendmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_blend = ("blend", 0)
        self.menu_mask = ("mask", 1)
        self.menu_opaque = ("opaque", 2)


class BasecolorTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class BasecolorTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class IorMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class IorTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class IorTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class RoughMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class RoughTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class RoughTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class AnisoMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class AnisoTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class AnisoTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class AnisodirMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class AnisodirTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class AnisodirTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class AnisodirTexturefilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("box", 0)
        self.menu_gaussian = ("gauss", 1)
        self.menu_bartlett_triangular = ("bartlett", 2)
        self.menu_sinc_sharpening = ("sinc", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_catmull_rom = ("catrom", 6)
        self.menu_mitchell = ("mitchell", 7)
        self.menu_point__no_filter_ = ("point", 8)


class MetallicMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class MetallicTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class MetallicTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class ReflectMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class ReflectTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class ReflectTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class ReflecttintMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class ReflecttintTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class ReflecttintTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class CoatMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class CoatTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class CoatTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class CoatroughMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class CoatroughTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class CoatroughTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class TransparencyMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class TransparencyTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class TransparencyTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class TranscolorTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class TranscolorTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class TransdistMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class TransdistTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class TransdistTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class DispersionMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class DispersionTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class DispersionTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class SssMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class SssTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class SssTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class SssdistMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class SssdistTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class SssdistTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class SsscolorTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class SsscolorTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class SheenMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class SheenTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class SheenTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class SheentintMonochannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class SheentintTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class SheentintTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class EmitcolorTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class EmitcolorTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class OpaccolorTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class OpaccolorTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class OcclusionTexturewrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class OcclusionTexturecolorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class SurfaceTexturefilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("box", 0)
        self.menu_gaussian = ("gauss", 1)
        self.menu_bartlett_triangular = ("bartlett", 2)
        self.menu_sinc_sharpening = ("sinc", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_catmull_rom = ("catrom", 6)
        self.menu_mitchell = ("mitchell", 7)


class RoundededgeModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_concave_and_convex_edges = ("both", 0)
        self.menu_concave_edges = ("concave", 1)
        self.menu_convex_edges = ("convex", 2)


class BasebumpandnormalTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bump = ("bump", 0)
        self.menu_normal = ("normal", 1)


class BasebumpColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class BasebumpWrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class BasebumpFilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("box", 0)
        self.menu_gaussian = ("gauss", 1)
        self.menu_bartlett_triangular = ("bartlett", 2)
        self.menu_sinc_sharpening = ("sinc", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_catmull_rom = ("catrom", 6)
        self.menu_mitchell = ("mitchell", 7)


class BasebumpChannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class BasenormalColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class BasenormalVectorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uv_tangent_space = ("uvtangent", 0)
        self.menu_object_space = ("object", 1)
        self.menu_world_space = ("world", 2)


class BasenormalWrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class BasenormalFilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("box", 0)
        self.menu_gaussian = ("gauss", 1)
        self.menu_bartlett_triangular = ("bartlett", 2)
        self.menu_sinc_sharpening = ("sinc", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_catmull_rom = ("catrom", 6)
        self.menu_mitchell = ("mitchell", 7)


class BasenormalChannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class BasenormalSpaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_to_1_0 = ("0", 0)
        self.menu__1_to_1 = ("1", 1)


class CoatbumpandnormalTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bump = ("bump", 0)
        self.menu_normal = ("normal", 1)


class CoatbumpColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class CoatbumpWrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class CoatbumpFilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("box", 0)
        self.menu_gaussian = ("gauss", 1)
        self.menu_bartlett_triangular = ("bartlett", 2)
        self.menu_sinc_sharpening = ("sinc", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_catmull_rom = ("catrom", 6)
        self.menu_mitchell = ("mitchell", 7)


class CoatbumpChannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class CoatnormalColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class CoatnormalVectorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uv_tangent_space = ("uvtangent", 0)
        self.menu_object_space = ("object", 1)
        self.menu_world_space = ("world", 2)


class CoatnormalWrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class CoatnormalFilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("box", 0)
        self.menu_gaussian = ("gauss", 1)
        self.menu_bartlett_triangular = ("bartlett", 2)
        self.menu_sinc_sharpening = ("sinc", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_catmull_rom = ("catrom", 6)
        self.menu_mitchell = ("mitchell", 7)


class CoatnormalChannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class CoatnormalSpaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_to_1_0 = ("0", 0)
        self.menu__1_to_1 = ("1", 1)


class DispinputVectorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uv_tangent_space = ("uvtangent", 0)
        self.menu_object_space = ("object", 1)
        self.menu_world_space = ("world", 2)


class DisptexTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_displacement_along_normal = ("disp", 0)
        self.menu_vector_displacement = ("vectordisp", 1)


class DisptexColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic = ("auto", 0)
        self.menu_linear = ("linear", 1)
        self.menu_srgb = ("sRGB", 2)
        self.menu_rec_709 = ("rec709", 3)
        self.menu_raw = ("raw", 4)
        self.menu__separator = ("_separator_", 5)
        self.menu_aces2065_1 = ("ACES2065-1", 6)
        self.menu_acescc = ("ACEScc", 7)
        self.menu_acescct = ("ACEScct", 8)
        self.menu_acescg = ("ACEScg", 9)
        self.menu_gamma_1_8_rec_709___texture = ("Gamma 1.8 Rec.709 - Texture", 10)
        self.menu_gamma_2_2_ap1___texture = ("Gamma 2.2 AP1 - Texture", 11)
        self.menu_gamma_2_2_rec_709___texture = ("Gamma 2.2 Rec.709 - Texture", 12)
        self.menu_gamma_2_4_rec_709___texture = ("Gamma 2.4 Rec.709 - Texture", 13)
        self.menu_linear_p3_d65 = ("Linear P3-D65", 14)
        self.menu_linear_rec_2020 = ("Linear Rec.2020", 15)
        self.menu_linear_rec_709__srgb_ = ("Linear Rec.709 (sRGB)", 16)
        self.menu_raw = ("Raw", 17)
        self.menu_srgb___texture = ("sRGB - Texture", 18)
        self.menu_srgb_encoded_ap1___texture = ("sRGB Encoded AP1 - Texture", 19)


class DisptexVectorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uv_tangent_space = ("uvtangent", 0)
        self.menu_object_space = ("object", 1)
        self.menu_world_space = ("world", 2)


class DisptexChannelorderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_xyz = ("xyz", 0)
        self.menu_xzy = ("xzy", 1)


class DisptexChannelMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_luminance = ("0", 0)
        self.menu_red = ("1", 1)
        self.menu_green = ("2", 2)
        self.menu_blue = ("3", 3)


class DisptexWrapMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_repeat = ("repeat", 0)
        self.menu_streak = ("streak", 1)
        self.menu_decal = ("decal", 2)


class DisptexFilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("box", 0)
        self.menu_gaussian = ("gauss", 1)
        self.menu_bartlett_triangular = ("bartlett", 2)
        self.menu_sinc_sharpening = ("sinc", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_catmull_rom = ("catrom", 6)
        self.menu_mitchell = ("mitchell", 7)


class DispnoiseTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_perlin_noise = ("pnoise", 0)
        self.menu_original_perlin_noise = ("onoise", 1)
        self.menu_simplex_noise = ("xnoise", 2)
        self.menu_sparse_convolution_noise = ("snoise", 3)
        self.menu_alligator_noise = ("anoise", 4)



