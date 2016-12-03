from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String) #add hashing to this field

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __str__(self):
        return "<ID: {}, Username:{}>".format(self.id,self.username)
