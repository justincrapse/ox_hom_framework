from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RopCompNode(OXNode):
    node_type = 'rop_comp'
    parm_lookup_dict = {'execute': 'execute', 'renderdialog': 'renderdialog', 'trange': 'trange', 'f1': 'f1', 'f2': 'f2', 'f3': 'f3', 'take': 'take', 'copswitcher1': 'copswitcher1', 'coppath': 'coppath', 'tres': 'tres', 'res1': 'res1', 'res2': 'res2', 'resmenu': 'resmenu', 'copoutput': 'copoutput', 'mkpath': 'mkpath', 'color': 'color', 'alpha': 'alpha', 'scopeplanes': 'scopeplanes', 'convertcolorspace': 'convertcolorspace', 'gamma': 'gamma', 'lut': 'lut', 'framedepend': 'framedepend', 'batchmode': 'batchmode', 'batchsize': 'batchsize', 'reloadfiles': 'reloadfiles', 'outputarea': 'outputarea', 'pixelcrop1': 'pixelcrop1', 'pixelcrop2': 'pixelcrop2', 'pixelcrop3': 'pixelcrop3', 'pixelcrop4': 'pixelcrop4', 'uvcrop1': 'uvcrop1', 'uvcrop2': 'uvcrop2', 'uvcrop3': 'uvcrop3', 'uvcrop4': 'uvcrop4', 'limitcanvaspixels': 'limitcanvaspixels', 'canvaspixels': 'canvaspixels', 'limitcanvaspercent': 'limitcanvaspercent', 'canvaspercent': 'canvaspercent', 'copaux1': 'copaux1', 'color1': 'color1', 'alpha1': 'alpha1', 'scopeplanes1': 'scopeplanes1', 'copaux2': 'copaux2', 'color2': 'color2', 'alpha2': 'alpha2', 'scopeplanes2': 'scopeplanes2', 'copaux3': 'copaux3', 'color3': 'color3', 'alpha3': 'alpha3', 'scopeplanes3': 'scopeplanes3', 'copaux4': 'copaux4', 'color4': 'color4', 'alpha4': 'alpha4', 'scopeplanes4': 'scopeplanes4', 'copaux5': 'copaux5', 'color5': 'color5', 'alpha5': 'alpha5', 'scopeplanes5': 'scopeplanes5', 'vm_image_artist': 'vm_image_artist', 'vm_image_comment': 'vm_image_comment', 'vm_image_hostname': 'vm_image_hostname', 'vm_image_mplay_label': 'vm_image_mplay_label', 'vm_image_mplay_gamma': 'vm_image_mplay_gamma', 'vm_image_jpeg_quality': 'vm_image_jpeg_quality', 'vm_image_tiff_compression': 'vm_image_tiff_compression', 'vm_image_exr_compression': 'vm_image_exr_compression', 'pngtga_alpha_multiplication': 'pngtga_alpha_multiplication', 'tprerender': 'tprerender', 'prerender': 'prerender', 'lprerender': 'lprerender', 'tpreframe': 'tpreframe', 'preframe': 'preframe', 'lpreframe': 'lpreframe', 'tpostframe': 'tpostframe', 'postframe': 'postframe', 'lpostframe': 'lpostframe', 'tpostrender': 'tpostrender', 'postrender': 'postrender', 'lpostrender': 'lpostrender'}

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
        self.parm_copswitcher1 = Parameter(parm=self.node.parm('copswitcher1'))
        self.parm_coppath = Parameter(parm=self.node.parm('coppath'))
        self.parm_res1 = Parameter(parm=self.node.parm('res1'))
        self.parm_res2 = Parameter(parm=self.node.parm('res2'))
        self.parm_mkpath = Parameter(parm=self.node.parm('mkpath'))
        self.parm_convertcolorspace = Parameter(parm=self.node.parm('convertcolorspace'))
        self.parm_gamma = Parameter(parm=self.node.parm('gamma'))
        self.parm_lut = Parameter(parm=self.node.parm('lut'))
        self.parm_framedepend = Parameter(parm=self.node.parm('framedepend'))
        self.parm_batchmode = Parameter(parm=self.node.parm('batchmode'))
        self.parm_batchsize = Parameter(parm=self.node.parm('batchsize'))
        self.parm_reloadfiles = Parameter(parm=self.node.parm('reloadfiles'))
        self.parm_pixelcrop1 = Parameter(parm=self.node.parm('pixelcrop1'))
        self.parm_pixelcrop2 = Parameter(parm=self.node.parm('pixelcrop2'))
        self.parm_pixelcrop3 = Parameter(parm=self.node.parm('pixelcrop3'))
        self.parm_pixelcrop4 = Parameter(parm=self.node.parm('pixelcrop4'))
        self.parm_uvcrop1 = Parameter(parm=self.node.parm('uvcrop1'))
        self.parm_uvcrop2 = Parameter(parm=self.node.parm('uvcrop2'))
        self.parm_uvcrop3 = Parameter(parm=self.node.parm('uvcrop3'))
        self.parm_uvcrop4 = Parameter(parm=self.node.parm('uvcrop4'))
        self.parm_limitcanvaspixels = Parameter(parm=self.node.parm('limitcanvaspixels'))
        self.parm_canvaspixels = Parameter(parm=self.node.parm('canvaspixels'))
        self.parm_limitcanvaspercent = Parameter(parm=self.node.parm('limitcanvaspercent'))
        self.parm_canvaspercent = Parameter(parm=self.node.parm('canvaspercent'))
        self.parm_vm_image_artist = Parameter(parm=self.node.parm('vm_image_artist'))
        self.parm_vm_image_comment = Parameter(parm=self.node.parm('vm_image_comment'))
        self.parm_vm_image_hostname = Parameter(parm=self.node.parm('vm_image_hostname'))
        self.parm_vm_image_mplay_label = Parameter(parm=self.node.parm('vm_image_mplay_label'))
        self.parm_vm_image_mplay_gamma = Parameter(parm=self.node.parm('vm_image_mplay_gamma'))
        self.parm_vm_image_jpeg_quality = Parameter(parm=self.node.parm('vm_image_jpeg_quality'))
        self.parm_tprerender = Parameter(parm=self.node.parm('tprerender'))
        self.parm_tpreframe = Parameter(parm=self.node.parm('tpreframe'))
        self.parm_tpostframe = Parameter(parm=self.node.parm('tpostframe'))
        self.parm_tpostrender = Parameter(parm=self.node.parm('tpostrender'))

        
        # parm menu vars:
        self.parm_trange = TrangeMenu(parm=self.node.parm('trange'))
        self.parm_take = TakeMenu(parm=self.node.parm('take'))
        self.parm_tres = TresMenu(parm=self.node.parm('tres'))
        self.parm_resmenu = ResmenuMenu(parm=self.node.parm('resmenu'))
        self.parm_copoutput = CopoutputMenu(parm=self.node.parm('copoutput'))
        self.parm_color = ColorMenu(parm=self.node.parm('color'))
        self.parm_alpha = AlphaMenu(parm=self.node.parm('alpha'))
        self.parm_scopeplanes = ScopeplanesMenu(parm=self.node.parm('scopeplanes'))
        self.parm_outputarea = OutputareaMenu(parm=self.node.parm('outputarea'))
        self.parm_copaux1 = Copaux1Menu(parm=self.node.parm('copaux1'))
        self.parm_color1 = Color1Menu(parm=self.node.parm('color1'))
        self.parm_alpha1 = Alpha1Menu(parm=self.node.parm('alpha1'))
        self.parm_scopeplanes1 = Scopeplanes1Menu(parm=self.node.parm('scopeplanes1'))
        self.parm_copaux2 = Copaux2Menu(parm=self.node.parm('copaux2'))
        self.parm_color2 = Color2Menu(parm=self.node.parm('color2'))
        self.parm_alpha2 = Alpha2Menu(parm=self.node.parm('alpha2'))
        self.parm_scopeplanes2 = Scopeplanes2Menu(parm=self.node.parm('scopeplanes2'))
        self.parm_copaux3 = Copaux3Menu(parm=self.node.parm('copaux3'))
        self.parm_color3 = Color3Menu(parm=self.node.parm('color3'))
        self.parm_alpha3 = Alpha3Menu(parm=self.node.parm('alpha3'))
        self.parm_scopeplanes3 = Scopeplanes3Menu(parm=self.node.parm('scopeplanes3'))
        self.parm_copaux4 = Copaux4Menu(parm=self.node.parm('copaux4'))
        self.parm_color4 = Color4Menu(parm=self.node.parm('color4'))
        self.parm_alpha4 = Alpha4Menu(parm=self.node.parm('alpha4'))
        self.parm_scopeplanes4 = Scopeplanes4Menu(parm=self.node.parm('scopeplanes4'))
        self.parm_copaux5 = Copaux5Menu(parm=self.node.parm('copaux5'))
        self.parm_color5 = Color5Menu(parm=self.node.parm('color5'))
        self.parm_alpha5 = Alpha5Menu(parm=self.node.parm('alpha5'))
        self.parm_scopeplanes5 = Scopeplanes5Menu(parm=self.node.parm('scopeplanes5'))
        self.parm_vm_image_tiff_compression = VmImageTiffCompressionMenu(parm=self.node.parm('vm_image_tiff_compression'))
        self.parm_vm_image_exr_compression = VmImageExrCompressionMenu(parm=self.node.parm('vm_image_exr_compression'))
        self.parm_pngtga_alpha_multiplication = PngtgaAlphaMultiplicationMenu(parm=self.node.parm('pngtga_alpha_multiplication'))
        self.parm_prerender = PrerenderMenu(parm=self.node.parm('prerender'))
        self.parm_lprerender = LprerenderMenu(parm=self.node.parm('lprerender'))
        self.parm_preframe = PreframeMenu(parm=self.node.parm('preframe'))
        self.parm_lpreframe = LpreframeMenu(parm=self.node.parm('lpreframe'))
        self.parm_postframe = PostframeMenu(parm=self.node.parm('postframe'))
        self.parm_lpostframe = LpostframeMenu(parm=self.node.parm('lpostframe'))
        self.parm_postrender = PostrenderMenu(parm=self.node.parm('postrender'))
        self.parm_lpostrender = LpostrenderMenu(parm=self.node.parm('lpostrender'))


        # input vars:
        self.input_input_1 = 'Input 1'


# parm menu classes:
class TrangeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_render_current_frame = ("off", 0)
        self.menu_render_frame_range = ("normal", 1)
        self.menu_render_frame_range_only__strict_ = ("on", 2)


class TakeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__current_ = ("_current_", 0)
        self.menu_main = ("Main", 1)


class TresMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__8_resolution_1 = ("proxy12", 0)
        self.menu__4_resolution_1 = ("proxy25", 1)
        self.menu__3_resolution_1 = ("proxy33", 2)
        self.menu__2_resolution_1 = ("proxy50", 3)
        self.menu__3_resolution_2 = ("proxy66", 4)
        self.menu__4_resolution_3 = ("proxy75", 5)
        self.menu_natural_resolution = ("natural", 6)
        self.menu_project_resolution = ("project", 7)
        self.menu_project_proxy_res = ("proxy", 8)
        self.menu_specify_resolution = ("specify", 9)
        self.menu__33x_resolution_1 = ("proxy133x", 10)
        self.menu__5x_resolution_1 = ("proxy15x", 11)
        self.menu_x_resolution_2 = ("proxy2x", 12)
        self.menu_x_resolution_4 = ("proxy4x", 13)
        self.menu_x_resolution_8 = ("proxy8x", 14)


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


class CopoutputMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = ("ip", 0)
        self.menu_mplay__non_interactive_ = ("md", 1)
        self.menu_sequence_of__pic_files = ("$HIP/render/$HIPNAME.$OS.$F4.pic", 2)
        self.menu_sequence_of__tif_files = ("$HIP/render/$HIPNAME.$OS.$F4.tif", 3)
        self.menu_sequence_of__exr_files = ("$HIP/render/$HIPNAME.$OS.$F4.exr", 4)


class ColorMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class AlphaMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class ScopeplanesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("*", 0)


class OutputareaMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_frame = ("frame", 0)
        self.menu_crop_region = ("crop", 1)
        self.menu_frame___surrounding_canvas = ("canvas", 2)


class Copaux1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = ("ip", 0)
        self.menu_mplay__non_interactive_ = ("md", 1)
        self.menu_sequence_of__pic_files = ("$HIP/render/$HIPNAME.$OS.$F4.pic", 2)
        self.menu_sequence_of__tif_files = ("$HIP/render/$HIPNAME.$OS.$F4.tif", 3)
        self.menu_sequence_of__exr_files = ("$HIP/render/$HIPNAME.$OS.$F4.exr", 4)


class Color1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Alpha1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Scopeplanes1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("*", 0)


class Copaux2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = ("ip", 0)
        self.menu_mplay__non_interactive_ = ("md", 1)
        self.menu_sequence_of__pic_files = ("$HIP/render/$HIPNAME.$OS.$F4.pic", 2)
        self.menu_sequence_of__tif_files = ("$HIP/render/$HIPNAME.$OS.$F4.tif", 3)
        self.menu_sequence_of__exr_files = ("$HIP/render/$HIPNAME.$OS.$F4.exr", 4)


class Color2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Alpha2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Scopeplanes2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("*", 0)


class Copaux3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = ("ip", 0)
        self.menu_mplay__non_interactive_ = ("md", 1)
        self.menu_sequence_of__pic_files = ("$HIP/render/$HIPNAME.$OS.$F4.pic", 2)
        self.menu_sequence_of__tif_files = ("$HIP/render/$HIPNAME.$OS.$F4.tif", 3)
        self.menu_sequence_of__exr_files = ("$HIP/render/$HIPNAME.$OS.$F4.exr", 4)


class Color3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Alpha3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Scopeplanes3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("*", 0)


class Copaux4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = ("ip", 0)
        self.menu_mplay__non_interactive_ = ("md", 1)
        self.menu_sequence_of__pic_files = ("$HIP/render/$HIPNAME.$OS.$F4.pic", 2)
        self.menu_sequence_of__tif_files = ("$HIP/render/$HIPNAME.$OS.$F4.tif", 3)
        self.menu_sequence_of__exr_files = ("$HIP/render/$HIPNAME.$OS.$F4.exr", 4)


class Color4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Alpha4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Scopeplanes4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("*", 0)


class Copaux5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = ("ip", 0)
        self.menu_mplay__non_interactive_ = ("md", 1)
        self.menu_sequence_of__pic_files = ("$HIP/render/$HIPNAME.$OS.$F4.pic", 2)
        self.menu_sequence_of__tif_files = ("$HIP/render/$HIPNAME.$OS.$F4.tif", 3)
        self.menu_sequence_of__exr_files = ("$HIP/render/$HIPNAME.$OS.$F4.exr", 4)


class Color5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Alpha5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = ("(none)", 0)


class Scopeplanes5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = ("*", 0)


class VmImageTiffCompressionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_compression = ("None", 0)
        self.menu_lzw_compression = ("LZW", 1)
        self.menu_adobe_deflate = ("AdobeDeflate", 2)
        self.menu_packbits = ("PackBits", 3)


class VmImageExrCompressionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = ("none", 0)
        self.menu_rle = ("rle", 1)
        self.menu_zip__single_scanline = ("zips", 2)
        self.menu_zip__multi_scanline_blocks = ("zip", 3)
        self.menu_piz_wavelet = ("piz", 4)
        self.menu_pxr24__32_bit_float_compression__lossy_ = ("pix", 5)
        self.menu_b44__4x4_block_compression__lossy_ = ("b44", 6)
        self.menu_b44a__4x4_block_extra_compression__lossy_ = ("b44a", 7)
        self.menu_dwa_a__32_scanline_block_compression__lossy_ = ("dwaa", 8)
        self.menu_dwa_b__256_scanline_block_compression__lossy_ = ("dwab", 9)


class PngtgaAlphaMultiplicationMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_premultiplied = ("premult", 0)
        self.menu_unpremultiplied = ("unpremult", 1)


class PrerenderMenu(Menu):
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


class LpostrenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = ("hscript", 0)
        self.menu_python = ("python", 1)



