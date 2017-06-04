import ConfigParser
from os import environ
from flask import (Flask, request,
from requests import                    jsonify)

app = Flask(__name__)



# starting app
if __name__ == '__main__':
    docname = raw_input("Enter the doctor's name: ")
    address = raw_input("Enter the address: ")
    
