from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'ashd8a9syg879re1g8r1bp9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserData.sqlite3'
db.init_app(app)

from .main import main as main_blueprint
from .auth import auth as auth_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)