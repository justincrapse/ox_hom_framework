from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class PartitionNode(OXNode):
    node_type = 'partition'
    parm_lookup_dict = {'group': 'group', 'entity': 'entity', 'geotype': 'geotype', 'rule': 'rule'}

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

        
        # parm menu vars:
        self.parm_entity = EntityMenu(parm=self.node.parm('entity'))
        self.parm_geotype = GeotypeMenu(parm=self.node.parm('geotype'))
        self.parm_rule = RuleMenu(parm=self.node.parm('rule'))


        # input vars:
        self.input_input_geometry = 'Input geometry'


# parm menu classes:
class EntityMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = "primitive"
        self.menu_points = "point"


class GeotypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_types = "all"
        self.menu_bezier_curve = "bezierc"
        self.menu_bezier_surface = "bezier"
        self.menu_bilinear_mesh = "mesh"
        self.menu_circle = "circle"
        self.menu_hexahedron = "Hexahedron"
        self.menu_meta_super_quad = "MetaSQuad"
        self.menu_metaball = "meta"
        self.menu_nurbs_curve = "nurbc"
        self.menu_nurbs_surface = "nurb"
        self.menu_packed_agent = "PackedAgent"
        self.menu_packed_alembic = "AlembicRef"
        self.menu_packed_disk = "PackedDisk"
        self.menu_packed_disk_sequence = "PackedDiskSequence"
        self.menu_packed_fragment = "PackedFragment"
        self.menu_packed_geometry = "PackedGeometry"
        self.menu_packed_usd = "PackedUSD"
        self.menu_particle_system = "part"
        self.menu_polygon = "poly"
        self.menu_polygon_soup = "polysoup"
        self.menu_sphere = "sphere"
        self.menu_tetrahedron = "tetrahedron"
        self.menu_triangle_fan = "trifan"
        self.menu_triangle_strip = "tristrip"
        self.menu_triangular_bezier_patch = "tribez"
        self.menu_tube = "tube"
        self.menu_vdb = "vdb"
        self.menu_volume = "volume"


class RuleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_group_by_color = "color_`rint(@Cd.r*255)`_`rint(@Cd.g*255)`_`rint(@Cd.b*255)`"
        self.menu_group_by_alpha = "alpha_`rint(@Alpha*255)`"



