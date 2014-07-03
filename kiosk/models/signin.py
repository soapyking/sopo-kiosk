from sqlalchemy import UniqueConstraint
import datetime

from kiosk import db

class Signin(db.Model):
	__tablename__ = 'signins'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
	event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
	time_in = db.Column(db.DateTime, default=datetime.datetime.utcnow())
