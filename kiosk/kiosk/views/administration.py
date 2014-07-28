from flask import render_template, request, session, redirect, url_for
from flask.ext.login import login_required, login_user, logout_user
from sopolib import auth

from kiosk import app, login_manager

@app.route('/administration/login', methods=['GET'])
def admin_login():
	return render_template('admin_login.html')

@app.route('/administration/login', methods=['POST'])
def admin_auth():
	uname = request.form['uname']
	password = request.form['password']
	valid_user = auth.login(uname, password)
	if valid_user:
		login_user(valid_user)
		session['current_admin'] = valid_user.uname
		return redirect(url_for('administration_home'))
	else:
		return render_template('admin_login.html')

@app.route('/administration/logout', methods=['GET'])
@login_required
def admin_logout():
	logout_user()
	session.pop('current_admin', None)
	return redirect(url_for('emit_signin'))

@app.route('/administration', methods=['GET'])
@login_required
def administration_home():
	return render_template('base.html')
