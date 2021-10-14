#Praveen Doluweera 
#First commit for project milestone2

from functions import *
import os
import flask  
from dotenv import find_dotenv, load_dotenv, main
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv, main


app = flask.Flask(__name__)

load_dotenv(find_dotenv())
url = os.getenv("DATABASE_URL")
if url and url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = os.getenv('secret')


db = SQLAlchemy(app)


class Username(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique = True)
  
    def __repr__(self):
        return f"<Username {self.name}"

class Singer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    artistName = db.Column(db.String(120), nullable=False)

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

@app.route('/index', methods = ['GET','POST'])
@login_required
def index():
    if flask.request.method == 'POST':
        data = flask.request.form.get("username")
        user = Singer(userID = current_user.id, artistName = data)
        db.session.add(user)
        db.session.commit()

    username = current_user.id
    data = Singer.query.filter(Singer.userID==username).all()
    print(data)
    if data:
        artist_list = []
        for artist in data:
            data2  = getArtistID(artist.artistName)
            artist_list.append(data2[0])
    
        a= songData(artist_list)
        return flask.render_template("index.html", name = current_user.name, song = a[0], artist = a[1], image= a[2], preview = a[3], url = a[4])
    return flask.render_template("index.html",name = current_user.name, newUser = True)





@app.route('/signup', methods = ["GET", "POST"])
def signup():
    if flask.request.method == 'POST':
        data = flask.request.form.get("username")
        d = Username.query.filter_by(name=data).first()
        print (d)
        if d is None: 
            user = Username(name=data)
            db.session.add(user)
            db.session.commit()
            return flask.redirect("/")
    return flask.render_template("signup.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(("/"))

app.run(
    debug = True,
    host = '0.0.0.0',
    port = int(os.getenv("PORT", 8080))
)

