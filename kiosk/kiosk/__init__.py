from flask import Flask
from sopolib.confighelper import SopoConfig
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from Crypto import Random

app = Flask(__name__)
app.secret_key = Random.new().read(64)

config = SopoConfig()
mysql_user = config.get('mysql','user')
mysql_pass = config.get('mysql','pass', raw=True)
mysql_host = config.get('mysql','host')
mysql_db = config.get('mysql','dbname')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
		mysql_user, mysql_pass, mysql_host, mysql_db)
db = SQLAlchemy(app)
db.session = db.create_scoped_session()
import logging
from logging.handlers import RotatingFileHandler
log_handler = RotatingFileHandler('debug.log', maxBytes=1024*1024)
log_handler.setLevel(logging.DEBUG)
app.logger.addHandler(log_handler)

login_manager = LoginManager()
login_manager.login_view = 'admin_login'
login_manager.init_app(app)

import kiosk.views.welcome
import kiosk.views.signin
import kiosk.views.signout
import kiosk.views.administration
