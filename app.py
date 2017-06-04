# Your goal is to help evaluate if public consumer review 
# and rating data could be incorporated to improve consumer 
# decision making. Specifically, we'd like you to write a 
# basic wrapper for the Yelp API that searches for a 
# specific entity (doctor name and address) and 
# returns relevant data.

# + Return search result json if there is a search match. 
# If no match is found, how would you propose a soft fallback solution? 
# (no need to implement fallback).
# + Place any keys in a config.ini and import using ConfigParser

from os import environ
from flask import (Flask, request,
from requests import                    jsonify)

app = Flask(__name__)


# starting app
if __name__ == '__main__':
    docname = raw_input("Enter the doctor's name: ")
    address = raw_input("Enter the address: ")
    
