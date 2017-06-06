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


@app.route('/search-result/<term><location>')
def make_api_request(term, location):
    """takes in a token, gets docname and address from form, and returns response"""
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    cred_dict = {}
    for section_name in Config.sections():
        for name, value in Config.items(section_name):
            cred_dict[name] = value
    url_params = {"term": term, "location": location}
    bearer_token = cred_dict.get("bearer_token")
    print bearer_token
    headers = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.request('GET', SEARCH_URL, headers=headers, params=url_params)
    return response.json()

# starting app
if __name__ == '__main__':

 # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=int(environ.get("PORT", 5000)), host='0.0.0.0')
