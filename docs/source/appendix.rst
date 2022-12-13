.. image:: images/index/under_construction.jpg
    
Appendix
===============

VSCode IDE Setup
----------------

Black Installation and Configuration:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install and configure Black Formatter: https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0
#. Set the line-length (This framework uses 150): https://dev.to/adamlombard/vscode-setting-line-lengths-in-the-black-python-code-formatter-1g62
#. Install Black for hython. You'll need to do this for auto-formatting to work when editing HDA scripts. See this video for how to install 3rd party libraries to hython: https://www.youtube.com/watch?v=cIEN50WuPoc

Configure the hou and ox Module for Auto-Complete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following code to your settings.json file (I recommend doing this at the user level.) Don't know how to do that? Here you go:
https://stackoverflow.com/questions/65908987/how-can-i-open-visual-studio-codes-settings-json-file

.. code-block:: json

     {
          "python.autoComplete.extraPaths": [
               "C:/Program Files/Side Effects Software/Houdini 19.5.303/houdini/python3.9libs",
               "C:/Users/justi/source/repos/ox_framework/python3.9libs",
          ],
          "python.analysis.extraPaths": [
               "C:/Program Files/Side Effects Software/Houdini 19.5.303/houdini/python3.9libs",
               "C:/Users/justi/source/repos/ox_framework/python3.9libs"
          ],
          "python.autoComplete.preloadModules": [
               "hou",
               "ox"
          ]
     }


PyCharm IDE Setup
-----------------

PyCharm is a great IDE. I never figured out how to get the hou module to work with it, unfortunately. 
Please consider contributing if you have been able to get this to work with Pycharm. 


Learning Resources
------------------


* Python Logging: https://realpython.com/python-logging/



Houdini HOM
^^^^^^^^^^^

Intro to Python in Houdini by Socratica FX:

.. raw:: html
    
     <iframe width="560" height="315" src="https://www.youtube.com/embed/59vetivUGes" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>