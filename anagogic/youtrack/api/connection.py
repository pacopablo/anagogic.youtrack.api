# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

""" Connection module

    Usage:

    >>> from anagogic.youtrack.api import connect
    >>> url='http://pacopablo.myjetbrains.com/youtrack'
    >>> username = 'testuser'
    >>> password = 'yeah, you wish'
    >>> cnx = connect(url=url, username=username, password=password)
    >>> cnx
    Connection('https://pacopablo.myjetbrains.com/youtrack', 'testuser', '******')

"""
# 3rd Party Imports
import requests

# Local imports
from .errors import YTLoginError

__all__ = [
    'Connection',
]

def connect(url='', username='', password=None):
    """
    :param url: Full URL to the YouTrack instance.  This should be the base url
                of the instance.

    :type url: str
    :param username: Name of the user being user to log in
    :type username: str
    :param password: Password of specified user
    :type password: str
    :return: a Connection() object
    :rtype: :class:`anagogic.youtrack.api.connection.Connection`
    :raises anagogic.youtrack.api.errors.YTLoginEError: On failed login
    """

    return Connection(url, username, password)


class Connection(object):
    """Connection object to a YouTrack instance

    The Connection object logs into the YouTrack instance and caches
    credentials for subsequent requests.

    """

    def __init__(self, url='', user='', passwd=None):
        self.base_url = url.rstrip('/')
        self.cookies = None
        self._get_credentials(user, passwd)
        self.login(user, passwd)

    def _get_credentials(self, user, passwd):
        """  Sets the :attr:`username` and :attr:`password` attributes
        for use by the :meth:`login` method.

        If the user attribute or password are blank, it will first look for
        credentials in the environment and then proceed to look for a
        ``.youtrack.creds`` file located in the user's home directory.

        If both the username and password can't be found in the same location,
        the corresponding attributes will be set to empty strings which should
        cause a login failure.

        :param user: Name of the user being used to log in.
        :type user: str
        :param passwd: Password for the specified user
        :type passwd: str
        """
        self.username = user
        self.password = passwd

    def login(self, user, passwd):
        """ Logs into the YouTrack instance

        The method is called automatically on object instantiation and should
        not need to be called directly.

        :param user: Name of the user being used to log in
        :type user: str
        :param passwd: Password for the specified user
        :type passwd: str
        :raises anagogic.youtrack.api.errors.YTLoginError: if login fails
        """
        url = self.base_url + '/rest/user/login'
        r = requests.post(url, params={'login' : user, 'password': passwd})
        if r.status_code == 200:
            self.cookies = r.cookies
        else:
            raise YTLoginError(r.status_code, r.text)

    def __str__(self):
        return "Connection(url='{}', user='{}', passwd='******')".format(
                            self.base_url, self.username)

    def __repr__(self):
        return "Connection(url='{}', user='{}', passwd='******')".format(
                            self.base_url, self.username)

