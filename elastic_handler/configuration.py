# -*- coding : utf-8 -*-
'''
     @project : Elastic-Handler
     @file    : __init__.py
     @author  : Marouane BENALLA
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
'''
from exceptions import ConfigParamsMissing
from json_generator import _params_generator as params_generator

"""
The aim of this module is to create a configuration interface to elasticsearch to simplify it.
the configuration is done automatically all you have to do is to check the config files that you'll find in
config folder.
For the time being the module doens't check if you have put the correct configuration so please check every time that at least
you json config files is correct.

"""

CONFIG_PATH = 'config/'


class ElasticConfig(dict):
    """
    The aim of this class is to handle the configuration file of Elasticsearch.
    The provided operations are:
        - Check the Configuration.
        - Serialize the Configuration.
    All the configuration file should be saved in the config files within the elastic_handler module
    """

    def __init__(self, *args, **kwargs):
        _config = kwargs.pop('_type', None)
        if _config is not None:
            self._config = params_generator(_config, abs_path=CONFIG_PATH)
            print self._config
        else:
            raise ConfigParamsMissing

    @property
    def serialize(self):
        """ Rendre the configuration into a serializable object"""
        return self._config
