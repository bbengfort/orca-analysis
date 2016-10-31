# orca.config
# Confire configuration for analysis.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Mon Oct 31 16:50:00 2016 -0400
#
# Copyright (C) 2016 University of Maryland
# For license information, see LICENSE.txt
#
# ID: config.py [] benjamin@bengfort.com $

"""
Confire configuration for analysis.
"""

##########################################################################
## Imports
##########################################################################

import os
import confire


##########################################################################
## Configuration
##########################################################################

class WebConfiguration(confire.Configuration):
    """
    Configuration for the web visual UI
    """

    host = "127.0.0.1"
    port = 5000


class KeikoConfiguration(confire.Configuration):
    """
    Meaningful defaults and required configuration
    """

    CONF_PATHS = [
        "/etc/keiko.yml",                        # System configuration
        os.path.expanduser("~/.orca/keiko.yml"), # User specific config
        os.path.abspath("conf/keiko.yml"),      # Local configuration
    ]

    # whether or not we're in debug mode
    debug    = True

    # path to the orca sqlite3 database
    database = os.path.expanduser(os.path.join("~", ".orca", "orca.db"))

    # the web application configuration
    web      = WebConfiguration()


## Load settings immediately for import
settings = KeikoConfiguration.load()

if __name__ == '__main__':
    print(settings)
