from flask import render_template, request, url_for, redirect, session
from kiosk import app, db

from models.user import *
from models.signin import *
from models.event import Event

@app.route('/', methods=["GET"])
def redirect_root():
	return redirect(url_for('emit_signin'))

@app.route('/signin', methods=["GET"])
def emit_signin():
	''' Let user input uname. User will
		continue to volunteer/visit screen or register screen.
	'''
	return render_template("signin.html")

@app.route('/signin', methods=["POST"])
def submit_signin():
	''' User submits user id
		Create new user if doesn't already exist
		Then bring user to edit his info
	'''
	uname = request.form.get('uname')
	whatup = request.form.get('whatup')
	name = request.form.get('fullname')
	email = request.form.get('email')
	zip = request.form.get('zip')
	utype = 'volunteer' if request.form.get('volunteering') else 'guest'
	user_class = Volunteer if request.form.get('volunteering') else Guest
	try:
		user = user_class.query.filter_by(uname=uname).first()
		if not user:
			app.logger.debug("New user %s registered", uname)
			user = user_class()
			user.uname = uname
			user.utype = utype
		user.name = name if name else user.name
		user.email = email if email else user.email
		user.zip = zip if zip else user.zip
		app.logger.debug("User object: {}".format(user))
		db.session.add(user)
		db.session.commit()

		app.logger.debug("User object after commit: {}".format(user))
		signin = Signin()
		app.logger.debug("User id after commit: {}".format(user.id))
		signin.user_id = user.id
		signin.event_id = Event.get_current_event().id
		signin.notes = whatup
		db.session.add(signin)
		db.session.commit()
	except:
		raise # winning
	
	return redirect(url_for('all_good'))

@app.route('/all_good', methods=["GET"])
def all_good():
	return render_template('all_good.html', target=url_for('emit_signin', _external=True))
