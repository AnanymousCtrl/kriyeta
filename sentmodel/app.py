from flask import Flask, request, jsonify, render_template
import joblib
import json

# Load the trained model
model = joblib.load('sentmodel\\model.pkl')

# Load the intent data
with open('sentmodel\\intents02.json') as file:
    intents_data = json.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
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
        for intent in intents_data['intents']:
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

if __name__ == '__main__':
    app.run(debug=True, port=5001)
