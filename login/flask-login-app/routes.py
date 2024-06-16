from flask import Blueprint, request, jsonify
from models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(f"Received registration data: {data}")
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'msg': 'Username and password are required'}), 400

    if User.find_user(username):
        return jsonify({'msg': 'User already exists'}), 400
    
    User.create_user(username, password)
    return jsonify({'msg': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(f"Received login data: {data}")
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'msg': 'Username and password are required'}), 400

    user = User.find_user(username)
    if not user or not User.verify_password(user['password'], password):
        return jsonify({'msg': 'Invalid credentials'}), 400
    
    return jsonify({'msg': 'Login successful'}), 200
