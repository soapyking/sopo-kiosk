from sqlalchemy.dialects import mysql
from sqlalchemy import UniqueConstraint
import datetime

from kiosk import db

#from enum import Enum

#class EventType(Enum):
#	SHOP_HOURS = "shop_hours"
#	SHOP_CLASS = "shop_class"
#	SHOP_SPECIAL = "shop_special"
#	REMOTE_EVENT = "remote_event"

class Event(db.Model):
	__tablename__ = 'events'

	id = db.Column(db.Integer, primary_key=True)
	event_type = db.Column(db.Text, mysql.ENUM('shop_hours','shop_class','shop_special', 'remote_event'), default = "shop_hours")
	event_name = db.Column(db.VARCHAR(255))
	time_start = db.Column(db.DateTime, default = datetime.datetime.utcnow())
	time_end = db.Column(db.DateTime)

	@staticmethod
	def get_current_event():
		current = db.session.query(Event).order_by(Event.id.desc()).first()
		if not current:
			current = Event()
			current.event_name = "Default shop hours"
			db.session.add(current)
			db.session.commit()
		return current
