from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RopFbxcharacteroutputNode(OXNode):
    node_type = 'kinefx::rop_fbxcharacteroutput'
    parm_lookup_dict = {'execute': 'execute', 'renderdialog': 'renderdialog', 'cliprangemode': 'cliprangemode', 'f1': 'f1', 'f2': 'f2', 'f3': 'f3', 'take': 'take', 'skingeosop': 'skingeosop', 'captureposesop': 'captureposesop', 'animatedposesop': 'animatedposesop', 'inputfilepath': 'inputfilepath', 'outputfilepath': 'outputfilepath', 'skinmethod': 'skinmethod', 'dqblendattrib': 'dqblendattrib', 'clipname': 'clipname', 'userestpose': 'userestpose', 'restposeattrib': 'restposeattrib', 'mkpath': 'mkpath', 'shiftstart': 'shiftstart', 'axissystem': 'axissystem', 'convertaxis': 'convertaxis', 'convertunits': 'convertunits', 'savebinary': 'savebinary', 'embedmedia': 'embedmedia', 'exportuserdefattrib': 'exportuserdefattrib', 'removeconstantanimcurves': 'removeconstantanimcurves', 'computesmoothinggroups': 'computesmoothinggroups', 'tprerender': 'tprerender', 'prerender': 'prerender', 'lprerender': 'lprerender', 'tpreframe': 'tpreframe', 'preframe': 'preframe', 'lpreframe': 'lpreframe', 'tpostframe': 'tpostframe', 'postframe': 'postframe', 'lpostframe': 'lpostframe', 'tpostrender': 'tpostrender', 'postrender': 'postrender', 'lpostrender': 'lpostrender'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_execute = Parameter(parm=self.node.parm('execute'))
        self.parm_renderdialog = Parameter(parm=self.node.parm('renderdialog'))
        self.parm_f1 = Parameter(parm=self.node.parm('f1'))
        self.parm_f2 = Parameter(parm=self.node.parm('f2'))
        self.parm_f3 = Parameter(parm=self.node.parm('f3'))
        self.parm_skingeosop = Parameter(parm=self.node.parm('skingeosop'))
        self.parm_captureposesop = Parameter(parm=self.node.parm('captureposesop'))
        self.parm_animatedposesop = Parameter(parm=self.node.parm('animatedposesop'))
        self.parm_dqblendattrib = Parameter(parm=self.node.parm('dqblendattrib'))
        self.parm_clipname = Parameter(parm=self.node.parm('clipname'))
        self.parm_userestpose = Parameter(parm=self.node.parm('userestpose'))
        self.parm_restposeattrib = Parameter(parm=self.node.parm('restposeattrib'))
        self.parm_mkpath = Parameter(parm=self.node.parm('mkpath'))
        self.parm_shiftstart = Parameter(parm=self.node.parm('shiftstart'))
        self.parm_convertaxis = Parameter(parm=self.node.parm('convertaxis'))
        self.parm_convertunits = Parameter(parm=self.node.parm('convertunits'))
        self.parm_savebinary = Parameter(parm=self.node.parm('savebinary'))
        self.parm_embedmedia = Parameter(parm=self.node.parm('embedmedia'))
        self.parm_exportuserdefattrib = Parameter(parm=self.node.parm('exportuserdefattrib'))
        self.parm_removeconstantanimcurves = Parameter(parm=self.node.parm('removeconstantanimcurves'))
        self.parm_computesmoothinggroups = Parameter(parm=self.node.parm('computesmoothinggroups'))
        self.parm_tprerender = Parameter(parm=self.node.parm('tprerender'))
        self.parm_tpreframe = Parameter(parm=self.node.parm('tpreframe'))
        self.parm_tpostframe = Parameter(parm=self.node.parm('tpostframe'))
        self.parm_tpostrender = Parameter(parm=self.node.parm('tpostrender'))

        
        # parm menu vars:
        self.parm_cliprangemode = CliprangemodeMenu(parm=self.node.parm('cliprangemode'))
        self.parm_take = TakeMenu(parm=self.node.parm('take'))
        self.parm_inputfilepath = InputfilepathMenu(parm=self.node.parm('inputfilepath'))
        self.parm_outputfilepath = OutputfilepathMenu(parm=self.node.parm('outputfilepath'))
        self.parm_skinmethod = SkinmethodMenu(parm=self.node.parm('skinmethod'))
        self.parm_axissystem = AxissystemMenu(parm=self.node.parm('axissystem'))
        self.parm_prerender = PrerenderMenu(parm=self.node.parm('prerender'))
        self.parm_lprerender = LprerenderMenu(parm=self.node.parm('lprerender'))
        self.parm_preframe = PreframeMenu(parm=self.node.parm('preframe'))
        self.parm_lpreframe = LpreframeMenu(parm=self.node.parm('lpreframe'))
        self.parm_postframe = PostframeMenu(parm=self.node.parm('postframe'))
        self.parm_lpostframe = LpostframeMenu(parm=self.node.parm('lpostframe'))
        self.parm_postrender = PostrenderMenu(parm=self.node.parm('postrender'))
        self.parm_lpostrender = LpostrenderMenu(parm=self.node.parm('lpostrender'))


        # input vars:
        self.input_rest_geometry = 'Rest Geometry'
        self.input_capture_pose = 'Capture Pose'
        self.input_animated_pose = 'Animated Pose'


# parm menu classes:
class CliprangemodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_use_clipinfo_detail_attribute = ("useattrib", 0)
        self.menu_render_current_frame = ("off", 1)
        self.menu_render_frame_range = ("normal", 2)
        self.menu_render_frame_range_only__strict_ = ("on", 3)


class TakeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__current_ = ("_current_", 0)
        self.menu_main = ("Main", 1)
        self.menu_cursed = ("Cursed", 2)
        self.menu_cyber = ("Cyber", 3)
        self.menu_fb = ("FB", 4)
        self.menu_fb_fleshy = ("FB_Fleshy", 5)
        self.menu_fallen = ("Fallen", 6)
        self.menu_funguys = ("Funguys", 7)
        self.menu_ooze = ("Ooze", 8)
        self.menu_plushy = ("Plushy", 9)


class InputfilepathMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_test_this_fbx = ("$HIP/test_this.fbx", 0)
        self.menu__hip_out_glb = ("$HIP/out.glb", 1)
        self.menu__hip_out_fbx = ("$HIP/out.fbx", 2)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 3)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 4)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 5)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 6)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 7)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 8)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 33)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 34)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 35)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 36)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 37)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 38)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 39)


class OutputfilepathMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_test_this_fbx = ("$HIP/test_this.fbx", 0)
        self.menu__hip_out_glb = ("$HIP/out.glb", 1)
        self.menu__hip_out_fbx = ("$HIP/out.fbx", 2)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 3)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 4)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 5)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 6)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 7)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 8)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 33)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 34)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 35)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 36)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 37)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 38)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 39)


class SkinmethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_linear = ("linear", 0)
        self.menu_dual_quaternion = ("dualquat", 1)
        self.menu_blend_dual_quaternion_and_linear = ("blenddualquat", 2)


class AxissystemMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_y_up__right_handed_ = ("yupright", 0)
        self.menu_y_up__left_handed_ = ("yupleft", 1)
        self.menu_z_up__right_handed_ = ("zupright", 2)
        self.menu_current__y_up_right_handed_ = ("currentup", 3)


class PrerenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_test_this_fbx = ("$HIP/test_this.fbx", 0)
        self.menu__hip_out_glb = ("$HIP/out.glb", 1)
        self.menu__hip_out_fbx = ("$HIP/out.fbx", 2)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 3)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 4)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 5)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 6)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 7)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 8)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 33)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 34)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 35)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 36)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 37)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 38)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 39)


class LprerenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = ("hscript", 0)
        self.menu_python = ("python", 1)


class PreframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_test_this_fbx = ("$HIP/test_this.fbx", 0)
        self.menu__hip_out_glb = ("$HIP/out.glb", 1)
        self.menu__hip_out_fbx = ("$HIP/out.fbx", 2)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 3)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 4)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 5)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 6)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 7)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 8)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 33)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 34)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 35)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 36)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 37)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 38)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 39)


class LpreframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = ("hscript", 0)
        self.menu_python = ("python", 1)


class PostframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_test_this_fbx = ("$HIP/test_this.fbx", 0)
        self.menu__hip_out_glb = ("$HIP/out.glb", 1)
        self.menu__hip_out_fbx = ("$HIP/out.fbx", 2)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 3)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 4)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 5)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 6)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 7)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 8)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 33)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 34)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 35)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 36)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 37)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 38)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 39)


class LpostframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = ("hscript", 0)
        self.menu_python = ("python", 1)


class PostrenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_test_this_fbx = ("$HIP/test_this.fbx", 0)
        self.menu__hip_out_glb = ("$HIP/out.glb", 1)
        self.menu__hip_out_fbx = ("$HIP/out.fbx", 2)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 3)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 4)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 5)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 6)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 7)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 8)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 33)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 34)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 35)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 36)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 37)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 38)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 39)


class LpostrenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = ("hscript", 0)
        self.menu_python = ("python", 1)



