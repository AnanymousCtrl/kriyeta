from flask import Flask, render_template
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client.loginApp

from routes import auth

app.register_blueprint(auth, url_prefix='/api/auth')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
