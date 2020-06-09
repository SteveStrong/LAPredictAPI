#!/bin/bash

# build docker file and push to azure

# docker login lacontainers.azurecr.io
# username lacontainers
# pasword  (get it from azure access keys to azurecr)

# docker build -t lapredict .
# docker run -d -p 8000:8000 --name predictor lapredict

#  https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli
#  to put into azurecr.io 
#  az login
#  az acr login --name lapredict


docker build -t lapredict -f Dockerfile  .
echo "build done"
docker tag lapredict lapredict.azurecr.io/lapredict 
echo "tag done"
docker push lapredict.azurecr.io/lapredict 
echo "push done"
