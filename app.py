import ConfigParser
from os import environ
from flask import (Flask, request, jsonify)
from requests import *
from views.py import *

app = Flask(__name__)

SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'

# starting app
if __name__ == '__main__':

    app.run(port=int(environ.get("PORT", 5000)), host='0.0.0.0')
