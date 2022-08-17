from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Meetings(db.Model):
    __tablename__ = "meetings"

    id = db.Column(db.Integer(), primary_key = True)
    topic = db.Column(db.String())
    date = db.Column(db.String())
    s_Time = db.Column(db.String())
    e_Time = db.Column(db.String())
    users = db.Column(db.String())

    def __init__(self,topic,date,s_Time,e_Time,users):
        self.topic = topic
        self.date = date
        self.s_Time = s_Time
        self.e_Time = e_Time
        self.users = users

    def __repr__(self):
        return f"{self.topic}"
