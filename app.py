from flask import Flask, request, render_template, url_for, redirect
from modules.mysql import MySQLConn
import json, sys

app = Flask(__name__)

with open('./config.json') as f:
    conf = json.load(f)

sqlconf = conf['mysqldb']
mysql = None

try:
    mysql = MySQLConn(sqlconf['host'], sqlconf['user'], sqlconf['password'], sqlconf['db'])
    print("MySQL conn. successful..")
except:
    print("MYSQL error.. Exiting")
    sys.exit()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register")
def registration():
    return(render_template("regForm.html"))

@app.route("/submitregn", methods=["POST"])
def submit():
    full_name = request.form["fullName"]
    dept = request.form["dept"]
    sem = request.form["sem"]
    exam_roll = request.form["examroll"]
    email = request.form["email"]
    whatsapp = request.form["whatsapp"]
    team = request.form["team"]
    skill = request.form["skill"]
    about = request.form["about"]

    mysql.insertApp(full_name,dept,sem,exam_roll,email,whatsapp,team,skill,about)

    return(redirect(url_for('registration', success='true')))

@app.route("/patrons")
def patronsinfo():
    return render_template("patrons.html", patrons = conf['patrons'])

@app.route("/faqs")
def faq():
    return render_template("faqs.html")

@app.route("/tnc")
def terms():
    return render_template("tnc.html")

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