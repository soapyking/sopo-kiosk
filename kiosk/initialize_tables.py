from kiosk import db
from models.user import *
from models.event import *
from models.signin import *

if __name__ == "__main__":
	db.create_all()
