# -*- coding : utf-8 -*-
'''
     @project : Elastic-Handler
     @file    : __init__.py
     @author  : Marouane BENALLA    
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
'''

from collections import Iterable

from elastic_handler import NoFoundResult

permit_key = ['per_page', 'page', 'index', 'type']


def _filter_response(response, iteration_params):
    _response = []
    return _response


def _get_the_best(_results):
    pass


class SearchHandler(Iterable):
    def __init__(self, es=None, page=1, max_page=1, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.iteration_params, self.es, self.page, self.max_page = kwargs.copy(), es, page, max_page

    @property
    def count_params(self):
        _iteration_params = self.iteration_params.copy()
        _iteration_params.pop('_source_include')
        return _iteration_params

    def count(self):
        return self.es.count(**self.count_params)['count']

    def __iter__(self):
        return self

    # Return the iteration among the list
    def next(self):
        try:
            # check the type of the operatio)n to do
            if self.page <= self.max_page:
                _result = self.es.search(**self.iteration_params)
                self.page += 1
                return _result
            else:
                raise StopIteration
        except:
            raise StopIteration

    @property
    def max_score(self):
        try:
            return self.es.search(size=self.per_page,
                                  **self.iteration_params)['_max_score']
        except NoFoundResult:
            return 0

    def set_next(self):
        if self.page < self.max_page:
            self.page += 1
        else:
            raise StopIteration
        self.iteration_params['from_'] = self.page * self.per_page
