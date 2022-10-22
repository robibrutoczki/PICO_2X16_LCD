# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests


URL = "http://api.coindesk.com/v1/bpi/currentprice/USD.json"

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = ''
password = ''
wlan.connect(ssid, password)






        
# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
print("ETH GBP ")
r = urequests.get("https://www.bitstamp.net/api/v2/ticker/ethgbp")

print(r.json()['last'])
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("THE TIME IS :")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json()['date'] +" " + r.json()['time'])