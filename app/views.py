from app import app, db
from flask import request
from flask_cors import cross_origin
import json
import tools


@app.route("/",methods=["GET","POST"])
def index():
    return "server is running"

