from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
#Idk what your config is but change the Username or password to match yours. 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:24745252@localhost/capstone"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
