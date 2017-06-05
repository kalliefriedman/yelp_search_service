import ConfigParser

SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'


@app.route('/search_result', methods=["GET"])
def make_api_request():
    """takes in a token, gets docname and address from form, and returns response"""
    Config = ConfigParser.ConfigParser()
    Config.read("\config.ini")
    print Config.sections()
    # docname = request.args.get("term")
    # address = request.args.get("location")
    # url_params = {"term": docname, "location": address}
    # headers = {'Authorization': 'Bearer ' + bearer_token}
    # response = requests.request('GET', SEARCH_URL, headers=headers, params=url_params)
    # return response.json()
    return 'OK'
    