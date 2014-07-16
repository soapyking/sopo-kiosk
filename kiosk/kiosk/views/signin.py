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
	session['username'] = ""
	session['whatup'] = ""
	return render_template("signin.html")

@app.route('/signin', methods=["POST"])
def submit_signin():
	''' User submits user id
		Create new user if doesn't already exist
		Then bring user to edit his info
	'''
	uname = request.form['uname']
	user = User.query.filter_by(uname=uname).first()
	if not user:
		app.logger.debug("New user %s registered", uname)
		new_user = User()
		new_user.uname = uname
		db.session.add(new_user)
		db.session.commit()
	session['username'] = uname
	return redirect(url_for('emit_user_info'))

@app.route('/edit_info', methods=["GET"])
def emit_user_info():
	''' Show page for user to edit his info
	'''
	if not session['username']:
		return redirect(url_for('emit_signin'))
	user = User.query.filter_by(uname=session['username']).first()
	return render_template('edit_info.html', email=user.email, zip=user.zip, fullname = user.fullname)

@app.route('/edit_info', methods=["POST"])
def submit_user_info():
	''' Accept user's modified info and update his records
	'''
	if not session['username']:
		return redirect(url_for('emit_signin'))
	email = request.form['email']
	zip = request.form['zip']
	fullname = request.form['fullname']
	whatup = request.form['whatup']
	user = User.query.filter_by(uname=session['username']).first()
	user.email = email if len(email) > 0 else user.email
	user.zip = zip if len(zip) > 0 else user.zip
	user.fullname = fullname if len(fullname) > 0 else user.fullname
	session['whatup'] = whatup
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('emit_waiver'))

@app.route('/waiver_confirm', methods=["GET"])
def emit_waiver():
	''' CYA '''
	if not session['username']:
		return redirect(url_for('emit_signin'))
	return render_template('waiver.html')

@app.route('/waiver_confirm', methods=["POST"])
def accept_waiver():
	''' AC'd '''
	if not session['username']:
		return redirect(url_for('emit_signin'))
	signin = Signin()
	signin.user_id = User.query.filter_by(uname=session['username']).first().id
	signin.event_id = Event.get_current_event().id
	signin.notes = session['whatup']
	db.session.add(signin)
	db.session.commit()
	return redirect(url_for('all_good'))

@app.route('/all_good', methods=["GET"])
def all_good():
	return render_template('all_good.html', target=url_for('emit_signin', _external=True))
