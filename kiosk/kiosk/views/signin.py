from flask import render_template
from flask import url_for
from kiosk import app

@app.route('/signin', methods=["GET"])
def emit_signin():
	return render_template("signin.html")

@app.route('/signin', methods=["POST"])
def submit_signin():
	return render_template(url_for("emit_user_info"))

@app.route('/user_info', methods=["GET"])
def emit_user_info():
	pass
