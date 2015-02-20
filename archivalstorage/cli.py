# -*- coding: utf-8 -*-

"""Command line interface for ArchivalStorage."""

from __future__ import absolute_import, unicode_literals, print_function

from flask_appfactory.cli import create_cli
from .app import create_app


cli = create_cli(create_app)


def main():
    """Management script for the Archival Storage application."""
    cli()
