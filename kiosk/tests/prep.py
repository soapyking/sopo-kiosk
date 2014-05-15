# Inspired from http://alexmic.net/flask-sqlalchemy-pytest/
import os
import pytest
from flask import Flask

from kiosk import app, db, config
from sopolib.confighelper import SopoConfig


@pytest.fixture(scope='session')
def app_fixture(request):
	app = Flask(__name__)

	config = SopoConfig()
	mysql_user = config.get('mysql','user')
	mysql_pass = config.get('mysql','pass', raw=True)
	mysql_host = config.get('mysql','host')
	mysql_db = "sopo_test"

	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
			mysql_user, mysql_pass, mysql_host, mysql_db)

	test_context = app.app_context()
	test_context.push()

	def teardown():
		test_context.pop()

	request.addfinalizer(teardown)
	return app

@pytest.fixture(scope='session')
def db_fixture(app_fixture, request):
	db = SQLAlchemy(app_fixture)
	db.create_all()

	def teardown():
		db.drop_all()

	request.addfinalizer(teardown)
	return db

@pytest.fixture(scope='function')
def session_fixture(db_fixture, request):
	db_fixture.session = db_fixture.create_scoped_session()

	def teardown():
		db_fixture.session.rollback()
		db_fixture.session.remove()

	request.addfinalizer(teardown)
	return db_fixture.session
