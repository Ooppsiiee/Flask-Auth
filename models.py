from . import db

class DataUser(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    unique_key = db.Column(db.String(100))

    def __init__(self, email, username, password, unique_key):
        self.email = email
        self.username = username
        self.password = password
        self.unique_key = unique_key

