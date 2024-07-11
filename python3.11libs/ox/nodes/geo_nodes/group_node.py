from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class GroupNode(OXNode):
    node_type = 'groupcreate'
    parm_lookup_dict = {'groupname': 'groupname', 'grouptype': 'grouptype', 'mergeop': 'mergeop', 'folder0': 'folder0', 'groupbase': 'groupbase', 'basegroup': 'basegroup', 'ordered': 'ordered', 'geotype': 'geotype', 'switcher3': 'switcher3', 'groupbounding': 'groupbounding', 'boundtype': 'boundtype', 'sizex': 'sizex', 'sizey': 'sizey', 'sizez': 'sizez', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'initbounds': 'initbounds', 'includenotwhollycontained': 'includenotwhollycontained', 'iso': 'iso', 'invertvolume': 'invertvolume', 'switcher4': 'switcher4', 'groupnormal': 'groupnormal', 'camerapath': 'camerapath', 'nonplanar': 'nonplanar', 'nonplanartol': 'nonplanartol', 'dirx': 'dirx', 'diry': 'diry', 'dirz': 'dirz', 'angle': 'angle', 'switcher5': 'switcher5', 'groupedges': 'groupedges', 'dominedgeangle': 'dominedgeangle', 'minedgeangle': 'minedgeangle', 'domaxedgeangle': 'domaxedgeangle', 'maxedgeangle': 'maxedgeangle', 'edgeanglebetweenedges': 'edgeanglebetweenedges', 'dominedgelen': 'dominedgelen', 'minedgelen': 'minedgelen', 'domaxedgelen': 'domaxedgelen', 'maxedgelen': 'maxedgelen', 'dodepth': 'dodepth', 'edgestep': 'edgestep', 'edgeptgrp': 'edgeptgrp', 'unshared': 'unshared', 'boundarygroups': 'boundarygroups', 'switcher6': 'switcher6', 'grouprandom': 'grouprandom', 'globalseed': 'globalseed', 'useseedattrib': 'useseedattrib', 'seedattrib': 'seedattrib', 'percent': 'percent'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_groupname = Parameter(parm=self.node.parm('groupname'))
        self.parm_folder0 = Parameter(parm=self.node.parm('folder0'))
        self.parm_groupbase = Parameter(parm=self.node.parm('groupbase'))
        self.parm_basegroup = Parameter(parm=self.node.parm('basegroup'))
        self.parm_ordered = Parameter(parm=self.node.parm('ordered'))
        self.parm_switcher3 = Parameter(parm=self.node.parm('switcher3'))
        self.parm_groupbounding = Parameter(parm=self.node.parm('groupbounding'))
        self.parm_sizex = Parameter(parm=self.node.parm('sizex'))
        self.parm_sizey = Parameter(parm=self.node.parm('sizey'))
        self.parm_sizez = Parameter(parm=self.node.parm('sizez'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_initbounds = Parameter(parm=self.node.parm('initbounds'))
        self.parm_includenotwhollycontained = Parameter(parm=self.node.parm('includenotwhollycontained'))
        self.parm_iso = Parameter(parm=self.node.parm('iso'))
        self.parm_invertvolume = Parameter(parm=self.node.parm('invertvolume'))
        self.parm_switcher4 = Parameter(parm=self.node.parm('switcher4'))
        self.parm_groupnormal = Parameter(parm=self.node.parm('groupnormal'))
        self.parm_camerapath = Parameter(parm=self.node.parm('camerapath'))
        self.parm_nonplanar = Parameter(parm=self.node.parm('nonplanar'))
        self.parm_nonplanartol = Parameter(parm=self.node.parm('nonplanartol'))
        self.parm_dirx = Parameter(parm=self.node.parm('dirx'))
        self.parm_diry = Parameter(parm=self.node.parm('diry'))
        self.parm_dirz = Parameter(parm=self.node.parm('dirz'))
        self.parm_angle = Parameter(parm=self.node.parm('angle'))
        self.parm_switcher5 = Parameter(parm=self.node.parm('switcher5'))
        self.parm_groupedges = Parameter(parm=self.node.parm('groupedges'))
        self.parm_dominedgeangle = Parameter(parm=self.node.parm('dominedgeangle'))
        self.parm_minedgeangle = Parameter(parm=self.node.parm('minedgeangle'))
        self.parm_domaxedgeangle = Parameter(parm=self.node.parm('domaxedgeangle'))
        self.parm_maxedgeangle = Parameter(parm=self.node.parm('maxedgeangle'))
        self.parm_edgeanglebetweenedges = Parameter(parm=self.node.parm('edgeanglebetweenedges'))
        self.parm_dominedgelen = Parameter(parm=self.node.parm('dominedgelen'))
        self.parm_minedgelen = Parameter(parm=self.node.parm('minedgelen'))
        self.parm_domaxedgelen = Parameter(parm=self.node.parm('domaxedgelen'))
        self.parm_maxedgelen = Parameter(parm=self.node.parm('maxedgelen'))
        self.parm_dodepth = Parameter(parm=self.node.parm('dodepth'))
        self.parm_edgestep = Parameter(parm=self.node.parm('edgestep'))
        self.parm_edgeptgrp = Parameter(parm=self.node.parm('edgeptgrp'))
        self.parm_unshared = Parameter(parm=self.node.parm('unshared'))
        self.parm_boundarygroups = Parameter(parm=self.node.parm('boundarygroups'))
        self.parm_switcher6 = Parameter(parm=self.node.parm('switcher6'))
        self.parm_grouprandom = Parameter(parm=self.node.parm('grouprandom'))
        self.parm_globalseed = Parameter(parm=self.node.parm('globalseed'))
        self.parm_useseedattrib = Parameter(parm=self.node.parm('useseedattrib'))
        self.parm_seedattrib = Parameter(parm=self.node.parm('seedattrib'))
        self.parm_percent = Parameter(parm=self.node.parm('percent'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_mergeop = MergeopMenu(parm=self.node.parm('mergeop'))
        self.parm_geotype = GeotypeMenu(parm=self.node.parm('geotype'))
        self.parm_boundtype = BoundtypeMenu(parm=self.node.parm('boundtype'))


        # input vars:
        self.input_source_data = 'Source data'
        self.input_bounding_object = 'Bounding Object'


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = ("primitive", 0)
        self.menu_points = ("point", 1)
        self.menu_edges = ("edge", 2)
        self.menu_vertices = ("vertex", 3)


class MergeopMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_replace_existing = ("replace", 0)
        self.menu_union_with_existing = ("union", 1)
        self.menu_intersect_with_existing = ("intersect", 2)
        self.menu_subtract_from_existing = ("subtract", 3)


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


class BoundtypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_bounding_box = ("usebbox", 0)
        self.menu_bounding_sphere = ("usebsphere", 1)
        self.menu_bounding_object__points_or_vertices_only_ = ("usebobject", 2)
        self.menu_bounding_volume__points_or_vertices_only_ = ("usebvolume", 3)
        self.menu_bounding_convex_hull__points_or_vertices_only_ = ("usebconvex", 4)



