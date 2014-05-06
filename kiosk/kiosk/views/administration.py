from flask import render_template

from kiosk import app

@app.route('/login')
def admin_login():
	return render_template("admin_login.html")
