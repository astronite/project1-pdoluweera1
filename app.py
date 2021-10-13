#Praveen Doluweera 
#First commit for project milestone2

#RANDOM WRITINGS 
from functions import *
import os
import flask  
from dotenv import find_dotenv, load_dotenv, main
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://kuzgfouwsjmldd:67464b0aa5c549c457e27fa4d938c9e5066373fdd48ed68516f0726887ca2697@ec2-3-215-83-124.compute-1.amazonaws.com:5432/dedpghnpirtebi"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Username(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.relationship('Artist', backref='username', lazy=True)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arist = db.Column(db.String(120), nullable=False)
    username = db.Column(db.Integer, db.ForeignKey('username.id'),
        nullable=False)

db.create_all()

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
