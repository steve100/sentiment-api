
#run.sh 
docker stop sentiment-container
docker rm sentiment-container

docker run -d -p 8000:8000 --name sentiment-container sentiment-api

