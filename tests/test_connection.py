# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>
import responses
import pytest
from anagogic.youtrack.api import connect
from anagogic.youtrack.api.errors import YTLoginError

YOUTRACK_BASE_URL = 'http://localhost:8081'
LOGIN_PATH = '/rest/user/login'

@responses.activate
def test_connect_success():
    """ Test successful connection """

    responses.add(responses.POST, YOUTRACK_BASE_URL + LOGIN_PATH,
                  body='<login>Ok</login>', status=200,
                  content_type='application/xml;charset=UTF-8')

    cnx = connect(YOUTRACK_BASE_URL, username='testuser',
                  password='yeah, you wish')

    assert str(cnx) == \
           "Connection(url='{}', user='testuser', passwd='******')".format(
            YOUTRACK_BASE_URL)


@responses.activate
def test_connect_failure():
    """ Test failed connection """

    responses.add(responses.POST, YOUTRACK_BASE_URL + LOGIN_PATH,
                 body='<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                      '<error>Incorrect login or password.</error>',
                 status=403)
    with pytest.raises(YTLoginError):
        cnx = connect(YOUTRACK_BASE_URL, username='testuser',
                      password='this is not the correct password')



"""
HTTP/1.1 200 OK
Expires: Thu, 01-Jan-1970 00:00:00 GMT
Set-Cookie: JSESSIONID=n7hq7t8o49ae15sgbq5hn9ic;Path=/
Set-Cookie: jetbrains.charisma.main.security.PRINCIPAL=NDgxMzQ5NGQxMzdlMTYzMWJiYTMwMWQ1YWNhYjZlN2JiN2FhNzRjZTExODVkNDU2NTY1ZWY1MWQ3Mzc2NzdiMjpyb290;Path=/;Expires=Thu, 12-May-2011 16:37:10 GMT
Content-Type:
Transfer-Encoding: chunked
Server: Jetty(6.1.23)

<login>ok</login>
"""