# -*- coding: utf-8 -*-

"""Application factory for ArchivalStorage."""

from __future__ import absolute_import, unicode_literals, print_function

from flask_appfactory import appfactory


def create_app(**kwargs_config):
    """Application factory for Archival Storage."""
    return appfactory(
        'archivalstorage',
        'archivalstorage.config',
        **kwargs_config
    )
