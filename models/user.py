from config import db
from models.base_model import BaseModel


class User(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    events_created = db.relationship('Event', backref='user')
