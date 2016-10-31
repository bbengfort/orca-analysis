# orca.console.info
# The info command returns a text report of a single orca database.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Mon Oct 31 16:20:58 2016 -0400
#
# Copyright (C) 2016 University of Maryland
# For license information, see LICENSE.txt
#
# ID: info.py [] benjamin@bengfort.com $

"""
The info command returns a text report of a single orca database.
"""

##########################################################################
## Imports
##########################################################################

from commis import Command


##########################################################################
## Command
##########################################################################

class InfoCommand(Command):

    name = "info"
    help = "describe a single orca database as a text report"
    args = {
        'database': {
            'nargs': 1,
            'help': 'the path to the orca db',
        }
    }

    def handle(self, args):
        """
        Handles the info report
        """
        return "hello world"
