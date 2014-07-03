from sqlalchemy import UniqueConstraint
import datetime

from kiosk import db
from models.event_types import *

class Signin(db.Model):
	__tablename__ = 'signins'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(Integer, ForeignKey('users.id'), primary_key=True)
	event_id = db.Column(Integer, ForeignKey('events.id'), primary_key=True)
	time_in = db.Column(db.DateTime, default=datetime.datetime.utcnow())
