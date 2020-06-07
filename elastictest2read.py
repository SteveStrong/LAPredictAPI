from datetime import datetime
from elasticsearch import Elasticsearch


# https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html
# https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html






def elasticsearch_query():

    #  https://elasticsearch-py.readthedocs.io/en/master/
    # by default we connect to localhost:9200
    es = Elasticsearch()

    indexName = 'la-vern-cases'
    query = {
        "query": {"match_all": {}}
    }

    query = {
        "query": {
            "match": {
                "text": {
                     "query": "inadequate opinion"
                     }
                }
            }
    }


    query = {
        "query": {
            "match": {
                "sentID": {
                     "query": "1302554P20S1"
                     }
                }
            }
    }

    query = {
        "query": {
            "match": {
                "text": {
                     "query": " psychiatric problem in service "
                     }
                }
            }
    }
    
    query = {
        "query": {
            "match": {
                "rhetClass": {
                     "query": "FindingSentence"
                     }
                }
            }
    }

    res = es.search(index=indexName, body=query)
    ## print(res)

    for hit in res['hits']['hits']:
        print(hit["_source"])

# https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-body.html

    print("Got %d Hits:" % res['hits']['total']['value'])
     
elasticsearch_query()