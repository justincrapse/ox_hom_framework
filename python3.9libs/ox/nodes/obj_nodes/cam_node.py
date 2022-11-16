from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class CamNode(OXNode):
    node_type = 'cam'
    parm_lookup_dict = {'stdswitcher1': 'stdswitcher1', 'xord': 'xOrd', 'rord': 'rOrd', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'sx': 'sx', 'sy': 'sy', 'sz': 'sz', 'px': 'px', 'py': 'py', 'pz': 'pz', 'prx': 'prx', 'pry': 'pry', 'prz': 'prz', 'scale': 'scale', 'pre_xform': 'pre_xform', 'keeppos': 'keeppos', 'childcomp': 'childcomp', 'constraints_on': 'constraints_on', 'constraints_path': 'constraints_path', 'lookatpath': 'lookatpath', 'lookupobjpath': 'lookupobjpath', 'lookup': 'lookup', 'pathobjpath': 'pathobjpath', 'roll': 'roll', 'pos': 'pos', 'uparmtype': 'uparmtype', 'pathorient': 'pathorient', 'upx': 'upx', 'upy': 'upy', 'upz': 'upz', 'bank': 'bank', 'tdisplay': 'tdisplay', 'display': 'display', 'use_dcolor': 'use_dcolor', 'dcolorr': 'dcolorr', 'dcolorg': 'dcolorg', 'dcolorb': 'dcolorb', 'picking': 'picking', 'pickscript': 'pickscript', 'caching': 'caching', 'stdswitcher31': 'stdswitcher31', 'iconscale': 'iconscale', 'resx': 'resx', 'resy': 'resy', 'resmenu': 'resMenu', 'aspect': 'aspect', 'projection': 'projection', 'vm_lensshader': 'vm_lensshader', 'focal': 'focal', 'focalunits': 'focalunits', 'aperture': 'aperture', 'orthowidth': 'orthowidth', 'near': 'near', 'far': 'far', 'vm_bgenable': 'vm_bgenable', 'vm_background': 'vm_background', 'winx': 'winx', 'winy': 'winy', 'winsizex': 'winsizex', 'winsizey': 'winsizey', 'winmask': 'winmask', 'cropl': 'cropl', 'cropr': 'cropr', 'cropb': 'cropb', 'cropt': 'cropt', 'cropmask': 'cropmask', 'fgimage': 'fgimage', 'shutter': 'shutter', 'focus': 'focus', 'fstop': 'fstop', 'vm_bokeh': 'vm_bokeh', 'vm_bokehfile': 'vm_bokehfile', 'vm_bokehrotation': 'vm_bokehrotation', 'rs_camprop_switcher1': 'RS_camprop_switcher1', 'rs_campro_first': 'RS_campro_first', 'rs_campro_label0': 'RS_campro_label0', 'rs_campro_projection': 'RS_campro_projection', 'rs_campro_label1': 'RS_campro_label1', 'rs_campro_fisheyehscale': 'RS_campro_fisheyeHScale', 'rs_campro_fisheyevscale': 'RS_campro_fisheyeVScale', 'rs_campro_fisheyefov': 'RS_campro_fisheyeFOV', 'rs_campro_label2': 'RS_campro_label2', 'rs_campro_cylhfov': 'RS_campro_cylHFOV', 'rs_campro_cylvfov': 'RS_campro_cylVFOV', 'rs_campro_cylortho': 'RS_campro_cylOrtho', 'rs_campro_cylorthoheight': 'RS_campro_cylOrthoHeight', 'rs_campro_label3': 'RS_campro_label3', 'rs_campro_stereomode': 'RS_campro_stereoMode', 'rs_campro_stereoseparation': 'RS_campro_stereoSeparation', 'rs_campro_stereofocus': 'RS_campro_stereoFocus', 'rs_campro_stereofocuscam': 'RS_campro_stereoFocusCam', 'rs_campro_stereofocusdist': 'RS_campro_stereoFocusDist', 'rs_campro_stereohfov': 'RS_campro_stereoHFov', 'rs_campro_stereovfov': 'RS_campro_stereoVFov', 'rs_campro_mbdisable': 'RS_campro_mbDisable', 'rs_campro_label4': 'RS_campro_label4', 'rs_campro_dofenable': 'RS_campro_dofEnable', 'rs_campro_dofusehoudinicamera': 'RS_campro_dofUseHoudiniCamera', 'rs_campro_doflegacytechnique': 'RS_campro_dofLegacyTechnique', 'rs_campro_dofdistance': 'RS_campro_dofDistance', 'rs_campro_dofcoc': 'RS_campro_dofCoC', 'rs_campro_dofpower': 'RS_campro_dofPower', 'rs_campro_dofapect': 'RS_campro_dofApect', 'rs_campro_dofbladescount': 'RS_campro_dofBladesCount', 'rs_campro_dofbladesangle': 'RS_campro_dofBladesAngle', 'rs_campro_dofbokeh': 'RS_campro_dofBokeh', 'rs_campro_dofbokehnorm': 'RS_campro_dofBokehNorm', 'rs_campro_dofbokehimage': 'RS_campro_dofBokehImage', 'rs_campro_label5': 'RS_campro_label5', 'rs_campro_pycamenable': 'RS_campro_PyCamEnable', 'rs_campro_label5b': 'RS_campro_label5b', 'rs_campro_pycamiso': 'RS_campro_PyCamISO', 'rs_campro_pycamshutter': 'RS_campro_PyCamShutter', 'rs_campro_pycamfstop': 'RS_campro_PyCamfstop', 'rs_campro_pycamwpointr': 'RS_campro_PyCamWPointr', 'rs_campro_pycamwpointg': 'RS_campro_PyCamWPointg', 'rs_campro_pycamwpointb': 'RS_campro_PyCamWPointb', 'rs_campro_pycamvignetting': 'RS_campro_PyCamVignetting', 'rs_campro_label5c': 'RS_campro_label5c', 'rs_campro_pycamoverexp': 'RS_campro_PyCamOverExp', 'rs_campro_pycamallowdesat': 'RS_campro_PyCamAllowDesat', 'rs_campro_pycamcrusht': 'RS_campro_PyCamCrushT', 'rs_campro_pycamcrusha': 'RS_campro_PyCamCrushA', 'rs_campro_pycamsaturation': 'RS_campro_PyCamSaturation', 'rs_campro_label7': 'RS_campro_label7', 'rs_campro_enablepfx': 'RS_campro_enablePFX', 'rs_campro_applypfx': 'RS_campro_applyPFX', 'rs_campro_ocioswitcher': 'RS_campro_ocioSwitcher', 'rs_campro_ociodisplay': 'RS_campro_ocioDisplay', 'rs_campro_ocioview': 'RS_campro_ocioView', 'rs_campro_lutswitcher': 'RS_campro_lutSwitcher', 'rs_campro_lutenable': 'RS_campro_lutEnable', 'rs_campro_lutfile': 'RS_campro_lutFile', 'rs_campro_lutbeforecm': 'RS_campro_lutBeforeCM', 'rs_campro_lutislog': 'RS_campro_lutIsLog', 'rs_campro_lutstrength': 'RS_campro_lutStrength', 'rs_campro_colorswitcher': 'RS_campro_colorSwitcher', 'rs_campro_colorenable': 'RS_campro_colorEnable', 'rs_campro_colorexposure': 'RS_campro_colorExposure', 'rs_campro_colorcontrast': 'RS_campro_colorContrast', 'rs_campro_colorcurvesswitcher': 'RS_campro_colorCurvesSwitcher', 'rs_campro_colorcurvesr': 'RS_campro_colorCurvesR', 'rs_campro_colorcurvesg': 'RS_campro_colorCurvesG', 'rs_campro_colorcurvesb': 'RS_campro_colorCurvesB', 'rs_campro_colorcurvesrgb': 'RS_campro_colorCurvesRGB', 'rs_campro_bloomswitcher': 'RS_campro_bloomSwitcher', 'rs_campro_bloomenable': 'RS_campro_bloomEnable', 'rs_campro_bloomthreshold': 'RS_campro_bloomThreshold', 'rs_campro_bloomsoftness': 'RS_campro_bloomSoftness', 'rs_campro_bloomintensity': 'RS_campro_bloomIntensity', 'rs_campro_bloomtintswicther': 'RS_campro_bloomTintSwicther', 'rs_campro_bloomtint1r': 'RS_campro_bloomTint1r', 'rs_campro_bloomtint1g': 'RS_campro_bloomTint1g', 'rs_campro_bloomtint1b': 'RS_campro_bloomTint1b', 'rs_campro_bloomtint2r': 'RS_campro_bloomTint2r', 'rs_campro_bloomtint2g': 'RS_campro_bloomTint2g', 'rs_campro_bloomtint2b': 'RS_campro_bloomTint2b', 'rs_campro_bloomtint3r': 'RS_campro_bloomTint3r', 'rs_campro_bloomtint3g': 'RS_campro_bloomTint3g', 'rs_campro_bloomtint3b': 'RS_campro_bloomTint3b', 'rs_campro_bloomtint4r': 'RS_campro_bloomTint4r', 'rs_campro_bloomtint4g': 'RS_campro_bloomTint4g', 'rs_campro_bloomtint4b': 'RS_campro_bloomTint4b', 'rs_campro_bloomtint5r': 'RS_campro_bloomTint5r', 'rs_campro_bloomtint5g': 'RS_campro_bloomTint5g', 'rs_campro_bloomtint5b': 'RS_campro_bloomTint5b', 'rs_campro_flareswitcher': 'RS_campro_flareSwitcher', 'rs_campro_flareenable': 'RS_campro_flareEnable', 'rs_campro_flarethreshold': 'RS_campro_flareThreshold', 'rs_campro_flaresoftness': 'RS_campro_flareSoftness', 'rs_campro_flarechromatic': 'RS_campro_flareChromatic', 'rs_campro_flaresize': 'RS_campro_flareSize', 'rs_campro_flarehalo': 'RS_campro_flareHalo', 'rs_campro_flareintensity': 'RS_campro_flareIntensity', 'rs_campro_flaretintswitcher': 'RS_campro_flareTintSwitcher', 'rs_campro_flaretint1r': 'RS_campro_flareTint1r', 'rs_campro_flaretint1g': 'RS_campro_flareTint1g', 'rs_campro_flaretint1b': 'RS_campro_flareTint1b', 'rs_campro_flaretint2r': 'RS_campro_flareTint2r', 'rs_campro_flaretint2g': 'RS_campro_flareTint2g', 'rs_campro_flaretint2b': 'RS_campro_flareTint2b', 'rs_campro_flaretint3r': 'RS_campro_flareTint3r', 'rs_campro_flaretint3g': 'RS_campro_flareTint3g', 'rs_campro_flaretint3b': 'RS_campro_flareTint3b', 'rs_campro_flaretint4r': 'RS_campro_flareTint4r', 'rs_campro_flaretint4g': 'RS_campro_flareTint4g', 'rs_campro_flaretint4b': 'RS_campro_flareTint4b', 'rs_campro_flaretint5r': 'RS_campro_flareTint5r', 'rs_campro_flaretint5g': 'RS_campro_flareTint5g', 'rs_campro_flaretint5b': 'RS_campro_flareTint5b', 'rs_campro_flaretint6r': 'RS_campro_flareTint6r', 'rs_campro_flaretint6g': 'RS_campro_flareTint6g', 'rs_campro_flaretint6b': 'RS_campro_flareTint6b', 'rs_campro_streakswitcher': 'RS_campro_streakSwitcher', 'rs_campro_streakenable': 'RS_campro_streakEnable', 'rs_campro_streakthreshold': 'RS_campro_streakThreshold', 'rs_campro_streaktail': 'RS_campro_streakTail', 'rs_campro_streaksoftness': 'RS_campro_streakSoftness', 'rs_campro_streaknumber': 'RS_campro_streakNumber', 'rs_campro_streakangle': 'RS_campro_streakAngle', 'rs_campro_streakintensity': 'RS_campro_streakIntensity', 'rs_campro_label6': 'RS_campro_label6', 'rs_campro_distortionenable': 'RS_campro_distortionEnable', 'rs_campro_distortionimage': 'RS_campro_distortionImage', 'rs_campro_last': 'RS_campro_last'}

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
        self.parm_tdisplay = Parameter(parm=self.node.parm('tdisplay'))
        self.parm_display = Parameter(parm=self.node.parm('display'))
        self.parm_use_dcolor = Parameter(parm=self.node.parm('use_dcolor'))
        self.parm_dcolorr = Parameter(parm=self.node.parm('dcolorr'))
        self.parm_dcolorg = Parameter(parm=self.node.parm('dcolorg'))
        self.parm_dcolorb = Parameter(parm=self.node.parm('dcolorb'))
        self.parm_picking = Parameter(parm=self.node.parm('picking'))
        self.parm_caching = Parameter(parm=self.node.parm('caching'))
        self.parm_stdswitcher31 = Parameter(parm=self.node.parm('stdswitcher31'))
        self.parm_iconscale = Parameter(parm=self.node.parm('iconscale'))
        self.parm_resx = Parameter(parm=self.node.parm('resx'))
        self.parm_resy = Parameter(parm=self.node.parm('resy'))
        self.parm_aspect = Parameter(parm=self.node.parm('aspect'))
        self.parm_vm_lensshader = Parameter(parm=self.node.parm('vm_lensshader'))
        self.parm_focal = Parameter(parm=self.node.parm('focal'))
        self.parm_aperture = Parameter(parm=self.node.parm('aperture'))
        self.parm_orthowidth = Parameter(parm=self.node.parm('orthowidth'))
        self.parm_near = Parameter(parm=self.node.parm('near'))
        self.parm_far = Parameter(parm=self.node.parm('far'))
        self.parm_vm_bgenable = Parameter(parm=self.node.parm('vm_bgenable'))
        self.parm_winx = Parameter(parm=self.node.parm('winx'))
        self.parm_winy = Parameter(parm=self.node.parm('winy'))
        self.parm_winsizex = Parameter(parm=self.node.parm('winsizex'))
        self.parm_winsizey = Parameter(parm=self.node.parm('winsizey'))
        self.parm_winmask = Parameter(parm=self.node.parm('winmask'))
        self.parm_cropl = Parameter(parm=self.node.parm('cropl'))
        self.parm_cropr = Parameter(parm=self.node.parm('cropr'))
        self.parm_cropb = Parameter(parm=self.node.parm('cropb'))
        self.parm_cropt = Parameter(parm=self.node.parm('cropt'))
        self.parm_cropmask = Parameter(parm=self.node.parm('cropmask'))
        self.parm_shutter = Parameter(parm=self.node.parm('shutter'))
        self.parm_focus = Parameter(parm=self.node.parm('focus'))
        self.parm_fstop = Parameter(parm=self.node.parm('fstop'))
        self.parm_vm_bokehrotation = Parameter(parm=self.node.parm('vm_bokehrotation'))
        self.parm_rs_camprop_switcher1 = Parameter(parm=self.node.parm('RS_camprop_switcher1'))
        self.parm_rs_campro_first = Parameter(parm=self.node.parm('RS_campro_first'))
        self.parm_rs_campro_label0 = Parameter(parm=self.node.parm('RS_campro_label0'))
        self.parm_rs_campro_label1 = Parameter(parm=self.node.parm('RS_campro_label1'))
        self.parm_rs_campro_fisheyehscale = Parameter(parm=self.node.parm('RS_campro_fisheyeHScale'))
        self.parm_rs_campro_fisheyevscale = Parameter(parm=self.node.parm('RS_campro_fisheyeVScale'))
        self.parm_rs_campro_fisheyefov = Parameter(parm=self.node.parm('RS_campro_fisheyeFOV'))
        self.parm_rs_campro_label2 = Parameter(parm=self.node.parm('RS_campro_label2'))
        self.parm_rs_campro_cylhfov = Parameter(parm=self.node.parm('RS_campro_cylHFOV'))
        self.parm_rs_campro_cylvfov = Parameter(parm=self.node.parm('RS_campro_cylVFOV'))
        self.parm_rs_campro_cylortho = Parameter(parm=self.node.parm('RS_campro_cylOrtho'))
        self.parm_rs_campro_cylorthoheight = Parameter(parm=self.node.parm('RS_campro_cylOrthoHeight'))
        self.parm_rs_campro_label3 = Parameter(parm=self.node.parm('RS_campro_label3'))
        self.parm_rs_campro_stereoseparation = Parameter(parm=self.node.parm('RS_campro_stereoSeparation'))
        self.parm_rs_campro_stereofocus = Parameter(parm=self.node.parm('RS_campro_stereoFocus'))
        self.parm_rs_campro_stereofocuscam = Parameter(parm=self.node.parm('RS_campro_stereoFocusCam'))
        self.parm_rs_campro_stereofocusdist = Parameter(parm=self.node.parm('RS_campro_stereoFocusDist'))
        self.parm_rs_campro_stereohfov = Parameter(parm=self.node.parm('RS_campro_stereoHFov'))
        self.parm_rs_campro_stereovfov = Parameter(parm=self.node.parm('RS_campro_stereoVFov'))
        self.parm_rs_campro_mbdisable = Parameter(parm=self.node.parm('RS_campro_mbDisable'))
        self.parm_rs_campro_label4 = Parameter(parm=self.node.parm('RS_campro_label4'))
        self.parm_rs_campro_dofenable = Parameter(parm=self.node.parm('RS_campro_dofEnable'))
        self.parm_rs_campro_dofusehoudinicamera = Parameter(parm=self.node.parm('RS_campro_dofUseHoudiniCamera'))
        self.parm_rs_campro_doflegacytechnique = Parameter(parm=self.node.parm('RS_campro_dofLegacyTechnique'))
        self.parm_rs_campro_dofdistance = Parameter(parm=self.node.parm('RS_campro_dofDistance'))
        self.parm_rs_campro_dofcoc = Parameter(parm=self.node.parm('RS_campro_dofCoC'))
        self.parm_rs_campro_dofpower = Parameter(parm=self.node.parm('RS_campro_dofPower'))
        self.parm_rs_campro_dofapect = Parameter(parm=self.node.parm('RS_campro_dofApect'))
        self.parm_rs_campro_dofbladescount = Parameter(parm=self.node.parm('RS_campro_dofBladesCount'))
        self.parm_rs_campro_dofbladesangle = Parameter(parm=self.node.parm('RS_campro_dofBladesAngle'))
        self.parm_rs_campro_dofbokeh = Parameter(parm=self.node.parm('RS_campro_dofBokeh'))
        self.parm_rs_campro_label5 = Parameter(parm=self.node.parm('RS_campro_label5'))
        self.parm_rs_campro_pycamenable = Parameter(parm=self.node.parm('RS_campro_PyCamEnable'))
        self.parm_rs_campro_label5b = Parameter(parm=self.node.parm('RS_campro_label5b'))
        self.parm_rs_campro_pycamiso = Parameter(parm=self.node.parm('RS_campro_PyCamISO'))
        self.parm_rs_campro_pycamshutter = Parameter(parm=self.node.parm('RS_campro_PyCamShutter'))
        self.parm_rs_campro_pycamfstop = Parameter(parm=self.node.parm('RS_campro_PyCamfstop'))
        self.parm_rs_campro_pycamwpointr = Parameter(parm=self.node.parm('RS_campro_PyCamWPointr'))
        self.parm_rs_campro_pycamwpointg = Parameter(parm=self.node.parm('RS_campro_PyCamWPointg'))
        self.parm_rs_campro_pycamwpointb = Parameter(parm=self.node.parm('RS_campro_PyCamWPointb'))
        self.parm_rs_campro_pycamvignetting = Parameter(parm=self.node.parm('RS_campro_PyCamVignetting'))
        self.parm_rs_campro_label5c = Parameter(parm=self.node.parm('RS_campro_label5c'))
        self.parm_rs_campro_pycamoverexp = Parameter(parm=self.node.parm('RS_campro_PyCamOverExp'))
        self.parm_rs_campro_pycamallowdesat = Parameter(parm=self.node.parm('RS_campro_PyCamAllowDesat'))
        self.parm_rs_campro_pycamcrusht = Parameter(parm=self.node.parm('RS_campro_PyCamCrushT'))
        self.parm_rs_campro_pycamcrusha = Parameter(parm=self.node.parm('RS_campro_PyCamCrushA'))
        self.parm_rs_campro_pycamsaturation = Parameter(parm=self.node.parm('RS_campro_PyCamSaturation'))
        self.parm_rs_campro_label7 = Parameter(parm=self.node.parm('RS_campro_label7'))
        self.parm_rs_campro_enablepfx = Parameter(parm=self.node.parm('RS_campro_enablePFX'))
        self.parm_rs_campro_applypfx = Parameter(parm=self.node.parm('RS_campro_applyPFX'))
        self.parm_rs_campro_ocioswitcher = Parameter(parm=self.node.parm('RS_campro_ocioSwitcher'))
        self.parm_rs_campro_lutswitcher = Parameter(parm=self.node.parm('RS_campro_lutSwitcher'))
        self.parm_rs_campro_lutenable = Parameter(parm=self.node.parm('RS_campro_lutEnable'))
        self.parm_rs_campro_lutbeforecm = Parameter(parm=self.node.parm('RS_campro_lutBeforeCM'))
        self.parm_rs_campro_lutislog = Parameter(parm=self.node.parm('RS_campro_lutIsLog'))
        self.parm_rs_campro_lutstrength = Parameter(parm=self.node.parm('RS_campro_lutStrength'))
        self.parm_rs_campro_colorswitcher = Parameter(parm=self.node.parm('RS_campro_colorSwitcher'))
        self.parm_rs_campro_colorenable = Parameter(parm=self.node.parm('RS_campro_colorEnable'))
        self.parm_rs_campro_colorexposure = Parameter(parm=self.node.parm('RS_campro_colorExposure'))
        self.parm_rs_campro_colorcontrast = Parameter(parm=self.node.parm('RS_campro_colorContrast'))
        self.parm_rs_campro_colorcurvesswitcher = Parameter(parm=self.node.parm('RS_campro_colorCurvesSwitcher'))
        self.parm_rs_campro_colorcurvesr = Parameter(parm=self.node.parm('RS_campro_colorCurvesR'))
        self.parm_rs_campro_colorcurvesg = Parameter(parm=self.node.parm('RS_campro_colorCurvesG'))
        self.parm_rs_campro_colorcurvesb = Parameter(parm=self.node.parm('RS_campro_colorCurvesB'))
        self.parm_rs_campro_colorcurvesrgb = Parameter(parm=self.node.parm('RS_campro_colorCurvesRGB'))
        self.parm_rs_campro_bloomswitcher = Parameter(parm=self.node.parm('RS_campro_bloomSwitcher'))
        self.parm_rs_campro_bloomenable = Parameter(parm=self.node.parm('RS_campro_bloomEnable'))
        self.parm_rs_campro_bloomthreshold = Parameter(parm=self.node.parm('RS_campro_bloomThreshold'))
        self.parm_rs_campro_bloomsoftness = Parameter(parm=self.node.parm('RS_campro_bloomSoftness'))
        self.parm_rs_campro_bloomintensity = Parameter(parm=self.node.parm('RS_campro_bloomIntensity'))
        self.parm_rs_campro_bloomtintswicther = Parameter(parm=self.node.parm('RS_campro_bloomTintSwicther'))
        self.parm_rs_campro_bloomtint1r = Parameter(parm=self.node.parm('RS_campro_bloomTint1r'))
        self.parm_rs_campro_bloomtint1g = Parameter(parm=self.node.parm('RS_campro_bloomTint1g'))
        self.parm_rs_campro_bloomtint1b = Parameter(parm=self.node.parm('RS_campro_bloomTint1b'))
        self.parm_rs_campro_bloomtint2r = Parameter(parm=self.node.parm('RS_campro_bloomTint2r'))
        self.parm_rs_campro_bloomtint2g = Parameter(parm=self.node.parm('RS_campro_bloomTint2g'))
        self.parm_rs_campro_bloomtint2b = Parameter(parm=self.node.parm('RS_campro_bloomTint2b'))
        self.parm_rs_campro_bloomtint3r = Parameter(parm=self.node.parm('RS_campro_bloomTint3r'))
        self.parm_rs_campro_bloomtint3g = Parameter(parm=self.node.parm('RS_campro_bloomTint3g'))
        self.parm_rs_campro_bloomtint3b = Parameter(parm=self.node.parm('RS_campro_bloomTint3b'))
        self.parm_rs_campro_bloomtint4r = Parameter(parm=self.node.parm('RS_campro_bloomTint4r'))
        self.parm_rs_campro_bloomtint4g = Parameter(parm=self.node.parm('RS_campro_bloomTint4g'))
        self.parm_rs_campro_bloomtint4b = Parameter(parm=self.node.parm('RS_campro_bloomTint4b'))
        self.parm_rs_campro_bloomtint5r = Parameter(parm=self.node.parm('RS_campro_bloomTint5r'))
        self.parm_rs_campro_bloomtint5g = Parameter(parm=self.node.parm('RS_campro_bloomTint5g'))
        self.parm_rs_campro_bloomtint5b = Parameter(parm=self.node.parm('RS_campro_bloomTint5b'))
        self.parm_rs_campro_flareswitcher = Parameter(parm=self.node.parm('RS_campro_flareSwitcher'))
        self.parm_rs_campro_flareenable = Parameter(parm=self.node.parm('RS_campro_flareEnable'))
        self.parm_rs_campro_flarethreshold = Parameter(parm=self.node.parm('RS_campro_flareThreshold'))
        self.parm_rs_campro_flaresoftness = Parameter(parm=self.node.parm('RS_campro_flareSoftness'))
        self.parm_rs_campro_flarechromatic = Parameter(parm=self.node.parm('RS_campro_flareChromatic'))
        self.parm_rs_campro_flaresize = Parameter(parm=self.node.parm('RS_campro_flareSize'))
        self.parm_rs_campro_flarehalo = Parameter(parm=self.node.parm('RS_campro_flareHalo'))
        self.parm_rs_campro_flareintensity = Parameter(parm=self.node.parm('RS_campro_flareIntensity'))
        self.parm_rs_campro_flaretintswitcher = Parameter(parm=self.node.parm('RS_campro_flareTintSwitcher'))
        self.parm_rs_campro_flaretint1r = Parameter(parm=self.node.parm('RS_campro_flareTint1r'))
        self.parm_rs_campro_flaretint1g = Parameter(parm=self.node.parm('RS_campro_flareTint1g'))
        self.parm_rs_campro_flaretint1b = Parameter(parm=self.node.parm('RS_campro_flareTint1b'))
        self.parm_rs_campro_flaretint2r = Parameter(parm=self.node.parm('RS_campro_flareTint2r'))
        self.parm_rs_campro_flaretint2g = Parameter(parm=self.node.parm('RS_campro_flareTint2g'))
        self.parm_rs_campro_flaretint2b = Parameter(parm=self.node.parm('RS_campro_flareTint2b'))
        self.parm_rs_campro_flaretint3r = Parameter(parm=self.node.parm('RS_campro_flareTint3r'))
        self.parm_rs_campro_flaretint3g = Parameter(parm=self.node.parm('RS_campro_flareTint3g'))
        self.parm_rs_campro_flaretint3b = Parameter(parm=self.node.parm('RS_campro_flareTint3b'))
        self.parm_rs_campro_flaretint4r = Parameter(parm=self.node.parm('RS_campro_flareTint4r'))
        self.parm_rs_campro_flaretint4g = Parameter(parm=self.node.parm('RS_campro_flareTint4g'))
        self.parm_rs_campro_flaretint4b = Parameter(parm=self.node.parm('RS_campro_flareTint4b'))
        self.parm_rs_campro_flaretint5r = Parameter(parm=self.node.parm('RS_campro_flareTint5r'))
        self.parm_rs_campro_flaretint5g = Parameter(parm=self.node.parm('RS_campro_flareTint5g'))
        self.parm_rs_campro_flaretint5b = Parameter(parm=self.node.parm('RS_campro_flareTint5b'))
        self.parm_rs_campro_flaretint6r = Parameter(parm=self.node.parm('RS_campro_flareTint6r'))
        self.parm_rs_campro_flaretint6g = Parameter(parm=self.node.parm('RS_campro_flareTint6g'))
        self.parm_rs_campro_flaretint6b = Parameter(parm=self.node.parm('RS_campro_flareTint6b'))
        self.parm_rs_campro_streakswitcher = Parameter(parm=self.node.parm('RS_campro_streakSwitcher'))
        self.parm_rs_campro_streakenable = Parameter(parm=self.node.parm('RS_campro_streakEnable'))
        self.parm_rs_campro_streakthreshold = Parameter(parm=self.node.parm('RS_campro_streakThreshold'))
        self.parm_rs_campro_streaktail = Parameter(parm=self.node.parm('RS_campro_streakTail'))
        self.parm_rs_campro_streaksoftness = Parameter(parm=self.node.parm('RS_campro_streakSoftness'))
        self.parm_rs_campro_streaknumber = Parameter(parm=self.node.parm('RS_campro_streakNumber'))
        self.parm_rs_campro_streakangle = Parameter(parm=self.node.parm('RS_campro_streakAngle'))
        self.parm_rs_campro_streakintensity = Parameter(parm=self.node.parm('RS_campro_streakIntensity'))
        self.parm_rs_campro_label6 = Parameter(parm=self.node.parm('RS_campro_label6'))
        self.parm_rs_campro_distortionenable = Parameter(parm=self.node.parm('RS_campro_distortionEnable'))
        self.parm_rs_campro_last = Parameter(parm=self.node.parm('RS_campro_last'))

        
        # parm menu vars:
        self.parm_xord = XordMenu(parm=self.node.parm('xOrd'))
        self.parm_rord = RordMenu(parm=self.node.parm('rOrd'))
        self.parm_pre_xform = PreXformMenu(parm=self.node.parm('pre_xform'))
        self.parm_lookup = LookupMenu(parm=self.node.parm('lookup'))
        self.parm_uparmtype = UparmtypeMenu(parm=self.node.parm('uparmtype'))
        self.parm_pickscript = PickscriptMenu(parm=self.node.parm('pickscript'))
        self.parm_resmenu = ResmenuMenu(parm=self.node.parm('resMenu'))
        self.parm_projection = ProjectionMenu(parm=self.node.parm('projection'))
        self.parm_focalunits = FocalunitsMenu(parm=self.node.parm('focalunits'))
        self.parm_vm_background = VmBackgroundMenu(parm=self.node.parm('vm_background'))
        self.parm_fgimage = FgimageMenu(parm=self.node.parm('fgimage'))
        self.parm_vm_bokeh = VmBokehMenu(parm=self.node.parm('vm_bokeh'))
        self.parm_vm_bokehfile = VmBokehfileMenu(parm=self.node.parm('vm_bokehfile'))
        self.parm_rs_campro_projection = RsCamproProjectionMenu(parm=self.node.parm('RS_campro_projection'))
        self.parm_rs_campro_stereomode = RsCamproStereomodeMenu(parm=self.node.parm('RS_campro_stereoMode'))
        self.parm_rs_campro_dofbokehnorm = RsCamproDofbokehnormMenu(parm=self.node.parm('RS_campro_dofBokehNorm'))
        self.parm_rs_campro_dofbokehimage = RsCamproDofbokehimageMenu(parm=self.node.parm('RS_campro_dofBokehImage'))
        self.parm_rs_campro_ociodisplay = RsCamproOciodisplayMenu(parm=self.node.parm('RS_campro_ocioDisplay'))
        self.parm_rs_campro_ocioview = RsCamproOcioviewMenu(parm=self.node.parm('RS_campro_ocioView'))
        self.parm_rs_campro_lutfile = RsCamproLutfileMenu(parm=self.node.parm('RS_campro_lutFile'))
        self.parm_rs_campro_distortionimage = RsCamproDistortionimageMenu(parm=self.node.parm('RS_campro_distortionImage'))


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


class PickscriptMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__renders_houdi___name__os__f4_exr = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/$HIPNAME.$OS.$F4.exr", 0)
        self.menu_e__renders_houdi___r_magic_prev__f3 = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/magic_prev.$F3", 1)
        self.menu_e__art_projects____y_first_hdrlight = ("E:/ART/PROJECTS/00_shared/hdri/my_first_hdrlight", 2)


class ResmenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_480_640 = ("640 480 1", 0)
        self.menu_hdtv_720 = ("1280 720 1", 1)
        self.menu_hdtv_1080 = ("1920 1080 1", 2)
        self.menu_hdtv_2160__4k_ = ("3840 2160 1", 3)
        self.menu__________ = ("_separator_", 4)
        self.menu_ntsc = ("640 486 1", 5)
        self.menu_ntsc_d1 = ("720 486 0.9", 6)
        self.menu_pal = ("768 576 1", 7)
        self.menu_pal_d1 = ("720 576 1.067", 8)
        self.menu_pal_16_9_anamorphic = ("720 576 1.422", 9)
        self.menu_pal_16_9__1_to_1_ = ("1024 576 1", 10)
        self.menu__________ = ("_separator_", 11)
        self.menu_full_ap_4k = ("4096 3112 1", 12)
        self.menu_full_ap_2k = ("2048 1556 1", 13)
        self.menu_acad_4k = ("3656 2664 1", 14)
        self.menu_acad_2k = ("1828 1332 1", 15)
        self.menu_scope_4k = ("3656 3112 1", 16)
        self.menu_scope_2k = ("1828 1556 1", 17)
        self.menu_vista_4k = ("6144 4096 1", 18)
        self.menu_vista_2k = ("3072 2048 1", 19)
        self.menu__________ = ("_separator_", 20)
        self.menu__2_256 = ("256 256 1", 21)
        self.menu__2_512 = ("512 512 1", 22)
        self.menu__2_1024 = ("1024 1024 1", 23)
        self.menu__2_2048 = ("2048 2048 1", 24)
        self.menu__2_4096 = ("4096 4096 1", 25)
        self.menu__2_8192 = ("8192 8192 1", 26)


class ProjectionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_perspective = ("perspective", 0)
        self.menu_orthographic = ("ortho", 1)
        self.menu_polar__panoramic_ = ("sphere", 2)
        self.menu_cylindrical__panoramic_ = ("cylinder", 3)
        self.menu_lens_shader = ("lens", 4)


class FocalunitsMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_millimeters = ("mm", 0)
        self.menu_meters = ("m", 1)
        self.menu_nanometers = ("nm", 2)
        self.menu_inches = ("in", 3)
        self.menu_feet = ("ft", 4)


class VmBackgroundMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___quarry_02_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/quarry_02_4k.exr", 0)
        self.menu_e__art_old_proje____1d_clear_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr", 1)
        self.menu_e__art_old_proje___a_sunrise_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr", 2)
        self.menu_d__art_projects____e_background_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/hdri_exrs/subtle_background.exr", 3)
        self.menu_e__art_old_proje___s_on_fire_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr", 4)
        self.menu_e__art_old_proje___enheim_05_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr", 5)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 6)
        self.menu_e__art_old_proje___oon_grass_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/noon_grass_4k.exr", 7)
        self.menu_d__art_projects____arfield_hdri_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/first_starfield_hdri.exr", 8)
        self.menu_e__art_old_proje___e_purple_neb_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/purple_neb.jpg", 9)
        self.menu_e__art_old_proje___xl_128051940_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/dreamstime_xxl_128051940.jpg", 10)
        self.menu_d__art_projects____s_flare_star_png = ("D:/ART/PROJECTS/stars_rnd/starfields/my_star_sprites/blue_lens_flare_star.png", 11)


class FgimageMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___quarry_02_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/quarry_02_4k.exr", 0)
        self.menu_e__art_old_proje____1d_clear_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr", 1)
        self.menu_e__art_old_proje___a_sunrise_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr", 2)
        self.menu_d__art_projects____e_background_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/hdri_exrs/subtle_background.exr", 3)
        self.menu_e__art_old_proje___s_on_fire_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr", 4)
        self.menu_e__art_old_proje___enheim_05_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr", 5)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 6)
        self.menu_e__art_old_proje___oon_grass_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/noon_grass_4k.exr", 7)
        self.menu_d__art_projects____arfield_hdri_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/first_starfield_hdri.exr", 8)
        self.menu_e__art_old_proje___e_purple_neb_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/purple_neb.jpg", 9)
        self.menu_e__art_old_proje___xl_128051940_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/dreamstime_xxl_128051940.jpg", 10)
        self.menu_d__art_projects____s_flare_star_png = ("D:/ART/PROJECTS/stars_rnd/starfields/my_star_sprites/blue_lens_flare_star.png", 11)


class VmBokehMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_radial_bokeh = ("radial", 0)
        self.menu_image_file_bokeh = ("file", 1)
        self.menu_box_filter_bokeh = ("box", 2)
        self.menu_disable_bokeh = ("null", 3)


class VmBokehfileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___quarry_02_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/quarry_02_4k.exr", 0)
        self.menu_e__art_old_proje____1d_clear_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr", 1)
        self.menu_e__art_old_proje___a_sunrise_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr", 2)
        self.menu_d__art_projects____e_background_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/hdri_exrs/subtle_background.exr", 3)
        self.menu_e__art_old_proje___s_on_fire_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr", 4)
        self.menu_e__art_old_proje___enheim_05_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr", 5)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 6)
        self.menu_e__art_old_proje___oon_grass_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/noon_grass_4k.exr", 7)
        self.menu_d__art_projects____arfield_hdri_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/first_starfield_hdri.exr", 8)
        self.menu_e__art_old_proje___e_purple_neb_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/purple_neb.jpg", 9)
        self.menu_e__art_old_proje___xl_128051940_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/dreamstime_xxl_128051940.jpg", 10)
        self.menu_d__art_projects____s_flare_star_png = ("D:/ART/PROJECTS/stars_rnd/starfields/my_star_sprites/blue_lens_flare_star.png", 11)


class RsCamproProjectionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_houdini_camera_projection = ("houdini_camera", 0)
        self.menu_fisheye_projection = ("fisheye", 1)
        self.menu_stereo_spherical_projection = ("stereo_spherical", 2)


class RsCamproStereomodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_side_by_side = ("side_by_side", 0)
        self.menu_top_botton = ("top_botton", 1)
        self.menu_left_only = ("left_only", 2)
        self.menu_right_only = ("right_only", 3)


class RsCamproDofbokehnormMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("1", 0)
        self.menu_unit_intensity = ("2", 1)
        self.menu_white_color_sum = ("3", 2)


class RsCamproDofbokehimageMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___quarry_02_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/quarry_02_4k.exr", 0)
        self.menu_e__art_old_proje____1d_clear_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr", 1)
        self.menu_e__art_old_proje___a_sunrise_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr", 2)
        self.menu_d__art_projects____e_background_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/hdri_exrs/subtle_background.exr", 3)
        self.menu_e__art_old_proje___s_on_fire_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr", 4)
        self.menu_e__art_old_proje___enheim_05_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr", 5)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 6)
        self.menu_e__art_old_proje___oon_grass_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/noon_grass_4k.exr", 7)
        self.menu_d__art_projects____arfield_hdri_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/first_starfield_hdri.exr", 8)
        self.menu_e__art_old_proje___e_purple_neb_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/purple_neb.jpg", 9)
        self.menu_e__art_old_proje___xl_128051940_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/dreamstime_xxl_128051940.jpg", 10)
        self.menu_d__art_projects____s_flare_star_png = ("D:/ART/PROJECTS/stars_rnd/starfields/my_star_sprites/blue_lens_flare_star.png", 11)


class RsCamproOciodisplayMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_srgb = ("sRGB", 0)


class RsCamproOcioviewMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_aces_1_0_sdr_video = ("ACES 1.0 SDR-video", 0)
        self.menu_un_tone_mapped = ("Un-tone-mapped", 1)
        self.menu_log = ("Log", 2)
        self.menu_raw = ("Raw", 3)


class RsCamproLutfileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__renders_houdi___name__os__f4_exr = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/$HIPNAME.$OS.$F4.exr", 0)
        self.menu_e__renders_houdi___r_magic_prev__f3 = ("E:/RENDERS/HOUDINI/TUTORIALS/MAGIC_RENDR/magic_prev.$F3", 1)
        self.menu_e__art_projects____y_first_hdrlight = ("E:/ART/PROJECTS/00_shared/hdri/my_first_hdrlight", 2)


class RsCamproDistortionimageMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_old_proje___quarry_02_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/quarry_02_4k.exr", 0)
        self.menu_e__art_old_proje____1d_clear_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/syferfontein_1d_clear_4k.exr", 1)
        self.menu_e__art_old_proje___a_sunrise_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/umhlanga_sunrise_4k.exr", 2)
        self.menu_d__art_projects____e_background_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/hdri_exrs/subtle_background.exr", 3)
        self.menu_e__art_old_proje___s_on_fire_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/the_sky_is_on_fire_4k.exr", 4)
        self.menu_e__art_old_proje___enheim_05_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/kloppenheim_05_4k.exr", 5)
        self.menu_e__art_old_proje___anga_veld_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/mpumalanga_veld_4k.exr", 6)
        self.menu_e__art_old_proje___oon_grass_4k_exr = ("E:/ART_OLD/PROJECTS/00_shared/hdri/noon_grass_4k.exr", 7)
        self.menu_d__art_projects____arfield_hdri_exr = ("D:/ART/PROJECTS/stars_rnd/starfields/first_starfield_hdri.exr", 8)
        self.menu_e__art_old_proje___e_purple_neb_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/purple_neb.jpg", 9)
        self.menu_e__art_old_proje___xl_128051940_jpg = ("E:/ART_OLD/PROJECTS/00_hdri_hd/hdri_space/dreamstime_xxl_128051940.jpg", 10)
        self.menu_d__art_projects____s_flare_star_png = ("D:/ART/PROJECTS/stars_rnd/starfields/my_star_sprites/blue_lens_flare_star.png", 11)



