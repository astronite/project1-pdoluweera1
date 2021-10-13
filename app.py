#Praveen Doluweera 
#First commit for project milestone2

#RANDOM WRITINGS 
from functions import *
import os
import flask  
from dotenv import find_dotenv, load_dotenv, main

app = flask.Flask(__name__)

@app.route('/')

def index():
    a= songData()
    return flask.render_template("index.html", song = a[0], artist = a[1], image= a[2], preview = a[3], url = a[4])

@app.route('/login')

def login():
    return flask.render_template("login.html")
app.run(
    debug = True,
    host = '0.0.0.0',
    port = int(os.getenv("PORT", 8080))
)
