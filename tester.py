import json
import requests
import os
import random
import flask  
from dotenv import find_dotenv, load_dotenv, main

def genius(song,artist):
    load_dotenv(find_dotenv())
    genius_client_access_token = os.getenv('genius_Token')
    genius_search_url = f"http://api.genius.com/search?q={song}{artist}&access_token={genius_client_access_token}"
    l = requests.get(genius_search_url)
    l = l.json()
    lyrics_url = (l["response"]["hits"][0]["result"]["url"])

    return lyrics_url


