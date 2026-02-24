Downloadable Bookmarks
======================

You can download xlink-lists as bookmarks files that can be imported into your browser. This is useful for sharing collections of links with others or for keeping a backup of your links.

The same filters can be applied to the bookmark export as well. For example, you can export only links that start with a specific ID prefix or that belong to certain files.

Download DocDash Links
----------------------

.. xlink-list:: 
   :files: docdash
   :sort-by: title
   :order: asc

.. xlink-list:: 
   :files: docdash
   :sort-by: title
   :order: asc
   :download-as-bookmarks: DocDash Links

Download All Links in Project
-----------------------------

By Tag
""""""

.. xlink-list::
   :group-by: tag

.. xlink-list::
   :group-by: tag
   :download-as-bookmarks: All Links in Project by Tag

By Tag, Then File
"""""""""""""""""

.. xlink-list::
   :group-by: tag, file

.. xlink-list::
   :group-by: tag, file
   :download-as-bookmarks: All Links in Project by Tag, then File

All IDs containing
""""""""""""""""""

Download all links with IDs containing 'definition' anywhere in the ID.

.. xlink-list::
   :id-filter-regex: .*-definition.*
   :group-by: file, tag
   :files: protocols, plantuml
   :sort-by: title
   :order: asc

.. xlink-list::
   :id-filter-regex: .*-definition.*
   :group-by: file, tag
   :files: protocols, plantuml
   :sort-by: title
   :order: asc
   :download-as-bookmarks: All Protocol, PlantUML definitions





Sectioning
----------

.. xlink-list::
   :files: protocols, markup-languages
   :id-starts-with: wikipedia-
   :group-by-file:
   :sort-by: id
   :order: asc
