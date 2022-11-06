.. OX HOM Framework documentation master file, created by
   sphinx-quickstart on Tue Nov  1 12:23:38 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: images/index/under_construction.jpg

Welcome to OX HOM Framework for Houdini documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   rest_practice

The OX HOM Framework is an abstraction layer framework build on top of Houdini's HOM API. 
This framework makes it easy to organize many low-level steps into simple, high-level rerunnable code. 
The following is an example of how we can call a method on any node that can run any code and leverage the HOM in a
way that requires the least amount of boilerplate code as possible. 

.. image:: images/index/abstract_code_example.png
   :width: 1125

Another main feature of the framework is providing quality-of-life coding environament capabilities such as auto-complete
for all nodes and parameter

.. image:: images/index/auto_complete_parm.jpg
   :width: 615

You might have noticed the OOP class in the image above and think "writing classes for each node and including every parm is insane
and there is no way this project can be maintained." If I or anyone else were to code these classes, yes, that would be unsustainable. 
However, these classes are auto-generated and require very little additional work compared to the benefits yielded with the framework. 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
