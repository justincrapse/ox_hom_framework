from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class AttribwrangleNode(OXNode):
    node_type = 'attribwrangle'
    parm_lookup_dict = {'folder01': 'folder01', 'group': 'group', 'grouptype': 'grouptype', 'class_alt': 'class', 'vex_numcount': 'vex_numcount', 'vex_threadjobsize': 'vex_threadjobsize', 'snippet': 'snippet', 'exportlist': 'exportlist', 'vex_strict': 'vex_strict', 'autobind': 'autobind', 'bindings': 'bindings', 'groupautobind': 'groupautobind', 'groupbindings': 'groupbindings', 'vex_cwdpath': 'vex_cwdpath', 'vex_outputmask': 'vex_outputmask', 'vex_updatenmls': 'vex_updatenmls', 'vex_matchattrib': 'vex_matchattrib', 'vex_inplace': 'vex_inplace', 'vex_selectiongroup': 'vex_selectiongroup', 'vex_precision': 'vex_precision'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_folder01 = Parameter(parm=self.node.parm('folder01'))
        self.parm_group = Parameter(parm=self.node.parm('group'))
        self.parm_vex_numcount = Parameter(parm=self.node.parm('vex_numcount'))
        self.parm_vex_threadjobsize = Parameter(parm=self.node.parm('vex_threadjobsize'))
        self.parm_exportlist = Parameter(parm=self.node.parm('exportlist'))
        self.parm_vex_strict = Parameter(parm=self.node.parm('vex_strict'))
        self.parm_autobind = Parameter(parm=self.node.parm('autobind'))
        self.parm_bindings = Parameter(parm=self.node.parm('bindings'))
        self.parm_groupautobind = Parameter(parm=self.node.parm('groupautobind'))
        self.parm_groupbindings = Parameter(parm=self.node.parm('groupbindings'))
        self.parm_vex_cwdpath = Parameter(parm=self.node.parm('vex_cwdpath'))
        self.parm_vex_outputmask = Parameter(parm=self.node.parm('vex_outputmask'))
        self.parm_vex_updatenmls = Parameter(parm=self.node.parm('vex_updatenmls'))
        self.parm_vex_matchattrib = Parameter(parm=self.node.parm('vex_matchattrib'))
        self.parm_vex_inplace = Parameter(parm=self.node.parm('vex_inplace'))
        self.parm_vex_selectiongroup = Parameter(parm=self.node.parm('vex_selectiongroup'))

        
        # parm menu vars:
        self.parm_grouptype = GrouptypeMenu(parm=self.node.parm('grouptype'))
        self.parm_class_alt = ClassAltMenu(parm=self.node.parm('class'))
        self.parm_snippet = SnippetMenu(parm=self.node.parm('snippet'))
        self.parm_vex_precision = VexPrecisionMenu(parm=self.node.parm('vex_precision'))


        # input vars:
        self.input_geometry_to_process_with_wrangle = 'Geometry to Process with Wrangle'
        self.input_ancillary_input__point_1_______to_access = 'Ancillary Input, point(1, ...) to Access'
        self.input_ancillary_input__point_2_______to_access = 'Ancillary Input, point(2, ...) to Access'
        self.input_ancillary_input__point_3_______to_access = 'Ancillary Input, point(3, ...) to Access'


# parm menu classes:
class GrouptypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_guess_from_group = "guess"
        self.menu_vertices = "vertices"
        self.menu_edges = "edges"
        self.menu_points = "points"
        self.menu_primitives = "prims"


class ClassAltMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_detail__only_once_ = "detail"
        self.menu_primitives = "primitive"
        self.menu_points = "point"
        self.menu_vertices = "vertex"
        self.menu_numbers = "number"


class SnippetMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_color_from_bounding_box = """// Color from Bounding Box
@Cd = relbbox(0, @P);

"""
        self.menu_random_point_color = """// Random Point Color
float seed = 0.12345; // seed for rand
@Cd = rand(seed + @ptnum);

"""
        self.menu_color_based_on_threshold = """// Color Based on Threshold
int condition = (@P.x > 0) ? 1 : 0; // short form if() test
@Cd = set(condition, 0, 0);        // write condition into red color

"""
        self.menu_point_group_on_threshold = """// Point Group on Threshold
string group = "mygroup";         // group name to add points to
int condition = (@P.x > 0) ? 1: 0; // short form if() test
setpointgroup(geoself(), group, @ptnum, condition);
@Cd = set( condition, 0, 0);      // color if in group

"""
        self.menu_fetch_second_input_cd_attribute = """// Fetch Second Input Cd Attribute
// Second input used as reference geometry
// Use prim and @primnum to get a matching primitive attribute.
@Cd = point(1, "Cd", @ptnum);

"""
        self.menu_fetch_second_input_attribute_by_id_name = """// Fetch Second Input Attribute by id/name

// grab attribute by id match from second input
// id attribute present on both inputs for indexing
int match_pt = findattribval(1, "point", "id", @id); // matching point
@P = point(1, "P", match_pt);  // use matching point to fetch attribute

// grab attribute by name attribute
// int match_prim = findattribval(1, "prim", "name", @name); // matching name
// @Cd = prim(1, "Cd", match_prim);

"""
        self.menu_nearest_point_distance = """// Nearest Point Distance
// Second input used for reference geometry
int closept = nearpoint(1, @P);      // get point number of near point
vector value = point(1, "P", closept);// get position of near point
@dist = length(@P - value);           // export distance from nearest point
@Cd = set(@dist, 0, 0);

"""
        self.menu_grow_hairs = """// Grow Hairs
vector dir = { 0, 1, 0 };
// dir = @N;    // grow in normal direction
float len = 1.0;
int   steps = 10;
float jitter = 0.1;
float seed = 0.12345;

vector    pos = @P;
int        pr = addprim(geoself(), "polyline");

// Start the curve with our point
addvertex(geoself(), pr, @ptnum);
for (int i = 0; i < steps; i++)
{
    pos += dir * len / steps;
    pos += (vector(rand( @ptnum + seed )) - 0.5) * jitter;

    // Clone our point to copy attributes
    int pt = addpoint(geoself(), @ptnum);
    // But write a new position
    setpointattrib(geoself(), "P", pt, pos);

    // Connect the new point to our curve.
    addvertex(geoself(), pr, pt);
    seed += $PI;
}

"""
        self.menu_get_neighbouring_points_into_attribute = """// Get Neighbouring Points into Attribute
i[]@neighbours = neighbours(0, @ptnum);

"""
        self.menu_average_neighbouring_points = """// Average Neighbouring Points
int n[] = neighbours(0, @ptnum);
vector avgP = @P;

// Loops over all elements of n, setting pt
// to be the value of each element
foreach (int pt; n)
{
    avgP += point(0, "P", pt);
}

// +1 because we included ourself.
avgP /= len(n)+1;
@P = avgP;

"""


class VexPrecisionMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_auto = "auto"
        self.menu_bit_32 = "32"
        self.menu_bit_64 = "64"



