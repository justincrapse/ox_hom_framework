from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu

# node class version: 0.1


class AttribfrompiecesNode(OXNode):
    node_type = "attribfrompieces"
    parm_lookup_dict = {
        "pieceattrib": "pieceattrib",
        "piecefilter": "piecefilter",
        "mode": "mode",
        "copyattrib": "copyattrib",
        "copyp": "copyp",
        "copymethod": "copymethod",
        "piecesfolder": "piecesfolder",
        "shuffle": "shuffle",
        "seed": "seed",
        "offset": "offset",
        "sourcepointsfolder": "sourcepointsfolder",
        "overrideptnum": "overrideptnum",
        "ptnumattrib": "ptnumattrib",
        "locattrib": "locattrib",
        "patchesfolder": "patchesfolder",
        "patchsize": "patchsize",
        "patchscalex": "patchscalex",
        "patchscaley": "patchscaley",
        "patchscalez": "patchscalez",
        "patchoffsetx": "patchoffsetx",
        "patchoffsety": "patchoffsety",
        "patchoffsetz": "patchoffsetz",
        "worleydistortion": "worleydistortion",
        "distortstrength": "distortstrength",
        "distortsize": "distortsize",
        "worleyrough": "worleyrough",
        "distortoffsetx": "distortoffsetx",
        "distortoffsety": "distortoffsety",
        "distortoffsetz": "distortoffsetz",
        "noisefolder2": "noisefolder2",
        "noisebasis": "noisebasis",
        "noiseelementsize": "noiseelementsize",
        "noiseelementscalex": "noiseelementscalex",
        "noiseelementscaley": "noiseelementscaley",
        "noiseelementscalez": "noiseelementscalez",
        "offset2x": "offset2x",
        "offset2y": "offset2y",
        "offset2z": "offset2z",
        "noiseoct": "noiseoct",
        "noiserough": "noiserough",
        "noisedistortion": "noisedistortion",
        "disp": "disp",
        "dispfreq": "dispfreq",
        "gflow": "gflow",
        "noiseremap": "noiseremap",
        "randomfolder": "randomfolder",
        "weightmethod": "weightmethod",
        "randomseed": "randomseed",
        "autofillnamernd": "autofillnamernd",
        "numval": "numval",
        "weightattrib": "weightattrib",
        "folder0": "folder0",
        "attrib": "attrib",
        "attribtype": "attribtype",
        "mappiecesfrom": "mappiecesfrom",
        "autofillnamestring": "autofillnamestring",
        "nummaps": "nummaps",
        "autofillnamenumeric": "autofillnamenumeric",
        "numranges": "numranges",
        "attribunmatchedpiece": "attribunmatchedpiece",
        "useattribunmatchedgroup": "useattribunmatchedgroup",
        "attribunmatchedgroup": "attribunmatchedgroup",
        "seedmapattrib": "seedmapattrib",
        "vexfolder": "vexfolder",
        "autofillnamevex": "autofillnamevex",
        "numvex": "numvex",
        "vexunmatchedpiece": "vexunmatchedpiece",
        "usevexunmatchedgroup": "usevexunmatchedgroup",
        "vexunmatchedgroup": "vexunmatchedgroup",
        "seedvex": "seedvex",
        "noiseremap1pos": "noiseremap1pos",
        "noiseremap1value": "noiseremap1value",
        "noiseremap1interp": "noiseremap1interp",
        "noiseremap2pos": "noiseremap2pos",
        "noiseremap2value": "noiseremap2value",
        "noiseremap2interp": "noiseremap2interp",
    }

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(
                node_type_name=self.node_type, node_name=node_name
            )
        self.node_name = self.node.name()
        super().__init__(node=self.node)

        # parm vars:
        self.parm_pieceattrib = Parameter(parm=self.node.parm("pieceattrib"))
        self.parm_piecefilter = Parameter(parm=self.node.parm("piecefilter"))
        self.parm_copyattrib = Parameter(parm=self.node.parm("copyattrib"))
        self.parm_copyp = Parameter(parm=self.node.parm("copyp"))
        self.parm_piecesfolder = Parameter(parm=self.node.parm("piecesfolder"))
        self.parm_shuffle = Parameter(parm=self.node.parm("shuffle"))
        self.parm_seed = Parameter(parm=self.node.parm("seed"))
        self.parm_offset = Parameter(parm=self.node.parm("offset"))
        self.parm_sourcepointsfolder = Parameter(
            parm=self.node.parm("sourcepointsfolder")
        )
        self.parm_overrideptnum = Parameter(parm=self.node.parm("overrideptnum"))
        self.parm_ptnumattrib = Parameter(parm=self.node.parm("ptnumattrib"))
        self.parm_locattrib = Parameter(parm=self.node.parm("locattrib"))
        self.parm_patchesfolder = Parameter(parm=self.node.parm("patchesfolder"))
        self.parm_patchsize = Parameter(parm=self.node.parm("patchsize"))
        self.parm_patchscalex = Parameter(parm=self.node.parm("patchscalex"))
        self.parm_patchscaley = Parameter(parm=self.node.parm("patchscaley"))
        self.parm_patchscalez = Parameter(parm=self.node.parm("patchscalez"))
        self.parm_patchoffsetx = Parameter(parm=self.node.parm("patchoffsetx"))
        self.parm_patchoffsety = Parameter(parm=self.node.parm("patchoffsety"))
        self.parm_patchoffsetz = Parameter(parm=self.node.parm("patchoffsetz"))
        self.parm_worleydistortion = Parameter(parm=self.node.parm("worleydistortion"))
        self.parm_distortstrength = Parameter(parm=self.node.parm("distortstrength"))
        self.parm_distortsize = Parameter(parm=self.node.parm("distortsize"))
        self.parm_worleyrough = Parameter(parm=self.node.parm("worleyrough"))
        self.parm_distortoffsetx = Parameter(parm=self.node.parm("distortoffsetx"))
        self.parm_distortoffsety = Parameter(parm=self.node.parm("distortoffsety"))
        self.parm_distortoffsetz = Parameter(parm=self.node.parm("distortoffsetz"))
        self.parm_noisefolder2 = Parameter(parm=self.node.parm("noisefolder2"))
        self.parm_noiseelementsize = Parameter(parm=self.node.parm("noiseelementsize"))
        self.parm_noiseelementscalex = Parameter(
            parm=self.node.parm("noiseelementscalex")
        )
        self.parm_noiseelementscaley = Parameter(
            parm=self.node.parm("noiseelementscaley")
        )
        self.parm_noiseelementscalez = Parameter(
            parm=self.node.parm("noiseelementscalez")
        )
        self.parm_offset2x = Parameter(parm=self.node.parm("offset2x"))
        self.parm_offset2y = Parameter(parm=self.node.parm("offset2y"))
        self.parm_offset2z = Parameter(parm=self.node.parm("offset2z"))
        self.parm_noiseoct = Parameter(parm=self.node.parm("noiseoct"))
        self.parm_noiserough = Parameter(parm=self.node.parm("noiserough"))
        self.parm_noisedistortion = Parameter(parm=self.node.parm("noisedistortion"))
        self.parm_disp = Parameter(parm=self.node.parm("disp"))
        self.parm_dispfreq = Parameter(parm=self.node.parm("dispfreq"))
        self.parm_gflow = Parameter(parm=self.node.parm("gflow"))
        self.parm_noiseremap = Parameter(parm=self.node.parm("noiseremap"))
        self.parm_randomfolder = Parameter(parm=self.node.parm("randomfolder"))
        self.parm_randomseed = Parameter(parm=self.node.parm("randomseed"))
        self.parm_autofillnamernd = Parameter(parm=self.node.parm("autofillnamernd"))
        self.parm_numval = Parameter(parm=self.node.parm("numval"))
        self.parm_weightattrib = Parameter(parm=self.node.parm("weightattrib"))
        self.parm_folder0 = Parameter(parm=self.node.parm("folder0"))
        self.parm_attrib = Parameter(parm=self.node.parm("attrib"))
        self.parm_autofillnamestring = Parameter(
            parm=self.node.parm("autofillnamestring")
        )
        self.parm_nummaps = Parameter(parm=self.node.parm("nummaps"))
        self.parm_autofillnamenumeric = Parameter(
            parm=self.node.parm("autofillnamenumeric")
        )
        self.parm_numranges = Parameter(parm=self.node.parm("numranges"))
        self.parm_attribunmatchedpiece = Parameter(
            parm=self.node.parm("attribunmatchedpiece")
        )
        self.parm_useattribunmatchedgroup = Parameter(
            parm=self.node.parm("useattribunmatchedgroup")
        )
        self.parm_attribunmatchedgroup = Parameter(
            parm=self.node.parm("attribunmatchedgroup")
        )
        self.parm_seedmapattrib = Parameter(parm=self.node.parm("seedmapattrib"))
        self.parm_vexfolder = Parameter(parm=self.node.parm("vexfolder"))
        self.parm_autofillnamevex = Parameter(parm=self.node.parm("autofillnamevex"))
        self.parm_numvex = Parameter(parm=self.node.parm("numvex"))
        self.parm_vexunmatchedpiece = Parameter(
            parm=self.node.parm("vexunmatchedpiece")
        )
        self.parm_usevexunmatchedgroup = Parameter(
            parm=self.node.parm("usevexunmatchedgroup")
        )
        self.parm_vexunmatchedgroup = Parameter(
            parm=self.node.parm("vexunmatchedgroup")
        )
        self.parm_seedvex = Parameter(parm=self.node.parm("seedvex"))
        self.parm_noiseremap1pos = Parameter(parm=self.node.parm("noiseremap1pos"))
        self.parm_noiseremap1value = Parameter(parm=self.node.parm("noiseremap1value"))
        self.parm_noiseremap2pos = Parameter(parm=self.node.parm("noiseremap2pos"))
        self.parm_noiseremap2value = Parameter(parm=self.node.parm("noiseremap2value"))

        # parm menu vars:
        self.parm_mode = ModeMenu(parm=self.node.parm("mode"))
        self.parm_copymethod = CopymethodMenu(parm=self.node.parm("copymethod"))
        self.parm_noisebasis = NoisebasisMenu(parm=self.node.parm("noisebasis"))
        self.parm_weightmethod = WeightmethodMenu(parm=self.node.parm("weightmethod"))
        self.parm_attribtype = AttribtypeMenu(parm=self.node.parm("attribtype"))
        self.parm_mappiecesfrom = MappiecesfromMenu(
            parm=self.node.parm("mappiecesfrom")
        )
        self.parm_noiseremap1interp = Noiseremap1InterpMenu(
            parm=self.node.parm("noiseremap1interp")
        )
        self.parm_noiseremap2interp = Noiseremap2InterpMenu(
            parm=self.node.parm("noiseremap2interp")
        )

        # input vars:
        self.input_point_cloud = "Point Cloud"
        self.input_geometry_library = "Geometry Library"


# parm menu classes:
class ModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_cycle = ("cycle", 0)
        self.menu_patches = ("worley", 1)
        self.menu_noise = ("noise", 2)
        self.menu_random = ("random", 3)
        self.menu_map_attribute = ("attrib", 4)
        self.menu_vexpression = ("vex", 5)


class CopymethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_maximum = ("max", 0)
        self.menu_minimum = ("min", 1)
        self.menu_average = ("mean", 2)
        self.menu_mode = ("mode", 3)
        self.menu_median = ("median", 4)
        self.menu_sum = ("sum", 5)
        self.menu_sum_of_squares = ("sumsquare", 6)
        self.menu_root_mean_square = ("rms", 7)
        self.menu_first_match = ("first", 8)
        self.menu_last_match = ("last", 9)
        self.menu_array_of_all = ("array", 10)


class NoisebasisMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_fast = ("value_fast", 0)
        self.menu_sparse_convolution = ("sparse", 1)
        self.menu_alligator = ("alligator", 2)
        self.menu_perlin = ("perlin", 3)
        self.menu_perlin_flow = ("flow", 4)
        self.menu_simplex = ("simplex", 5)
        self.menu_worley_cellular_f1 = ("worleyFA", 6)
        self.menu_worley_cellular_f2_f1 = ("worleyFB", 7)
        self.menu_manhattan_cellular_f1 = ("mworleyFA", 8)
        self.menu_manhattan_cellular_f2_f1 = ("mworleyFB", 9)
        self.menu_chebyshev_cellular_f1 = ("cworleyFA", 10)
        self.menu_chebyshev_cellular_f2_f1 = ("cworleyFB", 11)


class WeightmethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uniform_distribution = ("uniform", 0)
        self.menu_piece_weights = ("weights", 1)
        self.menu_weight_attribute = ("attrib", 2)


class AttribtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_numeric = ("number", 0)
        self.menu_string = ("string", 1)


class MappiecesfromMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_automatic_ranges = ("auto", 0)
        self.menu_explicit_range = ("explicit", 1)


class Noiseremap1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_linear = ("linear", 1)
        self.menu_catmull_rom = ("catmull-rom", 2)
        self.menu_monotone_cubic = ("monotonecubic", 3)
        self.menu_bezier = ("bezier", 4)
        self.menu_b_spline = ("bspline", 5)
        self.menu_hermite = ("hermite", 6)


class Noiseremap2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = ("constant", 0)
        self.menu_linear = ("linear", 1)
        self.menu_catmull_rom = ("catmull-rom", 2)
        self.menu_monotone_cubic = ("monotonecubic", 3)
        self.menu_bezier = ("bezier", 4)
        self.menu_b_spline = ("bspline", 5)
        self.menu_hermite = ("hermite", 6)
