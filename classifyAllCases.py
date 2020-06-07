import os
import json
import logging

from nlp_engine import NLPEngine

# https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html
# https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html


#   capturePredictionData(item) {
#     this.rhetClassPredict = item.classification;
#     const keys = Object.keys(item.predictions);

#     const list = [];
#     keys.forEach(key => {
#       const data = 10000 * parseFloat(item.predictions[key]);
#       const obj = {
#         name: key,
#         value: Math.round(data) / 100
#       };
#       list.push(obj);
#     });

#     this.predictions = list.sort((a, b) => b.value - a.value);
#     return this.predictions;
#   }

def mergePrediction(sentence, prediction):
    sentence['rhetClassPredict'] = prediction['classification']
    predictions = prediction['predictions']

    #can we sort and simplify?  or wait until loaded
    sentence['modelUsed'] = prediction['name']
    sentence['predictions'] = predictions



def classifyAll():
    
    nlp = NLPEngine().createModel("original")


    # Getting the list of files in <data_path>:
    data_path = './data/semanticCase/'
    target_path = './data/predictedCase/'
    list_of_files = os.listdir(data_path)

    # ...and creating new lists for the texts of the sentences...
    index = 0
    
    print(len(list_of_files))
    # Using a for-loop to iterate over the filenames...
    for filename in list_of_files:
        # print ( filename )

        # ... and opening the given filename...
        file = open(data_path + filename)
        
        # ...using the json file loader to translate the json data...
        data = json.load(file)

        
        # ...and adding the sentences to those new lists...
        for sentence in data['sentences']:
            text = sentence['text']
            result = nlp.predict(text, print=False)

            #  print(result)

            ## only using the default prediction
            prediction = result
            mergePrediction(sentence,prediction)



        #  data['sentences'] = []

        target = target_path + filename
        print(target)

        with open(target, 'w') as outfile:
            json.dump(data, outfile)

if __name__ == '__main__':
    classifyAll()
