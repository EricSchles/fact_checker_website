from app import app, db
from flask import request, render_template
from flask_cors import cross_origin
import json
from app.models import Users

#This is going to be the splash page
@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index2.html")

#This is going to be the reporting fake-news instructions page
@app.route("/instructions",methods=["GET"])
def instructions():
    return render_template("instructions.html")

# About Route
@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html")

# Sign Up Route
@app.route("/sign-up",methods=["GET","POST"])
def sign_up():
    """
    Takes in username and password and creates new user in the database

    # Inputs:
    #     - @param username: string field
    #     - @param password: string field, currently no validations (12.3.2016)
    # Outputs:
    #     - None
    """
    if request.method=="POST":
        print(type(request.form))
        username = request.form.get("username")
        password = request.form.get("password_field")
        user = Users(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        print(username,password)
    return render_template("sign_up.html")

@app.route("/sign-in",methods=["GET","POST"])
def signin():
    return render_template("sign_in.html")


@app.route("/report",methods=["GET", "POST", "PUT"])
def report():
    return 'This is the report fake news page!'

#    Takes in comment and source url as inputs and creates new (or updates an existing) fake-news report in the database

    # Inputs:
    #     - @param comment: text/string field
    #     - @param sourceurl: string field, currently no validations (12.3.2016)
    # Outputs:
    #     - None Currently
    #     (should generate new report on the DOM)



# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
