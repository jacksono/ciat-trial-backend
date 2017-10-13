"""Module to initialise and configure the flask app and the db."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration.config import app_config
from flask_restful import Api
from flasgger import Swagger
from sqlalchemy.ext import mutable
from flask.ext.heroku import Heroku
import json

app = Flask(__name__)
app.config.from_object(app_config["development"])
db = SQLAlchemy(app)
heroku = Heroku(app)


class JsonEncodedDict(db.TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""

    impl = db.Text

    def process_bind_param(self, value, dialect):
        """Docstring."""
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        """Docstring."""
        if value is None:
            return {}
        else:
            return json.loads(value)


template = {
  "swagger": "2.0",
  "info": {
    "title": "INM API",
    "description": "API for managing research results",
    "contact": {
      "responsibleDeveloper": "Jackson Onyango",
      "email": "jackson.onyango@andela.com",
    },
    "version": "1.0"
  },
  "schemes": [
    "http",
    "https"
  ],
  "produces": ["application/x-www-form-urlencoded",
               "application/json",
               "application/txt"],
  "operationId": "getmyData",
  "content-type": "text"
}

api = Api(app=app, prefix="/api/v1")
swagger = Swagger(app, template=template)
mutable.MutableDict.associate_with(JsonEncodedDict)
