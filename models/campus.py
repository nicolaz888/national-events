from config import db


class Campus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    short_name = db.Column(db.String(5), unique=True, nullable=False)