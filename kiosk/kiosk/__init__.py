from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sopolib.confighelper import SopoConfig

app = Flask(__name__)
config = SopoConfig()
mysql_user = config.get('mysql','user')
mysql_pass = config.get('mysql','pass', raw=True)
mysql_host = config.get('mysql','host')
mysql_db = config.get('mysql','dbname') 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
		mysql_user, mysql_pass, mysql_host, mysql_db)

db = SQLAlchemy(app)

import kiosk.views
