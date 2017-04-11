from app import app 
from flask import render_template, request

@app.route("/")
def index():
	return render_template('index.html', palavrasChaves=["palavra1", "palavra2", "palavra2", "palavra2"], texto=None)