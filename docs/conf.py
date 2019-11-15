# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Project information -----------------------------------------------------

project = 'Web3 Foundation Research'
copyright = '2019, Web3 Foundation'
author = 'Web3 Foundation'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# For markdown support see https://gist.github.com/johncrossland/9f6f54d559e9136773172aa0a429b46f

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinxcontrib.fulltoc',
    'sphinx_markdown_tables',
    'sphinx_math_dollar',
]

templates_path = ['_templates']

source_suffix = ['.rst', '.md']

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

master_doc = 'index'


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

html_css_files = [
    'stylesheets/extra.css',
]

mathjax_config = {
    'extensions': ["tex2jax.js"],
    'jax': ["input/TeX", "output/HTML-CSS"],
    'tex2jax': {
      'inlineMath': [ ['$','$'], ["\\(","\\)"] ],
      'displayMath': [ ['$$','$$'], ["\\[","\\]"] ],
      'processEscapes': True
    },
    "HTML-CSS": { 'fonts': ["TeX"] }
}

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
