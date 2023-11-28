'''
Consists of functions that fetch back the weather info 
from an API, parse it into a dictionary obj, then
return an object of information that needed
'''
import json 
import requests


def fetch_api():
    # Required parameters to fetch the weather api...
    parameters = {
    'key': '64c4ff4519da47c6bf6224642231911',
    'q': 'hillsboro',
    'aqi': 'no'
    }
    
    # Fetch the api...
    api_call = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters)
    
    # Return the api json string...
    return api_call.text
    
def parse_object():
    # Parse the json object to a dictionary object...
    parse_json = json.loads(fetch_api())
    
    return parse_json


parse_object()