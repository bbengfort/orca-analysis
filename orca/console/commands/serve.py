# orca.console.commands.serve
# Run a local web server with visual analysis utilities
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Mon Oct 31 16:43:29 2016 -0400
#
# Copyright (C) 2016 University of Maryland
# For license information, see LICENSE.txt
#
# ID: serve.py [] benjamin@bengfort.com $

"""
Run a local web server with visual analysis utilities
"""

##########################################################################
## Imports
##########################################################################

from commis import Command
from orca.web.app import app
from orca.config import settings

##########################################################################
## Command
##########################################################################

class ServeCommand(Command):

    name = 'serve'
    help = 'run local web server with visual analysis utilities'
    args = {
        '--host': {
            'metavar': 'ADDR',
            'default': settings.web.host,
            'help': 'set the host to run the app on'
        },
        '--port': {
            'metavar': 'PORT',
            'type': int,
            'default': settings.web.port,
            'help': 'set the port to run the app on'
        },
        '--debug': {
            'action': 'store_true',
            'help': 'force debug mode in Flask'
        },
        'database': {
            'nargs': "?",
            'default': settings.database,
            'help': 'the path to the orca database to analyze',
        }
    }

    def handle(self, args):
        """
        Runs the Orca Flask application.
        """
        ## Need to do something with the database path?!

        kwargs = {
            'host': args.host,
            'port': args.port,
            'debug': args.debug or settings.debug,
        }

        app.run(**kwargs)
        return " * Web application stopped"
