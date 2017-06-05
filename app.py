import ConfigParser
from os import environ
from flask import (Flask, request, jsonify)
from requests import *
import views
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# starting app
if __name__ == '__main__':

 # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=int(environ.get("PORT", 5000)), host='0.0.0.0')
