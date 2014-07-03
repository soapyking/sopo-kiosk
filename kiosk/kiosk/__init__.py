from flask import Flask
from sopolib.confighelper import SopoConfig
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)

config = SopoConfig()
mysql_user = config.get('mysql','user')
mysql_pass = config.get('mysql','pass', raw=True)
mysql_host = config.get('mysql','host')
mysql_db = config.get('mysql','dbname')
app_key = config.get('flask','secret_key')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
		mysql_user, mysql_pass, mysql_host, mysql_db)
app.secret_key = app_key
db = SQLAlchemy(app)
db.session = db.create_scoped_session()
import logging
from logging.handlers import RotatingFileHandler
log_handler = RotatingFileHandler('debug.log', maxBytes=1024*1024)
log_handler.setLevel(logging.DEBUG)
app.logger.addHandler(log_handler)

login_manager = LoginManager()
login_manager.init_app(app)

import kiosk.views.signin
import kiosk.views.administration

from models.event import *

app.current_event = db.session.query(Event).order_by(Event.id.desc()).first()
