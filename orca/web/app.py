# orca.web.app
# Implements a Flask application for the interactive analysis UI.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Mon Oct 31 17:06:14 2016 -0400
#
# Copyright (C) 2016 University of Maryland
# For license information, see LICENSE.txt
#
# ID: app.py [] benjamin@bengfort.com $

"""
Implements a Flask application for the interactive analysis UI.
"""

##########################################################################
## Imports
##########################################################################

import orca

from orca.config import settings

from flask import Flask

##########################################################################
## Flask Application
##########################################################################

# set up an app instance
app = Flask(__name__)

# set debug to true to get debug pages when there is an error
app.debug = settings.debug
