import requests

# Set the latitude and longitude of your location
# latitude = 21.1619
# longitude = -86.8515

latitude = 19.432608
longitude = -99.133209

# Set the radius (in meters) around your location to search for cell towers
radius = 5000

# Set OpenCelliD API key
api_key = ""    # add your api key

# Set the API endpoint URL and parameters
url = "https://us1.unwiredlabs.com/v3/cellsearch"
params = {
    "token": api_key,
    "radio": "gsm",
    "lat": latitude,
    "lon": longitude,
    "range": radius,
}

# Send a GET request to the API and retrieve the JSON response
response = requests.get(url, params=params)
data = response.json()

# Check if the response contains any cell towers
if "cells" in data:
    # Loop through the list of cell towers and print their location information
    for cell in data["cells"]:
        print("Cell Tower Location: {cell['lat']}, {cell['lon']}")
else:
    print("There are no cell towers in your area.")
