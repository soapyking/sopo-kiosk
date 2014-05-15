from flask import render_template, request, url_for
from kiosk import app
import re

from models.user import *

''' Let user input phone number. User will
	continue to volunteer/visit screen or register screen.
'''
@app.route('/signin', methods=["GET"])
def emit_signin():
	return render_template("signin.html")

@app.route('/signin', methods=["POST"])
def submit_signin():
	phone_raw = request.form['phone']
	phone = re.sub("\D", "", phone_raw)
	user = session.query(User).get(phone)
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
