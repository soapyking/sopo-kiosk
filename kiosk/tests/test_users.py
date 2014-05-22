import pytest
from models.user import *
from tests.prep import *

class TestUser:

	@pytest.fixture(scope='function')
	def test_insert_user(self, session_fixture):
		test_user = User()
		test_user.phone = '0000000000'
		test_user.name = 'test_user'
		test_user.type = 'base_user'
		session_fixture.add(test_user)
		session_fixture.commit()

		assert session_fixture.query(User).count() == 1

	@pytest.fixture(scope='function')
	def test_insert_guest(self, session_fixture, test_insert_user):
		test_guest = Guest()
		test_guest.phone = '0000000000'
		test_guest.name = 'test_guest'
		test_guest.type = 'guest'
		session_fixture.add(test_guest)
		session_fixture.commit()

		assert session_fixture.query(Guest).count() == 1
		assert session_fixture.query(User).count() == 2

	def test_recognition(self, client_fixture, session_fixture, test_insert_guest):
		response = client_fixture.get('/signin')
		assert response.status_code == 200
		# TODO match on user identifier

	def test_null(user_fixture):
		assert True
