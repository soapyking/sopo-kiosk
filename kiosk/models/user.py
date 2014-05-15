#from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy import UniqueConstraint

from kiosk import db

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	phone = db.Column(db.VARCHAR(255), index=True)
	name = db.Column(db.VARCHAR(255), default="")
	type = db.Column('type', mysql.ENUM('admin','volunteer','guest', 'base_user'),
			default='base_user')
	__table_args__ = (UniqueConstraint('type', 'phone', name='_phone_type_uc'),)

	__mapper_args__ = {
		'polymorphic_on':type
	}

class Admin(User):
	__tablename__ = 'admins'

	id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
	password = db.Column(db.VARCHAR(255))

	__mapper_args__ = { 'polymorphic_identity':'admin' }

class Volunteer(User):
	__tablename__ = 'volunteers'

	id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

	def hours(start_time, end_time):
		''' Calculate hours spent volunteering between time arguments '''
		pass
	__mapper_args__ = { 'polymorphic_identity':'volunteer' }

class Guest(User):
	__tablename__ = 'guests'

	id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

	__mapper_args__ = { 'polymorphic_identity':'guest' }
