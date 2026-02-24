Grouping
========

You can group links by file. This is useful when you have a large number of links and want to organize them by their source file. You can also sort the links within each group by title, description, or any other metadata.

By File and Title
-----------------

.. xlink-list::
   :group-by: file
   :files: protocols, plantuml
   :sort-by: title
   :order: asc

By Tag and ID
-------------

.. xlink-list::
   :group-by: tag
   :files: protocols, plantuml
   :sort-by: id
   :order: desc

By Tag then File
----------------

.. xlink-list::
   :group-by: tag, file
   :files: protocols, plantuml
   :sort-by: id
   :order: asc

By File, then Tag
-----------------

.. xlink-list::
   :group-by: file, tag
   :files: protocols, plantuml
   :sort-by: title
   :order: asc
