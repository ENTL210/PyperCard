"""
A simple PyperCard app to get a user's name, and then display a friendly
"Hello world!" type message.
"""
# We need to use the a pypercard App.
from pypercard import App
# import requests
import requests

# import json
import json

#import pyodide_http
import pyodide_http

# Create the app as the object called hello_app.
weather_app = App()

# Patch the Requests Libarary so it works with Pyscript
pyodide_http.patch_all()

# In the "input" card, when you "click" on the "submit" button...
@weather_app.transition("input-card", "click", "submit-btn")
def hello(app, card):
    """
    Store the value in the card's input box, with the id "name", into the app's
    datastore, under the key "name".

    Then transition to the "say_hello" card.
    """
    app.datastore["city-input"] = card.get_by_id("city-input").value

    # Required parameters to fetch the weather api...
    parameters = {
    'key': '64c4ff4519da47c6bf6224642231911',
    'q': f'{app.datastore["city-input"]}',
    'aqi': 'no'
    }
    
    # Fetch the api...
    api_call = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters)

    # parse the entire api as a json to the local database...
    app.datastore["data"] = api_call.json()

    # Loop through the 'location' & 'current' section of the api, and add data to the database...
    for items in app.datastore["data"]["location"]:
        app.datastore[items] = app.datastore["data"]["location"][items]

    for items in app.datastore["data"]["current"]:
        app.datastore[items] = app.datastore["data"]["current"][items]


    return "result-card"


# In the "result_card" card, when you "click" on the "again" button...
@weather_app.transition("result-card", "click", "again")
def again(app, card):
    """
    Don't do anything except transition to the "get_name" card.
    """
    return "input-card"


# Start the hello_app
weather_app.start()
