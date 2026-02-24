Tagging
=======

You can tag xlinks too, to make the filter system even more powerful. This allows you to categorize links based on specific topics or themes, making it easier for readers to find relevant links.

To avoid typos and inconsistencies, you can define your tags in your `conf.py` file. This way, you can ensure that all tags are used consistently throughout your documentation.

Tags are optional to an xlink entry, but if you want to use them, you can define them in your `conf.py` like this, where the first entry is the tag name and the second entry is the human-readable label for that tag, when rendered out in a xlink-list:

.. code-block:: python

   xlink_allowed_tags = {
    'threat-model': 'Threat Model',
    'architecture': 'Architecture Notes',
    'api': 'API Specifications'
   }
