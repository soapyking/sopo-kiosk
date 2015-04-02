from kiosk import db
from models.user import *
from models.event import *
from models.signin import *
from Crypto.Hash import SHA256

if __name__ == "__main__":
		db.drop_all()
		db.create_all()
		first_admin = Admin()
		first_admin.uname = 'admin'
		first_admin.fullname = 'admin'
		first_admin.password = SHA256.new('stronkpass'.encode('utf-8')).hexdigest()
		db.session.add(first_admin)
		db.session.commit()
