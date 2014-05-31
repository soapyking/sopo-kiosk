from flask import render_template, request, url_for
from kiosk import app, db
import re

from models.user import *

''' Let user input uname. User will
	continue to volunteer/visit screen or register screen.
'''
@app.route('/signin', methods=["GET"])
def emit_signin():
	return render_template("signin.html")

@app.route('/signin', methods=["POST"])
def submit_signin():
	uname = request.form['uname']
	user = User.query.filter_by(uname=uname).first()
	if user:
		return "true"
	else:
		return "false"

@app.route('/user_info', methods=["GET"])
def emit_user_info():
	pass

@app.route('/waiver_confirm', methods=["GET"])
def emit_waiver():
	pass
