from app import app, db
from flask import request, render_template
from flask_cors import cross_origin
import json

#This is going to be the splash page
@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/sign-up",methods=["GET","POST"])
def sign_up():
    """
    sentence explaining what this method does
    inputs:
    @param x - explanation of param x
    outputs:
    @param y - explanation of param y
    """
    if request.method=="POST":
        print(type(request.form))
        
        username = request.form.get("username")
        password = request.form.get("password_field")
        print(username,password)
    return render_template("sign_up.html")

@app.route("/sign-in",methods=["GET","POST"])
def signin():
    return render_template("sign_in.html")

