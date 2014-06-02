#from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy import UniqueConstraint

from kiosk import db

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	uname = db.Column(db.VARCHAR(255), unique = True, nullable = False)
	fullname = db.Column(db.VARCHAR(255), default="")
	email = db.Column(db.VARCHAR(255), default = "")
	zip = db.Column(db.VARCHAR(5), default = "")
	type = db.Column('type', mysql.ENUM('admin','volunteer','guest', 'base_user'),
			default='base_user')
	__table_args__ = (UniqueConstraint('type', 'uname', name='_uname_type_uc'),)

	__mapper_args__ = {
		'polymorphic_on':type,
		'polymorphic_identity':'base_user'
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
