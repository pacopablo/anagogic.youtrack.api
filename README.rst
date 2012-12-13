anagogic.youtrack.api
======================

Python Client for JetBrains' YouTrack REST API

Introduction
-------------

JetBrains does provide a Python library for YouTrack [#]_.  Unfortunately, it
isn't available via PyPi.  It doesn't have a ``setup.py`` file, so making it
available for other scripts is tedius at best.  The library itself doesn't
feel Pythonic and the documentation is poor.

Changes could be done in the library itself.  However, the extent of the
changes will constitute a rewrite.  Maybe in the future this will become the
official Python client library.


Installation
--------------

Use ``pip``.

.. code-block:: sh

   pip install git+https://github.com/pacopablo/anagogic.youtrack.api.git

Once a release is made to PyPi, one will be able to simply ``pip install anagogic.youtrack.api``

To install from source, download the code and extract it to a directory.  
Change into unpacked directory and run:

.. code-block:: sh

   python setup.py install


Usage
------

.. code-block:: python

   >>> from anagogic.youtrack.api import Connection
   >>> cnx = Connection('<url to YouTrack instance', 'username', 'password')

The full API docmumentation can be found at:

.. TODO: put documentation on read the docs or in gh-pages





.. rubric:: Footnotes

.. [#] https://github.com/JetBrains/youtrack-rest-python-library
