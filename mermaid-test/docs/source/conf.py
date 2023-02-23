# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from sphinxcontrib.mermaid import mermaid

project = 'adfdsfa'
copyright = '2023, asdf'
author = 'asdf'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

extensions = ['sphinxcontrib.mermaid', 'myst_parser']

templates_path = ['_templates']
exclude_patterns = []

mermaid_output_format = 'png'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
