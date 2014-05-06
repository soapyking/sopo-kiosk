from flask import render_template
from kiosk import app

@app.route('/signin')
def emit_signin():
	return render_template("signin.html")
