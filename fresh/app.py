from flask import Flask, render_template,jsonify, redirect, url_for, session, request
from flask_pymongo import PyMongo
from pymongo import MongoClient

import json
import os
import pickle
import random
import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer

app = Flask(__name__, template_folder='template',
            static_folder='static', static_url_path='/')

client = MongoClient('mongodb://localhost:27017/')
mydk = client.mydk
mycom = mydk.mycom

app.secret_key='mynameissoni'


#model paths


#
# Initialize Flask app

    
    


#botpaths

# Disable certain TensorFlow optimizations (if needed)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Initialize the lemmatizer
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# Load the trained model
with open('C:\\Users\\prami\\OneDrive\\Desktop\\kriyeta\\fresh\\training.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load words and classes
words = pickle.load(open('C:\\Users\\prami\\OneDrive\\Desktop\\kriyeta\\fresh\\texts.pkl', 'rb'))
classes = pickle.load(open('C:\\Users\\prami\\OneDrive\\Desktop\\kriyeta\\fresh\\labels.pkl', 'rb'))

# Load intents from JSON
with open('C:\\Users\\prami\\OneDrive\\Desktop\\kriyeta\\fresh\\intents.json', 'r') as file:
    intents = json.load(file)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                bag[i] = 1
    return bag

def predict_class(sentence, model):
    bow_vector = bow(sentence, words)
    cleaned_sentence = ' '.join(clean_up_sentence(sentence))  # Join list of words into a string
    prediction = model.predict_proba([cleaned_sentence])[0]  # Use predict_proba to get probabilities

    # Debugging prints
    print(f"Cleaned sentence: {cleaned_sentence}")
    print(f"Prediction: {prediction}")
    print(f"Prediction type: {type(prediction)}")
    print(f"Prediction shape: {prediction.shape if hasattr(prediction, 'shape') else 'N/A'}")

    try:
        predicted_class_index = prediction.argmax()
        predicted_class = classes[predicted_class_index]
        probability = prediction[predicted_class_index]
        print(f"Predicted class index: {predicted_class_index}")
        print(f"Predicted class: {predicted_class}")
        print(f"Probability: {probability}")
    except (IndexError, AttributeError) as e:
        print(f"Error accessing prediction: {e}")
        return []

    return [{"intent": predicted_class, "probability": str(probability)}]

def getResponse(ints, intents_json):
    if ints:
        tag = ints[0]['intent']
        for intent in intents_json['intents']:
            if intent['tag'] == tag:
                responses = intent['responses']
                result = random.choice(responses)
                return result
    return "Sorry, I didn't understand that."

print('maitri is here for you!!')

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    print("Chatbot response: ", res)
    return res



# routes for the pages

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('main2.html', var_home=url_for('log_page'))


@app.route('/Login', methods=['GET', 'POST'])
def log_page():
    return render_template('login.html')

@app.route('/logind',methods=['post'])
def logind():
     mail= request.form.get('email')
     passw= request.form.get('password')
    
     user = mycom.find_one({'email': mail})
     
     name = user['name'].split(" ")
     first_name=name[0].capitalize()
     

     
     if user['password']==passw:
         session['email'] = mail
         return render_template('bash.html',var_hom=url_for('bot'),var_ho = url_for('psy'),your_name=first_name)
     else:
         return redirect(url_for('log_page'))
    
    
@app.route('/regis', methods=['get', 'post'])
def regis():
    return render_template('register.html')

@app.route('/signl', methods=['POST'])
def signl():
    naam= request.form.get('name')
    mail= request.form.get('email')
    passw= request.form.get('password')
    passw2= request.form.get('password1')
    
    
    
    existing_user=mycom.find_one({'email':mail})

    if existing_user:
        message="user already exists"
        return render_template('login.html',message=message)

    if passw != passw2 :
        message="password doesnt match"
        return render_template('register.html',message = message)
    
    message= "you can login now"
    mycom.insert_one({'name':naam , 'email':mail,'password': passw})
    return render_template('login.html',message=message)
    





#model routes

@app.route('/madal')
def madal():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the user input from the request
        user_input = request.json.get('message')

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Predict the intent
        prediction = model.predict([user_input])[0]

        # Find the corresponding responses
        for intent in intents_data['intentel']:
            if intent['tag'] == prediction:
                response = {
                    "tag": prediction,
                    "symptoms": intent['responses']['symptoms'],
                    "recommendations": intent['responses']['recommendations']
                }
                return jsonify(response)
        
        return jsonify({"error": "Intent not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500





#routes for bot

@app.route("/bot")
def bot():
    return render_template("bot.html" )

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print("User text: " + userText)

    chatbot_response_text = chatbot_response(userText)
    return chatbot_response_text

@app.route("/psycho")
def psy():
    return render_template("psycho.html")

if __name__ == '__main__':
    app.run(debug=True)
