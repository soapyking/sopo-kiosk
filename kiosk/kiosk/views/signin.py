from flask import render_template, request, url_for, redirect, session
from kiosk import app, db

from models.user import *
from models.signin import *
from models.event import Event

@app.route('/', methods=["GET"])
def redirect_root():
	return redirect(url_for('emit_welcome'))

@app.route('/signin', methods=["GET"])
def emit_signin():
	''' Let user input uname. User will
		continue to volunteer/visit screen or register screen.
	'''
	return render_template("signin.html")

@app.route('/signin', methods=["POST"])
def submit_signin():
	''' Ingest user's information, make record of existence '''
	uname = request.form.get('uname')
	whatup = request.form.get('whatup')
	fullname = request.form.get('fullname')
	email = request.form.get('email')
	uzip = request.form.get('zip')
	utype = 'volunteer' if request.form.get('volunteering') else 'guest'
	user_class = Volunteer if request.form.get('volunteering') else Guest # one step shy of metaclassing off a cliff
	try:
		user = user_class.query.filter_by(uname=uname).first()
		if not user:
			app.logger.debug("New user %s registered", uname)
			user = user_class()
			user.uname = uname
			user.utype = utype
		if fullname:
			user.fullname = fullname
		if not user.fullname:
			user.fullname = ""
		if email:
			user.email = email
		if not user.email:
			user.email = ""
		if uzip:
			user.uzip = uzip
		if not user.uzip:
			user.uzip = ""
		user.email = email if email else user.email if user.email else ""
		user.uzip = uzip if uzip else user.uzip if user.uzip else ""
		app.logger.debug("User object: {}".format(user))
		db.session.add(user)
		db.session.commit()

		signin = Signin()
		signin.user_id = user.id
		signin.event_id = Event.get_current_event().id
		signin.notes = whatup
		db.session.add(signin)
		db.session.commit()
	except:
		db.session.rollback()
		raise # winning

	return redirect(url_for('all_good'))

@app.route('/scratch', methods=["GET"])
def scratch():
	return render_template("scratch.html")

@app.route('/all_good', methods=["GET"])
def all_good():
	return render_template('all_good.html', target=url_for('emit_welcome', _external=True))
