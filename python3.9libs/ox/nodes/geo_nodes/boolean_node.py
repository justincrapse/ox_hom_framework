from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class BooleanNode(OXNode):
    node_type = 'boolean::2.0'
    parm_lookup_dict = {'inputa': 'inputa', 'agroup': 'agroup', 'asurface': 'asurface', 'resolvea': 'resolvea', 'inputb': 'inputb', 'bgroup': 'bgroup', 'bsurface': 'bsurface', 'resolveb': 'resolveb', 'output': 'output', 'booleanop': 'booleanop', 'subtractchoices': 'subtractchoices', 'shatterchoices': 'shatterchoices', 'opencurvesonly': 'opencurvesonly', 'generateaaseams': 'generateaaseams', 'generatebbseams': 'generatebbseams', 'generateabseams': 'generateabseams', 'adepth1': 'adepth1', 'adepth2': 'adepth2', 'bdepth1': 'bdepth1', 'bdepth2': 'bdepth2', 'windingop': 'windingop', 'mergenbrs': 'mergenbrs', 'detriangulate': 'detriangulate', 'removeinlinepoints': 'removeinlinepoints', 'uniqueseams': 'uniqueseams', 'correctnormals': 'correctnormals', 'useaxapolys': 'useaxapolys', 'axapolys': 'axapolys', 'useaxbpolys': 'useaxbpolys', 'axbpolys': 'axbpolys', 'useaxalist': 'useaxalist', 'axalist': 'axalist', 'useaxblist': 'useaxblist', 'axblist': 'axblist', 'collapsetinyedges': 'collapsetinyedges', 'lengththreshold': 'lengththreshold', 'outputprimgroups': 'outputprimgroups', 'useapolys': 'useapolys', 'apolys': 'apolys', 'useainsideb': 'useainsideb', 'ainsideb': 'ainsideb', 'useaoutsideb': 'useaoutsideb', 'aoutsideb': 'aoutsideb', 'usebpolys': 'usebpolys', 'bpolys': 'bpolys', 'usebinsidea': 'usebinsidea', 'binsidea': 'binsidea', 'useboutsidea': 'useboutsidea', 'boutsidea': 'boutsidea', 'useaboverlap': 'useaboverlap', 'aboverlap': 'aboverlap', 'useaonlypieces': 'useaonlypieces', 'aonlypieces': 'aonlypieces', 'usebonlypieces': 'usebonlypieces', 'bonlypieces': 'bonlypieces', 'useabpieces': 'useabpieces', 'abpieces': 'abpieces', 'usereversedpolys': 'usereversedpolys', 'reversedpolys': 'reversedpolys', 'outputedgegroups': 'outputedgegroups', 'useaaseamedges': 'useaaseamedges', 'aaseamedges': 'aaseamedges', 'usebbseamedges': 'usebbseamedges', 'bbseamedges': 'bbseamedges', 'useabseamedges': 'useabseamedges', 'abseamedges': 'abseamedges'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_inputa = Parameter(parm=self.node.parm('inputa'))
        self.parm_resolvea = Parameter(parm=self.node.parm('resolvea'))
        self.parm_inputb = Parameter(parm=self.node.parm('inputb'))
        self.parm_bgroup = Parameter(parm=self.node.parm('bgroup'))
        self.parm_resolveb = Parameter(parm=self.node.parm('resolveb'))
        self.parm_output = Parameter(parm=self.node.parm('output'))
        self.parm_opencurvesonly = Parameter(parm=self.node.parm('opencurvesonly'))
        self.parm_generateaaseams = Parameter(parm=self.node.parm('generateaaseams'))
        self.parm_generatebbseams = Parameter(parm=self.node.parm('generatebbseams'))
        self.parm_generateabseams = Parameter(parm=self.node.parm('generateabseams'))
        self.parm_adepth1 = Parameter(parm=self.node.parm('adepth1'))
        self.parm_adepth2 = Parameter(parm=self.node.parm('adepth2'))
        self.parm_bdepth1 = Parameter(parm=self.node.parm('bdepth1'))
        self.parm_bdepth2 = Parameter(parm=self.node.parm('bdepth2'))
        self.parm_mergenbrs = Parameter(parm=self.node.parm('mergenbrs'))
        self.parm_removeinlinepoints = Parameter(parm=self.node.parm('removeinlinepoints'))
        self.parm_uniqueseams = Parameter(parm=self.node.parm('uniqueseams'))
        self.parm_correctnormals = Parameter(parm=self.node.parm('correctnormals'))
        self.parm_useaxapolys = Parameter(parm=self.node.parm('useaxapolys'))
        self.parm_axapolys = Parameter(parm=self.node.parm('axapolys'))
        self.parm_useaxbpolys = Parameter(parm=self.node.parm('useaxbpolys'))
        self.parm_axbpolys = Parameter(parm=self.node.parm('axbpolys'))
        self.parm_useaxalist = Parameter(parm=self.node.parm('useaxalist'))
        self.parm_axalist = Parameter(parm=self.node.parm('axalist'))
        self.parm_useaxblist = Parameter(parm=self.node.parm('useaxblist'))
        self.parm_axblist = Parameter(parm=self.node.parm('axblist'))
        self.parm_collapsetinyedges = Parameter(parm=self.node.parm('collapsetinyedges'))
        self.parm_lengththreshold = Parameter(parm=self.node.parm('lengththreshold'))
        self.parm_outputprimgroups = Parameter(parm=self.node.parm('outputprimgroups'))
        self.parm_useapolys = Parameter(parm=self.node.parm('useapolys'))
        self.parm_apolys = Parameter(parm=self.node.parm('apolys'))
        self.parm_useainsideb = Parameter(parm=self.node.parm('useainsideb'))
        self.parm_ainsideb = Parameter(parm=self.node.parm('ainsideb'))
        self.parm_useaoutsideb = Parameter(parm=self.node.parm('useaoutsideb'))
        self.parm_aoutsideb = Parameter(parm=self.node.parm('aoutsideb'))
        self.parm_usebpolys = Parameter(parm=self.node.parm('usebpolys'))
        self.parm_bpolys = Parameter(parm=self.node.parm('bpolys'))
        self.parm_usebinsidea = Parameter(parm=self.node.parm('usebinsidea'))
        self.parm_binsidea = Parameter(parm=self.node.parm('binsidea'))
        self.parm_useboutsidea = Parameter(parm=self.node.parm('useboutsidea'))
        self.parm_boutsidea = Parameter(parm=self.node.parm('boutsidea'))
        self.parm_useaboverlap = Parameter(parm=self.node.parm('useaboverlap'))
        self.parm_aboverlap = Parameter(parm=self.node.parm('aboverlap'))
        self.parm_useaonlypieces = Parameter(parm=self.node.parm('useaonlypieces'))
        self.parm_aonlypieces = Parameter(parm=self.node.parm('aonlypieces'))
        self.parm_usebonlypieces = Parameter(parm=self.node.parm('usebonlypieces'))
        self.parm_bonlypieces = Parameter(parm=self.node.parm('bonlypieces'))
        self.parm_useabpieces = Parameter(parm=self.node.parm('useabpieces'))
        self.parm_abpieces = Parameter(parm=self.node.parm('abpieces'))
        self.parm_usereversedpolys = Parameter(parm=self.node.parm('usereversedpolys'))
        self.parm_reversedpolys = Parameter(parm=self.node.parm('reversedpolys'))
        self.parm_outputedgegroups = Parameter(parm=self.node.parm('outputedgegroups'))
        self.parm_useaaseamedges = Parameter(parm=self.node.parm('useaaseamedges'))
        self.parm_aaseamedges = Parameter(parm=self.node.parm('aaseamedges'))
        self.parm_usebbseamedges = Parameter(parm=self.node.parm('usebbseamedges'))
        self.parm_bbseamedges = Parameter(parm=self.node.parm('bbseamedges'))
        self.parm_useabseamedges = Parameter(parm=self.node.parm('useabseamedges'))
        self.parm_abseamedges = Parameter(parm=self.node.parm('abseamedges'))

        
        # parm menu vars:
        self.parm_agroup = AgroupMenu(parm=self.node.parm('agroup'))
        self.parm_asurface = AsurfaceMenu(parm=self.node.parm('asurface'))
        self.parm_bsurface = BsurfaceMenu(parm=self.node.parm('bsurface'))
        self.parm_booleanop = BooleanopMenu(parm=self.node.parm('booleanop'))
        self.parm_subtractchoices = SubtractchoicesMenu(parm=self.node.parm('subtractchoices'))
        self.parm_shatterchoices = ShatterchoicesMenu(parm=self.node.parm('shatterchoices'))
        self.parm_windingop = WindingopMenu(parm=self.node.parm('windingop'))
        self.parm_detriangulate = DetriangulateMenu(parm=self.node.parm('detriangulate'))


        # input vars:
        self.input_geometry_a = 'Geometry A'
        self.input_geometry_b = 'Geometry B'


# parm menu classes:
class AgroupMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu__name = ("", 0)
        self.menu_height = ("@name=height", 1)


class AsurfaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_solid = ("solid", 0)
        self.menu_surface = ("surface", 1)


class BsurfaceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_solid = ("solid", 0)
        self.menu_surface = ("surface", 1)


class BooleanopMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_union = ("union", 0)
        self.menu_intersect = ("intersect", 1)
        self.menu_subtract = ("subtract", 2)
        self.menu_shatter = ("shatter", 3)
        self.menu_custom = ("custom", 4)
        self.menu__separator_ = ("_separator_", 5)
        self.menu_seam = ("seam", 6)
        self.menu__separator_ = ("_separator_", 7)
        self.menu_detect = ("detect", 8)
        self.menu_resolve = ("resolve", 9)


class SubtractchoicesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_a___b = ("aminusb", 0)
        self.menu_b___a = ("bminusa", 1)
        self.menu_both = ("both", 2)


class ShatterchoicesMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_pieces_of_a = ("apieces", 0)
        self.menu_pieces_of_b = ("bpieces", 1)
        self.menu_both = ("both", 2)


class WindingopMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_a_range = ("arange", 0)
        self.menu_b_range = ("brange", 1)
        self.menu_both = ("and", 2)
        self.menu_at_least_one = ("or", 3)
        self.menu_exactly_one = ("xor", 4)


class DetriangulateMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_no_polygons = ("none", 0)
        self.menu_only_unchanged_polygons = ("unchanged", 1)
        self.menu_all_polygons = ("all", 2)



