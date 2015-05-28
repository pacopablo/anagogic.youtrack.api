.. YouTrack API documentation master file, created by
   sphinx-quickstart on Wed May 27 16:47:13 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Anagogic YouTrack API Wrapper documentation!
============================================

YouTrack_ is an awesome issue tracking system developed by JetBrains_.  It has
a decent API_ and even has a `Python client library`_.  The problem with the
library is that it's not available via PyPI and can't be easily installed via
normal Python package management (think pip, setup.py install, etc.).  It is
also not compatible with Python 3.

This project is an attempt to create a more Pythonic wrapper for the YouTrack_
API.  Currently the wrapper is Python 3.4 only.  Once it's complete, I'll worry
about Python 2.x compatibility.

Installation
------------

.. attention::
   anagogic.youtrack.api has not been uploaded to PyPI yet and therefore is
   only available via source download.

The easier way to install is to use ``pip``.

.. code-block:: sh

   pip install anagogic.youtrack.api


Or one can install the development branch

.. code-block:: sh

   pip install git+https://github.com/pacopablo/anagogic.youtrack.api.git


To install from source, download the code and extract it to a directory.
Change into unpacked directory and run:

.. code-block:: sh

   python setup.py install


Contents:
---------

.. toctree::
   :maxdepth: 2

   connecting
   api_reference
..   users
..   projects
..   issues



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. links:

.. _YouTrack: https://www.jetbrains.com/youtrack/
.. _JetBrains: https://www.jetbrains.com/
.. _API: https://confluence.jetbrains.com/display/YTD6/YouTrack+REST+API+Reference
.. _Python client library: https://github.com/JetBrains/youtrack-rest-python-library/