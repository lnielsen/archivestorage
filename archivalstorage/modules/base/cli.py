# -*- coding: utf-8 -*-

import click

from flask.cli import FlaskGroup

def _initdb():
    print "Init DB"


def setup(app):

    @app.cli.command()
    def initdb():
        return _initdb()
