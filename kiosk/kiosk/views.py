from kiosk import app

@app.route('/')
def emit_login():
	return "Login page"
