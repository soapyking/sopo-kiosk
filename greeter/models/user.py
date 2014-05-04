from sqlalchemy import Column, Integer, String, ForeignKey

from base_model import Base

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	phone = Column(String, index=True)
	name = Column(String, default="")
	type = Column(String)

	__mapper_args__ = {
		'polymorphic_identity':'',
		'polymorphic_on':type
	}

class Admin(User):
	__tablename__ = 'admins'

	id = Column(Integer, ForeignKey('users.id'), primary_key=True)
	password = Column(String)
	
	__mapper_args__ = { 'polymorphic_identity':'admin' }

class Volunteer(User):
	__mapper_args__ = { 'polymorphic_identity':'volunteer' }

	def hours(start_time, end_time):
		''' Calculate hours spent volunteering between time arguments '''
		pass

class Guest(User):
	__mapper_args__ = { 'polymorphic_identity':'guest' }
