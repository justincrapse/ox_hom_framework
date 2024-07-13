from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class FileNode(OXNode):
    node_type = 'file'
    parm_lookup_dict = {'source': 'source', 'filename': 'filename', 'clonename': 'clonename', 'clonesession': 'clonesession', 'clonemenu': 'clonemenu', 'reload': 'reload', 'videoframemethod': 'videoframemethod', 'videoframestart': 'videoframestart', 'videoframe': 'videoframe', 'border': 'border', 'missingdata': 'missingdata', 'missingcolorr': 'missingcolorr', 'missingcolorg': 'missingcolorg', 'missingcolorb': 'missingcolorb', 'missingcolora': 'missingcolora', 'colorspace': 'colorspace', 'addaovs': 'addaovs', 'aovs': 'aovs', 'aov1': 'aov1', 'type1': 'type1', 'precision1': 'precision1', 'raw1': 'raw1'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_filename = Parameter(parm=self.node.parm('filename'))
        self.parm_clonename = Parameter(parm=self.node.parm('clonename'))
        self.parm_clonesession = Parameter(parm=self.node.parm('clonesession'))
        self.parm_clonemenu = Parameter(parm=self.node.parm('clonemenu'))
        self.parm_reload = Parameter(parm=self.node.parm('reload'))
        self.parm_videoframestart = Parameter(parm=self.node.parm('videoframestart'))
        self.parm_videoframe = Parameter(parm=self.node.parm('videoframe'))
        self.parm_missingcolorr = Parameter(parm=self.node.parm('missingcolorr'))
        self.parm_missingcolorg = Parameter(parm=self.node.parm('missingcolorg'))
        self.parm_missingcolorb = Parameter(parm=self.node.parm('missingcolorb'))
        self.parm_missingcolora = Parameter(parm=self.node.parm('missingcolora'))
        self.parm_addaovs = Parameter(parm=self.node.parm('addaovs'))
        self.parm_aovs = Parameter(parm=self.node.parm('aovs'))
        self.parm_aov1 = Parameter(parm=self.node.parm('aov1'))
        self.parm_raw1 = Parameter(parm=self.node.parm('raw1'))

        
        # parm menu vars:
        self.parm_source = SourceMenu(parm=self.node.parm('source'))
        self.parm_videoframemethod = VideoframemethodMenu(parm=self.node.parm('videoframemethod'))
        self.parm_border = BorderMenu(parm=self.node.parm('border'))
        self.parm_missingdata = MissingdataMenu(parm=self.node.parm('missingdata'))
        self.parm_colorspace = ColorspaceMenu(parm=self.node.parm('colorspace'))
        self.parm_type1 = Type1Menu(parm=self.node.parm('type1'))
        self.parm_precision1 = Precision1Menu(parm=self.node.parm('precision1'))


        # input vars:


# parm menu classes:
class SourceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_file = ("file", 0)
        self.menu_clone = ("clone", 1)


class VideoframemethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_start_frame = ("start", 0)
        self.menu_frame_number = ("frame", 1)


class BorderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_default = ("default", 0)
        self.menu_constant = ("constant", 1)
        self.menu_clamp = ("clamp", 2)
        self.menu_mirror = ("mirror", 3)
        self.menu_wrap = ("wrap", 4)


class MissingdataMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_report_message = ("error", 0)
        self.menu_use_color = ("color", 1)


class ColorspaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_opencolorio = ("ocio", 0)
        self.menu_raw = ("raw", 1)


class Type1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mono = ("float", 0)
        self.menu_uv = ("vector2", 1)
        self.menu_rgb = ("vector", 2)
        self.menu_rgba = ("vector4", 3)
        self.menu_id = ("id", 4)


class Precision1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_default = ("default", 0)
        self.menu_file = ("file", 1)
        self.menu_bit_8 = ("b8", 2)
        self.menu_bit_16 = ("b16", 3)
        self.menu_bit_32 = ("b32", 4)



