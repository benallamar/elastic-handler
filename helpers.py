# -*- coding : utf-8 -*-
'''
     @project : Elastic-Handler
     @file    : __init__.py
     @author  : Marouane BENALLA
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
'''
from __future__ import unicode_literals

from os.path import join

__all__ = ['_upload_process']
permitted_get_params = ['id', 'index', 'type', '_all', '_token']


def get_field(_list, parent=None, key=None):
    _tmplist = _list
    if key:
        if parent:
            for field in parent.split('.'):
                _tmplist = _tmplist[field]
            return _tmplist[key]
        else:
            return _list[key]
    else:
        raise ValueError('the key params has not been given')


# Extract the source from ElasticSearch search result
def _extract_source(es_result):
    """ Extract the source from ElasticSearch """
    return es_result['_source']

    return _final_string


# Return an array of the splitted text, using the delimiter char
def _string_splitter(string, delimiter=' '):
    '''
    :param string:
    :return:
    '''
    return string.split(delimiter)


def _find(list, _value=None):
    """ Find the keys with the values _value """
    _found = {}
    for key, value in list.items():
        if value == _value:
            _found[key] = value
    return _found


def get_path(config_path, filename_):
    """ Get the join path """
    return join(config_path, filename_)


def _filter_fields(fields, filter_fields):
    """ Filte some fields"""
    _result = {}
    if fields.has_key('token'):
        _result['token'] = fields['token']
    for index, value in fields.items():
        if index in filter_fields:
            _result[index] = fields[index]
    return _result
