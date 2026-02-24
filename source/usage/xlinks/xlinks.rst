.. index:: xlinks, bookmark list

.. _xlinks:

******
xlinks
******

Xlinks are a powerful feature that allows you to manage external links in a centralized way. With xlinks, you can define a list of links in separate files and reference them throughout your documentation by using an identifier.

This makes it easier to maintain and update links, as you only need to change them in one place.

Aside from the central management of links, xlinks also provides features such as grouping, sorting, and filtering of links. This can be particularly useful when you have a large number of links to manage. 

To make links easily accessible to your reader, you can also generate a bookmark list of all the links defined in your xlink files. This allows readers to quickly find and navigate to the links they are interested in.

When you roll your own, this is how you can test the extension in the container, by doing:

.. code-block:: shell

   #> pip install --no-cache-dir --upgrade "sphinxcontrib-xlink @ git+https://github.com/authsec/sphinxcontrib-xlink" && make clean html

xlink file format
=================

An ``.xlink`` file is a simple text file that contains a list of links, each defined by a unique identifier and its associated metadata. The format of an xlink file is as follows:

.. code-block:: text

   # xlink-section-name: PlantUML
   # id :: title :: url (:: tags)
   plantuml-home :: PlantUML at a Glance :: https://plantuml.com/ :: threat-model

Lines starting with a :code:`#` are comments and are ignored by the extension. One of the first lines of the file can optionally define a section name for the links in that file, which can be used for grouping purposes when rendering the links in a list, or exporting them as bookmarks.

Adding tags to the entry is optional, but it can be useful for categorizing links and making them easier to filter and organize. Tags are defined as a comma-separated list of keywords at the end of the line, after the URL.

For a tag to be valid, it must be defined in the `xlink_allowed_tags` dictionary in your `conf.py` file. This ensures that only predefined tags are used, which helps to avoid typos and maintain consistency.

xlink Options
=============

The `xlink` directive supports several options that allow you to customize how the links are displayed and organized. Some of the key options include:

:group-by-file: Group links by their source file.
:sort-by: Sort links by a specific metadata field (e.g., title, description).
:order: Specify the sort order (asc or desc).
:id-starts-with: Filter links by their ID prefix.
:class: Add a CSS class to the generated list for custom styling.
:latex-show-urls: footnote

You can use them like this:

- :xlink:`sphinx-ref`
- :xlink:`Some Setup~@~docdash-setup` 
- :xlink:`Some New Setup <docdash-setup>`

.. toctree::
   :hidden:

   tagging
   sorting
   grouping
   custom-style
   bookmarks
   filtering
   latex-export