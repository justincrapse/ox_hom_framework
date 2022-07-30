from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldMasknoiseNode(OXNode):
    node_type = 'heightfield_noise'
    parm_lookup_dict = {'layer': 'layer', 'masklayer': 'masklayer', 'combine': 'combine', 'blend': 'blend', 'centernoise': 'centernoise', 'amp': 'amp', 'elementsize': 'elementsize', 'elementscalex': 'elementscalex', 'elementscaley': 'elementscaley', 'elementscalez': 'elementscalez', 'offsetx': 'offsetx', 'offsety': 'offsety', 'offsetz': 'offsetz', 'noise': 'noise', 'basis': 'basis', 'fractal': 'fractal', 'periodx': 'periodx', 'periody': 'periody', 'periodz': 'periodz', 'oct': 'oct', 'lac': 'lac', 'rough': 'rough', 'flowrot': 'flowrot', 'output': 'output', 'fold': 'fold', 'complement': 'complement', 'dogain': 'dogain', 'gain': 'gain', 'dobias': 'dobias', 'bias': 'bias', 'clipping': 'Clipping', 'clipmin': 'clipmin', 'clipmax': 'clipmax', 'distortion': 'distortion', 'latticewarp': 'latticewarp', 'dolwarp': 'dolwarp', 'accuml': 'accuml', 'disp': 'disp', 'dispfreq': 'dispfreq', 'folder1': 'folder1', 'dogwarp': 'dogwarp', 'accumg': 'accumg', 'gflow': 'gflow'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_masklayer = Parameter(parm=self.node.parm('masklayer'))
        self.parm_blend = Parameter(parm=self.node.parm('blend'))
        self.parm_centernoise = Parameter(parm=self.node.parm('centernoise'))
        self.parm_amp = Parameter(parm=self.node.parm('amp'))
        self.parm_elementsize = Parameter(parm=self.node.parm('elementsize'))
        self.parm_elementscalex = Parameter(parm=self.node.parm('elementscalex'))
        self.parm_elementscaley = Parameter(parm=self.node.parm('elementscaley'))
        self.parm_elementscalez = Parameter(parm=self.node.parm('elementscalez'))
        self.parm_offsetx = Parameter(parm=self.node.parm('offsetx'))
        self.parm_offsety = Parameter(parm=self.node.parm('offsety'))
        self.parm_offsetz = Parameter(parm=self.node.parm('offsetz'))
        self.parm_noise = Parameter(parm=self.node.parm('noise'))
        self.parm_periodx = Parameter(parm=self.node.parm('periodx'))
        self.parm_periody = Parameter(parm=self.node.parm('periody'))
        self.parm_periodz = Parameter(parm=self.node.parm('periodz'))
        self.parm_oct = Parameter(parm=self.node.parm('oct'))
        self.parm_lac = Parameter(parm=self.node.parm('lac'))
        self.parm_rough = Parameter(parm=self.node.parm('rough'))
        self.parm_flowrot = Parameter(parm=self.node.parm('flowrot'))
        self.parm_output = Parameter(parm=self.node.parm('output'))
        self.parm_fold = Parameter(parm=self.node.parm('fold'))
        self.parm_complement = Parameter(parm=self.node.parm('complement'))
        self.parm_dogain = Parameter(parm=self.node.parm('dogain'))
        self.parm_gain = Parameter(parm=self.node.parm('gain'))
        self.parm_dobias = Parameter(parm=self.node.parm('dobias'))
        self.parm_bias = Parameter(parm=self.node.parm('bias'))
        self.parm_clipping = Parameter(parm=self.node.parm('Clipping'))
        self.parm_clipmin = Parameter(parm=self.node.parm('clipmin'))
        self.parm_clipmax = Parameter(parm=self.node.parm('clipmax'))
        self.parm_distortion = Parameter(parm=self.node.parm('distortion'))
        self.parm_latticewarp = Parameter(parm=self.node.parm('latticewarp'))
        self.parm_dolwarp = Parameter(parm=self.node.parm('dolwarp'))
        self.parm_accuml = Parameter(parm=self.node.parm('accuml'))
        self.parm_disp = Parameter(parm=self.node.parm('disp'))
        self.parm_dispfreq = Parameter(parm=self.node.parm('dispfreq'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_dogwarp = Parameter(parm=self.node.parm('dogwarp'))
        self.parm_accumg = Parameter(parm=self.node.parm('accumg'))
        self.parm_gflow = Parameter(parm=self.node.parm('gflow'))

        
        # parm menu vars:
        self.parm_layer = LayerMenu(parm=self.node.parm('layer'))
        self.parm_combine = CombineMenu(parm=self.node.parm('combine'))
        self.parm_basis = BasisMenu(parm=self.node.parm('basis'))
        self.parm_fractal = FractalMenu(parm=self.node.parm('fractal'))


        # input vars:
        self.input_terrain = 0
        self.input_mask = 1


# parm menu classes:
class LayerMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_height = 0
        self.menu_mask = 1


class CombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = 0
        self.menu_add = 1
        self.menu_subtract = 2
        self.menu_difference = 3
        self.menu_multiply = 4
        self.menu_maximum = 5
        self.menu_minimum = 6
        self.menu_blend = 7


class BasisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_sinusoid = 0
        self.menu_perlin = 1
        self.menu_periodic_perlin = 2
        self.menu_simplex__improved_perlin_ = 3
        self.menu_sparse_convolution = 4
        self.menu_flow = 5
        self.menu_periodic_flow = 6
        self.menu_worley__cellular__f1 = 7
        self.menu_worley__cellular__f2_f1 = 8
        self.menu_manhattan_worley__cellular__f1 = 9
        self.menu_manhattan_worley__cellular__f2_f1 = 10
        self.menu_chebyshev_worley__cellular__f1 = 11
        self.menu_chebyshev_worley__cellular__f2_f1 = 12
        self.menu_alligator = 13


class FractalMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = 0
        self.menu_standard__fbm_ = 1
        self.menu_terrain = 2
        self.menu_hybrid_terrain = 3



