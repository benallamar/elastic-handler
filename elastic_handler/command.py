# -*- coding: utf-8 -*- 
"""
     @project : elastic-handler
     @file    : command
     @author  : Marouane BENALLA    
     @email   : marouan.benalla@gmail.com
     @company : bubble tech
"""
"""
Here the command to interact with ElasticSearch
    @mode: -u                               the mode upload
        @param: --input                     the name of the file to be uploaded
    @mode: -d                               the mode download
        @param: --output                    The output filename


    Common Params:
        @param: --host                      the host to interact with - by default localhost
        @param: --port                      the post to interact with - by default 9200
        @param: --index                     the indexes' list to be download     - No param is by default
        @param: --doc_typ                   the doc_type to download  - Could be null
        @param: --exclude_fields            list field to exlude from the processing
        @param: --size                      the number of the document to handle
        @param: --from                      Accepting the pagination
        @param: --all                       if this params is activated (--size and --from will be disabled)
"""


class CommandParser:
    mode = 'd'
    params = dict()

    def __init__(self, *args):
        """ Generate a command parser through the argument given by the user """
        pass
