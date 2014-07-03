from sqlalchemy import UniqueConstraint
import datetime

from kiosk import db

from enum import Enum

class EventType(Enum):
	SHOP_HOURS = 1
	SHOP_CLASS = 2
	SHOP_SPECIAL = 3
	REMOTE_EVENT = 4

class Event(db.Model):
	__tablename__ = 'events'

	id = db.Column(db.Integer, primary_key=True)
	event_type = db.Column(db.Integer, default = EventType.SHOP_HOURS)
	event_name = db.Column(db.VARCHAR(255))
	time_start = db.Column(db.DateTime, default = datetime.datetime.utcnow())
	time_end = db.Column(db.DateTime)
