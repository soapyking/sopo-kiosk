from flask import render_template, request, url_for, redirect, session
from kiosk import app

@app.route('/', methods=["GET"])
def emit_welcome():
	return render_template('welcome.html',
			signin_url = url_for('emit_signin'),
			signout_url = url_for('emit_signout')
	)
