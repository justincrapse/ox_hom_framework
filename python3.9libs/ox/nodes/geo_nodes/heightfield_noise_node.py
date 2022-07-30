from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldNoiseNode(OXNode):
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
        self.parm_layer = Parameter(parm=self.node.parm('layer'))
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
        self.parm_combine = CombineMenu(parm=self.node.parm('combine'))
        self.parm_basis = BasisMenu(parm=self.node.parm('basis'))
        self.parm_fractal = FractalMenu(parm=self.node.parm('fractal'))


        # input vars:
        self.input_terrain = 'Terrain'
        self.input_mask = 'Mask'


# parm menu classes:
class CombineMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace = "replace"
        self.menu_add = "add"
        self.menu_subtract = "subtract"
        self.menu_difference = "diff"
        self.menu_multiply = "multiply"
        self.menu_maximum = "max"
        self.menu_minimum = "min"
        self.menu_blend = "blend"


class BasisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_sinusoid = "sine"
        self.menu_perlin = "perlin"
        self.menu_periodic_perlin = "pperlin"
        self.menu_simplex = "simplex"
        self.menu_sparse_convolution = "sparse"
        self.menu_perlin_flow = "flow"
        self.menu_periodic_perlin_flow = "pflow"
        self.menu_worley_cellular_f1 = "worleyFA"
        self.menu_worley_cellular_f2_f1 = "worleyFB"
        self.menu_manhattan_cellular_f1 = "mworleyFA"
        self.menu_manhattan_cellular_f2_f1 = "mworleyFB"
        self.menu_chebyshev_cellular_f1 = "cworleyFA"
        self.menu_chebyshev_cellular_f2_f1 = "cworleyFB"
        self.menu_alligator = "alligator"


class FractalMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_none = "none"
        self.menu_standard__fbm_ = "fBm"
        self.menu_terrain = "mfT"
        self.menu_hybrid_terrain = "hmfT"



