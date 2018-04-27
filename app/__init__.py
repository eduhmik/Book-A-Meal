"""
Code used to initialize the app module
""" 
<<<<<<< HEAD
from flask_api import FlaskAPI
from flask_restful import Api

APP = FlaskAPI(__name__, instance_relative_config=True)
API = Api(APP)
from app import routes

APP.config.from_object('config')
=======
from flask import Flask
from instance.config import app_config

APP = Flask(__name__, instance_relative_config=True)

APP.config.from_object(app_config['development'])
APP.config.from_pyfile("config.py")
>>>>>>> aa4422cd6bf4a290eb8cd09067f4315883f3884c
