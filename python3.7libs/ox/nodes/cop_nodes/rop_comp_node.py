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
        self.menu_render_current_frame = 'off'
        self.menu_render_frame_range = 'normal'
        self.menu_render_frame_range_only__strict_ = 'on'


class TakeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__current_ = '_current_'
        self.menu_main = 'Main'


class TresMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__8_resolution_1 = 'proxy12'
        self.menu__4_resolution_1 = 'proxy25'
        self.menu__3_resolution_1 = 'proxy33'
        self.menu__2_resolution_1 = 'proxy50'
        self.menu__3_resolution_2 = 'proxy66'
        self.menu__4_resolution_3 = 'proxy75'
        self.menu_natural_resolution = 'natural'
        self.menu_project_resolution = 'project'
        self.menu_project_proxy_res = 'proxy'
        self.menu_specify_resolution = 'specify'
        self.menu__33x_resolution_1 = 'proxy133x'
        self.menu__5x_resolution_1 = 'proxy15x'
        self.menu_x_resolution_2 = 'proxy2x'
        self.menu_x_resolution_4 = 'proxy4x'
        self.menu_x_resolution_8 = 'proxy8x'


class ResmenuMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_480_640 = '640 480 1'
        self.menu_hdtv_720 = '1280 720 1'
        self.menu_hdtv_1080 = '1920 1080 1'
        self.menu_hdtv_2160__4k_ = '3840 2160 1'
        self.menu__________ = '_separator_'
        self.menu_ntsc = '640 486 1'
        self.menu_ntsc_d1 = '720 486 0.9'
        self.menu_pal = '768 576 1'
        self.menu_pal_d1 = '720 576 1.067'
        self.menu_pal_16_9_anamorphic = '720 576 1.422'
        self.menu_pal_16_9__1_to_1_ = '1024 576 1'
        self.menu__________ = '_separator_'
        self.menu_full_ap_4k = '4096 3112 1'
        self.menu_full_ap_2k = '2048 1556 1'
        self.menu_acad_4k = '3656 2664 1'
        self.menu_acad_2k = '1828 1332 1'
        self.menu_scope_4k = '3656 3112 1'
        self.menu_scope_2k = '1828 1556 1'
        self.menu_vista_4k = '6144 4096 1'
        self.menu_vista_2k = '3072 2048 1'
        self.menu__________ = '_separator_'
        self.menu__2_256 = '256 256 1'
        self.menu__2_512 = '512 512 1'
        self.menu__2_1024 = '1024 1024 1'
        self.menu__2_2048 = '2048 2048 1'
        self.menu__2_4096 = '4096 4096 1'
        self.menu__2_8192 = '8192 8192 1'


class CopoutputMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = 'ip'
        self.menu_mplay__non_interactive_ = 'md'
        self.menu_sequence_of__pic_files = '$HIP/render/$HIPNAME.$OS.$F4.pic'
        self.menu_sequence_of__tif_files = '$HIP/render/$HIPNAME.$OS.$F4.tif'
        self.menu_sequence_of__exr_files = '$HIP/render/$HIPNAME.$OS.$F4.exr'


class ColorMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class AlphaMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class ScopeplanesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = '*'
        self.menu_c = 'C'


class OutputareaMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_frame = 'frame'
        self.menu_crop_region = 'crop'
        self.menu_frame___surrounding_canvas = 'canvas'


class Copaux1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = 'ip'
        self.menu_mplay__non_interactive_ = 'md'
        self.menu_sequence_of__pic_files = '$HIP/render/$HIPNAME.$OS.$F4.pic'
        self.menu_sequence_of__tif_files = '$HIP/render/$HIPNAME.$OS.$F4.tif'
        self.menu_sequence_of__exr_files = '$HIP/render/$HIPNAME.$OS.$F4.exr'


class Color1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Alpha1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Scopeplanes1Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = '*'
        self.menu_c = 'C'


class Copaux2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = 'ip'
        self.menu_mplay__non_interactive_ = 'md'
        self.menu_sequence_of__pic_files = '$HIP/render/$HIPNAME.$OS.$F4.pic'
        self.menu_sequence_of__tif_files = '$HIP/render/$HIPNAME.$OS.$F4.tif'
        self.menu_sequence_of__exr_files = '$HIP/render/$HIPNAME.$OS.$F4.exr'


class Color2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Alpha2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Scopeplanes2Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = '*'
        self.menu_c = 'C'


class Copaux3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = 'ip'
        self.menu_mplay__non_interactive_ = 'md'
        self.menu_sequence_of__pic_files = '$HIP/render/$HIPNAME.$OS.$F4.pic'
        self.menu_sequence_of__tif_files = '$HIP/render/$HIPNAME.$OS.$F4.tif'
        self.menu_sequence_of__exr_files = '$HIP/render/$HIPNAME.$OS.$F4.exr'


class Color3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Alpha3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Scopeplanes3Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = '*'
        self.menu_c = 'C'


class Copaux4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = 'ip'
        self.menu_mplay__non_interactive_ = 'md'
        self.menu_sequence_of__pic_files = '$HIP/render/$HIPNAME.$OS.$F4.pic'
        self.menu_sequence_of__tif_files = '$HIP/render/$HIPNAME.$OS.$F4.tif'
        self.menu_sequence_of__exr_files = '$HIP/render/$HIPNAME.$OS.$F4.exr'


class Color4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Alpha4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Scopeplanes4Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = '*'
        self.menu_c = 'C'


class Copaux5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_mplay__interactive_ = 'ip'
        self.menu_mplay__non_interactive_ = 'md'
        self.menu_sequence_of__pic_files = '$HIP/render/$HIPNAME.$OS.$F4.pic'
        self.menu_sequence_of__tif_files = '$HIP/render/$HIPNAME.$OS.$F4.tif'
        self.menu_sequence_of__exr_files = '$HIP/render/$HIPNAME.$OS.$F4.exr'


class Color5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Alpha5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__none_ = '(none)'
        self.menu_c = 'C'


class Scopeplanes5Menu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__ = '*'
        self.menu_c = 'C'


class VmImageTiffCompressionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_compression = 'None'
        self.menu_lzw_compression = 'LZW'
        self.menu_adobe_deflate = 'AdobeDeflate'
        self.menu_packbits = 'PackBits'


class VmImageExrCompressionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = 'none'
        self.menu_rle = 'rle'
        self.menu_zip__single_scanline = 'zips'
        self.menu_zip__multi_scanline_blocks = 'zip'
        self.menu_piz_wavelet = 'piz'
        self.menu_pxr24__32_bit_float_compression__lossy_ = 'pix'
        self.menu_b44__4x4_block_compression__lossy_ = 'b44'
        self.menu_b44a__4x4_block_extra_compression__lossy_ = 'b44a'
        self.menu_dwa_a__32_scanline_block_compression__lossy_ = 'dwaa'
        self.menu_dwa_b__256_scanline_block_compression__lossy_ = 'dwab'


class PngtgaAlphaMultiplicationMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_premultiplied = 'premult'
        self.menu_unpremultiplied = 'unpremult'


class PrerenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_products_ox_mtlx_hf_test_out = 'E:/ART/PRODUCTS/OX-MTLX/hf_test_out'
        self.menu_d__minecraft_sub___ded_copper_sbsar = 'D:/Minecraft/substance/hazelnut_3/copper_block/grinded_copper.sbsar'
        self.menu_d__minecraft_sub___dirt_field_sbsar = 'D:/Minecraft/substance/hazelnut/farmland_wet/arid_dirt_field.sbsar'
        self.menu_e__art_products____ers_rock_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_cpu.jpg'
        self.menu_e__art_products____ers_rock_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_xpu.jpg'
        self.menu_e__art_products____rs_quilt_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_xpu.jpg'
        self.menu_e__art_products____rs_quilt_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_cpu.jpg'
        self.menu_e__art_products____ers_lava_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_cpu.jpg'
        self.menu_e__art_products____ers_lava_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_xpu.jpg'
        self.menu_e__art_products____s_glazed_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_xpu.jpg'
        self.menu_e__art_products____s_glazed_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_cpu.jpg'
        self.menu_e__art_products____s_copper_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/copper_cpu.jpg'


class LprerenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = 'hscript'
        self.menu_python = 'python'


class PreframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_products_ox_mtlx_hf_test_out = 'E:/ART/PRODUCTS/OX-MTLX/hf_test_out'
        self.menu_d__minecraft_sub___ded_copper_sbsar = 'D:/Minecraft/substance/hazelnut_3/copper_block/grinded_copper.sbsar'
        self.menu_d__minecraft_sub___dirt_field_sbsar = 'D:/Minecraft/substance/hazelnut/farmland_wet/arid_dirt_field.sbsar'
        self.menu_e__art_products____ers_rock_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_cpu.jpg'
        self.menu_e__art_products____ers_rock_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_xpu.jpg'
        self.menu_e__art_products____rs_quilt_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_xpu.jpg'
        self.menu_e__art_products____rs_quilt_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_cpu.jpg'
        self.menu_e__art_products____ers_lava_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_cpu.jpg'
        self.menu_e__art_products____ers_lava_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_xpu.jpg'
        self.menu_e__art_products____s_glazed_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_xpu.jpg'
        self.menu_e__art_products____s_glazed_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_cpu.jpg'
        self.menu_e__art_products____s_copper_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/copper_cpu.jpg'


class LpreframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = 'hscript'
        self.menu_python = 'python'


class PostframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_products_ox_mtlx_hf_test_out = 'E:/ART/PRODUCTS/OX-MTLX/hf_test_out'
        self.menu_d__minecraft_sub___ded_copper_sbsar = 'D:/Minecraft/substance/hazelnut_3/copper_block/grinded_copper.sbsar'
        self.menu_d__minecraft_sub___dirt_field_sbsar = 'D:/Minecraft/substance/hazelnut/farmland_wet/arid_dirt_field.sbsar'
        self.menu_e__art_products____ers_rock_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_cpu.jpg'
        self.menu_e__art_products____ers_rock_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_xpu.jpg'
        self.menu_e__art_products____rs_quilt_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_xpu.jpg'
        self.menu_e__art_products____rs_quilt_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_cpu.jpg'
        self.menu_e__art_products____ers_lava_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_cpu.jpg'
        self.menu_e__art_products____ers_lava_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_xpu.jpg'
        self.menu_e__art_products____s_glazed_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_xpu.jpg'
        self.menu_e__art_products____s_glazed_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_cpu.jpg'
        self.menu_e__art_products____s_copper_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/copper_cpu.jpg'


class LpostframeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = 'hscript'
        self.menu_python = 'python'


class PostrenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_e__art_products_ox_mtlx_hf_test_out = 'E:/ART/PRODUCTS/OX-MTLX/hf_test_out'
        self.menu_d__minecraft_sub___ded_copper_sbsar = 'D:/Minecraft/substance/hazelnut_3/copper_block/grinded_copper.sbsar'
        self.menu_d__minecraft_sub___dirt_field_sbsar = 'D:/Minecraft/substance/hazelnut/farmland_wet/arid_dirt_field.sbsar'
        self.menu_e__art_products____ers_rock_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_cpu.jpg'
        self.menu_e__art_products____ers_rock_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/rock_xpu.jpg'
        self.menu_e__art_products____rs_quilt_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_xpu.jpg'
        self.menu_e__art_products____rs_quilt_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/quilt_cpu.jpg'
        self.menu_e__art_products____ers_lava_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_cpu.jpg'
        self.menu_e__art_products____ers_lava_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/lava_xpu.jpg'
        self.menu_e__art_products____s_glazed_xpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_xpu.jpg'
        self.menu_e__art_products____s_glazed_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/glazed_cpu.jpg'
        self.menu_e__art_products____s_copper_cpu_jpg = 'E:/ART/PRODUCTS/OX-MTLX/renders/copper_cpu.jpg'


class LpostrenderMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_hscript = 'hscript'
        self.menu_python = 'python'



