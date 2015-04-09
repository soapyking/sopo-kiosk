from flask import render_template, request, session, redirect, url_for, make_response
from flask.ext.login import login_required, login_user, logout_user
import datetime
import io
import csv

from sopolib import auth
from kiosk import app, login_manager
from models.signin import *

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
		return redirect(request.args.get("next") or url_for('administration_home'))
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
	return render_template('admin_home.html')

@app.route('/administration/download/guest_signins')
@login_required
def download_signins(since=None):
	intimeformat = "%m/%d/%Y"
	outtimeformat = "%Y-%b-%dT%H-%M-%S"
	nowtime = datetime.datetime.utcnow()
	since = request.args.get('since', None)
	if since:
		since = datetime.datetime.strptime(since, intimeformat)
		since = since.strftime(outtimeformat)
	else:
		# By default, give signins in last week
		since = (nowtime - datetime.timedelta(weeks=1)).strftime(outtimeformat)
	# If excel allowed commented lines...
	#csv_body = "\"\"\" These are the guest signins since {0} \"\"\"".format(since)
	csv_body = ""
	recent_signins = Signin.query.filter(Signin.time_in >= since).all()
	with io.BytesIO() as csv_out:
		csv_writer = csv.writer(csv_out, dialect='excel', quoting=csv.QUOTE_ALL)
		for signin in recent_signins:
			guest = signin.user
			if guest.utype in ['guest', 'base_user']:
				event = signin.event
				csv_line = [
						guest.uname,
						guest.email,
						guest.uzip,
						signin.time_in.strftime(outtimeformat),
						signin.notes,
				]
				csv_writer.writerow(csv_line)
		csv_body = csv_body + csv_out.getvalue()
	response = make_response(csv_body)
	dated_filename = "guests_{0}_{1}".format(since, nowtime.strftime(outtimeformat))
	response.headers["Content-Disposition"] = "attachment; filename={0}.csv".format(dated_filename)
	return response

def utf_8_encoder(unicode_csv_data):
	for line in unicode_csv_data:
		yield line.encode('utf-8')
