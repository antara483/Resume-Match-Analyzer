# from flask import Flask
# from flask_mysqldb import MySQL
# import os
# from dotenv import load_dotenv
# mysql = MySQL()

# load_dotenv()

# def create_app():
#     app = Flask(__name__)

#     app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
#     app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
#     app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'your_password')
#     app.config['MYSQL_DB'] = os.environ.get('MYSQL_DATABASE', 'your_database')

#     app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'fallback_secret_key')

#     mysql.init_app(app)

    
#     # add
#     from app.routes import main_routes
#     app.register_blueprint(main_routes)
#     # add
#     return app

# from flask import Flask
# from flask_mysqldb import MySQL
# from flask_session import Session
# import os
# from dotenv import load_dotenv

# mysql = MySQL()

# load_dotenv()

# def create_app():
#     app = Flask(__name__)

#     app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
#     app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
#     app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
#     app.config['MYSQL_DB'] = os.environ.get('MYSQL_DATABASE', 'resume_db')
#     app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'supersecret')
#     app.config['SESSION_TYPE'] = 'filesystem'

#     mysql.init_app(app)
#     Session(app)

   


   
#     from app.routes.auth_routes import auth_routes
#     app.register_blueprint(auth_routes)

#     return app


# app/__init__.py
# from flask import Flask
# from flask_mysqldb import MySQL
# from dotenv import load_dotenv
# import os

# mysql = MySQL()
# load_dotenv()

# def create_app():
#     app = Flask(__name__)

#     app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
#     app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
#     app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
#     app.config['MYSQL_DB'] = os.environ.get('MYSQL_DATABASE', 'resume_db')
#     app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'mysecret')

#     mysql.init_app(app)

#     from app.routes.main_routes import main_routes
#     from app.routes.auth_routes import auth_routes

#     app.register_blueprint(main_routes)
#     app.register_blueprint(auth_routes)

#     return app

# from flask import Flask
# from flask_mysqldb import MySQL
# import os
# from dotenv import load_dotenv

# mysql = MySQL()
# load_dotenv()

# def create_app():
#     app = Flask(__name__)

#     app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
#     app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
#     app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')  # update this
#     app.config['MYSQL_DB'] = 'resume_db'  # use your actual db

#     app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'fallback_secret_key')

#     mysql.init_app(app)
#     # added
#     # ✅ Register both main and auth routes
#     from app.main_routes import main_routes
#     from app.auth_routes import auth_routes
#     # added
#     # add
#     # from routes import main_routes
#     # from app.main_routes import auth_routes  # we will create this file next
#     # add

#     app.register_blueprint(main_routes)
#     app.register_blueprint(auth_routes)

#     return app

# app/__init__.py

# from flask import Flask
# from flask_mysqldb import MySQL
# from flask_session import Session
# from dotenv import load_dotenv
# import os

# mysql = MySQL()
# load_dotenv()

# def create_app():
#     app = Flask(__name__)

#     # MySQL Configuration
#     app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
#     app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
#     app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
#     app.config['MYSQL_DB'] = os.environ.get('MYSQL_DATABASE', 'resume_db')

#     # Security & Session Configuration
#     app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'supersecret')
#     app.config['SESSION_TYPE'] = 'filesystem'

#     # Initialize MySQL and Session
#     mysql.init_app(app)
#     Session(app)

#     # Register Blueprints
#     from app.routes.main_routes import main_routes
#     from app.routes.auth_routes import auth_routes
#     app.register_blueprint(main_routes)
#     app.register_blueprint(auth_routes)

#     return app


import os
from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()

mysql = MySQL()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    CORS(app)
    CORS(app, supports_credentials=True) 
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DATABASE')

    mysql.init_app(app)
    bcrypt.init_app(app)

    
    from app.auth_routes import auth_routes
    app.register_blueprint(auth_routes, url_prefix='/api/auth')

    from app.routes import main_routes         # ✅ add this line
    app.register_blueprint(main_routes)        # ✅ and this one

    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/resume_matcher.log',
                                         maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Resume Matcher startup')
    
    return app

