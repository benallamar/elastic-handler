# elastic-handler

A samll layer to interact with Elasticsearch build on the official version (so all the security issues are handled by the officiel version of the library). What make elastichandler more simple and powerful, is the fact that it use the search templates that make your dsl query more simple and easy to manipulate.
## Installation:
To install the package just use the command line pip:
```bash
pip install elastichandler
```
## How to use:
### Project Architect
```
elastic-handler/
  |
  config/
    default.json
  
```
### Configuration:
Most configuration files and search templates are based on tjson format. so all you is a bit knowledge about how to manipulate a json file and it's easy.
By default, the configuration is saved in config/default.json. You have two way to set your configuration, either you update the default.json file, and thus all your elastichandler object will have the same configuration, or you customize the configuration by create a file json for every elasticsearch node handler.
```json
{
  "name": "Elasticsearch",
  "hosts": [
    "your_host_url"
  ],
  "username": "your_user_name",
  "password": "your_password"
}
```
so change the values of every fields to get the same configuration.
#### How can I test my configuration ?
Elastic handler comes with many powerful command lines that helps you configurate, customize and generate all the elastichandler instance files. To have many infomation about the command line you check command line section.
### How to use ElasticHandler object ?
Most of the function of the object are inherited from the elasticsearch object (official version-5.0). But we have through this package to make more powerful in performance. Some times, due to many reason, you want to iterate through your results, instead of download them all into your application.
SearchHandler, is the object that makes the distant iterations more simple, because all you need to do is to use you for boucle, and it's for the search handler object to get the result from the distant server. also, all the extra information (infomration related to the status of the servers, the totals of the answer to your search ...) could be fined very usely as attribute of the instantiate object of searchhandler.
### How to manipulate DSL ?
DSL Handler, is an 
