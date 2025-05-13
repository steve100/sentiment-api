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

## Server and client
```
Server:
|-----------------|----------------------|
| Docker image     | sentiment-api |
| Docker container | sentiment-container |

Client:

|-----------------|----------------------|
| Sample curl program   | curl-client-sentiment_api.sh       |
| Sample python program | python-client-sentiment_package.py |
```

## Installation
### Tested on windows and Linux
Make sure you have  git installed.

git clone https://github.com/steve100/sentiment-api.git

- cd sentiment-api

| File Name           | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| `app.py`            | The Flask/gunicorn web application                                |
| `build.sh`          | Builds the Docker image                                           |
| `curl-port80.sh`    | Tests the web service on port 80 (reverse proxy must be installed)|
| `Dockerfile`        | Instructions on how to make the Docker image                      |
| `requirements.txt`  | Python modules used                                               |
| `run.sh`            | Starts and runs the Docker container that runs the web service    |


### tests-tools
- cd tests-tools

| File Name                          | Description                                                           |
|-----------------------------------|-----------------------------------------------------------------------|
| `python-client-sentiment_package.py` | Tests the web service on port 8000 with Python (run this in a venv)   |
| `curl-client-sentiment_api.sh`    | Tests the web service on port 8000 with Curl                          |
| `curl-port80.sh`                  | Tests the web service on port 80 (reverse proxy must be installed)    |
| `onequery-sentiment.py`           | Runs the model without a web service                                  |
| `requirements.txt`                | Python modules used                                                   |


## Run
### Start the server

```
cd sentiment-api
bash run.sh
```

### Test the client
```
cd tests-tools
bash curl-client-sentiment_api.sh
```

### Test the Python client and write your application

Chose a location for the Python Virtual Environment
HOW To Link: https://www.geeksforgeeks.org/python-virtual-environment/

```
python3 -m venv vpython
cd vpython
source ./bin/activate

#copy the tests and tools to your virtual environment.
#in this case vpython

cp  tests-tools/* . 
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir -r requirements.txt

python3 onequery-sentiment.py
python3 python-client-sentiment_package.py


#when done
deactivate 
```

## How to Install GIT
### General Git
```
https://git-scm.com/
https://git-scm.com/doc
```
### Linux Ubuntu Git
- Information 
```
Use your Distro
sudo apt upgrade -y  ; sudo   apt install git -y

or you can get the latest
https://git-scm.com/downloads/linux
```


### Windows Git
- Information
```
https://git-scm.com/downloads/win

or same thing, more information
https://gitforwindows.org/
```

### Git Usage
- Set the identity in the repo for push
```
  git config --global user.email youremail@yourdomain
  git config --global user.name  yourname
```
- Cheat sheet
```
  git status
  git add . 
  git commit -m "your commit"
  #you will now need a token because  userid/password depreciated
  git push
```
    
- tokens
```
https://git-scm.com/downloads/win
```

- Markdown
```
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github
```

- Authentication
```
vim install-gh.sh ; bash install-gh.sh
gh auth login
```

## Docker
### Docker for Linux
```
Used the convience script
 https://docs.docker.com/engine/install/ubuntu/

It makes things easier if you add your user to the docker group

```

### Docker for Windows
```
 https://docs.docker.com/desktop/setup/install/windows-install/

 Video Installing  Docker Desktop and optonal  with WSL2
 https://www.youtube.com/watch?v=ZyBBv1JmnWQ

```

