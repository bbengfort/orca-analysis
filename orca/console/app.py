# orca.console.app
# Definition of the KeikoUtility app and commands.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Mon Oct 31 16:14:34 2016 -0400
#
# Copyright (C) 2016 University of Maryland
# For license information, see LICENSE.txt
#
# ID: app.py [] benjamin@bengfort.com $

"""
Definition of the KeikoUtility app and commands.
http://bbengfort.github.io/tutorials/2016/01/23/console-utility-commis.html
"""

##########################################################################
## Imports
##########################################################################

from commis import color
from commis import ConsoleProgram

from orca.version import get_version
from orca.console.commands import *

##########################################################################
## Utility Definition
##########################################################################

DESCRIPTION = "Analysis utilities for orca databases"
EPILOG      = "If there are any bugs or concerns, submit an issue on GitHub"
COMMANDS    = [
    InfoCommand,
]

##########################################################################
## The Keiko CLI Utility
##########################################################################

class KeikoUtility(ConsoleProgram):

    description = color.format(DESCRIPTION, color.CYAN)
    epilog      = color.format(EPILOG, color.MAGENTA)
    version     = color.format("keiko.py v{}", color.CYAN, get_version())

    @classmethod
    def load(klass, commands=COMMANDS):
        utility = klass()
        for command in commands:
            utility.register(command)
        return utility
