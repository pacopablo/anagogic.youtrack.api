:Author: John Hampton
:Date: 5/28/15

===========
Development
===========

.. TODO::

   Figure out a workflow with Docker for development and testing

Setup Environment
-----------------

After cloning the code repository_, setting up development should be as easy as
using pip to install a requirements file.

.. code-block:: sh

   $ clone https://github.com/pacopablo/anagogic.youtrack.api.git
   $ cd anagogic.youtrack.api
   $ pyvenv env
   $ pushd env
   $ source bin/activate
   $ popd
   $ pip install -t requirements_dev.txt
   $ python setup.py develop


Run Tests
---------

Assuming one has created a virtual environment and has activated said
environment, the tests can be run via:

.. code-block:: sh

   $ python setup.py test

Alternately, tests can be run by calling ``py.test``

.. code-block:: sh

   $ py.test



.. links:

.. _repository: https://github.com/pacopablo/anagogic.youtrack.api