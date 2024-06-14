import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline


with open('O:\\hackathon\\fresh\\intents02.json') as file:
    intents_data = json.load(file)


patterns = []
tags = []
for intent in intents_data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])


model = make_pipeline(TfidfVectorizer(), LogisticRegression())


model.fit(patterns, tags)


joblib.dump(model, 'O:\\hackathon\\fresh\\model.pkl')
