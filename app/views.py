from app import app, db
from flask import request, render_template
from flask_cors import cross_origin
import json

@app.route("/",methods=["GET","POST"])
def index():
    return "server is running"

@app.route("/whatever",methods=["GET","POST"])
def whatever():
    whatever = True
    blarg ="yes, yes he sucks"
    reasons = [1,2,3,4]
    reasons.append(5)
    return render_template("whatever.html",reasons=reasons,blarg=blarg,whatever=whatever)

