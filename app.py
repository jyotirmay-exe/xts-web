from flask import Flask, request, render_template, url_for, redirect
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
    return render_template("patrons.html", patrons = conf['patrons'])

@app.route("/teams")
def teaminfo():
    return render_template("teams.html", heads = conf['team-heads'])

@app.route("/contact")
def contactus():
    return render_template("contact.html")

@app.route("/send-message", methods=["POST"])
def sendMessage():
    name = request.form['name']
    email = request.form['email']
    msg = request.form['message']
    print(name, email, msg)
    return redirect(url_for("contactus"))

if __name__ == "__main__":
    app.run()