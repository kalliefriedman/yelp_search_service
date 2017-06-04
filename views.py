from app.py import *

SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'


@app.route('/search_result.json', methods=["GET"])
def request(bearer_token):
    """takes in a token, gets docname and address from form, and returns response"""
    docname = request.args.get("docname")
    address = request.args.get("address")
    url_params = {"term": docname, "location": address}
    headers = {'Authorization': 'Bearer ' + bearer_token}
    response = requests.request('GET', SEARCH_URL, headers=headers, params=url_params)
    return response.json()
