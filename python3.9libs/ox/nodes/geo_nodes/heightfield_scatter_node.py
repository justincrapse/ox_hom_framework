from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldScatterNode(OXNode):
    node_type = 'heightfield_scatter::2.0'
    parm_lookup_dict = {'tag': 'tag', 'scattermethod': 'scattermethod', 'folder1': 'folder1', 'layer': 'layer', 'coverage': 'coverage', 'density': 'density', 'totalpointcount': 'totalpointcount', 'sourcetag': 'sourcetag', 'perpointcount_method': 'perpointcount_method', 'perpointcount_exactnumber': 'perpointcount_exactnumber', 'perpointcount_poissonrangemin': 'perpointcount_poissonrangemin', 'perpointcount_poissonrangemax': 'perpointcount_poissonrangemax', 'positioning_method': 'positioning_method', 'positioning_originmin': 'positioning_originmin', 'positioning_originmax': 'positioning_originmax', 'positioning_offsetmin': 'positioning_offsetmin', 'positioning_offsetmax': 'positioning_offsetmax', 'positioning_ratiomin': 'positioning_ratiomin', 'positioning_ratiomax': 'positioning_ratiomax', 'outerradius': 'outerradius', 'falloff': 'falloff', 'folder2': 'folder2', 'variability_method': 'variability_method', 'variability_exactscale': 'variability_exactscale', 'variability_unifromrangemin': 'variability_unifromrangemin', 'variability_unifromrangemax': 'variability_unifromrangemax', 'variability_normalrangemin': 'variability_normalrangemin', 'variability_normalrangemax': 'variability_normalrangemax', 'variability_normalspread': 'variability_normalspread', 'folder0': 'folder0', 'relax_points': 'relax_points', 'relax_selfoverlap': 'relax_selfoverlap', 'relax_avoidtag': 'relax_avoidtag', 'relax_maskcutoff': 'relax_maskcutoff', 'relax_iterations': 'relax_iterations', 'relax_removingrate': 'relax_removingrate', 'relax_stepratio': 'relax_stepratio', 'relax_allowoutofbounds': 'relax_allowoutofbounds', 'relax_pointremovalmethod': 'relax_pointremovalmethod', 'keepscatterpoints': 'keepscatterpoints', 'keepterrain': 'keepterrain', 'matchnormalterrain': 'matchnormalterrain', 'matchslopeterrain': 'matchslopeterrain', 'randomup': 'randomup', 'randomyaw': 'randomyaw', 'instancenewpoints': 'instancenewpoints', 'piecemode': 'piecemode', 'pieceattrib': 'pieceattrib', 'quant': 'quant', 'seed': 'seed', 'useemergencylimit': 'useemergencylimit', 'emergencylimit': 'emergencylimit'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_tag = Parameter(parm=self.node.parm('tag'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_layer = Parameter(parm=self.node.parm('layer'))
        self.parm_coverage = Parameter(parm=self.node.parm('coverage'))
        self.parm_density = Parameter(parm=self.node.parm('density'))
        self.parm_totalpointcount = Parameter(parm=self.node.parm('totalpointcount'))
        self.parm_sourcetag = Parameter(parm=self.node.parm('sourcetag'))
        self.parm_perpointcount_exactnumber = Parameter(parm=self.node.parm('perpointcount_exactnumber'))
        self.parm_perpointcount_poissonrangemin = Parameter(parm=self.node.parm('perpointcount_poissonrangemin'))
        self.parm_perpointcount_poissonrangemax = Parameter(parm=self.node.parm('perpointcount_poissonrangemax'))
        self.parm_positioning_originmin = Parameter(parm=self.node.parm('positioning_originmin'))
        self.parm_positioning_originmax = Parameter(parm=self.node.parm('positioning_originmax'))
        self.parm_positioning_offsetmin = Parameter(parm=self.node.parm('positioning_offsetmin'))
        self.parm_positioning_offsetmax = Parameter(parm=self.node.parm('positioning_offsetmax'))
        self.parm_positioning_ratiomin = Parameter(parm=self.node.parm('positioning_ratiomin'))
        self.parm_positioning_ratiomax = Parameter(parm=self.node.parm('positioning_ratiomax'))
        self.parm_outerradius = Parameter(parm=self.node.parm('outerradius'))
        self.parm_falloff = Parameter(parm=self.node.parm('falloff'))
        self.parm_folder2 = Parameter(parm=self.node.parm('folder2'))
        self.parm_variability_exactscale = Parameter(parm=self.node.parm('variability_exactscale'))
        self.parm_variability_unifromrangemin = Parameter(parm=self.node.parm('variability_unifromrangemin'))
        self.parm_variability_unifromrangemax = Parameter(parm=self.node.parm('variability_unifromrangemax'))
        self.parm_variability_normalrangemin = Parameter(parm=self.node.parm('variability_normalrangemin'))
        self.parm_variability_normalrangemax = Parameter(parm=self.node.parm('variability_normalrangemax'))
        self.parm_variability_normalspread = Parameter(parm=self.node.parm('variability_normalspread'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_relax_points = Parameter(parm=self.node.parm('relax_points'))
        self.parm_relax_selfoverlap = Parameter(parm=self.node.parm('relax_selfoverlap'))
        self.parm_relax_avoidtag = Parameter(parm=self.node.parm('relax_avoidtag'))
        self.parm_relax_maskcutoff = Parameter(parm=self.node.parm('relax_maskcutoff'))
        self.parm_relax_iterations = Parameter(parm=self.node.parm('relax_iterations'))
        self.parm_relax_removingrate = Parameter(parm=self.node.parm('relax_removingrate'))
        self.parm_relax_stepratio = Parameter(parm=self.node.parm('relax_stepratio'))
        self.parm_relax_allowoutofbounds = Parameter(parm=self.node.parm('relax_allowoutofbounds'))
        self.parm_keepscatterpoints = Parameter(parm=self.node.parm('keepscatterpoints'))
        self.parm_keepterrain = Parameter(parm=self.node.parm('keepterrain'))
        self.parm_matchnormalterrain = Parameter(parm=self.node.parm('matchnormalterrain'))
        self.parm_matchslopeterrain = Parameter(parm=self.node.parm('matchslopeterrain'))
        self.parm_randomup = Parameter(parm=self.node.parm('randomup'))
        self.parm_randomyaw = Parameter(parm=self.node.parm('randomyaw'))
        self.parm_instancenewpoints = Parameter(parm=self.node.parm('instancenewpoints'))
        self.parm_pieceattrib = Parameter(parm=self.node.parm('pieceattrib'))
        self.parm_quant = Parameter(parm=self.node.parm('quant'))
        self.parm_seed = Parameter(parm=self.node.parm('seed'))
        self.parm_useemergencylimit = Parameter(parm=self.node.parm('useemergencylimit'))
        self.parm_emergencylimit = Parameter(parm=self.node.parm('emergencylimit'))

        
        # parm menu vars:
        self.parm_scattermethod = ScattermethodMenu(parm=self.node.parm('scattermethod'))
        self.parm_perpointcount_method = PerpointcountMethodMenu(parm=self.node.parm('perpointcount_method'))
        self.parm_positioning_method = PositioningMethodMenu(parm=self.node.parm('positioning_method'))
        self.parm_variability_method = VariabilityMethodMenu(parm=self.node.parm('variability_method'))
        self.parm_relax_pointremovalmethod = RelaxPointremovalmethodMenu(parm=self.node.parm('relax_pointremovalmethod'))
        self.parm_piecemode = PiecemodeMenu(parm=self.node.parm('piecemode'))


        # input vars:
        self.input_terrain = 'Terrain'
        self.input_mask_or_scatter_points = 'Mask or Scatter Points'
        self.input_primitives_to_instance = 'Primitives to Instance'


# parm menu classes:
class ScattermethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_by_coverage_using_mask_layer = ("coverage", 0)
        self.menu_by_density_using_mask_layer = ("density", 1)
        self.menu_total_point_count_using_mask_layer = ("totalpointcount", 2)
        self.menu_per_point_count_using_source_points = ("perpointcount", 3)


class PerpointcountMethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_poisson_distribution = ("poissondist", 0)
        self.menu_exact_number = ("exactnumber", 1)


class PositioningMethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_offset = ("offset", 0)
        self.menu_origin = ("origin", 1)
        self.menu_ratio = ("ratio", 2)


class VariabilityMethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uniform_distribution = ("uniformdist", 0)
        self.menu_normal_distribution = ("normaldist", 1)
        self.menu_exact_scale = ("exactscale", 2)


class RelaxPointremovalmethodMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_only_flag = ("onlyflag", 0)
        self.menu_remove = ("remove", 1)


class PiecemodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_from_attribute = ("attribute", 0)
        self.menu_from_connectivity = ("connectivity", 1)
        self.menu_single_piece = ("single", 2)



