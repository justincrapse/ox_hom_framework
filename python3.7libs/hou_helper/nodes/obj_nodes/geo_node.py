from hou_helper.base_objects.hh_node import HHNode
from hou_helper.base_objects.parameter import Parameter
from hou_helper.base_objects.menu import Menu
# node class version: 0.1


class GeoNode(HHNode):
    node_type = 'geo'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz', 'scale': 'scale', 'pre_xform': 'pre_xform', 'keeppos': 'keeppos', 'childcomp': 'childcomp', 'constraints_on': 'constraints_on', 'constraints_path': 'constraints_path', 'lookatpath': 'lookatpath', 'lookupobjpath': 'lookupobjpath', 'lookup': 'lookup', 'pathobjpath': 'pathobjpath', 'roll': 'roll', 'pos': 'pos', 'uparmtype': 'uparmtype', 'pathorient': 'pathorient', 'upx': 'upx', 'upy': 'upy', 'upz': 'upz', 'bank': 'bank', 'shop_materialpath': 'shop_materialpath', 'shop_materialopts': 'shop_materialopts', 'tdisplay': 'tdisplay', 'display': 'display', 'use_dcolor': 'use_dcolor', 'dcolorr': 'dcolorr', 'dcolorg': 'dcolorg', 'dcolorb': 'dcolorb', 'picking': 'picking', 'pickscript': 'pickscript', 'caching': 'caching', 'vport_shadeopen': 'vport_shadeopen', 'vport_displayassubdiv': 'vport_displayassubdiv', 'vport_onionskin': 'vport_onionskin', 'stdswitcher41': 'stdswitcher41', 'viewportlod': 'viewportlod', 'vm_rendervisibility': 'vm_rendervisibility', 'vm_rendersubd': 'vm_rendersubd', 'vm_subdstyle': 'vm_subdstyle', 'vm_subdgroup': 'vm_subdgroup', 'vm_osd_quality': 'vm_osd_quality', 'vm_osd_vtxinterp': 'vm_osd_vtxinterp', 'vm_osd_fvarinterp': 'vm_osd_fvarinterp', 'folder01': 'folder01', 'categories': 'categories', 'reflectmask': 'reflectmask', 'refractmask': 'refractmask', 'lightmask': 'lightmask', 'lightcategories': 'lightcategories', 'vm_lpetag': 'vm_lpetag', 'vm_volumefilter': 'vm_volumefilter', 'vm_volumefilterwidth': 'vm_volumefilterwidth', 'vm_matte': 'vm_matte', 'vm_rayshade': 'vm_rayshade', 'geo_velocityblur': 'geo_velocityblur', 'geo_accelattribute': 'geo_accelattribute', 'vm_shadingquality': 'vm_shadingquality', 'vm_flatness': 'vm_flatness', 'vm_raypredice': 'vm_raypredice', 'vm_curvesurface': 'vm_curvesurface', 'vm_rmbackface': 'vm_rmbackface', 'shop_geometrypath': 'shop_geometrypath', 'vm_forcegeometry': 'vm_forcegeometry', 'vm_rendersubdcurves': 'vm_rendersubdcurves', 'vm_renderpoints': 'vm_renderpoints', 'vm_renderpointsas': 'vm_renderpointsas', 'vm_usenforpoints': 'vm_usenforpoints', 'vm_pointscale': 'vm_pointscale', 'vm_pscalediameter': 'vm_pscalediameter', 'vm_metavolume': 'vm_metavolume', 'vm_coving': 'vm_coving', 'vm_materialoverride': 'vm_materialoverride', 'vm_overridedetail': 'vm_overridedetail', 'vm_procuseroottransform': 'vm_procuseroottransform', 'rs_objprop_switcher1': 'RS_objprop_switcher1', 'rs_objpro_first': 'RS_objpro_first', 'rs_campropshapes_switcher1': 'RS_campropshapes_switcher1', 'rs_objprop_id': 'RS_objprop_ID', 'rs_objprop_cryptoid': 'RS_objprop_CryptoID', 'rs_objprop_cryptomatid_allmat': 'RS_objprop_CryptoMatID_AllMat', 'rs_objprop_ngons_enable': 'RS_objprop_ngons_enable', 'rs_objprop_ngons_tessmode': 'RS_objprop_ngons_tessMode', 'rs_objprop_ngons_avoiddegen': 'RS_objprop_ngons_avoidDegen', 'rs_objprop_normals_normalize': 'RS_objprop_normals_normalize', 'rs_objprop_renderashair': 'RS_objprop_renderAsHair', 'rs_objprop_defaulthairwidth': 'RS_objprop_defaultHairWidth', 'rs_objprop_hairhalfthickness': 'RS_objprop_hairHalfThickness', 'rs_objprop_mb_trans': 'RS_objprop_mb_trans', 'rs_objprop_mb_def': 'RS_objprop_mb_def', 'rs_objprop_mb_points': 'RS_objprop_mb_points', 'rs_objprop_mb_def_use_v': 'RS_objprop_mb_def_use_v', 'rs_objprop_mb_v_attr': 'RS_objprop_mb_v_attr', 'rs_objprop_mb_deformsteps': 'RS_objprop_mb_deformSteps', 'rs_objprop_mb_fd_scale': 'RS_objprop_mb_fd_scale', 'rs_objprop_mb_offset': 'RS_objprop_mb_offset', 'rs_objprop_rendersopsubnets': 'RS_objprop_renderSOPsubnets', 'rs_objprop_tess_enable': 'RS_objprop_tess_enable', 'rs_objprop_tess_u': 'RS_objprop_tess_u', 'rs_objprop_tess_v': 'RS_objprop_tess_v', 'rs_objprop_tess_trim': 'RS_objprop_tess_trim', 'rs_objprop_inst_mode': 'RS_objprop_inst_mode', 'rs_objprop_inst_mb': 'RS_objprop_inst_mb', 'rs_objprop_inst_lightshader': 'RS_objprop_inst_lightShader', 'rs_objprop_inst_universalif': 'RS_objprop_inst_universalIF', 'rs_objprop_inst_ignorepivot': 'RS_objprop_inst_ignorePivot', 'rs_objprop_inst_fileoverride': 'RS_objprop_inst_fileOverride', 'rs_objprop_inst_packed': 'RS_objprop_inst_packed', 'rs_objprop_inst_packedpriminstancing': 'RS_objprop_inst_PackedPrimInstancing', 'rs_objprop_inst_subnetinstancing': 'RS_objprop_inst_subnetInstancing', 'rs_objprop_attr_auto': 'RS_objprop_attr_auto', 'rs_objprop_attr_vertex': 'RS_objprop_attr_vertex', 'rs_objprop_attr_points': 'RS_objprop_attr_points', 'rs_objprop_attr_primitives': 'RS_objprop_attr_primitives', 'rs_objprop_attr_detail': 'RS_objprop_attr_detail', 'rs_objprop_pckattr_promotion': 'RS_objprop_pckattr_promotion', 'rs_objprop_pckattr_replace': 'RS_objprop_pckattr_replace', 'rs_objprop_pckattr_mult': 'RS_objprop_pckattr_mult', 'rs_objprop_pckattr_add': 'RS_objprop_pckattr_add', 'rs_objprop_tracesets_enabled': 'RS_objprop_tracesets_enabled', 'rs_objprop_tracesets_reflection': 'RS_objprop_tracesets_reflection', 'rs_objprop_tracesets_refraction': 'RS_objprop_tracesets_refraction', 'rs_objprop_tracesets_sss': 'RS_objprop_tracesets_sss', 'rs_objprop_ipr_forcemeshupdate': 'RS_objprop_ipr_forceMeshUpdate', 'rs_objpro_label5': 'RS_objpro_label5', 'rs_objprop_proxy_enable': 'RS_objprop_proxy_enable', 'rs_objprop_proxy_file': 'RS_objprop_proxy_file', 'rs_objprop_proxy_preview': 'RS_objprop_proxy_preview', 'rs_objprop_proxy_prevpercent': 'RS_objprop_proxy_prevPercent', 'rs_objprop_proxy_prevlines': 'RS_objprop_proxy_prevLines', 'rs_objprop_proxy_prevanimated': 'RS_objprop_proxy_prevAnimated', 'rs_objprop_proxy_materials': 'RS_objprop_proxy_materials', 'rs_objprop_proxy_override': 'RS_objprop_proxy_override', 'rs_objprop_proxy_overridelist': 'RS_objprop_proxy_overrideList', 'rs_objprop_proxy_elements_mesh': 'RS_objprop_proxy_elements_mesh', 'rs_objprop_proxy_elements_volume': 'RS_objprop_proxy_elements_volume', 'rs_objprop_proxy_elements_light': 'RS_objprop_proxy_elements_light', 'rs_objprop_proxy_elements_proxy': 'RS_objprop_proxy_elements_proxy', 'rs_objprop_proxy_ovrid': 'RS_objprop_proxy_ovrID', 'rs_objprop_proxy_ovrvis': 'RS_objprop_proxy_ovrVis', 'rs_objprop_proxy_ovrtess': 'RS_objprop_proxy_ovrTess', 'rs_objprop_proxy_ovrtraces': 'RS_objprop_proxy_ovrTraceS', 'rs_objprop_proxy_ovruserdata': 'RS_objprop_proxy_ovrUserData', 'rs_objpro_label1o': 'RS_objpro_label1o', 'meshflag_primaryrayvisible': 'MESHFLAG_PRIMARYRAYVISIBLE', 'meshflag_secondaryrayvisible': 'MESHFLAG_SECONDARYRAYVISIBLE', 'meshflag_shadowcaster': 'MESHFLAG_SHADOWCASTER', 'meshflag_shadowreceiver': 'MESHFLAG_SHADOWRECEIVER', 'meshflag_noselfshadow': 'MESHFLAG_NOSELFSHADOW', 'meshflag_aocaster': 'MESHFLAG_AOCASTER', 'meshflag_reflectionvisible': 'MESHFLAG_REFLECTIONVISIBLE', 'meshflag_refractionvisible': 'MESHFLAG_REFRACTIONVISIBLE', 'meshflag_reflectioncaster': 'MESHFLAG_REFLECTIONCASTER', 'meshflag_refractioncaster': 'MESHFLAG_REFRACTIONCASTER', 'meshflag_fgvisible': 'MESHFLAG_FGVISIBLE', 'meshflag_givisible': 'MESHFLAG_GIVISIBLE', 'meshflag_causticvisible': 'MESHFLAG_CAUSTICVISIBLE', 'meshflag_fgcaster': 'MESHFLAG_FGCASTER', 'meshflag_forcebruteforcegi': 'MESHFLAG_FORCEBRUTEFORCEGI', 'meshflag_gicaster': 'MESHFLAG_GICASTER', 'meshflag_causticcaster': 'MESHFLAG_CAUSTICCASTER', 'rs_objpro_label2': 'RS_objpro_label2', 'rs_objprop_rstess_enable': 'RS_objprop_rstess_enable', 'rs_objprop_rstess_rule': 'RS_objprop_rstess_rule', 'rs_objprop_rstess_ssadaptive': 'RS_objprop_rstess_ssadaptive', 'rs_objprop_rstess_smoothsub': 'RS_objprop_rstess_smoothsub', 'rs_objprop_rstess_triquads': 'RS_objprop_rstess_triQuads', 'rs_objprop_rstess_melenght': 'RS_objprop_rstess_melenght', 'rs_objprop_rstess_maxsubd': 'RS_objprop_rstess_maxsubd', 'rs_objprop_rstess_ooftf': 'RS_objprop_rstess_ooftf', 'rs_objprop_rstess_looft': 'RS_objprop_rstess_looft', 'rs_objprop_rstess_looftsubd': 'RS_objprop_rstess_looftSubd', 'rs_objprop_rstess_smooth': 'RS_objprop_rstess_smooth', 'rs_objprop_rstess_smoothbound': 'RS_objprop_rstess_smoothBound', 'rs_objpro_label3': 'RS_objpro_label3', 'rs_objprop_displace_enable': 'RS_objprop_displace_enable', 'rs_objprop_displace_max': 'RS_objprop_displace_max', 'rs_objprop_displace_scale': 'RS_objprop_displace_scale', 'rs_objprop_displace_autob': 'RS_objprop_displace_autob', 'rs_objpro_label4': 'RS_objpro_label4', 'rs_objprop_matte_enable': 'RS_objprop_matte_enable', 'rs_objprop_matte_showbackg': 'RS_objprop_matte_showbackg', 'rs_objprop_matte_applysec': 'RS_objprop_matte_applysec', 'rs_objprop_matte_abyml': 'RS_objprop_matte_abyml', 'rs_objprop_matte_includepm': 'RS_objprop_matte_includePM', 'rs_objprop_matte_alpha': 'RS_objprop_matte_alpha', 'rs_objprop_matte_reflscale': 'RS_objprop_matte_reflscale', 'rs_objprop_matte_refrscale': 'RS_objprop_matte_refrscale', 'rs_objprop_matte_diffscale': 'RS_objprop_matte_diffscale', 'rs_objprop_matte_shadowenable': 'RS_objprop_matte_shadowenable', 'rs_objprop_matte_shadowsfromm': 'RS_objprop_matte_shadowsFromM', 'rs_objprop_matte_shadowalpha': 'RS_objprop_matte_shadowalpha', 'rs_objprop_matte_shadowcolorr': 'RS_objprop_matte_shadowcolorr', 'rs_objprop_matte_shadowcolorg': 'RS_objprop_matte_shadowcolorg', 'rs_objprop_matte_shadowcolorb': 'RS_objprop_matte_shadowcolorb', 'rs_objprop_matte_shadowtrans': 'RS_objprop_matte_shadowtrans', 'rs_objpro_label6': 'RS_objpro_label6', 'rs_objprop_strands_enable': 'RS_objprop_strands_enable', 'rs_objprop_strands_type': 'RS_objprop_strands_type', 'rs_objprop_strands_maxsubd': 'RS_objprop_strands_maxSubd', 'rs_objprop_strands_scale': 'RS_objprop_strands_scale', 'rs_objprop_strands_scalemult': 'RS_objprop_strands_scaleMult', 'rs_objprop_strands_ignorepscale': 'RS_objprop_strands_ignorePScale', 'rs_objprop_strands_usecamera': 'RS_objprop_strands_useCamera', 'rs_objpro_label10': 'RS_objpro_label10', 'rs_objprop_particles_enable': 'RS_objprop_particles_enable', 'rs_objprop_particles_ignorescale': 'RS_objprop_particles_ignoreScale', 'rs_objprop_particles_scale': 'RS_objprop_particles_scale', 'rs_objprop_particles_scalemult': 'RS_objprop_particles_scaleMult', 'rs_objpro_label7': 'RS_objpro_label7', 'rs_objprop_volume_enable': 'RS_objprop_volume_enable', 'rs_objprop_volume_type': 'RS_objprop_volume_type', 'rs_objprop_volume_filtern': 'RS_objprop_volume_filterN', 'rs_objprop_volume_filterdeg': 'RS_objprop_volume_filterDeg', 'rs_objprop_volume_filterdegthr': 'RS_objprop_volume_filterDegThr', 'rs_objprop_volume_cleanbackg': 'RS_objprop_volume_cleanBackg', 'rs_objprop_volume_v': 'RS_objprop_volume_v', 'rs_objprop_volume_vx': 'RS_objprop_volume_vx', 'rs_objprop_volume_vy': 'RS_objprop_volume_vy', 'rs_objprop_volume_vz': 'RS_objprop_volume_vz', 'rs_objprop_volume_vs': 'RS_objprop_volume_vs', 'rs_objpro_last': 'RS_objpro_last'}

    def __init__(self, node=None, hh_parent=None, node_name=None):
        self.hh_parent = hh_parent
        if node:
            self.node = node
        else:
            self.node = self.hh_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_sx = Parameter(parm=self.node.parm('sx'))
        self.parm_sy = Parameter(parm=self.node.parm('sy'))
        self.parm_sz = Parameter(parm=self.node.parm('sz'))
        self.parm_px = Parameter(parm=self.node.parm('px'))
        self.parm_py = Parameter(parm=self.node.parm('py'))
        self.parm_pz = Parameter(parm=self.node.parm('pz'))
        self.parm_prx = Parameter(parm=self.node.parm('prx'))
        self.parm_pry = Parameter(parm=self.node.parm('pry'))
        self.parm_prz = Parameter(parm=self.node.parm('prz'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_keeppos = Parameter(parm=self.node.parm('keeppos'))
        self.parm_childcomp = Parameter(parm=self.node.parm('childcomp'))
        self.parm_constraints_on = Parameter(parm=self.node.parm('constraints_on'))
        self.parm_constraints_path = Parameter(parm=self.node.parm('constraints_path'))
        self.parm_lookatpath = Parameter(parm=self.node.parm('lookatpath'))
        self.parm_lookupobjpath = Parameter(parm=self.node.parm('lookupobjpath'))
        self.parm_pathobjpath = Parameter(parm=self.node.parm('pathobjpath'))
        self.parm_roll = Parameter(parm=self.node.parm('roll'))
        self.parm_pos = Parameter(parm=self.node.parm('pos'))
        self.parm_pathorient = Parameter(parm=self.node.parm('pathorient'))
        self.parm_upx = Parameter(parm=self.node.parm('upx'))
        self.parm_upy = Parameter(parm=self.node.parm('upy'))
        self.parm_upz = Parameter(parm=self.node.parm('upz'))
        self.parm_bank = Parameter(parm=self.node.parm('bank'))
        self.parm_shop_materialpath = Parameter(parm=self.node.parm('shop_materialpath'))
        self.parm_tdisplay = Parameter(parm=self.node.parm('tdisplay'))
        self.parm_display = Parameter(parm=self.node.parm('display'))
        self.parm_use_dcolor = Parameter(parm=self.node.parm('use_dcolor'))
        self.parm_dcolorr = Parameter(parm=self.node.parm('dcolorr'))
        self.parm_dcolorg = Parameter(parm=self.node.parm('dcolorg'))
        self.parm_dcolorb = Parameter(parm=self.node.parm('dcolorb'))
        self.parm_picking = Parameter(parm=self.node.parm('picking'))
        self.parm_caching = Parameter(parm=self.node.parm('caching'))
        self.parm_vport_shadeopen = Parameter(parm=self.node.parm('vport_shadeopen'))
        self.parm_vport_displayassubdiv = Parameter(parm=self.node.parm('vport_displayassubdiv'))
        self.parm_stdswitcher41 = Parameter(parm=self.node.parm('stdswitcher41'))
        self.parm_vm_rendersubd = Parameter(parm=self.node.parm('vm_rendersubd'))
        self.parm_vm_subdgroup = Parameter(parm=self.node.parm('vm_subdgroup'))
        self.parm_vm_osd_quality = Parameter(parm=self.node.parm('vm_osd_quality'))
        self.parm_folder01 = Parameter(parm=self.node.parm('folder01'))
        self.parm_categories = Parameter(parm=self.node.parm('categories'))
        self.parm_reflectmask = Parameter(parm=self.node.parm('reflectmask'))
        self.parm_refractmask = Parameter(parm=self.node.parm('refractmask'))
        self.parm_lightmask = Parameter(parm=self.node.parm('lightmask'))
        self.parm_lightcategories = Parameter(parm=self.node.parm('lightcategories'))
        self.parm_vm_lpetag = Parameter(parm=self.node.parm('vm_lpetag'))
        self.parm_vm_volumefilterwidth = Parameter(parm=self.node.parm('vm_volumefilterwidth'))
        self.parm_vm_matte = Parameter(parm=self.node.parm('vm_matte'))
        self.parm_vm_rayshade = Parameter(parm=self.node.parm('vm_rayshade'))
        self.parm_geo_accelattribute = Parameter(parm=self.node.parm('geo_accelattribute'))
        self.parm_vm_shadingquality = Parameter(parm=self.node.parm('vm_shadingquality'))
        self.parm_vm_flatness = Parameter(parm=self.node.parm('vm_flatness'))
        self.parm_vm_curvesurface = Parameter(parm=self.node.parm('vm_curvesurface'))
        self.parm_vm_rmbackface = Parameter(parm=self.node.parm('vm_rmbackface'))
        self.parm_shop_geometrypath = Parameter(parm=self.node.parm('shop_geometrypath'))
        self.parm_vm_forcegeometry = Parameter(parm=self.node.parm('vm_forcegeometry'))
        self.parm_vm_rendersubdcurves = Parameter(parm=self.node.parm('vm_rendersubdcurves'))
        self.parm_vm_usenforpoints = Parameter(parm=self.node.parm('vm_usenforpoints'))
        self.parm_vm_pointscale = Parameter(parm=self.node.parm('vm_pointscale'))
        self.parm_vm_pscalediameter = Parameter(parm=self.node.parm('vm_pscalediameter'))
        self.parm_vm_metavolume = Parameter(parm=self.node.parm('vm_metavolume'))
        self.parm_vm_overridedetail = Parameter(parm=self.node.parm('vm_overridedetail'))
        self.parm_vm_procuseroottransform = Parameter(parm=self.node.parm('vm_procuseroottransform'))
        self.parm_rs_objprop_switcher1 = Parameter(parm=self.node.parm('rs_objprop_switcher1'))
        self.parm_rs_objpro_first = Parameter(parm=self.node.parm('rs_objpro_first'))
        self.parm_rs_campropshapes_switcher1 = Parameter(parm=self.node.parm('rs_campropshapes_switcher1'))
        self.parm_rs_objprop_id = Parameter(parm=self.node.parm('rs_objprop_id'))
        self.parm_rs_objprop_cryptoid = Parameter(parm=self.node.parm('rs_objprop_cryptoid'))
        self.parm_rs_objprop_cryptomatid_allmat = Parameter(parm=self.node.parm('rs_objprop_cryptomatid_allmat'))
        self.parm_rs_objprop_ngons_enable = Parameter(parm=self.node.parm('rs_objprop_ngons_enable'))
        self.parm_rs_objprop_ngons_avoiddegen = Parameter(parm=self.node.parm('rs_objprop_ngons_avoiddegen'))
        self.parm_rs_objprop_normals_normalize = Parameter(parm=self.node.parm('rs_objprop_normals_normalize'))
        self.parm_rs_objprop_renderashair = Parameter(parm=self.node.parm('rs_objprop_renderashair'))
        self.parm_rs_objprop_defaulthairwidth = Parameter(parm=self.node.parm('rs_objprop_defaulthairwidth'))
        self.parm_rs_objprop_hairhalfthickness = Parameter(parm=self.node.parm('rs_objprop_hairhalfthickness'))
        self.parm_rs_objprop_mb_trans = Parameter(parm=self.node.parm('rs_objprop_mb_trans'))
        self.parm_rs_objprop_mb_def = Parameter(parm=self.node.parm('rs_objprop_mb_def'))
        self.parm_rs_objprop_mb_points = Parameter(parm=self.node.parm('rs_objprop_mb_points'))
        self.parm_rs_objprop_mb_def_use_v = Parameter(parm=self.node.parm('rs_objprop_mb_def_use_v'))
        self.parm_rs_objprop_mb_v_attr = Parameter(parm=self.node.parm('rs_objprop_mb_v_attr'))
        self.parm_rs_objprop_mb_fd_scale = Parameter(parm=self.node.parm('rs_objprop_mb_fd_scale'))
        self.parm_rs_objprop_mb_offset = Parameter(parm=self.node.parm('rs_objprop_mb_offset'))
        self.parm_rs_objprop_rendersopsubnets = Parameter(parm=self.node.parm('rs_objprop_rendersopsubnets'))
        self.parm_rs_objprop_tess_enable = Parameter(parm=self.node.parm('rs_objprop_tess_enable'))
        self.parm_rs_objprop_tess_u = Parameter(parm=self.node.parm('rs_objprop_tess_u'))
        self.parm_rs_objprop_tess_v = Parameter(parm=self.node.parm('rs_objprop_tess_v'))
        self.parm_rs_objprop_tess_trim = Parameter(parm=self.node.parm('rs_objprop_tess_trim'))
        self.parm_rs_objprop_inst_ignorepivot = Parameter(parm=self.node.parm('rs_objprop_inst_ignorepivot'))
        self.parm_rs_objprop_inst_fileoverride = Parameter(parm=self.node.parm('rs_objprop_inst_fileoverride'))
        self.parm_rs_objprop_inst_packed = Parameter(parm=self.node.parm('rs_objprop_inst_packed'))
        self.parm_rs_objprop_inst_packedpriminstancing = Parameter(parm=self.node.parm('rs_objprop_inst_packedpriminstancing'))
        self.parm_rs_objprop_inst_subnetinstancing = Parameter(parm=self.node.parm('rs_objprop_inst_subnetinstancing'))
        self.parm_rs_objprop_attr_auto = Parameter(parm=self.node.parm('rs_objprop_attr_auto'))
        self.parm_rs_objprop_attr_vertex = Parameter(parm=self.node.parm('rs_objprop_attr_vertex'))
        self.parm_rs_objprop_attr_points = Parameter(parm=self.node.parm('rs_objprop_attr_points'))
        self.parm_rs_objprop_attr_primitives = Parameter(parm=self.node.parm('rs_objprop_attr_primitives'))
        self.parm_rs_objprop_attr_detail = Parameter(parm=self.node.parm('rs_objprop_attr_detail'))
        self.parm_rs_objprop_pckattr_promotion = Parameter(parm=self.node.parm('rs_objprop_pckattr_promotion'))
        self.parm_rs_objprop_pckattr_replace = Parameter(parm=self.node.parm('rs_objprop_pckattr_replace'))
        self.parm_rs_objprop_pckattr_mult = Parameter(parm=self.node.parm('rs_objprop_pckattr_mult'))
        self.parm_rs_objprop_pckattr_add = Parameter(parm=self.node.parm('rs_objprop_pckattr_add'))
        self.parm_rs_objprop_tracesets_enabled = Parameter(parm=self.node.parm('rs_objprop_tracesets_enabled'))
        self.parm_rs_objprop_tracesets_reflection = Parameter(parm=self.node.parm('rs_objprop_tracesets_reflection'))
        self.parm_rs_objprop_tracesets_refraction = Parameter(parm=self.node.parm('rs_objprop_tracesets_refraction'))
        self.parm_rs_objprop_tracesets_sss = Parameter(parm=self.node.parm('rs_objprop_tracesets_sss'))
        self.parm_rs_objprop_ipr_forcemeshupdate = Parameter(parm=self.node.parm('rs_objprop_ipr_forcemeshupdate'))
        self.parm_rs_objpro_label5 = Parameter(parm=self.node.parm('rs_objpro_label5'))
        self.parm_rs_objprop_proxy_enable = Parameter(parm=self.node.parm('rs_objprop_proxy_enable'))
        self.parm_rs_objprop_proxy_prevpercent = Parameter(parm=self.node.parm('rs_objprop_proxy_prevpercent'))
        self.parm_rs_objprop_proxy_prevlines = Parameter(parm=self.node.parm('rs_objprop_proxy_prevlines'))
        self.parm_rs_objprop_proxy_prevanimated = Parameter(parm=self.node.parm('rs_objprop_proxy_prevanimated'))
        self.parm_rs_objprop_proxy_override = Parameter(parm=self.node.parm('rs_objprop_proxy_override'))
        self.parm_rs_objprop_proxy_overridelist = Parameter(parm=self.node.parm('rs_objprop_proxy_overridelist'))
        self.parm_rs_objprop_proxy_elements_mesh = Parameter(parm=self.node.parm('rs_objprop_proxy_elements_mesh'))
        self.parm_rs_objprop_proxy_elements_volume = Parameter(parm=self.node.parm('rs_objprop_proxy_elements_volume'))
        self.parm_rs_objprop_proxy_elements_light = Parameter(parm=self.node.parm('rs_objprop_proxy_elements_light'))
        self.parm_rs_objprop_proxy_elements_proxy = Parameter(parm=self.node.parm('rs_objprop_proxy_elements_proxy'))
        self.parm_rs_objprop_proxy_ovrid = Parameter(parm=self.node.parm('rs_objprop_proxy_ovrid'))
        self.parm_rs_objprop_proxy_ovrvis = Parameter(parm=self.node.parm('rs_objprop_proxy_ovrvis'))
        self.parm_rs_objprop_proxy_ovrtess = Parameter(parm=self.node.parm('rs_objprop_proxy_ovrtess'))
        self.parm_rs_objprop_proxy_ovrtraces = Parameter(parm=self.node.parm('rs_objprop_proxy_ovrtraces'))
        self.parm_rs_objprop_proxy_ovruserdata = Parameter(parm=self.node.parm('rs_objprop_proxy_ovruserdata'))
        self.parm_rs_objpro_label1o = Parameter(parm=self.node.parm('rs_objpro_label1o'))
        self.parm_meshflag_primaryrayvisible = Parameter(parm=self.node.parm('meshflag_primaryrayvisible'))
        self.parm_meshflag_secondaryrayvisible = Parameter(parm=self.node.parm('meshflag_secondaryrayvisible'))
        self.parm_meshflag_shadowcaster = Parameter(parm=self.node.parm('meshflag_shadowcaster'))
        self.parm_meshflag_shadowreceiver = Parameter(parm=self.node.parm('meshflag_shadowreceiver'))
        self.parm_meshflag_noselfshadow = Parameter(parm=self.node.parm('meshflag_noselfshadow'))
        self.parm_meshflag_aocaster = Parameter(parm=self.node.parm('meshflag_aocaster'))
        self.parm_meshflag_reflectionvisible = Parameter(parm=self.node.parm('meshflag_reflectionvisible'))
        self.parm_meshflag_refractionvisible = Parameter(parm=self.node.parm('meshflag_refractionvisible'))
        self.parm_meshflag_reflectioncaster = Parameter(parm=self.node.parm('meshflag_reflectioncaster'))
        self.parm_meshflag_refractioncaster = Parameter(parm=self.node.parm('meshflag_refractioncaster'))
        self.parm_meshflag_fgvisible = Parameter(parm=self.node.parm('meshflag_fgvisible'))
        self.parm_meshflag_givisible = Parameter(parm=self.node.parm('meshflag_givisible'))
        self.parm_meshflag_causticvisible = Parameter(parm=self.node.parm('meshflag_causticvisible'))
        self.parm_meshflag_fgcaster = Parameter(parm=self.node.parm('meshflag_fgcaster'))
        self.parm_meshflag_forcebruteforcegi = Parameter(parm=self.node.parm('meshflag_forcebruteforcegi'))
        self.parm_meshflag_gicaster = Parameter(parm=self.node.parm('meshflag_gicaster'))
        self.parm_meshflag_causticcaster = Parameter(parm=self.node.parm('meshflag_causticcaster'))
        self.parm_rs_objpro_label2 = Parameter(parm=self.node.parm('rs_objpro_label2'))
        self.parm_rs_objprop_rstess_enable = Parameter(parm=self.node.parm('rs_objprop_rstess_enable'))
        self.parm_rs_objprop_rstess_ssadaptive = Parameter(parm=self.node.parm('rs_objprop_rstess_ssadaptive'))
        self.parm_rs_objprop_rstess_smoothsub = Parameter(parm=self.node.parm('rs_objprop_rstess_smoothsub'))
        self.parm_rs_objprop_rstess_triquads = Parameter(parm=self.node.parm('rs_objprop_rstess_triquads'))
        self.parm_rs_objprop_rstess_melenght = Parameter(parm=self.node.parm('rs_objprop_rstess_melenght'))
        self.parm_rs_objprop_rstess_maxsubd = Parameter(parm=self.node.parm('rs_objprop_rstess_maxsubd'))
        self.parm_rs_objprop_rstess_ooftf = Parameter(parm=self.node.parm('rs_objprop_rstess_ooftf'))
        self.parm_rs_objprop_rstess_looft = Parameter(parm=self.node.parm('rs_objprop_rstess_looft'))
        self.parm_rs_objprop_rstess_looftsubd = Parameter(parm=self.node.parm('rs_objprop_rstess_looftsubd'))
        self.parm_rs_objprop_rstess_smooth = Parameter(parm=self.node.parm('rs_objprop_rstess_smooth'))
        self.parm_rs_objprop_rstess_smoothbound = Parameter(parm=self.node.parm('rs_objprop_rstess_smoothbound'))
        self.parm_rs_objpro_label3 = Parameter(parm=self.node.parm('rs_objpro_label3'))
        self.parm_rs_objprop_displace_enable = Parameter(parm=self.node.parm('rs_objprop_displace_enable'))
        self.parm_rs_objprop_displace_max = Parameter(parm=self.node.parm('rs_objprop_displace_max'))
        self.parm_rs_objprop_displace_scale = Parameter(parm=self.node.parm('rs_objprop_displace_scale'))
        self.parm_rs_objprop_displace_autob = Parameter(parm=self.node.parm('rs_objprop_displace_autob'))
        self.parm_rs_objpro_label4 = Parameter(parm=self.node.parm('rs_objpro_label4'))
        self.parm_rs_objprop_matte_enable = Parameter(parm=self.node.parm('rs_objprop_matte_enable'))
        self.parm_rs_objprop_matte_showbackg = Parameter(parm=self.node.parm('rs_objprop_matte_showbackg'))
        self.parm_rs_objprop_matte_applysec = Parameter(parm=self.node.parm('rs_objprop_matte_applysec'))
        self.parm_rs_objprop_matte_abyml = Parameter(parm=self.node.parm('rs_objprop_matte_abyml'))
        self.parm_rs_objprop_matte_includepm = Parameter(parm=self.node.parm('rs_objprop_matte_includepm'))
        self.parm_rs_objprop_matte_alpha = Parameter(parm=self.node.parm('rs_objprop_matte_alpha'))
        self.parm_rs_objprop_matte_reflscale = Parameter(parm=self.node.parm('rs_objprop_matte_reflscale'))
        self.parm_rs_objprop_matte_refrscale = Parameter(parm=self.node.parm('rs_objprop_matte_refrscale'))
        self.parm_rs_objprop_matte_diffscale = Parameter(parm=self.node.parm('rs_objprop_matte_diffscale'))
        self.parm_rs_objprop_matte_shadowenable = Parameter(parm=self.node.parm('rs_objprop_matte_shadowenable'))
        self.parm_rs_objprop_matte_shadowsfromm = Parameter(parm=self.node.parm('rs_objprop_matte_shadowsfromm'))
        self.parm_rs_objprop_matte_shadowalpha = Parameter(parm=self.node.parm('rs_objprop_matte_shadowalpha'))
        self.parm_rs_objprop_matte_shadowcolorr = Parameter(parm=self.node.parm('rs_objprop_matte_shadowcolorr'))
        self.parm_rs_objprop_matte_shadowcolorg = Parameter(parm=self.node.parm('rs_objprop_matte_shadowcolorg'))
        self.parm_rs_objprop_matte_shadowcolorb = Parameter(parm=self.node.parm('rs_objprop_matte_shadowcolorb'))
        self.parm_rs_objprop_matte_shadowtrans = Parameter(parm=self.node.parm('rs_objprop_matte_shadowtrans'))
        self.parm_rs_objpro_label6 = Parameter(parm=self.node.parm('rs_objpro_label6'))
        self.parm_rs_objprop_strands_enable = Parameter(parm=self.node.parm('rs_objprop_strands_enable'))
        self.parm_rs_objprop_strands_maxsubd = Parameter(parm=self.node.parm('rs_objprop_strands_maxsubd'))
        self.parm_rs_objprop_strands_scale = Parameter(parm=self.node.parm('rs_objprop_strands_scale'))
        self.parm_rs_objprop_strands_scalemult = Parameter(parm=self.node.parm('rs_objprop_strands_scalemult'))
        self.parm_rs_objprop_strands_ignorepscale = Parameter(parm=self.node.parm('rs_objprop_strands_ignorepscale'))
        self.parm_rs_objprop_strands_usecamera = Parameter(parm=self.node.parm('rs_objprop_strands_usecamera'))
        self.parm_rs_objpro_label10 = Parameter(parm=self.node.parm('rs_objpro_label10'))
        self.parm_rs_objprop_particles_enable = Parameter(parm=self.node.parm('rs_objprop_particles_enable'))
        self.parm_rs_objprop_particles_ignorescale = Parameter(parm=self.node.parm('rs_objprop_particles_ignorescale'))
        self.parm_rs_objprop_particles_scale = Parameter(parm=self.node.parm('rs_objprop_particles_scale'))
        self.parm_rs_objprop_particles_scalemult = Parameter(parm=self.node.parm('rs_objprop_particles_scalemult'))
        self.parm_rs_objpro_label7 = Parameter(parm=self.node.parm('rs_objpro_label7'))
        self.parm_rs_objprop_volume_enable = Parameter(parm=self.node.parm('rs_objprop_volume_enable'))
        self.parm_rs_objprop_volume_filtern = Parameter(parm=self.node.parm('rs_objprop_volume_filtern'))
        self.parm_rs_objprop_volume_filterdeg = Parameter(parm=self.node.parm('rs_objprop_volume_filterdeg'))
        self.parm_rs_objprop_volume_filterdegthr = Parameter(parm=self.node.parm('rs_objprop_volume_filterdegthr'))
        self.parm_rs_objprop_volume_cleanbackg = Parameter(parm=self.node.parm('rs_objprop_volume_cleanbackg'))
        self.parm_rs_objprop_volume_v = Parameter(parm=self.node.parm('rs_objprop_volume_v'))
        self.parm_rs_objprop_volume_vx = Parameter(parm=self.node.parm('rs_objprop_volume_vx'))
        self.parm_rs_objprop_volume_vy = Parameter(parm=self.node.parm('rs_objprop_volume_vy'))
        self.parm_rs_objprop_volume_vz = Parameter(parm=self.node.parm('rs_objprop_volume_vz'))
        self.parm_rs_objprop_volume_vs = Parameter(parm=self.node.parm('rs_objprop_volume_vs'))
        self.parm_rs_objpro_last = Parameter(parm=self.node.parm('rs_objpro_last'))

        
        # parm menu vars:
        self.parm_xord_menu = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord_menu = RordMenu(parm=self.node.parm('rOrd'))
        self.parm_pre_xform_menu = PreXformMenu(parm=self.node.parm('pre_xform'))
        self.parm_lookup_menu = LookupMenu(parm=self.node.parm('lookup'))
        self.parm_uparmtype_menu = UparmtypeMenu(parm=self.node.parm('uparmtype'))
        self.parm_shop_materialopts_menu = ShopMaterialoptsMenu(parm=self.node.parm('shop_materialopts'))
        self.parm_pickscript_menu = PickscriptMenu(parm=self.node.parm('pickscript'))
        self.parm_vport_onionskin_menu = VportOnionskinMenu(parm=self.node.parm('vport_onionskin'))
        self.parm_viewportlod_menu = ViewportlodMenu(parm=self.node.parm('viewportlod'))
        self.parm_vm_rendervisibility_menu = VmRendervisibilityMenu(parm=self.node.parm('vm_rendervisibility'))
        self.parm_vm_subdstyle_menu = VmSubdstyleMenu(parm=self.node.parm('vm_subdstyle'))
        self.parm_vm_osd_vtxinterp_menu = VmOsdVtxinterpMenu(parm=self.node.parm('vm_osd_vtxinterp'))
        self.parm_vm_osd_fvarinterp_menu = VmOsdFvarinterpMenu(parm=self.node.parm('vm_osd_fvarinterp'))
        self.parm_vm_volumefilter_menu = VmVolumefilterMenu(parm=self.node.parm('vm_volumefilter'))
        self.parm_geo_velocityblur_menu = GeoVelocityblurMenu(parm=self.node.parm('geo_velocityblur'))
        self.parm_vm_raypredice_menu = VmRayprediceMenu(parm=self.node.parm('vm_raypredice'))
        self.parm_vm_renderpoints_menu = VmRenderpointsMenu(parm=self.node.parm('vm_renderpoints'))
        self.parm_vm_renderpointsas_menu = VmRenderpointsasMenu(parm=self.node.parm('vm_renderpointsas'))
        self.parm_vm_coving_menu = VmCovingMenu(parm=self.node.parm('vm_coving'))
        self.parm_vm_materialoverride_menu = VmMaterialoverrideMenu(parm=self.node.parm('vm_materialoverride'))
        self.parm_rs_objprop_ngons_tessmode_menu = RsObjpropNgonsTessmodeMenu(parm=self.node.parm('RS_objprop_ngons_tessMode'))
        self.parm_rs_objprop_mb_deformsteps_menu = RsObjpropMbDeformstepsMenu(parm=self.node.parm('RS_objprop_mb_deformSteps'))
        self.parm_rs_objprop_inst_mode_menu = RsObjpropInstModeMenu(parm=self.node.parm('RS_objprop_inst_mode'))
        self.parm_rs_objprop_inst_mb_menu = RsObjpropInstMbMenu(parm=self.node.parm('RS_objprop_inst_mb'))
        self.parm_rs_objprop_inst_lightshader_menu = RsObjpropInstLightshaderMenu(parm=self.node.parm('RS_objprop_inst_lightShader'))
        self.parm_rs_objprop_inst_universalif_menu = RsObjpropInstUniversalifMenu(parm=self.node.parm('RS_objprop_inst_universalIF'))
        self.parm_rs_objprop_proxy_file_menu = RsObjpropProxyFileMenu(parm=self.node.parm('RS_objprop_proxy_file'))
        self.parm_rs_objprop_proxy_preview_menu = RsObjpropProxyPreviewMenu(parm=self.node.parm('RS_objprop_proxy_preview'))
        self.parm_rs_objprop_proxy_materials_menu = RsObjpropProxyMaterialsMenu(parm=self.node.parm('RS_objprop_proxy_materials'))
        self.parm_rs_objprop_rstess_rule_menu = RsObjpropRstessRuleMenu(parm=self.node.parm('RS_objprop_rstess_rule'))
        self.parm_rs_objprop_strands_type_menu = RsObjpropStrandsTypeMenu(parm=self.node.parm('RS_objprop_strands_type'))
        self.parm_rs_objprop_volume_type_menu = RsObjpropVolumeTypeMenu(parm=self.node.parm('RS_objprop_volume_type'))


        # input vars:
        self.input_parent = 0


# parm menu classes:
class XordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.scale_rot_trans = 0
        self.scale_trans_rot = 1
        self.rot_scale_trans = 2
        self.rot_trans_scale = 3
        self.trans_scale_rot = 4
        self.trans_rot_scale = 5


class RordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.rx_ry_rz = 0
        self.rx_rz_ry = 1
        self.ry_rx_rz = 2
        self.ry_rz_rx = 3
        self.rz_rx_ry = 4
        self.rz_ry_rx = 5


class PreXformMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.clean_transform = 0
        self.clean_translates = 1
        self.clean_rotates = 2
        self.clean_scales = 3
        self.extract_pre_transform = 4
        self.reset_pre_transform = 5


class LookupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.don_t_use_up_vector = 0
        self.use_up_vector = 1
        self.use_quaternions = 2
        self.use_global_position = 3
        self.use_up_object = 4


class UparmtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.uniform = 0
        self.arc_length = 1


class ShopMaterialoptsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.create_all_local_material_parameters = 0
        self.select_and_create_local_material_parameters = 1
        self.remove_all_local_material_parameters = 2
        self.remove_unchanged_local_material_parameters = 3
        self.synchronize_with_global_material_parameters = 4
        self.revert_to_global_material_parameter_values = 5


class PickscriptMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self._hip_my_first_tree_prox_rs = 0
        self.c__programdata_r____portra_800_cube = 1
        self._hip_grasses_grass_card_001_fbx = 2
        self.e__art_projects____rock_stone_sbsar = 3
        self.e__art_projects____mud_ground_sbsar = 4
        self.e__art_projects____u_sugi_ban_sbsar = 5
        self.e__art_projects_____facade_02_sbsar = 6
        self.e__art_projects____and_smooth_sbsar = 7
        self._hip_crystallize___ice_nugget_sbsar = 8
        self._hip_chromatic_glass_gradient_sbsar = 9
        self._hip_acid_etched_glass_rough_sbsar = 10
        self.e__art_projects____agon_tiles_sbsar = 11


class VportOnionskinMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.off = 0
        self.transform_only = 1
        self.full_deformation = 2


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.full_geometry = 0
        self.point_cloud = 1
        self.bounding_box = 2
        self.centroid = 3
        self.hidden = 4
        self.subdivision_surface___curves = 5


class VmRendervisibilityMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.visible_to_all = 0
        self.visible_only_to_primary_rays = 1
        self.visible_only_to_primary_and_shadow_rays = 2
        self.invisible_to_primary_rays__phantom_ = 3
        self.invisible_to_diffuse_rays = 4
        self.invisible_to_secondary_rays = 5
        self.invisible__unrenderable_ = 6


class VmSubdstyleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.mantra_catmull_clark = 0
        self.opensubdiv_catmull_clark = 1


class VmOsdVtxinterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.no_vertex_interpolation = 0
        self.edges_only = 1
        self.edges_and_corners = 2


class VmOsdFvarinterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.smooth_everywhere = 0
        self.sharpen_corners_only = 1
        self.sharpen_edges_and_corners = 2
        self.sharpen_edges_and_propagated_corners = 3
        self.sharpen_all_boundaries = 4
        self.bilinear_interpolation = 5


class VmVolumefilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.box_filter = 0
        self.gaussian = 1
        self.bartlett__triangle_ = 2
        self.catmull_rom = 3
        self.hanning = 4
        self.blackman = 5
        self.sinc__sharpening_ = 6


class GeoVelocityblurMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.no_velocity_blur = 0
        self.velocity_blur = 1
        self.acceleration_blur = 2


class VmRayprediceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.disable_predicing = 0
        self.full_predicing = 1
        self.precompute_bounds = 2


class VmRenderpointsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.no_point_rendering = 0
        self.render_only_points = 1
        self.render_unconnected_points = 2


class VmRenderpointsasMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.spheres = 0
        self.circles = 1


class VmCovingMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.disable_coving = 0
        self.coving_for_displacement_sub_d = 1
        self.coving_for_all_primitives = 2


class VmMaterialoverrideMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.disabled = 0
        self.evaluate_for_each_primitve_point = 1
        self.evaluate_once = 2


class RsObjpropNgonsTessmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.to_quads = 0
        self.to_triangles = 1


class RsObjpropMbDeformstepsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.auto = 0
        self.steps_2 = 1
        self.steps_3 = 2
        self.steps_5 = 3
        self.steps_9 = 4
        self.steps_17 = 5


class RsObjpropInstModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.redshift_instances = 0
        self.redshift_point_clouds = 1


class RsObjpropInstMbMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.compute_sub_frame_geometry__deformation_ = 0
        self.use_point_velocity_attribute = 1


class RsObjpropInstLightshaderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.attributes_support_using_individual_shaders = 0
        self.using_a_common_shared_shader = 1


class RsObjpropInstUniversalifMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.instance_redshift_proxy_objects = 0
        self.instance_houdini_compatible_objects = 1


class RsObjpropProxyFileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self._hip_my_first_tree_prox_rs = 0
        self.c__programdata_r____portra_800_cube = 1
        self._hip_grasses_grass_card_001_fbx = 2
        self.e__art_projects____rock_stone_sbsar = 3
        self.e__art_projects____mud_ground_sbsar = 4
        self.e__art_projects____u_sugi_ban_sbsar = 5
        self.e__art_projects_____facade_02_sbsar = 6
        self.e__art_projects____and_smooth_sbsar = 7
        self._hip_crystallize___ice_nugget_sbsar = 8
        self._hip_chromatic_glass_gradient_sbsar = 9
        self._hip_acid_etched_glass_rough_sbsar = 10
        self.e__art_projects____agon_tiles_sbsar = 11


class RsObjpropProxyPreviewMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.none = 0
        self.bounding_box = 1
        self.mesh = 2
        self.points = 3


class RsObjpropProxyMaterialsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.from_proxy = 0
        self.from_obj_node = 1
        self.full_override = 2
        self.list_override = 3
        self.from_scene_materials = 4


class RsObjpropRstessRuleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.catmull_clark___loop = 0
        self.catmull_clark_only = 1


class RsObjpropStrandsTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.box = 0
        self.cylinder = 1
        self.capsule = 2
        self.cone = 3
        self.strip = 4


class RsObjpropVolumeTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.openvdb_file = 0
        self.volume_vdb_houdini_primitive = 1



