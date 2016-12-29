from app import app, db
from flask import request, render_template,redirect, url_for
import json
from app.models import Users

#This is going to be the splash page
@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/results",methods=["GET","POST"])
def results():
    return render_template("results.html")
