# Orca Analysis

[![Orca Image](fixtures/orca.jpg)](https://flic.kr/p/6dV2wi)

**Analysis utilities for Orca databases**

Provides console utilities to manage orca generated sqlite databases and to aggregate and analyze them. Additionally the application supports a web application that can be locally run to provide interactive analysis of an orca database file. This is not intended for production deployment, but rather effective analysis of orca latency experiment results.

## Getting Started

By default, the orca commands operate on a database stored at `~/.orca/orca.db`. You can modify this and other settings by copying the `keiko-example.yml` file to `~/.orca/keiko.yml` and modifying the configuration. Additionally, you can pass in arguments to the command line for dynamic analysis.

## Basic Usage

To get a text report of the current state of the orca database:

    $ python3 keiko.py info path/to/orca.db

To run the local web server for interactive analysis:

    $ python3 keiko.py serve path/to/orca.db

Note that in both those commands, if the path to the database is ommited, the app will look in `~/.orca/orca.db` for the database.
