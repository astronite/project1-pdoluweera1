#Praveen Doluweera 
#First commit for project milestone2

from functions import *
import os
import flask  
from dotenv import find_dotenv, load_dotenv, main
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://kuzgfouwsjmldd:67464b0aa5c549c457e27fa4d938c9e5066373fdd48ed68516f0726887ca2697@ec2-3-215-83-124.compute-1.amazonaws.com:5432/dedpghnpirtebi"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '0045b9de9d4fe8cb33009403fc47d3077e681c64ebc4e83f32c763adbc420d47'


db = SQLAlchemy(app)


class Username(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique = True)
  
    def __repr__(self):
        return f"<Username {self.name}"

class Arist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(120), nullable=False, unique = True)
    aristName = db.Column(db.String(120), nullable=False, unique = True)

db.create_all()

login_manager = LoginManager()
login_manager.login_view = '/'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Username.query.get(int(user_id))

@app.route('/', methods = ['GET','POST'])

def login():
    if flask.request.method == "POST":
        data = flask.request.form.get("username")
        user = Username.query.filter_by(name=data).first()
        if user:
            login_user(user)
            return flask.redirect('/index')
        else:
            print("error")

    return flask.render_template("login.html")

@app.route('/index')
@login_required
def index():
    a= songData()
    return flask.render_template("index.html", song = a[0], artist = a[1], image= a[2], preview = a[3], url = a[4])

@app.route('/signup', methods = ["GET", "POST"])
def signup():
    if flask.request.method == 'POST':
        data = flask.request.form.get("username")
        user = Username(name=data)
        db.session.add(user)
        db.session.commit()
        return flask.redirect("/")

    return flask.render_template("signup.html")

app.run(
    debug = True,
    host = '0.0.0.0',
    port = int(os.getenv("PORT", 8080))
)

