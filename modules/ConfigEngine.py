#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import os
from configparser import ConfigParser


class BaseConfigEngine:
    def __init__(self):
        self._config_file = os.path.join(
            os.path.dirname(__file__), '../config.ini')

        self.parser = ConfigParser()
        self.parser.read(self._config_file)

    def get_config(self, section, option):
        return self.parser.get(section, option)

    def get_config_boolean(self, section, option):
        return self.parser.getboolean(section, option)


class TwitterAPIConfig(BaseConfigEngine):
    def __init__(self):
        super().__init__()

    @property
    def user_id(self):
        return self.get_config('TwitterAPI', 'user_id')

    @property
    def consumer_key(self):
        return self.get_config('TwitterAPI', 'consumer_key')

    @property
    def consumer_secret(self):
        return self.get_config('TwitterAPI', 'consumer_secret')

    @property
    def access_token(self):
        return self.get_config('TwitterAPI', 'access_token')

    @property
    def access_token_secret(self):
        return self.get_config('TwitterAPI', 'access_token_secret')

    @property
    def app_name(self):
        return self.get_config('TwitterAPI', 'app_name')

    @property
    def preview_id(self):
        return self.get_config('TwitterAPI', 'preview_id')

    @property
    def account_name(self):
        return self.get_config('TwitterAPI', 'account_name')
