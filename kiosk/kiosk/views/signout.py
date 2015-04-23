from flask import render_template, request, url_for, redirect, session, abort, current_app
from kiosk import app, db

from models.user import *
from models.signin import *
from models.event import Event

@app.route('/signout', methods=["GET"])
def emit_signout():
	''' Let user leave feedback	'''
	return render_template("signout.html")

@app.route('/signout', methods=["POST"])
def submit_signout():
	uname = request.form.get('uname')
	feedback = request.form.get('feedback')
	try:
		user = User.query.filter_by(uname=uname).first()
		if not user:
			app.logger.warn("User by name {0} not found".format(uname))
			raise Exception("User by name {0} not found".format(uname)) # must improve this
		latest_signin = Signin.query.filter_by(user_id = user.id).order_by(Signin.time_in.desc()).first()
		latest_signin.feedback = feedback
		latest_signin.time_out = datetime.datetime.now()
		db.session.add(latest_signin)
		db.session.commit()
	except:
		db.session.rollback()
		raise

	return redirect(url_for('all_good'))
