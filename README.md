# poc-ai-text-generation
![](https://build.redpencil.io/api/badges/lblod/poc-ai-text-generation/status.svg)

This repository contains the code for the text generation api. The soul purpose of this api is to generate text given a start prompt.

## Getting started
In order to run this code, you will have to download some models from our public read access GCP bucket, once that is completed, you can
mount the downloaded models into the container that you can pull from dockerhub.

### COPY model from GCP bucket
An easy way to download files from a google cloud bucket, is by installing the gsultil client, You can find more information on how to install this client [here](https://cloud.google.com/storage/docs/gsutil_install).

Gsutil command(s):
```
gsutil -m cp -r gs://abb-textgen-models/dutch-gpt-neo .
gsutil -m cp -r gs://abb-textgen-models/gpt2-retrain .
gsutil -m cp -r gs://abb-textgen-models/dutch-gpt-medium/ .
```

### Starting the docker container
First you pull the container (can be skipped --> will be pulled either if not present when executing the run command)
```
docker pull lblod/poc-ai-text-generation
```

Once the container is pulled, you can start it using the following command
```
docker run -it --rm  -v <folder_container_model>:/models/ -p 8080:8080 lblod/poc-ai-text-generation
```

Text generation API  by ML2Grow
