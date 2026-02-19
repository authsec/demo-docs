Draw.io
=======

To use draw.io diagrams in your documentation, the draw.io extension is required. This extension allows you to include draw.io diagrams directly in your reStructuredText files.

To get some privacy, you can start a local draw.io container with the following :command:`podman` command:

.. code-block:: shell

    #> podman run -it --rm --name="draw" -p 8080:8080 -p 8443:8443 jgraph/drawio

After running the above command, you can access the draw.io interface by navigating to http://localhost:8080 in your web browser. You can create and edit your diagrams there, and once you're done, you can save them to your local machine. Make sure to save the file using the :menuselection:`Where --> Download` location to store the file, and store it in the .drawio format, as this is required for the next steps.

.. image:: img/save-drawio.png
   :alt: Save draw.io diagram

.. note:: Make sure it's not running inside the VScode container, as this will not work.

Save the draw.io file by downloading and copying it into the documentation tree, under say :download:`example.drawio <img/example.drawio>`. Once that's done, the file can be included with the following command:

.. code-block:: reStructuredText

    .. drawio-image:: example.drawio

Which will render the image like this:

.. drawio-image:: img/example.drawio