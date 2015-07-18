# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext import login
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__, static_folder='static', static_url_path='')

# config to flasb application "Mongo connection"
# app.config.from_object('config.ProductionConfig')

# SQL alchemy url
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty1$@localhost/flasb'
app.config['SECRET_KEY'] = "plasb"

#login_manager = LoginManager()
#login_manager.init_app(app)

# mongo engine
#db = MongoEngine(app)

# SQL alchemy
db = SQLAlchemy(app)

from views import *



#login_manager.login_view = 'login'

if __name__ == '__main__':
    app.run(port=5000, host="127.0.0.1")
