# orca.console.commands.info
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

import os
import sqlite3

from commis import Command
from commis.exceptions import ConsoleError


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

        # Ensure the path to the database exists
        dbpath = args.database[0]
        if not os.path.exists(dbpath) or not os.path.isfile(dbpath):
            raise ConsoleError(
                "'{}' is not a valid path to a sqlite3 database".format(dbpath)
            )

        try:
            # Connect to the database
            self.conn = sqlite3.connect(dbpath)
        except Exception as e:
            raise CommandError(str(e))

        # Construct the output
        output = []

        # Count the number of rows in the database
        output.append(
            "Database contains {:,} pings in {:,} locations between {:,} devices.".format(
                self.count_table('pings'), self.count_table('locations'), self.count_table('devices')
            )
        )

        # Return the output
        return "\n".join(output)

    def count_table(self, table):
        """
        Returns the number of rows in the specified table.
        """
        sql = "SELECT count(id) FROM {}".format(table)
        cur = self.conn.cursor()
        cur.execute(sql)

        return cur.fetchone()[0]
