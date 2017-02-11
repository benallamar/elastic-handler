# Charlie - ElasticHandler:
##ElasticHandler:
Inherite from the the Elasticsearch package(which is the officiel distribution from the elasticsearch company).
###Methods:
#### save:

The function save is the function handling the indexation of the documents and the data in elasticsearch.
Parms:
    * _file_config: is the file configurations of the data that should be stored.
    exmple:
```json
{
  "name": "red",
  "separated": true,
  "fields": {
    "armed_id": {
      "index": "your_index",
      "type": "red",
      "primary_key": true
    },
    "name":{
      "index":"your_index",
      "type":""
    }
  }
}
```
every time this params has been given, there no need for the rest of the params, exept t∞∞∞∞∞∞………÷t‘‘““he body which is so important.