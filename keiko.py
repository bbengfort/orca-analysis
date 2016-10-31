#!/usr/bin/env python3
# keiko
# Command line utility to perform analyses.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Mon Oct 31 16:06:13 2016 -0400
#
# Copyright (C) 2016 University of Maryland
# For license information, see LICENSE.txt
#
# ID: keiko.py [] benjamin@bengfort.com $

"""
Command line utility to perform analyses.
"""

##########################################################################
## Imports
##########################################################################

from orca.console.app import KeikoUtility

##########################################################################
## Load and execute the CLI utility
##########################################################################

if __name__ == '__main__':
    app = KeikoUtility.load()
    app.execute()
