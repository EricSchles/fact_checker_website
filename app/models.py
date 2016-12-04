"""
Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/

__init__ function for each model is a constructor, and is necessary to enter
""" 
from app import db

class Users(db.Model):
    """
    This model gives us a set of specific information for each user in this application
    
    parameters:
    @username - username of the user
    @password - password of the user, hashed for secrutiy reasons

    functions:
    __str__ - Returns the user name and password as an formatted string <Id: id, Username: username>
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String) #add hashing to this field

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __str__(self):
        return "<ID: {}, Username:{}>".format(self.id,self.username)
