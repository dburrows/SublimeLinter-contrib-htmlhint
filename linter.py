#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by David Burrows
# Copyright (c) 2014 David Burrows
#
# License: MIT
#

"""This module exports the Htmlhint plugin class."""

from SublimeLinter.lint import Linter, util


class Htmlhint(Linter):

    """Provides an interface to htmlhint."""

    syntax = 'html'
    cmd = 'htmlhint @'
    regex = r'^\s*line (?P<line>\d+), col (?P<col>\d+): (?P<message>.+)'
