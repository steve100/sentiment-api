from transformers import pipeline

#simple program to load the huggingface  model and send it a query
#results returned as json~/sentiment_package/sentiment_app

# Load sentiment analysis pipeline with DistilBERT
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Example text
text = "I absolutely love this product!"

# Run classification
result = classifier(text)
print(result)

print("working with a list")
texts = ["I love this!", "This is terrible."]
results = classifier(texts)
for r in results:
    print(f"{r['label']}: {r['score']:.4f}")
