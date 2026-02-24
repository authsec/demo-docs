Custom List Styling
===================

If you want to make a list stand out, you can apply custom CSS styling to it. This can be done by adding a CSS class to the list and defining the styles in your CSS file. For example, you could create a class called "important-links" and style it with a different background color or font size to make it more noticeable.

.. code-block:: rst

   .. xlink-list::
      :files: protocols
      :id-starts-with: wikipedia-
      :class: my-custom-list
      :sort-by: title

You need a class entry in your custom CSS file (at :file:`source/_static/css/custom.css`) like this:

.. code-block:: CSS

   .my-custom-list ul {
      font-family: 'Orbitron', Georgia,Arial,sans-serif;
      list-style-type: square;
      background: #ffd175;
      padding: 10px;
   }

Will give this output: 

.. xlink-list::
   :files: protocols
   :id-starts-with: wikipedia-
   :class: my-custom-list
   :sort-by: title

Rendering the Link Icon
-----------------------

If you want to render the link icon (with the HTML builder) next to each link, you can use the `:render-link-icon:` option. This will add a small icon next to each link, making it easier for readers to identify them as links.

This is on by default, if you use the `:xlink:` role, and can be turned off by setting the following in your conf.py:

.. code-block:: python

   # Inline role: :xlink:`key` (Default: True)
   xlink_render_link_icon = False

You can also control the rendering of the link icon in the `xlink-list` directive by setting the following option for a specific list:

.. code-block:: rst

   .. xlink-list::
      :render-link-icon: true

Which will give you this output:

.. xlink-list::
   :render-link-icon: true

