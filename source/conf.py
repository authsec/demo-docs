# conf.py

import os

project = 'My Demo'
copyright = '2026, Siegfried Sphinx'
author = 'Siegfried Sphinx'
version = '0.0.1'
release = '0.0.1'

# 1. RESTORE EXTENSIONS
# We add 'sphinx.ext.todo' back so your ".. todo::" directives work again.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinx_diagrams',
    'sphinxcontrib.drawio',
    'sphinxcontrib.plantuml'
]

templates_path = ['_templates']
exclude_patterns = []
language = 'en'
html_theme = 'alabaster'
todo_include_todos = True  # Make sure todos are visible

#################################
#     Draw.io configuration     #
#################################

# See https://pypi.org/project/sphinxcontrib-drawio/
drawio_no_sandbox = True
drawio_builder_export_format = {
     "html": "svg",
     "latexpdf": "png",
     "docx": "png"
}
drawio_default_export_scale = 100
drawio_default_transparency = True

# --- LATEX CONFIGURATION ---
bibtex_bibfiles = ['references.bib']
# If you can't see a table of contents being generated, this option could be the reason.
# You may also reference a page in there, that doesn't exist, which could cause a crash.
# Comment it out to see if it fixes the issue.
latex_appendices = ['glossary', 'appendices', 'references']

latex_engine = "lualatex"
latex_docclass = {'manual': 'scrbook'}
latex_toplevel_sectioning = "part"
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_table_style = ['booktabs']
latex_logo = '_templates/latex/doc-logo-small.png'

latex_additional_files = [
    # The 2 empty style files are required, they prevent a compile error if you're using KOMA classes.
    # They can be left empty, but they must exist.
    '_templates/latex/sphinxlatexstyleheadings.sty', 
    '_templates/latex/sphinxlatexstylepage.sty',
    'outpdfname.xmpdata',
    '_templates/latex/doc-logo-small.png'
]

# 3. DEFINE PREAMBLE HERE
f_preamble = open('_templates/latex/preamble.tex.input', 'r+')
MY_PREAMBLE = f_preamble.read()

latex_elements = {
    'fncychap': '',
    'tableofcontents': '\\tableofcontents',
    'sphinxsetup': 'hmargin={1.5cm,2.5cm}, vmargin={1.5cm,2cm}, marginpar=2.5cm',
    # Inject the preamble variable we defined above
    'preamble': MY_PREAMBLE,

    'papersize': 'a4paper',
    'pointsize': '11pt',
    'extraclassoptions': 'openright,twoside,parskip=half,numbers=noenddot',

    'fontpkg': r'''
    \makeatletter
    \AddToHook{package/capt-of/before}{\let\captionof\undefined}
    \providecommand{\py@HeaderFamily}{\sffamily\bfseries}
    \makeatother

    \usepackage{fontspec}
    \setmainfont{Lato Light}[
        BoldFont={Lato Regular},
        ItalicFont={Lato Light Italic},
        BoldItalicFont={Lato Italic}
    ]
    \setsansfont{Exo 2}
    \setmonofont{IosevkaTerm NF}
    ''',
}

latex_documents = [
    ('index', 'outpdfname.tex', project, author, 'manual'),
]