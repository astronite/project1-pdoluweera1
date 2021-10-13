#Praveen Doluweera 
#First commit for project milestone2

#RANDOM WRITINGS 
from functions import *
import os
import flask  
from dotenv import find_dotenv, load_dotenv, main
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 

app = flask.Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def login():
    return flask.render_template("login.html")

@app.route('/index')
def index():
    a= songData()
    return flask.render_template("index.html", song = a[0], artist = a[1], image= a[2], preview = a[3], url = a[4])

@app.route('/signup', methods = ["GET", "POST"])
def signup():
    if flask.request.method == 'POST':
        data = flask.request.form
        data = data["username"]
        return flask.render_template("signup.html",data = data)

    return flask.render_template("signup.html")

app.run(
    debug = True,
    host = '0.0.0.0',
    port = int(os.getenv("PORT", 8080))
)
