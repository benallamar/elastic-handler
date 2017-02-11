# -*- coding : utf-8 -*-
'''
     @project : Elastic-Handler
     @file    : __init__.py
     @author  : Marouane BENALLA
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
'''
from __future__ import unicode_literals

from elasticsearch import Elasticsearch

from exceptions import NoFoundResult
from search_handler import SearchHandler

__all__ = ['ElasticHandler']

# Set the permitted allowed iteration operation type
permitted_iteration_type = ['search', 'fetch']


class ElasticHandler(Elasticsearch):
    """
    A middle class the handle the interaction with ElasticSearch
    :param
        - All the params of the class'll be shown here
    """

    def fetch(self, many=False, **kwargs):
        """ Get many document at once from Elasticsearch """
        if many:
            return self.get(**kwargs)
        else:
            return self.mget(**kwargs)  # Next function

    def init_iterator(self, **kwargs):
        """ Initi search iterator """
        return SearchHandler(es=self, **kwargs)

    def search(self, source_field="hits.hits", **kwargs):
        """ Apply a search DSL """
        _result = super(ElasticHandler, self).search(**kwargs)
        for element in source_field.split('.'):
            _result = _result[element]
        if len(_result) > 0:
            return _result
        else:
            raise NoFoundResult

    def ping(self, params=None):
        """ Check if Elasticsearch is running """
        try:
            super(ElasticHandler, self).ping(params=None)
            return True
        except Exception as e:
            return False

    def list(self, index=None, doc_type=None, doc_id=None, page=0, per_page=10):
        """ List an element of the list """
        if id:
            return self.get(index, doc_id, doc_type=doc_type)
        else:
            if per_page and page:
                _from = int(per_page) * int(page)
            else:
                _from, per_page = 0, 20
            return self.search(index=index, doc_type=type, size=per_page, from_=_from)
