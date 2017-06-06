# Yelp Search
Yelp Search is a 


# Technologies
Backend: Python, Flask, Requests library, ConfigParser Libarary

Frontend: None

APIs: Yelp Search API

# Features
*Ability to search for a doctor by name and address


# Installation
To run Yelp Search:

*Clone or fork this repo:

    *https://github.com/kalliefriedman/yelp_search_service

*Create and activate a virtual environment inside your yelp-search directory:

    *virtualenv env

    *source env/bin/activate

*Install the dependencies:

    *pip install -r requirements.txt

*Sign up for the Yelp Search API by signing in and creating an app. 
    
    *Then get your bearer token by making a POST request using your client key and client secret. Instructions can be found here: https://www.yelp.com/developers/documentation/v3/authentication

*Run the app:

    *python app.py on command line

*You can now navigate to 'localhost:5000/' to access Yelp Search. 
    *Put your term and location data as query parameters in the URL when you hit the /search endpoint.

