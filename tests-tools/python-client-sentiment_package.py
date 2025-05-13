import requests, os




# API endpoint
url = "http://127.0.0.1:8000/predict"

# Text to classify
data = {"text": "I love this movie!"}

# Send POST request
response = requests.post(url, json=data)

# Print result
print(response.json())


#curl
#curl -X POST http://127.0.0.1:5000/predict \
#  -H "Content-Type: application/json" \
#  -d '{"text": "I love this movie!"}'
