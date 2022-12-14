Adding Node Classes
===================


The node classes in the framework are auto-generated based on live Houdini nodes. Because houdini's node parameters and options change over time, the 
framework can also re-run all existing node classes. 

Adding A New Node Class To The Framework
----------------------------------------

Before considering adding a new node to the framework, you'll want to make sure it has not already been added. Node class names use the default node 
name when the node is created, minus and trailing digits. The node type, however, is taken from hom_node.type().name() and is a class-level variable
as "node_type" for every generated node class. 

Once you have determined that the node class does not already exist, create a new, clean node of the type you want to add, select it, then click on
the "Node Class Generator" tool in the "OX:Admin" toolbar. Shoutout to our cat Zero who possed for the icon photo:

.. image:: ../../../icons/cat_icon.png
   :width: 100
   :alt: alt text here

If there are dynamic parameters that only show up after adjusting parameters or imputs, we will want to add these to the "Regenerate Node Classes" 
tool. Please contact the repository owner if planning to create a pull request for this type of scenario. 


Updating Existing Node Classes
------------------------------

The "Regenerate Node Classes" tool in the "OX:Admin" toolbar:

.. image:: ../../../icons/cat_blue_icon.png
   :width: 100
   :alt: alt text here

This should not be ran in general. This will update all node classes currently in the framework. This should idealy only be ran after a major release
and merged into the main branch shortly after. 



Handling Dynamic Parameters
---------------------------

Some parameters will not show up in the auto-generated node class if that parameters is not preset by default. To work around this, we can add a node 
type in the appropriate section of the "Regenerate Node Classes" tool in the "OX:Admin" toolbar (explained above.) For example, in the geo_nodes 
section, the script is checking for a node of type "labs::hf_combine_masks". Before the node class is generated, the parameter "folder0" is given a 
value of 10, which dynamically generates parameters that we will likely need to access via the node class. Otherwise, we would not be able to see 
that parm from our node class. 

Of course you can always call some_ox_node.node.parm('layername_1') to access the parameter, but the whole point of the framework is to keep
hardcoding to a minimum. Anytime we can code something once, such as in this workaround, it is the preferred standard when adding to this framework.

