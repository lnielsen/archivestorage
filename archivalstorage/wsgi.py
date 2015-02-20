# -*- coding: utf-8 -*-

"""WSGI application."""

from __future__ import absolute_import, unicode_literals, print_function

from archivalstorage.app import create_app

application = create_app()
