from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
#from app import views

db = SQLAlchemy(app)

from app import models
from app import views