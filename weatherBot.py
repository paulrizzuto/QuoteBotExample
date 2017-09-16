# Dependencies
import tweepy
import time
import json
import random
import numpy as np
import requests as req
from citipy import citipy

def weatherUpdate():
    #twitter
    consumer_key = 	"DwLw79XZY4889gxF7kQX0PkcO"
    consumer_secret = "1SAO5vgeLGikldPHv3bHFEQpct4MyVvFKQHSTDhBbq9meTVNLE"
    access_token = "901933530258829312-6LurEa2LxZQRFGSVCAuXAT1QPIgVj6p"
    access_token_secret = "OGBiYPhUyDaBnAVslQ9ERKkkBhEjMmmn3pK1aKgSvIBDU"

    #weather
    api_key = "577f692bda463ed51e5e7f3632a90604"
    url = "http://api.openweathermap.org/data/2.5/weather?" 
    units = "imperial"

    #authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    lat = np.random.uniform(low=-90.0, high=90.0)
    lng = np.random.uniform(low=-180.0, high=180.0)
    try:
        city = citipy.nearest_city(lat, lng)
        cityname = city.city_name
        countryname = city.country_code
        query_url = url + "appid=" + api_key + "&units=" + units + "&q=" + cityname + "," + countryname
        response = req.get(query_url).json()
        temperature = response["main"]["temp_max"]
        api.update_status("The temperature in %s, %s is %sF" % (cityname, countryname, temperature))
        print("Successful tweet!")
    except:
        print("Skipping this one!")

while(True):
    weatherUpdate()
    time.sleep(30)
