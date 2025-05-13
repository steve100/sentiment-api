# sentiment-api

A lightweight Flask API for sentiment analysis using Hugging Face's `transformers` library and the DistilBERT model.
Packaged as docker container.  Optional Nginx Reverse Proxy to redirect port 8000 to port 80 

Using HTTP protocol you send a string to the service and it gives output on like/dislike
example:
 run the program - asking about ""I love this movie!"

 bash curl-clientusentiment_api.sh

 output:
 [{"label":"POSITIVE","score":0.9998775720596313}]



##  Features

- RESTful API with a `/predict` endpoint
- Uses `distilbert-base-uncased-finetuned-sst-2-english` for binary sentiment classification
- Packaged as a Python module with CLI entry point
- Easy to install and extend

## Installation
Tested on windows and Linux
Make sure you have  git installed.

git clone https://github.com/steve100/sentiment-api.git

cd sentiment-api

app.py                              The Flask/gunicorn web application                                      
build.sh                            Builds the Docker image
curl-port80.sh                      Tests the web service on port 80 (reverse proxy must be installed)
Dockerfile                          Instructions on how to make the docker image
requirements.txt                    python modules used 
run.sh                              Starts and Runs the docker container that runs the web service

## tests-tools
cd tests-tools
python-client-sentiment_package.py  Tests the web service on port 8000 with Python (run this in a venv) 
curl-client-sentiment_api.sh        Tests the web service on port 8000    with Curl
curl-port80.sh                      Tests the web service on port 80 (reverse proxy must be installed)
onequery-sentiment.py               Runs the model without a web service 
requirements.txt                    python modules used 

## Run
###Start the server

cd sentiment-api
bash run.sh

###Test the client
cd tests-tools
bash curl-client-sentiment_api.sh

###Test the Python client and write your application

Chose a location for the Python Virtual Environment
HOW To Link: https://www.geeksforgeeks.org/python-virtual-environment/


python3 -m venv vpython
cd vpython
source ./bin/activate


cp  tests-tools/* . 
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir -r requirements.txt

python3 onequery-sentiment.py
python3 python-client-sentiment_package.py


when done
deactivate 

