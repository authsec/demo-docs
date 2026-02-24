Filtering
=========

ID Starting with
----------------

Here we list bookmarks with IDs starting with 'docdash-'.

.. xlink-list::
   :id-filter-regex: ^docdash-
   :group-by: file, tag
   :sort-by: title
   :order: asc

ID Containing
-------------

Here we list bookmarks with IDs containing 'definition' anywhere in the ID.

.. xlink-list::
   :id-filter-regex: .*-definition.*
   :group-by: file, tag
   :files: protocols, plantuml
   :sort-by: title
   :order: asc

Files containing tag
--------------------

Search for tags 'threat-model' and 'api' in files 'protocols' and 'plantuml'.

.. xlink-list::
   :files: protocols, plantuml
   :tags: threat-model, api

Files containing tag grouped by tag
-----------------------------------

Search for tags 'threat-model' and 'api' in files 'protocols' and 'plantuml'.

.. xlink-list::
   :files: protocols, plantuml
   :group-by: tag
   :tags: threat-model, api
   :order: desc