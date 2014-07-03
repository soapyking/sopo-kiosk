from flask import render_template, request, url_for, redirect
from kiosk import app, db
import re

from models.user import *

@app.route('/', methods=["GET"])
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
	uname = request.form['uname']
	user = User.query.filter_by(uname=uname).first()
	if not user:
		app.logger.debug("New user %s registered", uname)
		new_user = User()
		new_user.uname = uname
		db.session.add(new_user)
		db.session.commit()
	return redirect(url_for('emit_user_info', uname=uname))

@app.route('/edit_info', methods=["GET"])
def emit_user_info():
	''' Show page for user to edit his info
	'''
	uname = request.args['uname']
	user = User.query.filter_by(uname=uname).first()
	return render_template('edit_info.html', email=user.email, zip=user.zip, fullname = user.fullname)

@app.route('/edit_info', methods=["POST"])
def submit_user_info():
	''' Accept user's modified info and update his records
	'''
	email = request.form['email']
	zip = request.form['zip']
	fullname = request.form['fullname']
	uname = request.args['uname']
	user = User.query.filter_by(uname=uname).first()
	user.email = email if len(email) > 0 else user.email
	user.zip = zip if len(zip) > 0 else user.zip
	user.fullname = fullname if len(fullname) > 0 else user.fullname
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('emit_waiver'))

@app.route('/waiver_confirm', methods=["GET"])
def emit_waiver():
	''' CYA '''
	return render_template('base.html')
