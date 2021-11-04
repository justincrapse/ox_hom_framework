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
        self.input_input_geometry = 0


# parm menu classes:
class EntityMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitives = 0
        self.menu_points = 1


class GeotypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_all_types = 0
        self.menu_bezier_curve = 1
        self.menu_bezier_surface = 2
        self.menu_bilinear_mesh = 3
        self.menu_circle = 4
        self.menu_meta_super_quad = 5
        self.menu_metaball = 6
        self.menu_nurbs_curve = 7
        self.menu_nurbs_surface = 8
        self.menu_packed_agent = 9
        self.menu_packed_alembic = 10
        self.menu_packed_disk = 11
        self.menu_packed_disk_sequence = 12
        self.menu_packed_fragment = 13
        self.menu_packed_geometry = 14
        self.menu_packed_usd = 15
        self.menu_particle_system = 16
        self.menu_pasted_nurbs_surface = 17
        self.menu_polygon = 18
        self.menu_polygon_soup = 19
        self.menu_sphere = 20
        self.menu_tetrahedron = 21
        self.menu_triangle_fan = 22
        self.menu_triangle_strip = 23
        self.menu_triangular_bezier_patch = 24
        self.menu_tube = 25
        self.menu_vdb = 26
        self.menu_volume = 27


class RuleMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_group_by_color = 0
        self.menu_group_by_alpha = 1



