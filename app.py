# Your goal is to help evaluate if public consumer review 
# and rating data could be incorporated to improve consumer 
# decision making. Specifically, we'd like you to write a 
# basic wrapper for the Yelp API that searches for a 
# specific entity (doctor name and address) and 
# returns relevant data.

# + Use the Yelp Search API (you'll need to register for a key)
# + Return search result json if there is a search match. 
# If no match is found, how would you propose a soft fallback solution? 
# (no need to implement fallback).
# + Place any keys in a config.ini and import using ConfigParser
# + Uses `requests` library for http calls

# starting app
if __name__ == '__main__':
    docname = raw_input("Enter the doctor's name: ")
    address = raw_input("Enter the address: ")
