from flask import render_template, request, url_for, redirect, session
from kiosk import app, db

from models.user import *
from models.signin import *
from models.event import Event

@app.route('/signout', methods=["GET"])
def emit_signout():
	''' Let user leave feedback	'''
	return render_template("signout.html")
