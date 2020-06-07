from datetime import datetime
from elasticsearch import Elasticsearch


# https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html
# https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html



def elasticsearch_publish():

    #  https://elasticsearch-py.readthedocs.io/en/master/
    # by default we connect to localhost:9200
    es = Elasticsearch()
    
    indexName = 'la-vern-cases'
    
    # Imports of import.
    import json
    import os
        

    # Getting the list of files in <data_path>:
    data_path = './data/Pickling/'
    list_of_files = os.listdir(data_path)

    # ...and creating new lists for the texts of the sentences...
    index = 0
    
    print(len(list_of_files))
    # Using a for-loop to iterate over the filenames...
    for filename in list_of_files:
        print ( filename )

        # ... and opening the given filename...
        file = open(data_path + filename)
        
        # ...using the json file loader to translate the json data...
        data = json.load(file)

        # ...and adding the sentences to those new lists...
        for sentence in data['sentences']:
            sentenceNumber = int(sentence['sentenceNumber'])
            paragraphNumber = int(sentence['paragraphNumber'])
            

            res = es.index(index=indexName, id=index, body=sentence)
            
            index += 1

            
elasticsearch_publish()
