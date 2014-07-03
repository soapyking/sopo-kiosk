from sqlalchemy import UniqueConstraint
import datetime

from kiosk import db
from models.event_types import *

import Enum

class EventType(Enum):
	SHOP_HOURS = 1
	SHOP_CLASS = 2
	SHOP_SPECIAL = 3
	REMOTE_EVENT = 4

class Event(db.Models):
	__tablename__ = 'events'

	def __init__(self, event_type):
		if event_type == EventType.SHOP_HOURS:

	id = db.Column(db.Integer, primary_key=True)
	event_type = db.Column(db.Integer, default = EventType.SHOP_HOURS)
	event_name = db.Column(db.VARCHAR(255))
	time_start = db.Column(db.DateTime, default = datetime.datetime.utcnow())
	time_end = db.Column(db.DateTime)
