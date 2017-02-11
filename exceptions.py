# -*- coding : utf-8 -*-
'''
     @project : Elastic-Handler
     @file    : __init__.py
     @author  : Marouane BENALLA    
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
'''

__all__ = ['NoBodyGiven', 'ElasticIsOff', 'SearchHasNotBeenInitiated', 'NoFoundResult', 'NotPermittedParams']


class NoMatchFileType(Exception):
    message = "the given type doesnt match with the file, please check either your file or the type"

    def __str__(self):
        return self.message


# Exceptions for ElasticSearchHandler
class NoBodyGiven(Exception):
    message = "No Array body was given"

    def __str__(self):
        return self.message


class ElasticIsOff(Exception):
    message = "ElasticSearch is off, please turn it on"

    def __str__(self):
        return self.message


class SearchHasNotBeenInitiated(Exception):
    message = "Please make sure you have well initiated your search params"

    def __str__(self):
        return self.message


class InvalidQueryError(Exception):
    message = "Your Query is invalid"

    def __str__(self):
        return self.message


class NoFoundResult(Exception):
    message = "No search result"

    def __str__(self):
        return self.message


class NotPermittedParams(Exception):
    message = "Wrong given params"

    def __str__(self):
        return self.message


# Exceptions for Configuration Handler
class ConfigError(Exception):
    message = "ElasticSearch is off, please turn it on"

    def __str__(self):
        return self.message


# For the configuration classes
class ConfigParamsMissing(Exception):
    message = "No configuration file directory has been given"

    def __str__(self):
        return self.message


# For functions
class MissingParams(Exception):
    message = "The type file is wrong, or some configuration params are missing"

    def __str__(self):
        return message
