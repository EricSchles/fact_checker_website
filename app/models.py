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
    @name - the persons name; in order first, last
    @email - the person's gsa email
    functions:
    __str__ - Returns the user name and password as an formatted string <Id: id, Username: username>
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String,unique=True) 

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __str__(self):
        return "<name: {}, email:{}>".format(self.name,self.email)

class Languages(db.Model):
    """
    This model gives us a mapping from email to the languages associated with that user

    parameters:
    @email - the person's gsa email
    @language - a computer programming language the person knows
    @competency_level - describes the skill level with a given language, 
    options are: novice, basic, experienced, expert, master 
    """
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    language = db.Column(db.String)
    competency_level = db.Column(db.String)

    def __init__(self,email,language,competency_level):
        self.email = email
        self.language = language
        self.competency_level = competency_level

    def __str__(self):
        return repr(self.email)

class Specializations(db.Model):
    """
    This model gives us a mapping from email to the specializations associated with that user.
    
    parameters:
    @email - the person's gsa email
    @specialization - this is a broad set of discrete skills
    @competency_level - describes the skill level with a given specialization,
    options are: novice, basic, experienced, expert, master
    """
    __tablename__ = 'specializations'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    specialization = db.Column(db.String)
    competency_level = db.Column(db.String)

    def __init__(self,email,specialization,competency_level):
        self.email = email
        self.specialization = specialization
        self.competency_level = competency_level

class SocialConnections(db.Model):
    """
    This model captures the relationships at 18F.  Everything is with respect to a user.
    
    parameters:
    @email - the person's gsa email
    @facilitator - the person's facilitator
    @manager - the person's manager
    @mentored - someone this person has mentored - these relationships are modeled by the mentored table 
    @mentored_by - someone who has mentored this person - these relationships are modeled by the mentored table 
    @worked_project 
    """
    __tablename__ = "social_connections"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    facilitator = db.Column(db.String)
    manager = db.Column(db.String)
    mentored = db.relationship('SocialConnections',
                               secondary=mentored,
                               primaryjoin=(mentored.c.mentee == email),
                               secondaryjoin=(mentored.c.mentored == email),
                               backref=db.backref('mentored', lazy='dynamic'),
                               lazy='dynamic')
                                            
    def __init__(self,email,specialization,competency_level):
        self.email = email
        self.specialization = specialization
        self.competency_level = competency_level

    def mentored(self, mentor):
        if not self.mentored_by(mentor):
            self.mentored.append(mentor)
            return self

    def menteed(self, mentee):
        if not self.menteed_by(mentee):
            self.menteed.append(mentee)
            return self
        
mentored = db.Table('mentored',
    db.Column('mentee', db.Integer, db.ForeignKey('social_connections.email')),
    db.Column('mentored', db.Integer, db.ForeignKey('social_connections.email'))
)

