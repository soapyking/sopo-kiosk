from flask import render_template, request, url_for, redirect
from kiosk import app, db
import re

from models.user import *

''' Let user input uname. User will
	continue to volunteer/visit screen or register screen.
'''
@app.route('/', methods=["GET"])
@app.route('/signin', methods=["GET"])
def emit_signin():
	return render_template("signin.html")

@app.route('/signin', methods=["POST"])
def submit_signin():
	uname = request.form['uname']
	return redirect(url_for('emit_user_info', uname=uname))

@app.route('/edit_info', methods=["GET"])
def emit_user_info():
	uname = request.args['uname']
	user = User.query.filter_by(uname=uname).first()
	if user:
		return render_template('edit_info.html', returning = True)
	else:
		return render_template('edit_info.html', returning = False)

@app.route('/waiver_confirm', methods=["GET"])
def emit_waiver():
	pass
