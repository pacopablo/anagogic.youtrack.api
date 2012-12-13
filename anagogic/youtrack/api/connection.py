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

    >>> from anagogic.youtrack.api import Connection
    >>> cnx = Connection('http://pacopablo.myjetbrains.com/youtrack', 'apitest', 'this is a test password')
    >>> cnx
    Connection('http://pacopablo.myjetbrains.com', 'apitest', 'this is a test password')

"""
# 3rd Party Imports
import requests

# Local imports
from errors import YTLoginError

__all__ = [
    'Connection',
]


class Connection(object):
    """Connection object to a YouTrack instance

    The Connection object logs into the YouTrack instance and caches
    credentials for subsequent requests.

    """

    def __init__(self, url, user, passwd):
        self.base_url = url.rstrip('/')
        self.cookies = None
        self.login(user, passwd)


    def login(self, user, passwd):
        url = self.base_url + '/rest/user/login'
        r = requests.post(url, params={'login':user, 'password': passwd})
        if r.status_code == 200:
            self.cookies = r.cookies
        else:
            raise YTLoginError(r.status_code, r.text)
