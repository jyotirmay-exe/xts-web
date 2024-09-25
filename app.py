from flask import Flask, request, render_template
import json

app = Flask(__name__)

with open('./config.json') as f:
    conf = json.load(f)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register")
def registration():
    return(render_template("regForm.html"))

@app.route("/submitregn", methods=["POST"])
def submit():
    return(request.form)

@app.route("/patrons")
def patronsinfo():
    return render_template("patrons.html")

@app.route("/teams")
def teaminfo():
    return render_template("teams.html",heads = conf['team-heads'])

if __name__ == "__main__":
    app.run()