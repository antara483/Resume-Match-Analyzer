# from functools import wraps
# from flask import request, jsonify
# import jwt
# import os

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None

#         # Get token from Authorization header
#         if 'Authorization' in request.headers:
#             auth_header = request.headers['Authorization']
#             if auth_header.startswith("Bearer "):
#                 token = auth_header.split(" ")[1]

#         if not token:
#             return jsonify({"message": "Token is missing!"}), 401

#         try:
#             data = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])
#             # You can use this data for user info (e.g., user_id, username, etc.)
#             request.user = data
#         except jwt.ExpiredSignatureError:
#             return jsonify({"message": "Token expired!"}), 401
#         except jwt.InvalidTokenError:
#             return jsonify({"message": "Invalid token!"}), 401

#         return f(*args, **kwargs)

#     return decorated

# app/auth_utils.py
from functools import wraps
from flask import request, jsonify
import jwt
import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check the Authorization header
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])
            request.user = data  # Store decoded data for use in the route
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        # return f(*args, **kwargs)
        return f(data, *args, **kwargs)
    return decorated
