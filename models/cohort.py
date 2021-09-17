from config import db


class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    date_start = db.Column(db.Date, nullable=False)
