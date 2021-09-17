from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)

event_cohort = db.Table('event_cohort',
                        db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                        db.Column('cohort_id', db.Integer, db.ForeignKey('cohort.id'), primary_key=True)
                        )

event_campus = db.Table('event_campus',
                        db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                        db.Column('campus_id', db.Integer, db.ForeignKey('campus.id'), primary_key=True)
                        )
