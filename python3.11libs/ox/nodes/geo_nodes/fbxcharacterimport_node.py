from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class FbxcharacterimportNode(OXNode):
    node_type = 'kinefx::fbxcharacterimport'
    parm_lookup_dict = {'folder11': 'folder11', 'fbxfile': 'fbxfile', 'animfbxfile': 'animfbxfile', 'clipname': 'clipname', 'setnewclipname': 'setnewclipname', 'newclipname': 'newclipname', 'rigcolorr': 'rigcolorr', 'rigcolorg': 'rigcolorg', 'rigcolorb': 'rigcolorb', 'convertunits': 'convertunits', 'importinvisibleshapes': 'importinvisibleshapes', 'importuserdefattrib': 'importuserdefattrib', 'reload': 'reload', 'timeshiftmethod': 'timeshiftmethod', 'time': 'time', 'useanimationstarttime': 'useanimationstarttime', 'animationstarttime': 'animationstarttime', 'useanimationendtime': 'useanimationendtime', 'animationendtime': 'animationendtime', 'useplaybackstarttime': 'useplaybackstarttime', 'playbackstarttime': 'playbackstarttime', 'frame': 'frame', 'useanimationstartframe': 'useanimationstartframe', 'animationstartframe': 'animationstartframe', 'useanimationendframe': 'useanimationendframe', 'animationendframe': 'animationendframe', 'useplaybackstartframe': 'useplaybackstartframe', 'playbackstartframe': 'playbackstartframe', 'speed': 'speed'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder11 = Parameter(parm=self.node.parm('folder11'))
        self.parm_setnewclipname = Parameter(parm=self.node.parm('setnewclipname'))
        self.parm_newclipname = Parameter(parm=self.node.parm('newclipname'))
        self.parm_rigcolorr = Parameter(parm=self.node.parm('rigcolorr'))
        self.parm_rigcolorg = Parameter(parm=self.node.parm('rigcolorg'))
        self.parm_rigcolorb = Parameter(parm=self.node.parm('rigcolorb'))
        self.parm_convertunits = Parameter(parm=self.node.parm('convertunits'))
        self.parm_importinvisibleshapes = Parameter(parm=self.node.parm('importinvisibleshapes'))
        self.parm_importuserdefattrib = Parameter(parm=self.node.parm('importuserdefattrib'))
        self.parm_reload = Parameter(parm=self.node.parm('reload'))
        self.parm_time = Parameter(parm=self.node.parm('time'))
        self.parm_useanimationstarttime = Parameter(parm=self.node.parm('useanimationstarttime'))
        self.parm_animationstarttime = Parameter(parm=self.node.parm('animationstarttime'))
        self.parm_useanimationendtime = Parameter(parm=self.node.parm('useanimationendtime'))
        self.parm_animationendtime = Parameter(parm=self.node.parm('animationendtime'))
        self.parm_useplaybackstarttime = Parameter(parm=self.node.parm('useplaybackstarttime'))
        self.parm_playbackstarttime = Parameter(parm=self.node.parm('playbackstarttime'))
        self.parm_frame = Parameter(parm=self.node.parm('frame'))
        self.parm_useanimationstartframe = Parameter(parm=self.node.parm('useanimationstartframe'))
        self.parm_animationstartframe = Parameter(parm=self.node.parm('animationstartframe'))
        self.parm_useanimationendframe = Parameter(parm=self.node.parm('useanimationendframe'))
        self.parm_animationendframe = Parameter(parm=self.node.parm('animationendframe'))
        self.parm_useplaybackstartframe = Parameter(parm=self.node.parm('useplaybackstartframe'))
        self.parm_playbackstartframe = Parameter(parm=self.node.parm('playbackstartframe'))
        self.parm_speed = Parameter(parm=self.node.parm('speed'))

        
        # parm menu vars:
        self.parm_fbxfile = FbxfileMenu(parm=self.node.parm('fbxfile'))
        self.parm_animfbxfile = AnimfbxfileMenu(parm=self.node.parm('animfbxfile'))
        self.parm_clipname = ClipnameMenu(parm=self.node.parm('clipname'))
        self.parm_timeshiftmethod = TimeshiftmethodMenu(parm=self.node.parm('timeshiftmethod'))


        # input vars:


# parm menu classes:
class FbxfileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 0)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 1)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 2)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 3)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 4)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 5)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 30)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 31)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 32)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 33)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 34)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 35)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 36)
        self.menu_g__shared_drives___x_out_cursed_fbx = ("G:/Shared drives/meevil_pipeline_shared/output/traits/animated_fbx_out/Cursed.fbx", 37)
        self.menu_g__shared_drives___st_anim_out_gltf = ("G:/Shared drives/meevil_pipeline_shared/resources/test_anim_out.gltf", 38)
        self.menu_g__shared_drives___f423e0423d56_glb = ("G:\Shared drives\meevil_pipeline_shared\output\meevils\glb_out\7954da3e-df0c-4ec4-b7c6-f423e0423d56.glb", 39)


class AnimfbxfileMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__hip_animated_sa____arms_coffee_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_arms_coffee.fbx", 0)
        self.menu__hip_animated_sa___d_mouth_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_mouth_base.fbx", 1)
        self.menu__hip_animated_sa___d_legs_wings_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_legs_wings.fbx", 2)
        self.menu__hip_animated_sa___ed_eyes_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_eyes_base.fbx", 3)
        self.menu__hip_animated_sa____crown_arrow_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_crown_arrow.fbx", 4)
        self.menu__hip_animated_sa___ed_body_base_fbx = ("G:/Shared drives/meevil_pipeline_shared/resources/animation/animated_samples/cursed_body_base.fbx", 5)
        self.menu__hip_sandbox_cyb___ame_____dude_glb = ("$HIP/sandbox/cyber_test_.`@details('../uvunwrap4', 'name')`._dude.glb", 14)
        self.menu__hip_sandbox_cyb___index___dude_glb = ("$HIP/sandbox/cyber_test_.`@details('../uvunwrap4', 'name')`.`@pdg_index`._dude.glb", 15)
        self.menu__hip_sandbox_cyb___index___dude_glb = ("$HIP/sandbox/cyber_test_.`@details('../uvunwrap4', 'name', 0)`.`@pdg_index`._dude.glb", 16)
        self.menu__hip_sandbox_cyb___index___dude_glb = ("$HIP/sandbox/cyber_test_.`@detail('../uvunwrap4', 'name', 0)`.`@pdg_index`._dude.glb", 17)
        self.menu__hip_sandbox_cyb___index___dude_glb = ("$HIP/sandbox/cyber_test_.`@detail('../uvunwrap4/', 'name', 0)`.`@pdg_index`._dude.glb", 18)
        self.menu__hip_sandbox_cyb___index___dude_glb = ("$HIP/sandbox/cyber_test_.`@detail('../', 'name', 0)`.`@pdg_index`._dude.glb", 19)
        self.menu__hip_sandbox_cyb___index___dude_glb = ("$HIP/sandbox/cyber_test_.`@detail('.', 'name', 0)`.`@pdg_index`._dude.glb", 20)
        self.menu__hip_sandbox_cyb___index___dude_glb = ("$HIP/sandbox/cyber_test_.`@pdg_index`._dude.glb", 21)
        self.menu__hip_sandbox_cyb___ndex___dude_gltf = ("$HIP/sandbox/cyber_test_.`@pdg_index`._dude.gltf", 22)
        self.menu__hip_sandbox_cyber___pdg_index__glb = ("$HIP/sandbox/cyber_`@pdg_index`.glb", 23)
        self.menu__hip_sandbox_cyb____pdg_index__gltf = ("$HIP/sandbox/cyber_`@pdg_index`.gltf", 24)
        self.menu__hip_sandbox_cyb___t___f4__dude_glb = ("$HIP/sandbox/cyber_test_.$F4._dude.glb", 25)
        self.menu__hip_sandbox_cyb______f4__dude_gltf = ("$HIP/sandbox/cyber_test_.$F4._dude.gltf", 26)
        self.menu__hip_sandbox_cyb___st__f4_dude_gltf = ("$HIP/sandbox/cyber_test_$F4_dude.gltf", 27)
        self.menu__hip_sandbox_cyb___st__f3_dude_gltf = ("$HIP/sandbox/cyber_test_$F3_dude.gltf", 28)
        self.menu__hip_sandbox_fbx___g_index__out_fbx = ("$HIP/sandbox/fbx_out/`@pdg_index`_out.fbx", 29)
        self.menu_g__shared_drives___ls_glb_out___glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/*.glb", 30)
        self.menu_g__shared_drives___1aa5f9caa8d6_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0a8dc483-bf01-426a-b70e-1aa5f9caa8d6.glb", 31)
        self.menu__hip_sandbox_cyber_test__f4_fbx = ("$HIP/sandbox/cyber_test.$F4.fbx", 32)
        self.menu__hip_sandbox_cyber_test_glb = ("$HIP/sandbox/cyber_test.glb", 33)
        self.menu__hip_sandbox_cyber_test_gltf = ("$HIP/sandbox/cyber_test.gltf", 34)
        self.menu_g__shared_drives___a88bc5d5afa9_glb = ("G:/Shared drives/meevil_pipeline_shared/output/meevils/glb_out/0b03bec9-6e39-4812-93cb-a88bc5d5afa9.glb", 35)
        self.menu_g__shared_drives___own_sideears_fbx = ("G:/Shared drives/meevil_pipeline_shared/meevil_trait_upload_folder/plushy/Animated/Plushy_Crown_SideEars.fbx", 36)
        self.menu_g__shared_drives___x_out_cursed_fbx = ("G:/Shared drives/meevil_pipeline_shared/output/traits/animated_fbx_out/Cursed.fbx", 37)
        self.menu_g__shared_drives___st_anim_out_gltf = ("G:/Shared drives/meevil_pipeline_shared/resources/test_anim_out.gltf", 38)
        self.menu_g__shared_drives___f423e0423d56_glb = ("G:\Shared drives\meevil_pipeline_shared\output\meevils\glb_out\7954da3e-df0c-4ec4-b7c6-f423e0423d56.glb", 39)


class ClipnameMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_take_001 = ("Take 001", 0)


class TimeshiftmethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_by_time = ("bytime", 0)
        self.menu_by_frame = ("byframe", 1)



