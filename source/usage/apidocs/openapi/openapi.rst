.. index:: OpenAPI Documentation, API Documentation; OpenAPI


OpenAPI Documentation
=====================

You can find the OpenAPI documentation at https://sphinxcontrib-openapi.readthedocs.io/

You can use https://sphinxcontrib-openapi.readthedocs.io/en/latest/ to generate API documentation from OpenAPI specifications. This allows you to create comprehensive and interactive API documentation for your project.

We're going to look at the following JSON file as an example:

.. openapi:: tictactoe.json

Visualizing the API
-------------------

With the PlantUML extension, we can fairly easily generate diagrams from the OpenAPI specification. This can be a great way to visualize the structure of your API and how different endpoints relate to each other.

.. raw:: latex

   \begin{landscape}

.. uml:: tictactoe.puml

.. raw:: latex

   \end{landscape}
