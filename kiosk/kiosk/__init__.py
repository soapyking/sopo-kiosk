from flask import Flask
from sopolib.confighelper import SopoConfig
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

config = SopoConfig()
mysql_user = config.get('mysql','user')
mysql_pass = config.get('mysql','pass', raw=True)
mysql_host = config.get('mysql','host')
mysql_db = config.get('mysql','dbname')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
		mysql_user, mysql_pass, mysql_host, mysql_db)
db = SQLAlchemy(app)
db.session = db.create_scoped_session()

import kiosk.views.signin
import kiosk.views.administration
