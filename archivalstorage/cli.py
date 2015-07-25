# -*- coding: utf-8 -*-

"""Command line interface for ArchivalStorage."""

from __future__ import absolute_import, unicode_literals, print_function

from flask_appfactory.cli import clifactory
from .app import create_app

cli = clifactory(create_app)


def main():
    """Management script for the Archival Storage application."""
    cli()
