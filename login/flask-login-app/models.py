from pymongo import MongoClient
from flask_bcrypt import generate_password_hash, check_password_hash

client = MongoClient('mongodb://localhost:27017/')
db = client.loginApp

class User:
    @staticmethod
    def create_user(username, password):
        print(f"Creating user: {username}")
        password_hash = generate_password_hash(password).decode('utf-8')
        result = db.users.insert_one({
            'username': username,
            'password': password_hash
        })
        print(f"User created with id: {result.inserted_id}")

    @staticmethod
    def find_user(username):
        print(f"Finding user: {username}")
        user = db.users.find_one({'username': username})
        if user:
            print(f"User found: {user}")
        else:
            print("User not found")
        return user

    @staticmethod
    def verify_password(stored_password, provided_password):
        print(f"Verifying password for provided password: {provided_password}")
        return check_password_hash(stored_password, provided_password)
