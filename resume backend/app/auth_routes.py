# from flask import Blueprint, request, jsonify
# from app import mysql, bcrypt
# import jwt
# import datetime

# auth_routes = Blueprint("auth_routes", __name__)

# def generate_token(user_id, secret_key):
#     payload = {
#         "user_id": user_id,
#         "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
#     }
#     return jwt.encode(payload, secret_key, algorithm='HS256')


# @auth_routes.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()

#     name = data.get('name')
#     email = data.get('email')
#     password = data.get('password')

#     if not all([name, email, password]):
#         return jsonify({"message": "Missing fields"}), 400

#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
#     if cursor.fetchone():
#         return jsonify({"message": "User already exists"}), 409

#     hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
#     cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
#                    (name, email, hashed_pw))
#     mysql.connection.commit()
#     cursor.close()

#     return jsonify({"message": "User registered successfully"}), 201


# @auth_routes.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()

#     email = data.get('email')
#     password = data.get('password')

#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT id, password FROM users WHERE email = %s", (email,))
#     user = cursor.fetchone()
#     cursor.close()

#     if not user:
#         return jsonify({"message": "Invalid credentials"}), 401

#     user_id, hashed_pw = user
#     if not bcrypt.check_password_hash(hashed_pw, password):
#         return jsonify({"message": "Invalid credentials"}), 401

#     token = generate_token(user_id, secret_key='jwt-secret-key')

#     return jsonify({"token": token}), 200

# from flask import Blueprint, request, jsonify
# from app import mysql, bcrypt
# import jwt
# import datetime
# import os

# auth_routes = Blueprint('auth_routes', __name__)

# @auth_routes.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')

#     if not username or not email or not password:
#         return jsonify({'message': 'Missing fields'}), 400

#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     existing_user = cursor.fetchone()

#     if existing_user:
#         return jsonify({'message': 'Email already registered'}), 409

#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#     cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
#                    (username, email, hashed_password))
#     mysql.connection.commit()
#     cursor.close()

#     return jsonify({'message': 'User registered successfully'}), 201


# @auth_routes.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     if not email or not password:
#         return jsonify({'message': 'Missing fields'}), 400

#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT id, username, password FROM users WHERE email = %s", (email,))
#     user = cursor.fetchone()
#     cursor.close()

#     if user and bcrypt.check_password_hash(user[2], password):
#         token = jwt.encode({
#             'user_id': user[0],
#             'name': user[1],
#             'email': email,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
#         }, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')

#         return jsonify({'token': token}), 200
#     else:
#         return jsonify({'message': 'Invalid credentials'}), 401
from flask import Blueprint, request, jsonify
from app import mysql, bcrypt
import jwt
import datetime
import os

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        print(data,"data")
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'message': 'Missing fields'}), 400

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({'message': 'Email already registered'}), 409

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, hashed_password))
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        print(e)
        return jsonify({'error': 'Signup failed', 'details': str(e)}), 500


@auth_routes.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Missing fields'}), 400

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, username, password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and bcrypt.check_password_hash(user[2], password):
            token = jwt.encode({
                'user_id': user[0],
                'username': user[1],
                'email': email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')

            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

    except Exception as e:
        print(e)
        return jsonify({'error': 'Login failed', 'details': str(e)}), 500
