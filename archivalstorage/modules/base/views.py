# -*- coding: utf-8 -*-

"""Define base Blueprint."""

from __future__ import absolute_import, unicode_literals, print_function

from flask import Blueprint

blueprint = Blueprint(
    'base',
    __name__,
    template_folder='templates',
    static_folder='static'
)
