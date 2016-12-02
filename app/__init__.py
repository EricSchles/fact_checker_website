from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from .commands import REPL
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "testing"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://eric_s:1234@localhost/testing"
db = SQLAlchemy(app)
migrate = Migrate(app,db)
cors = CORS(app, resources={"/send_data":{"origins":"serene-reef-39081.herokuapp.com"})

app.config["CORS_HEADERS"] = 'Content-Type'
headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": '*',
    "Access-Control-Allow-Methods": 'PUT, GET, POST, DELETE, OPTIONS',
    "Access-Control-Allow-Headers": 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
}
manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command("shell",REPL())

from app import views, models
