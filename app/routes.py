from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/Welcome')
def welcome():
    return render_template("Welcome.html")

@app.route('/SignUp')
def sign():
    username = ""
    return render_template("Sign.html", username=username)



    