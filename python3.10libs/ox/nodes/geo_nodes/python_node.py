from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class PythonNode(OXNode):
    node_type = 'python'
    parm_lookup_dict = {'python': 'python', 'maintainstate': 'maintainstate'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_maintainstate = Parameter(parm=self.node.parm('maintainstate'))

        
        # parm menu vars:
        self.parm_python = PythonMenu(parm=self.node.parm('python'))


        # input vars:
        self.input_input_1 = 'Input 1'
        self.input_input_2 = 'Input 2'
        self.input_input_3 = 'Input 3'
        self.input_input_4 = 'Input 4'


# parm menu classes:
class PythonMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_default_script = """# Default Script
node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

"""
        self.menu_move_points_up = """# Move Points Up
node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
for point in geo.points():
    pos = point.position()
    pos += hou.Vector3(0, 1, 0)
    point.setPosition(pos)

"""
        self.menu_apply_subdivide_sop_verb = """# Apply Subdivide SOP Verb
node = hou.pwd()
geo = node.geometry()

verb = hou.sopNodeTypeCategory().nodeVerb("subdivide")

# Dictionary of parameter/values.  Unspecified values
# will be default (which may change each version!)
verb.setParms( { 'iterations' : 1 } )

# hou.Geometry.execute makes itself the first input.
geo.execute(verb)

# Save results back to the node
node.geometry().clear()
node.geometry().merge(geo)

"""
        self.menu_run_a_generator_box_sop_verb = """# Run a generator Box SOP Verb
node = hou.pwd()
geo = node.geometry()

verb = hou.sopNodeTypeCategory().nodeVerb("box")

# Get a fresh geometry to write to
geo = hou.Geometry()

# Dictionary of parameter/values.  Unspecified values
# will be default (which may change each version!)
verb.setParms( { 
                't' : (2, 1, 2 ),
                'size' : (3, 2, 5)
               } )

# To run a generator we have to use verb.execute
# otherwise we become the input and override the size.
verb.execute(geo, [])

# Save results back to the node
node.geometry().clear()
node.geometry().merge(geo)


"""



