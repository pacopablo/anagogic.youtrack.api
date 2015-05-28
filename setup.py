# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

from setuptools import setup, find_packages
#from distutils.core import setup

setup(
    name = 'anagogic.youtrack.api',
    version = '0.4.3',
    description = 'Python client for JetBrains\' YouTrack REST API',
    author = 'John Hampton',
    author_email = 'pacopablo@pacopablo.com',
    maintainer = 'John Hampton',
    maintainer_email = 'pacopablo@pacopablo.com',
    license = 'MIT',
    packages = [
            'anagogic.youtrack.api',
    ],
)
