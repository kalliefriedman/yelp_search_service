import ConfigParser
from os import environ
from flask import (Flask, request, jsonify)
import requests
import views
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'
TEST_URL = '/test'

# feedback as follows:
# could cache response in database or dictionary like redis
# should define the interface
# validate parameters that are passed in, that they are correct in format
# separate out view and controller
# don't put the ConfigParser object in a dictionary, work with the object directly
# name the config file sections by service name
# route could decide which function to use based on service
# use mock and vcr for testing

@app.route('/search')
def make_api_request():
    """Takes in term and address via URL parameters, and returns json object response data"""
    cred_dict = {}
    for section_name in Config.sections():
        for name, value in Config.items(section_name):
            cred_dict[name] = value

    term = request.args.get('term')
    location = request.args.get('location')
    # could make validation more extensive
    if term and location:
        url_params = {"term": term, "location": location}
        bearer_token = cred_dict.get("bearer_token")
        headers = {'Authorization': 'Bearer ' + bearer_token}
        response = requests.request('GET', SEARCH_URL, headers=headers, params=url_params)
        dict_response = response.json()
        json_response = jsonify(dict_response)

        return json_response
    else:
        return "term or location have not been specified"


# starting app
if __name__ == '__main__':

 # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    cred_dict = {}
    for section_name in Config.sections():
        for name, value in Config.items(section_name):
            cred_dict[name] = value

    app.run(port=int(environ.get("PORT", 5000)), host='0.0.0.0')
