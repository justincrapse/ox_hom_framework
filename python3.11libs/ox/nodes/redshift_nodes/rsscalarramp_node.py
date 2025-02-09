from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class RsscalarrampNode(OXNode):
    node_type = 'redshift::RSScalarRamp'
    parm_lookup_dict = {'input_0': 'Input_0', 'tspace_id': 'tspace_id', 'inputsource': 'inputSource', 'input': 'input', 'inputmapping': 'inputMapping', 'adjust_1': 'Adjust_1', 'exposure': 'exposure', 'old_min': 'old_min', 'old_max': 'old_max', 'new_min': 'new_min', 'new_max': 'new_max', 'inputinvert': 'inputInvert', 'noise': 'noise', 'noisefreq': 'noiseFreq', 'ramp_2': 'Ramp_2', 'ramp': 'ramp', 'ramp_interp': 'ramp_interp', 'shader_skipdefvalparms': 'shader_skipdefvalparms', 'ramp1pos': 'ramp1pos', 'ramp1value': 'ramp1value', 'ramp1interp': 'ramp1interp', 'ramp2pos': 'ramp2pos', 'ramp2value': 'ramp2value', 'ramp2interp': 'ramp2interp'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_input_0 = Parameter(parm=self.node.parm('Input_0'))
        self.parm_tspace_id = Parameter(parm=self.node.parm('tspace_id'))
        self.parm_input = Parameter(parm=self.node.parm('input'))
        self.parm_adjust_1 = Parameter(parm=self.node.parm('Adjust_1'))
        self.parm_exposure = Parameter(parm=self.node.parm('exposure'))
        self.parm_old_min = Parameter(parm=self.node.parm('old_min'))
        self.parm_old_max = Parameter(parm=self.node.parm('old_max'))
        self.parm_new_min = Parameter(parm=self.node.parm('new_min'))
        self.parm_new_max = Parameter(parm=self.node.parm('new_max'))
        self.parm_inputinvert = Parameter(parm=self.node.parm('inputInvert'))
        self.parm_noise = Parameter(parm=self.node.parm('noise'))
        self.parm_noisefreq = Parameter(parm=self.node.parm('noiseFreq'))
        self.parm_ramp_2 = Parameter(parm=self.node.parm('Ramp_2'))
        self.parm_ramp = Parameter(parm=self.node.parm('ramp'))
        self.parm_shader_skipdefvalparms = Parameter(parm=self.node.parm('shader_skipdefvalparms'))
        self.parm_ramp1pos = Parameter(parm=self.node.parm('ramp1pos'))
        self.parm_ramp1value = Parameter(parm=self.node.parm('ramp1value'))
        self.parm_ramp2pos = Parameter(parm=self.node.parm('ramp2pos'))
        self.parm_ramp2value = Parameter(parm=self.node.parm('ramp2value'))

        
        # parm menu vars:
        self.parm_inputsource = InputsourceMenu(parm=self.node.parm('inputSource'))
        self.parm_inputmapping = InputmappingMenu(parm=self.node.parm('inputMapping'))
        self.parm_ramp_interp = RampInterpMenu(parm=self.node.parm('ramp_interp'))
        self.parm_ramp1interp = Ramp1InterpMenu(parm=self.node.parm('ramp1interp'))
        self.parm_ramp2interp = Ramp2InterpMenu(parm=self.node.parm('ramp2interp'))


        # input vars:
        self.input_input = 'input'
        self.input_exposure = 'exposure'
        self.input_old_min = 'old_min'
        self.input_old_max = 'old_max'
        self.input_new_min = 'new_min'
        self.input_new_max = 'new_max'


# parm menu classes:
class InputsourceMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_uv_map = ("0", 0)
        self.menu_alt = ("1", 1)
        self.menu_auto = ("2", 2)


class InputmappingMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_vertical = ("0", 0)
        self.menu_horizontal = ("1", 1)
        self.menu_diagonal = ("2", 2)
        self.menu_radial = ("3", 3)
        self.menu_circular = ("4", 4)


class RampInterpMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_step = ("0", 0)
        self.menu_linear = ("1", 1)
        self.menu_smooth = ("2", 2)
        self.menu_spline = ("3", 3)


class Ramp1InterpMenu(Menu):
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


class Ramp2InterpMenu(Menu):
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



