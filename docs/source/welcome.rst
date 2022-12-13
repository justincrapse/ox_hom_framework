.. image:: images/index/under_construction.jpg

Welcome 
=======

Welcome to OX HOM Framework for Houdini documentation!

The OX HOM Framework is a light-weight Python Object Oriented Framework build on top of Houdini's HOM API. 
This framework makes it easier to organize and write code for Houdini's hou module (HOM.)

* connecting nodes together by input and output labels
* Easy adding and deleting parm templates from nodes
* Setting menu parm values by label instead of by index (with auto complete)
* Search for child nodes by substring or regex (returns a list of nodes)
* Handling saving and loading of presets
* Simple logging system for helpful debugging (no print statements needed!)

   * Easily change logging level

* Easily extendible framework. 
* Extensive auto-complete features:

   * Input and output labels for any given node type
   * parameter name values
   * node types organized by network context

* And many more helpful functions and improved workflows

The following is an example of how we can call a method on any node that can leverage the HOM under the hood. 

.. image:: images/index/abstract_code_example.png
   :width: 1125

Another main feature of the framework is providing quality-of-life coding environament capabilities such as auto-complete
for all nodes and parameters

.. image:: images/index/auto_complete_parm.jpg
   :width: 615

This OOP class structure is posible through automatic class generation and import registration. This requires very little additional setup, if any,
per node. 
