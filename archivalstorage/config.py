# -*- coding: utf-8 -*-

"""ArchivalStorage configuration."""

from __future__ import absolute_import, unicode_literals, print_function

PACKAGES = [
    "archivalstorage.modules.*",
]

EXTENSIONS = [
    #"flask_babel:Babel",
    #"flask.ext.sqlalchemy:SQLAlchemy",
    "flask_appfactory.ext.jinja2",
    #"flask_appfactory.ext.cache",
    #"flask_appfactory.ext.collect",
    #"flask_appfactory.ext.admin",
    #"flask_appfactory.ext.restful",
    # Security/Login/Principal
    # Flask-Mail
    # Jasmine
    # Breadcrumbs
    # Menu
    # Session
]

# Flask
DEBUG = True

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"

# Flask-Babel
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_TIMEZONE = "utc"

# Flask-Cache
CACHE_TYPE = "simple"

# Flask-Collect
COLLECT_STORAGE = "flask.ext.collect.storage.link"
