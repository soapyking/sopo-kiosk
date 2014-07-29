from sqlalchemy import UniqueConstraint
import datetime

from kiosk import db

class Signin(db.Model):
	__tablename__ = 'signins'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
	event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True, nullable=False)
	time_in = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)
	notes = db.Column(db.VARCHAR(255), default="", nullable=True)
	user = db.relationship("User", backref="Signin")
	event = db.relationship("Event", backref="Signin")
