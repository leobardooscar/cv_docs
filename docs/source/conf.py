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


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_rtd_theme'

html_theme = 'furo'
html_static_path = ['_static']
#Sidebar title
html_title = "Main page"
#Banner top
html_theme_options = {
    "announcement": "<h2> CV & Project Gallery</h2>  <h3> Leobardo Oscar Alcántara Ocaña</h3> ",
}

#From Pufflib project

text = '#f1f1f1'
background = '#061a1a'
foreground = '#000000'
highlight = '#00bbbb'
muted = '#005050'


html_theme_options = {
    "light_css_variables": {
        "color-foreground-primary": "black",
        "color-foreground-secondary": muted,
        "color-foreground-muted": muted,
        "color-foreground-border": "#878787",
        "color-background-primary": "white",
        "color-background-secondary": "#bbcccc",
        "color-background-hover": "#efeff4ff",
        "color-background-hover--transparent": "#efeff400",
        "color-background-border": muted,
        "color-background-item": "#ccc",
        "color-announcement-background": "#000000dd",
        "color-announcement-text": "#eeebee",
        "color-brand-primary": "black",
        "color-brand-content": "black",
        "color-inline-code-background": "#f8f9fb",
        "color-highlighted-background": "#ddeeff",
        "color-guilabel-background": "#ddeeff80",
        "color-guilabel-border": "#bedaf580",
        "color-card-background": "#bbcccc",
    },
    
   
}

