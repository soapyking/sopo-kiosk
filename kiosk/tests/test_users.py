import pytest
from models.user import *
from tests.prep import *

class TestUser:

	@pytest.fixture(scope='function')
	def user_fixture(session_fixture, request):
		db.session.execute("drop database if exists {0}".format(self.test_db_name))
		db.session.execute("create database {0}".format(self.test_db_name))
		db.session.commit()
		test_user = User()
		test_user.phone = '0000000000'
		test_user.name = 'test_user'
		test_user.type = ''
		test_user.type = ''
		db.session.add(test_user)
		db.session.commit()

	def test_null(user_fixture, request):
		assert True
