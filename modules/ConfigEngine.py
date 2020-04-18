#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import os
from configparser import ConfigParser

config_file = os.path.join(os.path.dirname(__file__), '../config.ini')


def get_config(section, option):
    parser = ConfigParser()
    parser.read(config_file)
    return parser.get(section, option)


def get_config_boolean(section, option):
    parser = ConfigParser()
    parser.read(config_file)
    return parser.getboolean(section, option)
