# -*- coding: utf-8 -*- 
"""
     @project : Json-GENERATOR
     @file    : json_generator
     @author  : Marouane BENALLA    
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
"""
from os.path import join

from helpers import get_path

SEARCH_TEMPLATE_PATH = "../templates"


def _string_splitter(string, delimiter=" "):
    return string.split(delimiter)


def _params_generator(json_template, abs_path=SEARCH_TEMPLATE_PATH, **kwargs):
    """ Generate the search params DSL for elasticsearch using a prepared template """
    import json
    return json.loads(_json_generator(join(abs_path, json_template), **kwargs))


def _line_generator(split_text, **kwargs):
    """ Generate line if does contain variable to be handled """
    _final_line = ''
    if len(split_text) > 1:
        for word in split_text:
            if '<' not in word and '>' not in word:
                value = kwargs.pop(word.replace(' ', ''), None)
                if value is not None:
                    if type(value) in [unicode, int, str]:
                        _final_line += '"' + str(value) + '"'
                    else:
                        _final_line += str(value)
                else:
                    raise AttributeError('Params missing {}'.format(word))
            else:
                _final_line += word.replace('<', '').replace('>', '')
    else:
        _final_line = split_text[0]
    return _final_line


def _json_generator(file_path, abs_path=None, **kwargs):
    """
    Generate json file based on the  given path of the template
    :param file_path:
    :param abs_path:
    :param kwargs:
    :return:
    """
    _final_string = ''
    if abs_path:
        _file_path = abs_path + file_path
    else:
        _file_path = file_path
    with open(_file_path + '.json', 'r+') as json_template:
        for line in json_template:
            _split_line = _string_splitter(line, delimiter='%')
            _final_string += _line_generator(_split_line, **kwargs) + '\n'
    return _final_string


def _json_loader(abs_path=None, _file=None, filename=None):
    """ Load the json file """
    import json
    if _file:
        return json.load(_file)
    elif filename:
        return json.load(open(get_path(abs_path, filename) + '.json'))
