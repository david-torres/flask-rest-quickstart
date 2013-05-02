from flask import Flask
from application.config import DevelopmentConfig
from application.config import ProductionConfig
from flask.ext.mongoengine import MongoEngine
from flask.ext import restful
import os

# create the main Flask app
app = Flask(__name__)
if 'APP_ENV' in os.environ and os.environ['APP_ENV'] == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# connect to the database
db = MongoEngine(app)

# setup restful support
api = restful.Api(app)

# load routes
import routes