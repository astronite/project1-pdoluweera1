#Praveen Doluweera 

import json
import requests
import os
import random
import flask  
from dotenv import find_dotenv, load_dotenv, main

app = flask.Flask(__name__)

@app.route('/')

def index():
    load_dotenv(find_dotenv())

    genius_client_access_token = os.getenv('genius_Token')
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")

    url = "https://accounts.spotify.com/api/token"
    genius_url = 'https://api.genius.com/'

    # POST
    auth_response = requests.post(url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token,) 
    }

    artists_ID = ["4LLpKhyESsyAXpc4laK94U", "1ShZZUjkbXCjhwrb18BA8I", "4kI8Ie27vjvonwaB2ePh8T"] #Mac Miller, Bryce Vine, portugal. the man 
    artist_Random = random.choice(artists_ID)
    song_Random = random.randint(0, 9)


    BASE_URL = 'https://api.spotify.com/v1/artists/%s/top-tracks?market=US' % (artist_Random)  #Every refresh chooses a new artist id

    r = requests.get(BASE_URL, headers=headers,
            params={'limit': 10})
    r = r.json()

   
    song = (r['tracks'][song_Random]['name']) #random song 
    artist = (r['tracks'][song_Random]['album']['artists'][0]['name'])
    images_Link = (r['tracks'][song_Random]['album']['images'][0]['url'])
    preview_Link = (r['tracks'][song_Random]['preview_url'])

    genius_search_url = f"http://api.genius.com/search?q={song}{artist}&access_token={genius_client_access_token}"

    l = requests.get(genius_search_url)
    l = l.json()

    lyrics_url = (l["response"]["hits"][0]["result"]["url"])
    
    return flask.render_template("index.html", song = song, artist = artist, image= images_Link, preview = preview_Link, url = lyrics_url)



if __name__ == '__main__':
    app.run(debug = True)



