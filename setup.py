# -*- coding: utf-8 -*-
#
# This file is part of Flask-AppFactory
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from setuptools import setup
import os
import re

# Get the version string.  Cannot be done with import!
with open(os.path.join('archivalstorage', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='ArchivalStorage',
    version=version,
    url='http://github.com/inveniosoftware/archivalstorage/',
    license='GPLv3',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description='ArchivalStorage is a API service for storing '
                'archival packages.',
    long_description=open('README.rst').read(),
    packages=['archivalstorage', ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'archivalstorage = archivalstorage.cli:main',
        ]
    },
    install_requires=[
        'Flask>=0.11.dev0',
        'Flask-AppFactory',
        'Flask-Script',
        'Flask-Babel',
        'Flask-SQLAlchemy',
        'Flask-Babel',
        'six',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
)
