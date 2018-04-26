"""
Code used to initialize the app module
""" 
from flask import Flask
from instance.config import app_config

APP = Flask(__name__, instance_relative_config=True)

APP.config.from_object(app_config['development'])
APP.config.from_pyfile("config.py")
