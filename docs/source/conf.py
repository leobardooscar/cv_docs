# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CV & P. gallery'
copyright = '2024, Leobardo Oscar Alcantara Ocana'
author = 'Leobardo Oscar Alcantara Ocana'
release = 'August 2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "contents"


extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
#Sidebar title
html_title = "Main page"
#Banner top
html_theme_options = {
    "announcement": "<h2> CV & Project Gallery</h2>  <h3> Leobardo Oscar Alcántara Ocaña</h3> ",
}