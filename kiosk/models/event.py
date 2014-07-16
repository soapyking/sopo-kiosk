from sqlalchemy import UniqueConstraint
import datetime

from kiosk import db

from enum import Enum

class EventType(Enum):
	SHOP_HOURS = "shop_hours"
	SHOP_CLASS = "shop_class"
	SHOP_SPECIAL = "shop_special"
	REMOTE_EVENT = "remote_event"

class Event(db.Model):
	__tablename__ = 'events'

	id = db.Column(db.Integer, primary_key=True)
	event_type = db.Column(db.Text, default = EventType.SHOP_HOURS)
	event_name = db.Column(db.VARCHAR(255))
	time_start = db.Column(db.DateTime, default = datetime.datetime.utcnow())
	time_end = db.Column(db.DateTime)

	@staticmethod
	def get_current_event():
		return db.session.query(Event).order_by(Event.id.desc()).first()
