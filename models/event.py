from config import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    attendees = db.Column(db.Integer, default=0, nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.Integer, db.ForeignKey('event_type.id'), nullable=False)

    cohorts = db.relationship('Cohort', secondary='event_cohort')
    campuses = db.relationship('Campus', secondary='event_campus')
