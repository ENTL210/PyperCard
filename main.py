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

# In the "get_name" card, when you "click" on the "submit" button...
@weather_app.transition("get_name", "click", "submit")
def hello(app, card):
    """
    Store the value in the card's input box, with the id "name", into the app's
    datastore, under the key "name".

    Then transition to the "say_hello" card.
    """
    app.datastore["name"] = card.get_by_id("name").value

    # Required parameters to fetch the weather api...
    parameters = {
    'key': '64c4ff4519da47c6bf6224642231911',
    'q': f'{app.datastore["name"]}',
    'aqi': 'no'
    }
    
    # Fetch the api...
    api_call = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters)

    app.datastore["data"] = api_call.text

    return "say_hello"


# In the "say_hello" card, when you "click" on the "again" button...
@weather_app.transition("say_hello", "click", "again")
def again(app, card):
    """
    Don't do anything except transition to the "get_name" card.
    """
    return "get_name"


# Start the hello_app
weather_app.start()
