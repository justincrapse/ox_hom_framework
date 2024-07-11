from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class PolysliceNode(OXNode):
    node_type = 'labs::polyslice::1.0'
    parm_lookup_dict = {'group': 'group', 'mode': 'Mode', 'userest': 'userest', 'rest': 'rest', 'fd_visualize': 'fd_visualize', 'showguide': 'showguide', 'visualize': 'visualize', 'visualizerest': 'visualizerest', 'fd_dimensions': 'fd_dimensions', 'numslices': 'numslices', 'setbbox': 'setbbox', 't2x': 't2x', 't2y': 't2y', 't2z': 't2z', 'sizex': 'sizex', 'sizey': 'sizey', 'sizez': 'sizez', 'scale2': 'scale2', 'r2x': 'r2x', 'r2y': 'r2y', 'r2z': 'r2z', 'fd_topology': 'fd_topology', 'divideconvex': 'divideconvex', 'plantol': 'plantol', 'connectivitymode': 'connectivitymode', 'sliceborderedge': 'sliceborderedge', 'connectborderedge': 'connectborderedge', 'exportsliceid': 'exportsliceid', 'sliceidname': 'sliceidname', 'exportnormalizedsliceid': 'exportnormalizedsliceid', 'normalizedsliceidname': 'normalizedsliceidname', 'exportslicegroup': 'exportslicegroup', 'slicegroup': 'slicegroup', 'fd_cap': 'fd_cap', 'keepstartcap': 'keepstartcap', 'startcapgroupname': 'startcapgroupname', 'keependcap': 'keependcap', 'endcapgroupname': 'endcapgroupname', 'fd_advanced': 'fd_advanced', 'slicethreshold': 'slicethreshold', 'tol3d': 'tol3d', 'fd_remap': 'fd_remap', 'remapslice': 'remapslice', 'remap': 'remap', 'remap1pos': 'remap1pos', 'remap1value': 'remap1value', 'remap1interp': 'remap1interp', 'remap2pos': 'remap2pos', 'remap2value': 'remap2value', 'remap2interp': 'remap2interp'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_userest = Parameter(parm=self.node.parm('userest'))
        self.parm_rest = Parameter(parm=self.node.parm('rest'))
        self.parm_fd_visualize = Parameter(parm=self.node.parm('fd_visualize'))
        self.parm_showguide = Parameter(parm=self.node.parm('showguide'))
        self.parm_visualize = Parameter(parm=self.node.parm('visualize'))
        self.parm_visualizerest = Parameter(parm=self.node.parm('visualizerest'))
        self.parm_fd_dimensions = Parameter(parm=self.node.parm('fd_dimensions'))
        self.parm_numslices = Parameter(parm=self.node.parm('numslices'))
        self.parm_setbbox = Parameter(parm=self.node.parm('setbbox'))
        self.parm_t2x = Parameter(parm=self.node.parm('t2x'))
        self.parm_t2y = Parameter(parm=self.node.parm('t2y'))
        self.parm_t2z = Parameter(parm=self.node.parm('t2z'))
        self.parm_sizex = Parameter(parm=self.node.parm('sizex'))
        self.parm_sizey = Parameter(parm=self.node.parm('sizey'))
        self.parm_sizez = Parameter(parm=self.node.parm('sizez'))
        self.parm_scale2 = Parameter(parm=self.node.parm('scale2'))
        self.parm_r2x = Parameter(parm=self.node.parm('r2x'))
        self.parm_r2y = Parameter(parm=self.node.parm('r2y'))
        self.parm_r2z = Parameter(parm=self.node.parm('r2z'))
        self.parm_fd_topology = Parameter(parm=self.node.parm('fd_topology'))
        self.parm_divideconvex = Parameter(parm=self.node.parm('divideconvex'))
        self.parm_plantol = Parameter(parm=self.node.parm('plantol'))
        self.parm_sliceborderedge = Parameter(parm=self.node.parm('sliceborderedge'))
        self.parm_connectborderedge = Parameter(parm=self.node.parm('connectborderedge'))
        self.parm_exportsliceid = Parameter(parm=self.node.parm('exportsliceid'))
        self.parm_sliceidname = Parameter(parm=self.node.parm('sliceidname'))
        self.parm_exportnormalizedsliceid = Parameter(parm=self.node.parm('exportnormalizedsliceid'))
        self.parm_normalizedsliceidname = Parameter(parm=self.node.parm('normalizedsliceidname'))
        self.parm_exportslicegroup = Parameter(parm=self.node.parm('exportslicegroup'))
        self.parm_slicegroup = Parameter(parm=self.node.parm('slicegroup'))
        self.parm_fd_cap = Parameter(parm=self.node.parm('fd_cap'))
        self.parm_keepstartcap = Parameter(parm=self.node.parm('keepstartcap'))
        self.parm_startcapgroupname = Parameter(parm=self.node.parm('startcapgroupname'))
        self.parm_keependcap = Parameter(parm=self.node.parm('keependcap'))
        self.parm_endcapgroupname = Parameter(parm=self.node.parm('endcapgroupname'))
        self.parm_fd_advanced = Parameter(parm=self.node.parm('fd_advanced'))
        self.parm_slicethreshold = Parameter(parm=self.node.parm('slicethreshold'))
        self.parm_tol3d = Parameter(parm=self.node.parm('tol3d'))
        self.parm_fd_remap = Parameter(parm=self.node.parm('fd_remap'))
        self.parm_remapslice = Parameter(parm=self.node.parm('remapslice'))
        self.parm_remap = Parameter(parm=self.node.parm('remap'))
        self.parm_remap1pos = Parameter(parm=self.node.parm('remap1pos'))
        self.parm_remap1value = Parameter(parm=self.node.parm('remap1value'))
        self.parm_remap2pos = Parameter(parm=self.node.parm('remap2pos'))
        self.parm_remap2value = Parameter(parm=self.node.parm('remap2value'))

        
        # parm menu vars:
        self.parm_mode = ModeMenu(parm=self.node.parm('Mode'))
        self.parm_connectivitymode = ConnectivitymodeMenu(parm=self.node.parm('connectivitymode'))
        self.parm_remap1interp = Remap1InterpMenu(parm=self.node.parm('remap1interp'))
        self.parm_remap2interp = Remap2InterpMenu(parm=self.node.parm('remap2interp'))


        # input vars:
        self.input_geometry = 'Geometry'


# parm menu classes:
class ModeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_poly = ("poly", 0)
        self.menu_polyline = ("polyline", 1)


class ConnectivitymodeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_skip_connecting = ("0", 0)
        self.menu_slices_together = ("1", 1)
        self.menu_slice_separate = ("2", 2)


class Remap1InterpMenu(Menu):
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


class Remap2InterpMenu(Menu):
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



