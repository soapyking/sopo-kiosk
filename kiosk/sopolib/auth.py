from models.user import Admin
from Crypto.Hash import SHA256
from kiosk import login_manager, app

@login_manager.user_loader
def load_user(user_id):
  return Admin.query.filter_by(id=user_id).first()

def login(username, password):
  admin = Admin.query.filter_by(uname=username).first()
  passhash = SHA256.new(password.encode('utf-8')).hexdigest()
  #app.logger.error("{0} tried to log in with passhash {1}".format(username, passhash))
  #Adjust Admin model for password salts
  if admin and passhash == admin.password:
    return admin
  else: return None
