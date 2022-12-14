# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
my_path = os.path.abspath('../../python3.9libs')
print(f'my_path : {my_path}')
sys.path.insert(0, my_path)
# sys.path.insert(1, "C:/Program Files/Side Effects Software/Houdini 19.5.303/houdini/python3.9libs")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "OX HOM Framework"
copyright = "2022, Justin Crapse"
author = "Justin Crapse"
release = "[0.0.1]"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns = []

autodoc_mock_imports = ["hou"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
