from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class GeoNode(OXNode):
    node_type = 'geo'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz', 'scale': 'scale', 'pre_xform': 'pre_xform', 'keeppos': 'keeppos', 'childcomp': 'childcomp', 'constraints_on': 'constraints_on', 'constraints_path': 'constraints_path', 'lookatpath': 'lookatpath', 'lookupobjpath': 'lookupobjpath', 'lookup': 'lookup', 'pathobjpath': 'pathobjpath', 'roll': 'roll', 'pos': 'pos', 'uparmtype': 'uparmtype', 'pathorient': 'pathorient', 'upx': 'upx', 'upy': 'upy', 'upz': 'upz', 'bank': 'bank', 'shop_materialpath': 'shop_materialpath', 'shop_materialopts': 'shop_materialopts', 'tdisplay': 'tdisplay', 'display': 'display', 'use_dcolor': 'use_dcolor', 'dcolorr': 'dcolorr', 'dcolorg': 'dcolorg', 'dcolorb': 'dcolorb', 'picking': 'picking', 'pickscript': 'pickscript', 'caching': 'caching', 'vport_shadeopen': 'vport_shadeopen', 'vport_displayassubdiv': 'vport_displayassubdiv', 'vport_onionskin': 'vport_onionskin', 'stdswitcher41': 'stdswitcher41', 'viewportlod': 'viewportlod', 'vm_rendervisibility': 'vm_rendervisibility', 'vm_rendersubd': 'vm_rendersubd', 'vm_subdstyle': 'vm_subdstyle', 'vm_subdgroup': 'vm_subdgroup', 'vm_osd_quality': 'vm_osd_quality', 'vm_osd_vtxinterp': 'vm_osd_vtxinterp', 'vm_osd_fvarinterp': 'vm_osd_fvarinterp', 'folder01': 'folder01', 'categories': 'categories', 'reflectmask': 'reflectmask', 'refractmask': 'refractmask', 'lightmask': 'lightmask', 'lightcategories': 'lightcategories', 'vm_lpetag': 'vm_lpetag', 'vm_volumefilter': 'vm_volumefilter', 'vm_volumefilterwidth': 'vm_volumefilterwidth', 'vm_matte': 'vm_matte', 'vm_rayshade': 'vm_rayshade', 'geo_velocityblur': 'geo_velocityblur', 'geo_accelattribute': 'geo_accelattribute', 'vm_shadingquality': 'vm_shadingquality', 'vm_flatness': 'vm_flatness', 'vm_raypredice': 'vm_raypredice', 'vm_curvesurface': 'vm_curvesurface', 'vm_rmbackface': 'vm_rmbackface', 'shop_geometrypath': 'shop_geometrypath', 'vm_forcegeometry': 'vm_forcegeometry', 'vm_rendersubdcurves': 'vm_rendersubdcurves', 'vm_renderpoints': 'vm_renderpoints', 'vm_renderpointsas': 'vm_renderpointsas', 'vm_usenforpoints': 'vm_usenforpoints', 'vm_pointscale': 'vm_pointscale', 'vm_pscalediameter': 'vm_pscalediameter', 'vm_metavolume': 'vm_metavolume', 'vm_coving': 'vm_coving', 'vm_materialoverride': 'vm_materialoverride', 'vm_overridedetail': 'vm_overridedetail', 'vm_procuseroottransform': 'vm_procuseroottransform', 'rs_objprop_switcher1': 'RS_objprop_switcher1', 'rs_objpro_first': 'RS_objpro_first', 'rs_campropshapes_switcher1': 'RS_campropshapes_switcher1', 'rs_objprop_id': 'RS_objprop_ID', 'rs_objprop_cryptoid': 'RS_objprop_CryptoID', 'rs_objprop_cryptomatid_allmat': 'RS_objprop_CryptoMatID_AllMat', 'rs_objprop_ngons_enable': 'RS_objprop_ngons_enable', 'rs_objprop_ngons_tessmode': 'RS_objprop_ngons_tessMode', 'rs_objprop_ngons_avoiddegen': 'RS_objprop_ngons_avoidDegen', 'rs_objprop_normals_normalize': 'RS_objprop_normals_normalize', 'rs_objprop_renderashair': 'RS_objprop_renderAsHair', 'rs_objprop_defaulthairwidth': 'RS_objprop_defaultHairWidth', 'rs_objprop_hairhalfthickness': 'RS_objprop_hairHalfThickness', 'rs_objprop_mb_trans': 'RS_objprop_mb_trans', 'rs_objprop_mb_def': 'RS_objprop_mb_def', 'rs_objprop_mb_points': 'RS_objprop_mb_points', 'rs_objprop_mb_def_use_v': 'RS_objprop_mb_def_use_v', 'rs_objprop_mb_v_attr': 'RS_objprop_mb_v_attr', 'rs_objprop_mb_deformsteps': 'RS_objprop_mb_deformSteps', 'rs_objprop_mb_fd_scale': 'RS_objprop_mb_fd_scale', 'rs_objprop_mb_offset': 'RS_objprop_mb_offset', 'rs_objprop_rendersopsubnets': 'RS_objprop_renderSOPsubnets', 'rs_objprop_tess_enable': 'RS_objprop_tess_enable', 'rs_objprop_tess_u': 'RS_objprop_tess_u', 'rs_objprop_tess_v': 'RS_objprop_tess_v', 'rs_objprop_tess_trim': 'RS_objprop_tess_trim', 'rs_objprop_inst_mode': 'RS_objprop_inst_mode', 'rs_objprop_inst_mb': 'RS_objprop_inst_mb', 'rs_objprop_inst_lightshader': 'RS_objprop_inst_lightShader', 'rs_objprop_inst_universalif': 'RS_objprop_inst_universalIF', 'rs_objprop_inst_ignorepivot': 'RS_objprop_inst_ignorePivot', 'rs_objprop_inst_fileoverride': 'RS_objprop_inst_fileOverride', 'rs_objprop_inst_packed': 'RS_objprop_inst_packed', 'rs_objprop_inst_packedpriminstancing': 'RS_objprop_inst_PackedPrimInstancing', 'rs_objprop_inst_subnetinstancing': 'RS_objprop_inst_subnetInstancing', 'rs_objprop_attr_auto': 'RS_objprop_attr_auto', 'rs_objprop_attr_vertex': 'RS_objprop_attr_vertex', 'rs_objprop_attr_points': 'RS_objprop_attr_points', 'rs_objprop_attr_primitives': 'RS_objprop_attr_primitives', 'rs_objprop_attr_detail': 'RS_objprop_attr_detail', 'rs_objprop_pckattr_promotion': 'RS_objprop_pckattr_promotion', 'rs_objprop_pckattr_replace': 'RS_objprop_pckattr_replace', 'rs_objprop_pckattr_mult': 'RS_objprop_pckattr_mult', 'rs_objprop_pckattr_add': 'RS_objprop_pckattr_add', 'rs_objprop_tracesets_enabled': 'RS_objprop_tracesets_enabled', 'rs_objprop_tracesets_reflection': 'RS_objprop_tracesets_reflection', 'rs_objprop_tracesets_refraction': 'RS_objprop_tracesets_refraction', 'rs_objprop_tracesets_sss': 'RS_objprop_tracesets_sss', 'rs_objprop_ipr_forcemeshupdate': 'RS_objprop_ipr_forceMeshUpdate', 'rs_objpro_label5': 'RS_objpro_label5', 'rs_objprop_proxy_enable': 'RS_objprop_proxy_enable', 'rs_objprop_proxy_file': 'RS_objprop_proxy_file', 'rs_objprop_proxy_preview': 'RS_objprop_proxy_preview', 'rs_objprop_proxy_prevpercent': 'RS_objprop_proxy_prevPercent', 'rs_objprop_proxy_prevlines': 'RS_objprop_proxy_prevLines', 'rs_objprop_proxy_prevanimated': 'RS_objprop_proxy_prevAnimated', 'rs_objprop_proxy_materials': 'RS_objprop_proxy_materials', 'rs_objprop_proxy_override': 'RS_objprop_proxy_override', 'rs_objprop_proxy_overridelist': 'RS_objprop_proxy_overrideList', 'rs_objprop_proxy_elements_mesh': 'RS_objprop_proxy_elements_mesh', 'rs_objprop_proxy_elements_volume': 'RS_objprop_proxy_elements_volume', 'rs_objprop_proxy_elements_light': 'RS_objprop_proxy_elements_light', 'rs_objprop_proxy_elements_proxy': 'RS_objprop_proxy_elements_proxy', 'rs_objprop_proxy_ovrid': 'RS_objprop_proxy_ovrID', 'rs_objprop_proxy_ovrvis': 'RS_objprop_proxy_ovrVis', 'rs_objprop_proxy_ovrtess': 'RS_objprop_proxy_ovrTess', 'rs_objprop_proxy_ovrtraces': 'RS_objprop_proxy_ovrTraceS', 'rs_objprop_proxy_ovruserdata': 'RS_objprop_proxy_ovrUserData', 'rs_objpro_label1o': 'RS_objpro_label1o', 'meshflag_primaryrayvisible': 'MESHFLAG_PRIMARYRAYVISIBLE', 'meshflag_secondaryrayvisible': 'MESHFLAG_SECONDARYRAYVISIBLE', 'meshflag_shadowcaster': 'MESHFLAG_SHADOWCASTER', 'meshflag_shadowreceiver': 'MESHFLAG_SHADOWRECEIVER', 'meshflag_noselfshadow': 'MESHFLAG_NOSELFSHADOW', 'meshflag_aocaster': 'MESHFLAG_AOCASTER', 'meshflag_reflectionvisible': 'MESHFLAG_REFLECTIONVISIBLE', 'meshflag_refractionvisible': 'MESHFLAG_REFRACTIONVISIBLE', 'meshflag_reflectioncaster': 'MESHFLAG_REFLECTIONCASTER', 'meshflag_refractioncaster': 'MESHFLAG_REFRACTIONCASTER', 'meshflag_fgvisible': 'MESHFLAG_FGVISIBLE', 'meshflag_givisible': 'MESHFLAG_GIVISIBLE', 'meshflag_causticvisible': 'MESHFLAG_CAUSTICVISIBLE', 'meshflag_fgcaster': 'MESHFLAG_FGCASTER', 'meshflag_forcebruteforcegi': 'MESHFLAG_FORCEBRUTEFORCEGI', 'meshflag_gicaster': 'MESHFLAG_GICASTER', 'meshflag_causticcaster': 'MESHFLAG_CAUSTICCASTER', 'meshflag_causticsreceiver': 'MESHFLAG_CAUSTICSRECEIVER', 'rs_objpro_label2': 'RS_objpro_label2', 'rs_objprop_rstess_enable': 'RS_objprop_rstess_enable', 'rs_objprop_rstess_rule': 'RS_objprop_rstess_rule', 'rs_objprop_rstess_ssadaptive': 'RS_objprop_rstess_ssadaptive', 'rs_objprop_rstess_smoothsub': 'RS_objprop_rstess_smoothsub', 'rs_objprop_rstess_triquads': 'RS_objprop_rstess_triQuads', 'rs_objprop_rstess_melenght': 'RS_objprop_rstess_melenght', 'rs_objprop_rstess_maxsubd': 'RS_objprop_rstess_maxsubd', 'rs_objprop_rstess_ooftf': 'RS_objprop_rstess_ooftf', 'rs_objprop_rstess_looft': 'RS_objprop_rstess_looft', 'rs_objprop_rstess_looftsubd': 'RS_objprop_rstess_looftSubd', 'rs_objprop_rstess_smooth': 'RS_objprop_rstess_smooth', 'rs_objprop_rstess_smoothbound': 'RS_objprop_rstess_smoothBound', 'rs_objpro_label3': 'RS_objpro_label3', 'rs_objprop_displace_enable': 'RS_objprop_displace_enable', 'rs_objprop_displace_max': 'RS_objprop_displace_max', 'rs_objprop_displace_scale': 'RS_objprop_displace_scale', 'rs_objprop_displace_autob': 'RS_objprop_displace_autob', 'rs_objpro_label4': 'RS_objpro_label4', 'rs_objprop_matte_enable': 'RS_objprop_matte_enable', 'rs_objprop_matte_showbackg': 'RS_objprop_matte_showbackg', 'rs_objprop_matte_applysec': 'RS_objprop_matte_applysec', 'rs_objprop_matte_abyml': 'RS_objprop_matte_abyml', 'rs_objprop_matte_includepm': 'RS_objprop_matte_includePM', 'rs_objprop_matte_alpha': 'RS_objprop_matte_alpha', 'rs_objprop_matte_reflscale': 'RS_objprop_matte_reflscale', 'rs_objprop_matte_refrscale': 'RS_objprop_matte_refrscale', 'rs_objprop_matte_diffscale': 'RS_objprop_matte_diffscale', 'rs_objprop_matte_shadowenable': 'RS_objprop_matte_shadowenable', 'rs_objprop_matte_shadowsfromm': 'RS_objprop_matte_shadowsFromM', 'rs_objprop_matte_shadowalpha': 'RS_objprop_matte_shadowalpha', 'rs_objprop_matte_shadowcolorr': 'RS_objprop_matte_shadowcolorr', 'rs_objprop_matte_shadowcolorg': 'RS_objprop_matte_shadowcolorg', 'rs_objprop_matte_shadowcolorb': 'RS_objprop_matte_shadowcolorb', 'rs_objprop_matte_shadowtrans': 'RS_objprop_matte_shadowtrans', 'rs_objpro_label6': 'RS_objpro_label6', 'rs_objprop_strands_enable': 'RS_objprop_strands_enable', 'rs_objprop_strands_type': 'RS_objprop_strands_type', 'rs_objprop_strands_maxsubd': 'RS_objprop_strands_maxSubd', 'rs_objprop_strands_scale': 'RS_objprop_strands_scale', 'rs_objprop_strands_scalemult': 'RS_objprop_strands_scaleMult', 'rs_objprop_strands_ignorepscale': 'RS_objprop_strands_ignorePScale', 'rs_objprop_strands_usecamera': 'RS_objprop_strands_useCamera', 'rs_objpro_label10': 'RS_objpro_label10', 'rs_objprop_particles_enable': 'RS_objprop_particles_enable', 'rs_objprop_particles_ignorescale': 'RS_objprop_particles_ignoreScale', 'rs_objprop_particles_scale': 'RS_objprop_particles_scale', 'rs_objprop_particles_scalemult': 'RS_objprop_particles_scaleMult', 'rs_objpro_label7': 'RS_objpro_label7', 'rs_objprop_volume_enable': 'RS_objprop_volume_enable', 'rs_objprop_volume_type': 'RS_objprop_volume_type', 'rs_objprop_volume_filtern': 'RS_objprop_volume_filterN', 'rs_objprop_volume_filterdeg': 'RS_objprop_volume_filterDeg', 'rs_objprop_volume_filterdegthr': 'RS_objprop_volume_filterDegThr', 'rs_objprop_volume_cleanbackg': 'RS_objprop_volume_cleanBackg', 'rs_objprop_volume_v': 'RS_objprop_volume_v', 'rs_objprop_volume_vx': 'RS_objprop_volume_vx', 'rs_objprop_volume_vy': 'RS_objprop_volume_vy', 'rs_objprop_volume_vz': 'RS_objprop_volume_vz', 'rs_objprop_volume_vs': 'RS_objprop_volume_vs', 'rs_objpro_last': 'RS_objpro_last'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
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
        self.parm_rs_objprop_switcher1 = Parameter(parm=self.node.parm('RS_objprop_switcher1'))
        self.parm_rs_objpro_first = Parameter(parm=self.node.parm('RS_objpro_first'))
        self.parm_rs_campropshapes_switcher1 = Parameter(parm=self.node.parm('RS_campropshapes_switcher1'))
        self.parm_rs_objprop_id = Parameter(parm=self.node.parm('RS_objprop_ID'))
        self.parm_rs_objprop_cryptoid = Parameter(parm=self.node.parm('RS_objprop_CryptoID'))
        self.parm_rs_objprop_cryptomatid_allmat = Parameter(parm=self.node.parm('RS_objprop_CryptoMatID_AllMat'))
        self.parm_rs_objprop_ngons_enable = Parameter(parm=self.node.parm('RS_objprop_ngons_enable'))
        self.parm_rs_objprop_ngons_avoiddegen = Parameter(parm=self.node.parm('RS_objprop_ngons_avoidDegen'))
        self.parm_rs_objprop_normals_normalize = Parameter(parm=self.node.parm('RS_objprop_normals_normalize'))
        self.parm_rs_objprop_renderashair = Parameter(parm=self.node.parm('RS_objprop_renderAsHair'))
        self.parm_rs_objprop_defaulthairwidth = Parameter(parm=self.node.parm('RS_objprop_defaultHairWidth'))
        self.parm_rs_objprop_hairhalfthickness = Parameter(parm=self.node.parm('RS_objprop_hairHalfThickness'))
        self.parm_rs_objprop_mb_trans = Parameter(parm=self.node.parm('RS_objprop_mb_trans'))
        self.parm_rs_objprop_mb_def = Parameter(parm=self.node.parm('RS_objprop_mb_def'))
        self.parm_rs_objprop_mb_points = Parameter(parm=self.node.parm('RS_objprop_mb_points'))
        self.parm_rs_objprop_mb_def_use_v = Parameter(parm=self.node.parm('RS_objprop_mb_def_use_v'))
        self.parm_rs_objprop_mb_v_attr = Parameter(parm=self.node.parm('RS_objprop_mb_v_attr'))
        self.parm_rs_objprop_mb_fd_scale = Parameter(parm=self.node.parm('RS_objprop_mb_fd_scale'))
        self.parm_rs_objprop_mb_offset = Parameter(parm=self.node.parm('RS_objprop_mb_offset'))
        self.parm_rs_objprop_rendersopsubnets = Parameter(parm=self.node.parm('RS_objprop_renderSOPsubnets'))
        self.parm_rs_objprop_tess_enable = Parameter(parm=self.node.parm('RS_objprop_tess_enable'))
        self.parm_rs_objprop_tess_u = Parameter(parm=self.node.parm('RS_objprop_tess_u'))
        self.parm_rs_objprop_tess_v = Parameter(parm=self.node.parm('RS_objprop_tess_v'))
        self.parm_rs_objprop_tess_trim = Parameter(parm=self.node.parm('RS_objprop_tess_trim'))
        self.parm_rs_objprop_inst_ignorepivot = Parameter(parm=self.node.parm('RS_objprop_inst_ignorePivot'))
        self.parm_rs_objprop_inst_fileoverride = Parameter(parm=self.node.parm('RS_objprop_inst_fileOverride'))
        self.parm_rs_objprop_inst_packed = Parameter(parm=self.node.parm('RS_objprop_inst_packed'))
        self.parm_rs_objprop_inst_packedpriminstancing = Parameter(parm=self.node.parm('RS_objprop_inst_PackedPrimInstancing'))
        self.parm_rs_objprop_inst_subnetinstancing = Parameter(parm=self.node.parm('RS_objprop_inst_subnetInstancing'))
        self.parm_rs_objprop_attr_auto = Parameter(parm=self.node.parm('RS_objprop_attr_auto'))
        self.parm_rs_objprop_attr_vertex = Parameter(parm=self.node.parm('RS_objprop_attr_vertex'))
        self.parm_rs_objprop_attr_points = Parameter(parm=self.node.parm('RS_objprop_attr_points'))
        self.parm_rs_objprop_attr_primitives = Parameter(parm=self.node.parm('RS_objprop_attr_primitives'))
        self.parm_rs_objprop_attr_detail = Parameter(parm=self.node.parm('RS_objprop_attr_detail'))
        self.parm_rs_objprop_pckattr_promotion = Parameter(parm=self.node.parm('RS_objprop_pckattr_promotion'))
        self.parm_rs_objprop_pckattr_replace = Parameter(parm=self.node.parm('RS_objprop_pckattr_replace'))
        self.parm_rs_objprop_pckattr_mult = Parameter(parm=self.node.parm('RS_objprop_pckattr_mult'))
        self.parm_rs_objprop_pckattr_add = Parameter(parm=self.node.parm('RS_objprop_pckattr_add'))
        self.parm_rs_objprop_tracesets_enabled = Parameter(parm=self.node.parm('RS_objprop_tracesets_enabled'))
        self.parm_rs_objprop_tracesets_reflection = Parameter(parm=self.node.parm('RS_objprop_tracesets_reflection'))
        self.parm_rs_objprop_tracesets_refraction = Parameter(parm=self.node.parm('RS_objprop_tracesets_refraction'))
        self.parm_rs_objprop_tracesets_sss = Parameter(parm=self.node.parm('RS_objprop_tracesets_sss'))
        self.parm_rs_objprop_ipr_forcemeshupdate = Parameter(parm=self.node.parm('RS_objprop_ipr_forceMeshUpdate'))
        self.parm_rs_objpro_label5 = Parameter(parm=self.node.parm('RS_objpro_label5'))
        self.parm_rs_objprop_proxy_enable = Parameter(parm=self.node.parm('RS_objprop_proxy_enable'))
        self.parm_rs_objprop_proxy_prevpercent = Parameter(parm=self.node.parm('RS_objprop_proxy_prevPercent'))
        self.parm_rs_objprop_proxy_prevlines = Parameter(parm=self.node.parm('RS_objprop_proxy_prevLines'))
        self.parm_rs_objprop_proxy_prevanimated = Parameter(parm=self.node.parm('RS_objprop_proxy_prevAnimated'))
        self.parm_rs_objprop_proxy_override = Parameter(parm=self.node.parm('RS_objprop_proxy_override'))
        self.parm_rs_objprop_proxy_overridelist = Parameter(parm=self.node.parm('RS_objprop_proxy_overrideList'))
        self.parm_rs_objprop_proxy_elements_mesh = Parameter(parm=self.node.parm('RS_objprop_proxy_elements_mesh'))
        self.parm_rs_objprop_proxy_elements_volume = Parameter(parm=self.node.parm('RS_objprop_proxy_elements_volume'))
        self.parm_rs_objprop_proxy_elements_light = Parameter(parm=self.node.parm('RS_objprop_proxy_elements_light'))
        self.parm_rs_objprop_proxy_elements_proxy = Parameter(parm=self.node.parm('RS_objprop_proxy_elements_proxy'))
        self.parm_rs_objprop_proxy_ovrid = Parameter(parm=self.node.parm('RS_objprop_proxy_ovrID'))
        self.parm_rs_objprop_proxy_ovrvis = Parameter(parm=self.node.parm('RS_objprop_proxy_ovrVis'))
        self.parm_rs_objprop_proxy_ovrtess = Parameter(parm=self.node.parm('RS_objprop_proxy_ovrTess'))
        self.parm_rs_objprop_proxy_ovrtraces = Parameter(parm=self.node.parm('RS_objprop_proxy_ovrTraceS'))
        self.parm_rs_objprop_proxy_ovruserdata = Parameter(parm=self.node.parm('RS_objprop_proxy_ovrUserData'))
        self.parm_rs_objpro_label1o = Parameter(parm=self.node.parm('RS_objpro_label1o'))
        self.parm_meshflag_primaryrayvisible = Parameter(parm=self.node.parm('MESHFLAG_PRIMARYRAYVISIBLE'))
        self.parm_meshflag_secondaryrayvisible = Parameter(parm=self.node.parm('MESHFLAG_SECONDARYRAYVISIBLE'))
        self.parm_meshflag_shadowcaster = Parameter(parm=self.node.parm('MESHFLAG_SHADOWCASTER'))
        self.parm_meshflag_shadowreceiver = Parameter(parm=self.node.parm('MESHFLAG_SHADOWRECEIVER'))
        self.parm_meshflag_noselfshadow = Parameter(parm=self.node.parm('MESHFLAG_NOSELFSHADOW'))
        self.parm_meshflag_aocaster = Parameter(parm=self.node.parm('MESHFLAG_AOCASTER'))
        self.parm_meshflag_reflectionvisible = Parameter(parm=self.node.parm('MESHFLAG_REFLECTIONVISIBLE'))
        self.parm_meshflag_refractionvisible = Parameter(parm=self.node.parm('MESHFLAG_REFRACTIONVISIBLE'))
        self.parm_meshflag_reflectioncaster = Parameter(parm=self.node.parm('MESHFLAG_REFLECTIONCASTER'))
        self.parm_meshflag_refractioncaster = Parameter(parm=self.node.parm('MESHFLAG_REFRACTIONCASTER'))
        self.parm_meshflag_fgvisible = Parameter(parm=self.node.parm('MESHFLAG_FGVISIBLE'))
        self.parm_meshflag_givisible = Parameter(parm=self.node.parm('MESHFLAG_GIVISIBLE'))
        self.parm_meshflag_causticvisible = Parameter(parm=self.node.parm('MESHFLAG_CAUSTICVISIBLE'))
        self.parm_meshflag_fgcaster = Parameter(parm=self.node.parm('MESHFLAG_FGCASTER'))
        self.parm_meshflag_forcebruteforcegi = Parameter(parm=self.node.parm('MESHFLAG_FORCEBRUTEFORCEGI'))
        self.parm_meshflag_gicaster = Parameter(parm=self.node.parm('MESHFLAG_GICASTER'))
        self.parm_meshflag_causticcaster = Parameter(parm=self.node.parm('MESHFLAG_CAUSTICCASTER'))
        self.parm_meshflag_causticsreceiver = Parameter(parm=self.node.parm('MESHFLAG_CAUSTICSRECEIVER'))
        self.parm_rs_objpro_label2 = Parameter(parm=self.node.parm('RS_objpro_label2'))
        self.parm_rs_objprop_rstess_enable = Parameter(parm=self.node.parm('RS_objprop_rstess_enable'))
        self.parm_rs_objprop_rstess_ssadaptive = Parameter(parm=self.node.parm('RS_objprop_rstess_ssadaptive'))
        self.parm_rs_objprop_rstess_smoothsub = Parameter(parm=self.node.parm('RS_objprop_rstess_smoothsub'))
        self.parm_rs_objprop_rstess_triquads = Parameter(parm=self.node.parm('RS_objprop_rstess_triQuads'))
        self.parm_rs_objprop_rstess_melenght = Parameter(parm=self.node.parm('RS_objprop_rstess_melenght'))
        self.parm_rs_objprop_rstess_maxsubd = Parameter(parm=self.node.parm('RS_objprop_rstess_maxsubd'))
        self.parm_rs_objprop_rstess_ooftf = Parameter(parm=self.node.parm('RS_objprop_rstess_ooftf'))
        self.parm_rs_objprop_rstess_looft = Parameter(parm=self.node.parm('RS_objprop_rstess_looft'))
        self.parm_rs_objprop_rstess_looftsubd = Parameter(parm=self.node.parm('RS_objprop_rstess_looftSubd'))
        self.parm_rs_objprop_rstess_smooth = Parameter(parm=self.node.parm('RS_objprop_rstess_smooth'))
        self.parm_rs_objprop_rstess_smoothbound = Parameter(parm=self.node.parm('RS_objprop_rstess_smoothBound'))
        self.parm_rs_objpro_label3 = Parameter(parm=self.node.parm('RS_objpro_label3'))
        self.parm_rs_objprop_displace_enable = Parameter(parm=self.node.parm('RS_objprop_displace_enable'))
        self.parm_rs_objprop_displace_max = Parameter(parm=self.node.parm('RS_objprop_displace_max'))
        self.parm_rs_objprop_displace_scale = Parameter(parm=self.node.parm('RS_objprop_displace_scale'))
        self.parm_rs_objprop_displace_autob = Parameter(parm=self.node.parm('RS_objprop_displace_autob'))
        self.parm_rs_objpro_label4 = Parameter(parm=self.node.parm('RS_objpro_label4'))
        self.parm_rs_objprop_matte_enable = Parameter(parm=self.node.parm('RS_objprop_matte_enable'))
        self.parm_rs_objprop_matte_showbackg = Parameter(parm=self.node.parm('RS_objprop_matte_showbackg'))
        self.parm_rs_objprop_matte_applysec = Parameter(parm=self.node.parm('RS_objprop_matte_applysec'))
        self.parm_rs_objprop_matte_abyml = Parameter(parm=self.node.parm('RS_objprop_matte_abyml'))
        self.parm_rs_objprop_matte_includepm = Parameter(parm=self.node.parm('RS_objprop_matte_includePM'))
        self.parm_rs_objprop_matte_alpha = Parameter(parm=self.node.parm('RS_objprop_matte_alpha'))
        self.parm_rs_objprop_matte_reflscale = Parameter(parm=self.node.parm('RS_objprop_matte_reflscale'))
        self.parm_rs_objprop_matte_refrscale = Parameter(parm=self.node.parm('RS_objprop_matte_refrscale'))
        self.parm_rs_objprop_matte_diffscale = Parameter(parm=self.node.parm('RS_objprop_matte_diffscale'))
        self.parm_rs_objprop_matte_shadowenable = Parameter(parm=self.node.parm('RS_objprop_matte_shadowenable'))
        self.parm_rs_objprop_matte_shadowsfromm = Parameter(parm=self.node.parm('RS_objprop_matte_shadowsFromM'))
        self.parm_rs_objprop_matte_shadowalpha = Parameter(parm=self.node.parm('RS_objprop_matte_shadowalpha'))
        self.parm_rs_objprop_matte_shadowcolorr = Parameter(parm=self.node.parm('RS_objprop_matte_shadowcolorr'))
        self.parm_rs_objprop_matte_shadowcolorg = Parameter(parm=self.node.parm('RS_objprop_matte_shadowcolorg'))
        self.parm_rs_objprop_matte_shadowcolorb = Parameter(parm=self.node.parm('RS_objprop_matte_shadowcolorb'))
        self.parm_rs_objprop_matte_shadowtrans = Parameter(parm=self.node.parm('RS_objprop_matte_shadowtrans'))
        self.parm_rs_objpro_label6 = Parameter(parm=self.node.parm('RS_objpro_label6'))
        self.parm_rs_objprop_strands_enable = Parameter(parm=self.node.parm('RS_objprop_strands_enable'))
        self.parm_rs_objprop_strands_maxsubd = Parameter(parm=self.node.parm('RS_objprop_strands_maxSubd'))
        self.parm_rs_objprop_strands_scale = Parameter(parm=self.node.parm('RS_objprop_strands_scale'))
        self.parm_rs_objprop_strands_scalemult = Parameter(parm=self.node.parm('RS_objprop_strands_scaleMult'))
        self.parm_rs_objprop_strands_ignorepscale = Parameter(parm=self.node.parm('RS_objprop_strands_ignorePScale'))
        self.parm_rs_objprop_strands_usecamera = Parameter(parm=self.node.parm('RS_objprop_strands_useCamera'))
        self.parm_rs_objpro_label10 = Parameter(parm=self.node.parm('RS_objpro_label10'))
        self.parm_rs_objprop_particles_enable = Parameter(parm=self.node.parm('RS_objprop_particles_enable'))
        self.parm_rs_objprop_particles_ignorescale = Parameter(parm=self.node.parm('RS_objprop_particles_ignoreScale'))
        self.parm_rs_objprop_particles_scale = Parameter(parm=self.node.parm('RS_objprop_particles_scale'))
        self.parm_rs_objprop_particles_scalemult = Parameter(parm=self.node.parm('RS_objprop_particles_scaleMult'))
        self.parm_rs_objpro_label7 = Parameter(parm=self.node.parm('RS_objpro_label7'))
        self.parm_rs_objprop_volume_enable = Parameter(parm=self.node.parm('RS_objprop_volume_enable'))
        self.parm_rs_objprop_volume_filtern = Parameter(parm=self.node.parm('RS_objprop_volume_filterN'))
        self.parm_rs_objprop_volume_filterdeg = Parameter(parm=self.node.parm('RS_objprop_volume_filterDeg'))
        self.parm_rs_objprop_volume_filterdegthr = Parameter(parm=self.node.parm('RS_objprop_volume_filterDegThr'))
        self.parm_rs_objprop_volume_cleanbackg = Parameter(parm=self.node.parm('RS_objprop_volume_cleanBackg'))
        self.parm_rs_objprop_volume_v = Parameter(parm=self.node.parm('RS_objprop_volume_v'))
        self.parm_rs_objprop_volume_vx = Parameter(parm=self.node.parm('RS_objprop_volume_vx'))
        self.parm_rs_objprop_volume_vy = Parameter(parm=self.node.parm('RS_objprop_volume_vy'))
        self.parm_rs_objprop_volume_vz = Parameter(parm=self.node.parm('RS_objprop_volume_vz'))
        self.parm_rs_objprop_volume_vs = Parameter(parm=self.node.parm('RS_objprop_volume_vs'))
        self.parm_rs_objpro_last = Parameter(parm=self.node.parm('RS_objpro_last'))

        
        # parm menu vars:
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))
        self.parm_pre_xform = PreXformMenu(parm=self.node.parm('pre_xform'))
        self.parm_lookup = LookupMenu(parm=self.node.parm('lookup'))
        self.parm_uparmtype = UparmtypeMenu(parm=self.node.parm('uparmtype'))
        self.parm_shop_materialopts = ShopMaterialoptsMenu(parm=self.node.parm('shop_materialopts'))
        self.parm_pickscript = PickscriptMenu(parm=self.node.parm('pickscript'))
        self.parm_vport_onionskin = VportOnionskinMenu(parm=self.node.parm('vport_onionskin'))
        self.parm_viewportlod = ViewportlodMenu(parm=self.node.parm('viewportlod'))
        self.parm_vm_rendervisibility = VmRendervisibilityMenu(parm=self.node.parm('vm_rendervisibility'))
        self.parm_vm_subdstyle = VmSubdstyleMenu(parm=self.node.parm('vm_subdstyle'))
        self.parm_vm_osd_vtxinterp = VmOsdVtxinterpMenu(parm=self.node.parm('vm_osd_vtxinterp'))
        self.parm_vm_osd_fvarinterp = VmOsdFvarinterpMenu(parm=self.node.parm('vm_osd_fvarinterp'))
        self.parm_vm_volumefilter = VmVolumefilterMenu(parm=self.node.parm('vm_volumefilter'))
        self.parm_geo_velocityblur = GeoVelocityblurMenu(parm=self.node.parm('geo_velocityblur'))
        self.parm_vm_raypredice = VmRayprediceMenu(parm=self.node.parm('vm_raypredice'))
        self.parm_vm_renderpoints = VmRenderpointsMenu(parm=self.node.parm('vm_renderpoints'))
        self.parm_vm_renderpointsas = VmRenderpointsasMenu(parm=self.node.parm('vm_renderpointsas'))
        self.parm_vm_coving = VmCovingMenu(parm=self.node.parm('vm_coving'))
        self.parm_vm_materialoverride = VmMaterialoverrideMenu(parm=self.node.parm('vm_materialoverride'))
        self.parm_rs_objprop_ngons_tessmode = RsObjpropNgonsTessmodeMenu(parm=self.node.parm('RS_objprop_ngons_tessMode'))
        self.parm_rs_objprop_mb_deformsteps = RsObjpropMbDeformstepsMenu(parm=self.node.parm('RS_objprop_mb_deformSteps'))
        self.parm_rs_objprop_inst_mode = RsObjpropInstModeMenu(parm=self.node.parm('RS_objprop_inst_mode'))
        self.parm_rs_objprop_inst_mb = RsObjpropInstMbMenu(parm=self.node.parm('RS_objprop_inst_mb'))
        self.parm_rs_objprop_inst_lightshader = RsObjpropInstLightshaderMenu(parm=self.node.parm('RS_objprop_inst_lightShader'))
        self.parm_rs_objprop_inst_universalif = RsObjpropInstUniversalifMenu(parm=self.node.parm('RS_objprop_inst_universalIF'))
        self.parm_rs_objprop_proxy_file = RsObjpropProxyFileMenu(parm=self.node.parm('RS_objprop_proxy_file'))
        self.parm_rs_objprop_proxy_preview = RsObjpropProxyPreviewMenu(parm=self.node.parm('RS_objprop_proxy_preview'))
        self.parm_rs_objprop_proxy_materials = RsObjpropProxyMaterialsMenu(parm=self.node.parm('RS_objprop_proxy_materials'))
        self.parm_rs_objprop_rstess_rule = RsObjpropRstessRuleMenu(parm=self.node.parm('RS_objprop_rstess_rule'))
        self.parm_rs_objprop_strands_type = RsObjpropStrandsTypeMenu(parm=self.node.parm('RS_objprop_strands_type'))
        self.parm_rs_objprop_volume_type = RsObjpropVolumeTypeMenu(parm=self.node.parm('RS_objprop_volume_type'))


        # input vars:
        self.input_parent = 'parent'


# parm menu classes:
class XordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_scale_rot_trans = ("srt", 0)
        self.menu_scale_trans_rot = ("str", 1)
        self.menu_rot_scale_trans = ("rst", 2)
        self.menu_rot_trans_scale = ("rts", 3)
        self.menu_trans_scale_rot = ("tsr", 4)
        self.menu_trans_rot_scale = ("trs", 5)


class RordMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rx_ry_rz = ("xyz", 0)
        self.menu_rx_rz_ry = ("xzy", 1)
        self.menu_ry_rx_rz = ("yxz", 2)
        self.menu_ry_rz_rx = ("yzx", 3)
        self.menu_rz_rx_ry = ("zxy", 4)
        self.menu_rz_ry_rx = ("zyx", 5)


class PreXformMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_clean_transform = ("clean", 0)
        self.menu_clean_translates = ("cleantrans", 1)
        self.menu_clean_rotates = ("cleanrot", 2)
        self.menu_clean_scales = ("cleanscales", 3)
        self.menu_extract_pre_transform = ("extract", 4)
        self.menu_reset_pre_transform = ("reset", 5)


class LookupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_don_t_use_up_vector = ("off", 0)
        self.menu_use_up_vector = ("on", 1)
        self.menu_use_quaternions = ("quat", 2)
        self.menu_use_global_position = ("pos", 3)
        self.menu_use_up_object = ("obj", 4)


class UparmtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uniform = ("uniform", 0)
        self.menu_arc_length = ("arc", 1)


class ShopMaterialoptsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_create_all_local_material_parameters = ("override", 0)
        self.menu_select_and_create_local_material_parameters = ("select", 1)
        self.menu_remove_all_local_material_parameters = ("remove", 2)
        self.menu_remove_unchanged_local_material_parameters = ("rmdefault", 3)
        self.menu_synchronize_with_global_material_parameters = ("sync", 4)
        self.menu_revert_to_global_material_parameter_values = ("revert", 5)


class PickscriptMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_render_whit___name__os__f4_exr = ("$HIP/render_white_desert_closeup/$HIPNAME.$OS.$F4.exr", 0)
        self.menu__hip_tunder_rend___name__os__f4_exr = ("$HIP/tunder_render_closeup/$HIPNAME.$OS.$F4.exr", 1)
        self.menu__hip_render_gras___name__os__f4_exr = ("$HIP/render_grassy_hills_closeup/$HIPNAME.$OS.$F4.exr", 2)
        self.menu__hip_render_gras___name__os__f4_exr = ("$HIP/render_grassy_hills/$HIPNAME.$OS.$F4.exr", 3)
        self.menu__hip_tunder_rend___name__os__f4_exr = ("$HIP/tunder_render/$HIPNAME.$OS.$F4.exr", 4)
        self.menu_e__art_old_3d_as___field_wind_2_abc = ("E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind_2.abc", 5)
        self.menu_e__art_old_3d_as___t_field_wind_abc = ("E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind.abc", 6)
        self.menu_e__renders_houdi___name__os__f4_exr = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/$HIPNAME.$OS.$F4.exr", 7)
        self.menu_e__renders_houdi___r_magic_prev__f3 = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/magic_prev.$F3", 8)
        self.menu_e__art_projects____y_first_hdrlight = ("E:/ART/PROJECTS/00_shared/hdri/my_first_hdrlight", 9)


class VportOnionskinMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_off = ("off", 0)
        self.menu_transform_only = ("xform", 1)
        self.menu_full_deformation = ("on", 2)


class ViewportlodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_full_geometry = ("full", 0)
        self.menu_point_cloud = ("points", 1)
        self.menu_bounding_box = ("box", 2)
        self.menu_centroid = ("centroid", 3)
        self.menu_hidden = ("hidden", 4)
        self.menu_subdivision_surface___curves = ("subd", 5)


class VmRendervisibilityMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_visible_to_all = ("*", 0)
        self.menu_visible_only_to_primary_rays = ("primary", 1)
        self.menu_visible_only_to_primary_and_shadow_rays = ("primary|shadow", 2)
        self.menu_invisible_to_primary_rays__phantom_ = ("-primary", 3)
        self.menu_invisible_to_diffuse_rays = ("-diffuse", 4)
        self.menu_invisible_to_secondary_rays = ("-diffuse&-reflect&-refract", 5)
        self.menu_invisible__unrenderable_ = ("", 6)


class VmSubdstyleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mantra_catmull_clark = ("mantra_catclark", 0)
        self.menu_opensubdiv_catmull_clark = ("osd_catclark", 1)


class VmOsdVtxinterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_vertex_interpolation = ("0", 0)
        self.menu_edges_only = ("1", 1)
        self.menu_edges_and_corners = ("2", 2)


class VmOsdFvarinterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_smooth_everywhere = ("0", 0)
        self.menu_sharpen_corners_only = ("1", 1)
        self.menu_sharpen_edges_and_corners = ("2", 2)
        self.menu_sharpen_edges_and_propagated_corners = ("3", 3)
        self.menu_sharpen_all_boundaries = ("4", 4)
        self.menu_bilinear_interpolation = ("5", 5)


class VmVolumefilterMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box_filter = ("box", 0)
        self.menu_gaussian = ("gaussian", 1)
        self.menu_bartlett__triangle_ = ("bartlett", 2)
        self.menu_catmull_rom = ("catrom", 3)
        self.menu_hanning = ("hanning", 4)
        self.menu_blackman = ("blackman", 5)
        self.menu_sinc__sharpening_ = ("sinc", 6)


class GeoVelocityblurMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_velocity_blur = ("off", 0)
        self.menu_velocity_blur = ("on", 1)
        self.menu_acceleration_blur = ("accelblur", 2)


class VmRayprediceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_disable_predicing = ("0", 0)
        self.menu_full_predicing = ("1", 1)
        self.menu_precompute_bounds = ("2", 2)


class VmRenderpointsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_point_rendering = ("0", 0)
        self.menu_render_only_points = ("1", 1)
        self.menu_render_unconnected_points = ("2", 2)


class VmRenderpointsasMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_spheres = ("0", 0)
        self.menu_circles = ("1", 1)


class VmCovingMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_disable_coving = ("0", 0)
        self.menu_coving_for_displacement_sub_d = ("1", 1)
        self.menu_coving_for_all_primitives = ("2", 2)


class VmMaterialoverrideMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_disabled = ("none", 0)
        self.menu_evaluate_for_each_primitve_point = ("full", 1)
        self.menu_evaluate_once = ("compact", 2)


class RsObjpropNgonsTessmodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_to_quads = ("0", 0)
        self.menu_to_triangles = ("1", 1)


class RsObjpropMbDeformstepsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = ("-1", 0)
        self.menu_steps_2 = ("2", 1)
        self.menu_steps_3 = ("3", 2)
        self.menu_steps_5 = ("5", 3)
        self.menu_steps_9 = ("9", 4)
        self.menu_steps_17 = ("17", 5)


class RsObjpropInstModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_redshift_instances = ("insInstances", 0)
        self.menu_redshift_point_clouds = ("insPointClouds", 1)


class RsObjpropInstMbMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_compute_sub_frame_geometry__deformation_ = ("insMBVectors", 0)
        self.menu_use_point_velocity_attribute = ("insMBFull", 1)


class RsObjpropInstLightshaderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_attributes_support_using_individual_shaders = ("insLightsNotShared", 0)
        self.menu_using_a_common_shared_shader = ("insLightsShared", 1)


class RsObjpropInstUniversalifMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_instance_redshift_proxy_objects = ("0", 0)
        self.menu_instance_houdini_compatible_objects = ("1", 1)


class RsObjpropProxyFileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_render_whit___name__os__f4_exr = ("$HIP/render_white_desert_closeup/$HIPNAME.$OS.$F4.exr", 0)
        self.menu__hip_tunder_rend___name__os__f4_exr = ("$HIP/tunder_render_closeup/$HIPNAME.$OS.$F4.exr", 1)
        self.menu__hip_render_gras___name__os__f4_exr = ("$HIP/render_grassy_hills_closeup/$HIPNAME.$OS.$F4.exr", 2)
        self.menu__hip_render_gras___name__os__f4_exr = ("$HIP/render_grassy_hills/$HIPNAME.$OS.$F4.exr", 3)
        self.menu__hip_tunder_rend___name__os__f4_exr = ("$HIP/tunder_render/$HIPNAME.$OS.$F4.exr", 4)
        self.menu_e__art_old_3d_as___field_wind_2_abc = ("E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind_2.abc", 5)
        self.menu_e__art_old_3d_as___t_field_wind_abc = ("E:/ART_OLD/3D_ASSETS/00_my_trees/palm_with_wind_abc/Palm_Coconut_Field_wind.abc", 6)
        self.menu_e__renders_houdi___name__os__f4_exr = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/$HIPNAME.$OS.$F4.exr", 7)
        self.menu_e__renders_houdi___r_magic_prev__f3 = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/magic_prev.$F3", 8)
        self.menu_e__art_projects____y_first_hdrlight = ("E:/ART/PROJECTS/00_shared/hdri/my_first_hdrlight", 9)


class RsObjpropProxyPreviewMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("proxyPrevNone", 0)
        self.menu_bounding_box = ("proxyPrevBB", 1)
        self.menu_mesh = ("proxyPrevSolid", 2)
        self.menu_points = ("proxyPrevPoints", 3)


class RsObjpropProxyMaterialsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_from_proxy = ("proxyMatProxy", 0)
        self.menu_from_obj_node = ("proxyMatObject", 1)
        self.menu_full_override = ("proxyMatOverride", 2)
        self.menu_list_override = ("proxyMatOvrList", 3)
        self.menu_from_scene_materials = ("proxyMatOvrScene", 4)


class RsObjpropRstessRuleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_catmull_clark___loop = ("ccLoop", 0)
        self.menu_catmull_clark_only = ("ccOnly", 1)


class RsObjpropStrandsTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_box = ("RS_STRAND_SHAPE_BOX", 0)
        self.menu_cylinder = ("RS_STRAND_SHAPE_CYLINDER", 1)
        self.menu_capsule = ("RS_STRAND_SHAPE_CAPSULE", 2)
        self.menu_cone = ("RS_STRAND_SHAPE_CONE", 3)
        self.menu_strip = ("RS_STRAND_SHAPE_STRIP", 4)


class RsObjpropVolumeTypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_openvdb_file = ("vOpenVDB", 0)
        self.menu_volume_vdb_houdini_primitive = ("vHoudiniVolume", 1)



