Getting Started
===============

Getting Started Video Tutorial
------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/B91hJ26vP-I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Working With Nodes
------------------

The OX Framework uses a basic class structure to work with nodes. Each node within houdini has a class associated with it within the framework. 
These node classes are generated from the nodes themselves. Any node can easily be added to the frameowrk or updated for new versions of Houdini. 

Here is an example of working with nodes in the framework:

.. code-block:: Python

    import hou

    from ox import nodes, OXNode


    obj_ox_node = OXNode(hou.node('/obj'))

    geo_ox_node = nodes.obj_nodes.GeoNode(ox_parent=obj_ox_node, node_name='my_geo_node')
    box_node = nodes.geo_nodes.BoxNode(ox_parent=geo_ox_node, node_name='my_box_node')

Instead of creating a node from a HOM node's .createNode() method and passing in the name of a node, we can leverage autocomplete to find the node
we want to create and simply pass the parent OX node in as a parameter. 
The node classes reside within their node context as seen above. With autocomplete, you can easily see all the contexts (obj_nodes, geo_nodes,
redshift_nodes etc.) as well as all the possible child nodes for those contexts.

To get a framework node for an existing node, you can use a number of methods to find the node from the parent and pass it in to the node class:

.. code-block:: python
    
    import hou

    from ox import nodes, OXNode


    obj_ox_node = OXNode(hou.node("/obj"))

    my_geo_node = obj_ox_node.get_child_node_by_name(child_name='my_geo_node')
    geo_ox_node = nodes.obj_nodes.GeoNode(my_geo_node)

Note that in the example above, I did not pass in a keyward argument into the GeoNode class. This is because the first positional argument is a hou
node. Because this a common and intiutive way to pass in this node, it is okay to break the regular rules of always passing in keyword arguments when
calling methods and instantiating classes. 

Best Practice For "ox_node" vs. "node"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Whenever the text "node" is expressed in the framework, it is reffering to hou.Node nodes. In the framework, as well as in all scripts written using
the framework, you should prepend "ox\_" to the term "node" that occurs in any variable refering to nodes to distiguish it from hou.Node nodes. 
See script below for an example. 


Parameters
----------

All parameters exist as class members starting with "parm\_" and ending with the name of the parameter. You may need to go into houdini and hover 
over a parm label to see its name (which can be quite different from the label,) or just type my_ox_node.parm\_ and let autocorrect give you all the 
parameter options for that node. 

Instead of:

.. code-block:: python

    node.parm('some_parm_name').set(some_value)

You can do:

.. code-block:: python

    som_ox_node.parm_<some_parm_name> = some_value


Menu Parameters
---------------

Menu parameters can be a pain to set using the HOM. Some menus use integer numbers and some use string values that map to the menu option labels. 
Instead of dealing with any of that, we can simple access the menu parameter label to set it like so:

.. code-block:: python

    some_ox_node.parm_some_menu_parameter.menu_<some_menu_value_label>

The code above will figure out what value to set that menu parameter. Just that one line of code will set it to the right menu value for that label. 
This is not a conventional way to modify an attribute, but it is incredibly simple and works well. See the code below for a real example of this in 
action. 



Here is a simple code snippet to illustrate the basic workflow for working with Nodes:

.. code-block:: python
    :emphasize-lines: 7, 9, 11, 21, 23

    import hou
    from ox import OXNode
    from ox import nodes
    from ox.helpers import ox_helperc

    obj_node = hou.node("/obj")
    obj_ox_node = OXNode(node=obj_node)

    geo_ox_node = nodes.obj_nodes.GeoNode(ox_parent=obj_ox_node, node_name="my_geo")
    cube_ox_node = nodes.geo_nodes.BoxNode(ox_parent=geo_ox_node, node_name="my_cube")
    cube_ox_node.parm_scale = 2

    cube_trans_ox_node = nodes.geo_nodes.TransformNode(ox_parent=geo_ox_node, node_name="cube_trans")
    cube_trans_ox_node.connect_from(cube_ox_node)

    cube_normal_ox_node = nodes.geo_nodes.NormalNode(ox_parent=geo_ox_node, node_name="cube_norm")
    cube_normal_ox_node.connect_from(cube_trans_ox_node)

    cube_uv_ox_node = nodes.geo_nodes.UvtextureNode(ox_parent=geo_ox_node, node_name="cube_uv")
    cube_uv_ox_node.connect_from(cube_normal_ox_node)
    cube_uv_ox_node.parm_type.menu_face
    cube_uv_ox_node.parm_sv = cube_uv_ox_node.parm_su.parm  # this will copy by reference
    cube_uv_ox_node.parm_sw = cube_uv_ox_node.parm_su.parm  # this will copy by reference

   
The OXNode Class
----------------

The "OXNode" class:

.. code-block:: python

    from ox import OXNode

This OXNode class contains the common methods for most nodes. All node classes inherit from OXNode. 

The OXNode class inherits from the "ParmTemplate"
base_objects class as a mix-in. Mix-ins are an uncommon Python inheritance pattern best avoided. In this case, it serves as a way to organize the 
parm template code into its own document as to not convolute the OXNode namespace. 

When automating scripts, you won't always know what type of node you are dealing with, but you'll still want the functionality of the framework. In 
these cases, you can simply use the OXNode class directly:

.. code-block:: python

    from ox import OXNode

    connected_node = some_ox_node.get_connected_output_node_by_index(index=0)
    connected_ox_node = OXNode(node=connected_node)

    connected_ox_node.run_some_oxnode_function()


Note that I passed in "connected_node" as a keyward agrument. While this is the general rule to live by, the "node" keyword can be omitted as it is A
common access pattern that will not change as the first parameter arg. 

The OX:Admin toolbar
--------------------

The administrative toolbar "OX:Admin" contains a couple of important node class generator tools and a sandbox tool See "Adding Node Classes" for more
information.


Logging/Debugging
-----------------

The framework uses a simple Python logging configuration that greatly helps debugging efforts as the Python framework is only loaded at Houdini 
Startup (so you cannot add print statements without restarted the software to see the output.)

To change the logging level for your session, type in the following into a Python terminal in houdini:

.. code-block:: python

    import ox

    ox.set_logging_level(level=10)


This will let the logging level to "10," which is the debug level. 

To set up the logger in your script, write the following code (with use case examples):

.. code-block:: python

    import logging

    ox_logger = logging.getLogger("ox_logger")


    # now the loger is ready to use
    ox_logger.debug('some debug message')
    ox_logger.info('some info message')

If you need a Python logging primer, Real Python has a great page here: https://realpython.com/python-logging/




