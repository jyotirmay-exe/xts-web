import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def home():
    return("HOME")

@app.route("/register")
def registration():
    return("REGISTER")

@app.route("/teams")
def teaminfo():
    return("TEAMS")

if __name__ == "__main__":
    app.run()