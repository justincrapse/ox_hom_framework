from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class HeightfieldMaskbyfeatureNode(OXNode):
    node_type = 'heightfield_maskbyfeature'
    parm_lookup_dict = {'folder31': 'folder31', 'smooth_radius': 'smooth_radius', 'combine': 'combine', 'blend': 'blend', 'invertmask': 'invertmask', 'folder1': 'folder1', 'maskbyslope': 'maskbyslope', 'min_slopeangle': 'min_slopeangle', 'max_slopeangle': 'max_slopeangle', 'sloperamp': 'sloperamp', 'folder2': 'folder2', 'maskbyheight': 'maskbyheight', 'computerange': 'computerange', 'minheight': 'minheight', 'maxheight': 'maxheight', 'heightramp': 'heightramp', 'folder4': 'folder4', 'maskbycurvature': 'maskbycurvature', 'computercurvature': 'computercurvature', 'max_curvature': 'max_curvature', 'curvatureramp': 'curvatureramp', 'folder0': 'folder0', 'maskbydir': 'maskbydir', 'goal_angle': 'goal_angle', 'angle_spread': 'angle_spread', 'dirramp': 'dirramp', 'folder5': 'folder5', 'maskbyocclusion': 'maskbyocclusion', 'minexposure': 'minexposure', 'maxexposure': 'maxexposure', 'ramp': 'ramp', 'folder6': 'folder6', 'viewdistance': 'viewdistance', 'stepscale': 'stepscale', 'numsearches': 'numsearches', 'heightlayer': 'heightlayer', 'masklayer': 'masklayer', 'sloperamp1pos': 'sloperamp1pos', 'sloperamp1value': 'sloperamp1value', 'sloperamp1interp': 'sloperamp1interp', 'sloperamp2pos': 'sloperamp2pos', 'sloperamp2value': 'sloperamp2value', 'sloperamp2interp': 'sloperamp2interp', 'sloperamp3pos': 'sloperamp3pos', 'sloperamp3value': 'sloperamp3value', 'sloperamp3interp': 'sloperamp3interp', 'sloperamp4pos': 'sloperamp4pos', 'sloperamp4value': 'sloperamp4value', 'sloperamp4interp': 'sloperamp4interp', 'heightramp1pos': 'heightramp1pos', 'heightramp1value': 'heightramp1value', 'heightramp1interp': 'heightramp1interp', 'heightramp2pos': 'heightramp2pos', 'heightramp2value': 'heightramp2value', 'heightramp2interp': 'heightramp2interp', 'heightramp3pos': 'heightramp3pos', 'heightramp3value': 'heightramp3value', 'heightramp3interp': 'heightramp3interp', 'heightramp4pos': 'heightramp4pos', 'heightramp4value': 'heightramp4value', 'heightramp4interp': 'heightramp4interp', 'curvatureramp1pos': 'curvatureramp1pos', 'curvatureramp1value': 'curvatureramp1value', 'curvatureramp1interp': 'curvatureramp1interp', 'curvatureramp2pos': 'curvatureramp2pos', 'curvatureramp2value': 'curvatureramp2value', 'curvatureramp2interp': 'curvatureramp2interp', 'curvatureramp3pos': 'curvatureramp3pos', 'curvatureramp3value': 'curvatureramp3value', 'curvatureramp3interp': 'curvatureramp3interp', 'curvatureramp4pos': 'curvatureramp4pos', 'curvatureramp4value': 'curvatureramp4value', 'curvatureramp4interp': 'curvatureramp4interp', 'dirramp1pos': 'dirramp1pos', 'dirramp1value': 'dirramp1value', 'dirramp1interp': 'dirramp1interp', 'dirramp2pos': 'dirramp2pos', 'dirramp2value': 'dirramp2value', 'dirramp2interp': 'dirramp2interp', 'dirramp3pos': 'dirramp3pos', 'dirramp3value': 'dirramp3value', 'dirramp3interp': 'dirramp3interp', 'dirramp4pos': 'dirramp4pos', 'dirramp4value': 'dirramp4value', 'dirramp4interp': 'dirramp4interp', 'ramp1pos': 'ramp1pos', 'ramp1value': 'ramp1value', 'ramp1interp': 'ramp1interp', 'ramp2pos': 'ramp2pos', 'ramp2value': 'ramp2value', 'ramp2interp': 'ramp2interp'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder31 = Parameter(parm=self.node.parm('folder31'))
        self.parm_smooth_radius = Parameter(parm=self.node.parm('smooth_radius'))
        self.parm_blend = Parameter(parm=self.node.parm('blend'))
        self.parm_invertmask = Parameter(parm=self.node.parm('invertmask'))
        self.parm_folder1 = Parameter(parm=self.node.parm('folder1'))
        self.parm_maskbyslope = Parameter(parm=self.node.parm('maskbyslope'))
        self.parm_min_slopeangle = Parameter(parm=self.node.parm('min_slopeangle'))
        self.parm_max_slopeangle = Parameter(parm=self.node.parm('max_slopeangle'))
        self.parm_sloperamp = Parameter(parm=self.node.parm('sloperamp'))
        self.parm_folder2 = Parameter(parm=self.node.parm('folder2'))
        self.parm_maskbyheight = Parameter(parm=self.node.parm('maskbyheight'))
        self.parm_computerange = Parameter(parm=self.node.parm('computerange'))
        self.parm_minheight = Parameter(parm=self.node.parm('minheight'))
        self.parm_maxheight = Parameter(parm=self.node.parm('maxheight'))
        self.parm_heightramp = Parameter(parm=self.node.parm('heightramp'))
        self.parm_folder4 = Parameter(parm=self.node.parm('folder4'))
        self.parm_maskbycurvature = Parameter(parm=self.node.parm('maskbycurvature'))
        self.parm_computercurvature = Parameter(parm=self.node.parm('computercurvature'))
        self.parm_max_curvature = Parameter(parm=self.node.parm('max_curvature'))
        self.parm_curvatureramp = Parameter(parm=self.node.parm('curvatureramp'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_maskbydir = Parameter(parm=self.node.parm('maskbydir'))
        self.parm_goal_angle = Parameter(parm=self.node.parm('goal_angle'))
        self.parm_angle_spread = Parameter(parm=self.node.parm('angle_spread'))
        self.parm_dirramp = Parameter(parm=self.node.parm('dirramp'))
        self.parm_folder5 = Parameter(parm=self.node.parm('folder5'))
        self.parm_maskbyocclusion = Parameter(parm=self.node.parm('maskbyocclusion'))
        self.parm_minexposure = Parameter(parm=self.node.parm('minexposure'))
        self.parm_maxexposure = Parameter(parm=self.node.parm('maxexposure'))
        self.parm_ramp = Parameter(parm=self.node.parm('ramp'))
        self.parm_folder6 = Parameter(parm=self.node.parm('folder6'))
        self.parm_viewdistance = Parameter(parm=self.node.parm('viewdistance'))
        self.parm_stepscale = Parameter(parm=self.node.parm('stepscale'))
        self.parm_numsearches = Parameter(parm=self.node.parm('numsearches'))
        self.parm_heightlayer = Parameter(parm=self.node.parm('heightlayer'))
        self.parm_masklayer = Parameter(parm=self.node.parm('masklayer'))
        self.parm_sloperamp1pos = Parameter(parm=self.node.parm('sloperamp1pos'))
        self.parm_sloperamp1value = Parameter(parm=self.node.parm('sloperamp1value'))
        self.parm_sloperamp2pos = Parameter(parm=self.node.parm('sloperamp2pos'))
        self.parm_sloperamp2value = Parameter(parm=self.node.parm('sloperamp2value'))
        self.parm_sloperamp3pos = Parameter(parm=self.node.parm('sloperamp3pos'))
        self.parm_sloperamp3value = Parameter(parm=self.node.parm('sloperamp3value'))
        self.parm_sloperamp4pos = Parameter(parm=self.node.parm('sloperamp4pos'))
        self.parm_sloperamp4value = Parameter(parm=self.node.parm('sloperamp4value'))
        self.parm_heightramp1pos = Parameter(parm=self.node.parm('heightramp1pos'))
        self.parm_heightramp1value = Parameter(parm=self.node.parm('heightramp1value'))
        self.parm_heightramp2pos = Parameter(parm=self.node.parm('heightramp2pos'))
        self.parm_heightramp2value = Parameter(parm=self.node.parm('heightramp2value'))
        self.parm_heightramp3pos = Parameter(parm=self.node.parm('heightramp3pos'))
        self.parm_heightramp3value = Parameter(parm=self.node.parm('heightramp3value'))
        self.parm_heightramp4pos = Parameter(parm=self.node.parm('heightramp4pos'))
        self.parm_heightramp4value = Parameter(parm=self.node.parm('heightramp4value'))
        self.parm_curvatureramp1pos = Parameter(parm=self.node.parm('curvatureramp1pos'))
        self.parm_curvatureramp1value = Parameter(parm=self.node.parm('curvatureramp1value'))
        self.parm_curvatureramp2pos = Parameter(parm=self.node.parm('curvatureramp2pos'))
        self.parm_curvatureramp2value = Parameter(parm=self.node.parm('curvatureramp2value'))
        self.parm_curvatureramp3pos = Parameter(parm=self.node.parm('curvatureramp3pos'))
        self.parm_curvatureramp3value = Parameter(parm=self.node.parm('curvatureramp3value'))
        self.parm_curvatureramp4pos = Parameter(parm=self.node.parm('curvatureramp4pos'))
        self.parm_curvatureramp4value = Parameter(parm=self.node.parm('curvatureramp4value'))
        self.parm_dirramp1pos = Parameter(parm=self.node.parm('dirramp1pos'))
        self.parm_dirramp1value = Parameter(parm=self.node.parm('dirramp1value'))
        self.parm_dirramp2pos = Parameter(parm=self.node.parm('dirramp2pos'))
        self.parm_dirramp2value = Parameter(parm=self.node.parm('dirramp2value'))
        self.parm_dirramp3pos = Parameter(parm=self.node.parm('dirramp3pos'))
        self.parm_dirramp3value = Parameter(parm=self.node.parm('dirramp3value'))
        self.parm_dirramp4pos = Parameter(parm=self.node.parm('dirramp4pos'))
        self.parm_dirramp4value = Parameter(parm=self.node.parm('dirramp4value'))
        self.parm_ramp1pos = Parameter(parm=self.node.parm('ramp1pos'))
        self.parm_ramp1value = Parameter(parm=self.node.parm('ramp1value'))
        self.parm_ramp2pos = Parameter(parm=self.node.parm('ramp2pos'))
        self.parm_ramp2value = Parameter(parm=self.node.parm('ramp2value'))

        
        # parm menu vars:
        self.parm_combine = CombineMenu(parm=self.node.parm('combine'))
        self.parm_sloperamp1interp = Sloperamp1InterpMenu(parm=self.node.parm('sloperamp1interp'))
        self.parm_sloperamp2interp = Sloperamp2InterpMenu(parm=self.node.parm('sloperamp2interp'))
        self.parm_sloperamp3interp = Sloperamp3InterpMenu(parm=self.node.parm('sloperamp3interp'))
        self.parm_sloperamp4interp = Sloperamp4InterpMenu(parm=self.node.parm('sloperamp4interp'))
        self.parm_heightramp1interp = Heightramp1InterpMenu(parm=self.node.parm('heightramp1interp'))
        self.parm_heightramp2interp = Heightramp2InterpMenu(parm=self.node.parm('heightramp2interp'))
        self.parm_heightramp3interp = Heightramp3InterpMenu(parm=self.node.parm('heightramp3interp'))
        self.parm_heightramp4interp = Heightramp4InterpMenu(parm=self.node.parm('heightramp4interp'))
        self.parm_curvatureramp1interp = Curvatureramp1InterpMenu(parm=self.node.parm('curvatureramp1interp'))
        self.parm_curvatureramp2interp = Curvatureramp2InterpMenu(parm=self.node.parm('curvatureramp2interp'))
        self.parm_curvatureramp3interp = Curvatureramp3InterpMenu(parm=self.node.parm('curvatureramp3interp'))
        self.parm_curvatureramp4interp = Curvatureramp4InterpMenu(parm=self.node.parm('curvatureramp4interp'))
        self.parm_dirramp1interp = Dirramp1InterpMenu(parm=self.node.parm('dirramp1interp'))
        self.parm_dirramp2interp = Dirramp2InterpMenu(parm=self.node.parm('dirramp2interp'))
        self.parm_dirramp3interp = Dirramp3InterpMenu(parm=self.node.parm('dirramp3interp'))
        self.parm_dirramp4interp = Dirramp4InterpMenu(parm=self.node.parm('dirramp4interp'))
        self.parm_ramp1interp = Ramp1InterpMenu(parm=self.node.parm('ramp1interp'))
        self.parm_ramp2interp = Ramp2InterpMenu(parm=self.node.parm('ramp2interp'))


        # input vars:
        self.input_terrain_to_create_mask_on = 'Terrain to Create Mask on'


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


class Sloperamp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Sloperamp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Sloperamp3InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Sloperamp4InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Heightramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Heightramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Heightramp3InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Heightramp4InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Curvatureramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Curvatureramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Curvatureramp3InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Curvatureramp4InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Dirramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Dirramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Dirramp3InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Dirramp4InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Ramp1InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"


class Ramp2InterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_constant = "constant"
        self.menu_linear = "linear"
        self.menu_catmull_rom = "catmull-rom"
        self.menu_monotone_cubic = "monotonecubic"
        self.menu_bezier = "bezier"
        self.menu_b_spline = "bspline"
        self.menu_hermite = "hermite"



