# -*- coding : utf-8 -*-
'''
     @project : Elastic-Handler
     @file    : __init__.py
     @author  : Marouane BENALLA
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
'''
from os.path import dirname, join

BASE_DIR = dirname(__file__)  # The directory name of the module Elasticsearch

CONFIG_PATH = join(BASE_DIR, 'config')  # The locatioin of the config params
SEARCH_TEMPLATE_PATH = join(BASE_DIR, 'search_template')  # The location of the search templates
