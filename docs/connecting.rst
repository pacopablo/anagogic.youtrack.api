:Author: John Hampton
:Date: 5/27/15

=====================================
Connecting to a YouTrack Installation
=====================================

The first thing that needs to be done is connecting to a YouTrack installation.
In order to connect, one needs the URL of the YouTrack installation as well as
a username and a password.

.. TODO::
   Find a way to link between the API docs and the references to methods and
   functions below

Credentials may be passed to the call to ``connect()``, pulled from environment
variables, or loaded from a ``.youtrack.creds`` file.  Credentials passed
directly to the call to ``connect()`` will have precedence over the other
methods.  If no credentials are passed, it will then check the environment for
the variables: ``YOUTRACK_USERNAME`` and ``YOUTRACK_PASSWORD``.  If they are not
present, it will look for a ``.youtrack.creds`` file in the user's home
directory.  The ``.youtrack.creds`` file should consist of two lines::

  username = <user>
  password = <password>

Replacing ``<user>`` and ``<password>`` with the appropriate values.  Spaces
around the equals signs are optional and will be stripped.  Trailing spaces on
each line will also be stripped.  This means that your password may not have
leading or trailing spaces.

The ``.youtrack.creds`` file should be protected via appropriate file system
permissions.  For \*nix platforms this can be accomplished via

.. code-block:: sh

   chmod 600 ~/.youtrack.creds

Windows platforms can remove all permissions except for the user's account.

The ``connect()`` function won't check the permissions of the file, so properly
protecting the username and password are user's responsibility.

Examples
--------

Passing credentials directly to the connect function.  Keyword arguments need
not be used:

.. code-block:: pycon

   >>> from anagogic.youtrack.api import connect
   >>> url = 'https://pacopablo.myjetbrains.com/youtrack'
   >>> cnx = connect(url=url, username='testuser', password='yeah, you wish')
   >>> cnx
   Connection('https://pacopablo.myjetbrains.com/youtrack', 'testuser', '******')

Passing credentials via environment variables:

.. code-block:: pycon

   $ YOUTRACK_USERNAME=testuser
   $ YOUTRACK_PASSWORD="yeah, you wish"
   $ python
   [GCC 4.9.2 20150107 (Red Hat 4.9.2-5)] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> from anagogic.youtrack.api import connect
   >>> url = 'https://pacopablo.myjetbrains.com/youtrack'
   >>> cnx = connect(url=url)
   >>> cnx
   Connection('https://pacopablo.myjetbrains.com/youtrack', 'testuser', '******')

Using a ``.youtrack.creds`` file is syntactically identical to the call when
passing credentials via environment variables.  The difference being that
environment variables aren't set and that the ``.youtrack.creds`` file is
located in the user's home directory.



.. TODO::
   Find out what permissions are needed for API access and mention it here