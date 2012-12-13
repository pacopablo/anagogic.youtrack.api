# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>


__all__ = [
    'YTLoginError',
]

class YTLoginError(Exception):
    """Raise when an error is encountered during login

    ``status_code``: the HTTP status code returned by YouTrack
    ``text``: any data returned in the body of the request
    """

    def __init__(self, status_code, text=''):
        self.status_code = status_code
        self.text = text

    def __repr__(self):
        return "YTLoginError(status_code={0})".format(self.status_code)

    def __str__(self):
        return "HTTP Status code: {0}.  HTTP Body length: {1}".format(
                                            self.status_code, len(self.text))

