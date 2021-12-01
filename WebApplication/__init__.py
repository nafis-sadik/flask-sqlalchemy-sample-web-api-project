from flask import Flask
from flask_cors import CORS

__version__ = '0.1'

app = Flask('WebApplication', static_folder=None)
CORS(app)
app.config['SECRET_KEY'] = 'random'
app.debug = True

from WebApplication.Controllers import *