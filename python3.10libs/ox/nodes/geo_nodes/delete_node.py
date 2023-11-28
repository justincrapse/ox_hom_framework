from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class DeleteNode(OXNode):
    node_type = 'delete'
    parm_lookup_dict = {'group': 'group', 'label0': 'label0', 'negate': 'negate', 'entity': 'entity', 'geotype': 'geotype', 'stdswitcher1': 'stdswitcher1', 'affectnumber': 'affectnumber', 'groupop': 'groupop', 'filter': 'filter', 'pattern': 'pattern', 'rangestart': 'rangestart', 'rangeend': 'rangeend', 'select1': 'select1', 'select2': 'select2', 'affectvolume': 'affectvolume', 'boundtype': 'boundtype', 'sizex': 'sizex', 'sizey': 'sizey', 'sizez': 'sizez', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'affectnormal': 'affectnormal', 'dirx': 'dirx', 'diry': 'diry', 'dirz': 'dirz', 'angle': 'angle', 'camerapath': 'camerapath', 'affectdegenerate': 'affectdegenerate', 'degenerate': 'degenerate', 'zaf': 'zaf', 'doopen': 'doopen', 'tol': 'tol', 'userandom': 'userandom', 'globalseed': 'globalseed', 'useseedattrib': 'useseedattrib', 'seedattrib': 'seedattrib', 'percent': 'percent', 'removegrp': 'removegrp', 'keeppoints': 'keeppoints'}

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
        self.parm_label0 = Parameter(parm=self.node.parm('label0'))
        self.parm_stdswitcher1 = Parameter(parm=self.node.parm('stdswitcher1'))
        self.parm_affectnumber = Parameter(parm=self.node.parm('affectnumber'))
        self.parm_filter = Parameter(parm=self.node.parm('filter'))
        self.parm_pattern = Parameter(parm=self.node.parm('pattern'))
        self.parm_rangestart = Parameter(parm=self.node.parm('rangestart'))
        self.parm_rangeend = Parameter(parm=self.node.parm('rangeend'))
        self.parm_select1 = Parameter(parm=self.node.parm('select1'))
        self.parm_select2 = Parameter(parm=self.node.parm('select2'))
        self.parm_affectvolume = Parameter(parm=self.node.parm('affectvolume'))
        self.parm_sizex = Parameter(parm=self.node.parm('sizex'))
        self.parm_sizey = Parameter(parm=self.node.parm('sizey'))
        self.parm_sizez = Parameter(parm=self.node.parm('sizez'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_affectnormal = Parameter(parm=self.node.parm('affectnormal'))
        self.parm_dirx = Parameter(parm=self.node.parm('dirx'))
        self.parm_diry = Parameter(parm=self.node.parm('diry'))
        self.parm_dirz = Parameter(parm=self.node.parm('dirz'))
        self.parm_angle = Parameter(parm=self.node.parm('angle'))
        self.parm_camerapath = Parameter(parm=self.node.parm('camerapath'))
        self.parm_affectdegenerate = Parameter(parm=self.node.parm('affectdegenerate'))
        self.parm_degenerate = Parameter(parm=self.node.parm('degenerate'))
        self.parm_zaf = Parameter(parm=self.node.parm('zaf'))
        self.parm_doopen = Parameter(parm=self.node.parm('doopen'))
        self.parm_tol = Parameter(parm=self.node.parm('tol'))
        self.parm_userandom = Parameter(parm=self.node.parm('userandom'))
        self.parm_globalseed = Parameter(parm=self.node.parm('globalseed'))
        self.parm_useseedattrib = Parameter(parm=self.node.parm('useseedattrib'))
        self.parm_seedattrib = Parameter(parm=self.node.parm('seedattrib'))
        self.parm_percent = Parameter(parm=self.node.parm('percent'))
        self.parm_removegrp = Parameter(parm=self.node.parm('removegrp'))
        self.parm_keeppoints = Parameter(parm=self.node.parm('keeppoints'))

        
        # parm menu vars:
        self.parm_negate = NegateMenu(parm=self.node.parm('negate'))
        self.parm_entity = EntityMenu(parm=self.node.parm('entity'))
        self.parm_geotype = GeotypeMenu(parm=self.node.parm('geotype'))
        self.parm_groupop = GroupopMenu(parm=self.node.parm('groupop'))
        self.parm_boundtype = BoundtypeMenu(parm=self.node.parm('boundtype'))


        # input vars:
        self.input_geometry_to_delete = 'Geometry to Delete'


# parm menu classes:
class NegateMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_delete_selected = ("dele", 0)
        self.menu_delete_non_selected = ("keep", 1)


class EntityMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = ("primitive", 0)
        self.menu_points = ("point", 1)
        self.menu_edges = ("edge", 2)


class GeotypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_types = ("all", 0)
        self.menu_bezier_curve = ("bezierc", 1)
        self.menu_bezier_surface = ("bezier", 2)
        self.menu_bilinear_mesh = ("mesh", 3)
        self.menu_circle = ("circle", 4)
        self.menu_hexahedron = ("Hexahedron", 5)
        self.menu_meta_super_quad = ("MetaSQuad", 6)
        self.menu_metaball = ("meta", 7)
        self.menu_nurbs_curve = ("nurbc", 8)
        self.menu_nurbs_surface = ("nurb", 9)
        self.menu_packed_agent = ("PackedAgent", 10)
        self.menu_packed_alembic = ("AlembicRef", 11)
        self.menu_packed_disk = ("PackedDisk", 12)
        self.menu_packed_disk_sequence = ("PackedDiskSequence", 13)
        self.menu_packed_fragment = ("PackedFragment", 14)
        self.menu_packed_geometry = ("PackedGeometry", 15)
        self.menu_packed_usd = ("PackedUSD", 16)
        self.menu_particle_system = ("part", 17)
        self.menu_polygon = ("poly", 18)
        self.menu_polygon_soup = ("polysoup", 19)
        self.menu_sphere = ("sphere", 20)
        self.menu_tetrahedron = ("tetrahedron", 21)
        self.menu_triangle_fan = ("trifan", 22)
        self.menu_triangle_strip = ("tristrip", 23)
        self.menu_triangular_bezier_patch = ("tribez", 24)
        self.menu_tube = ("tube", 25)
        self.menu_vdb = ("vdb", 26)
        self.menu_volume = ("volume", 27)


class GroupopMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_delete_by_pattern = ("pattern", 0)
        self.menu_delete_by_range = ("range", 1)
        self.menu_delete_by_expression = ("filter", 2)


class BoundtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bounding_box = ("usebbox", 0)
        self.menu_bounding_sphere = ("usebsphere", 1)



