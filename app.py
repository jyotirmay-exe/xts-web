from flask import Flask, request, render_template, url_for, redirect
from discord_webhook import DiscordWebhook, DiscordEmbed
from modules.mysql import MySQLConn
from dotenv import load_dotenv
import json, sys, os

app = Flask(__name__)

load_dotenv()

with open('./static/config.json') as f:
    conf = json.load(f)

mysql = None
webhook = DiscordWebhook(url=os.getenv("WEBHOOK_URL"), username="New Webhook Username")

try:
    mysql = MySQLConn(os.getenv('DB_HOST'), os.getenv('DB_USER'), os.getenv('DB_PASS'), os.getenv('DB_NAME'))
    print("MySQL conn. successful..")
except Exception as ex:
    print("MYSQL error.. Exiting")
    print(ex)
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
    return render_template("teams.html", heads = conf['team-heads'], members = conf['team-members'])

@app.route("/contact")
def contactus():
    return render_template("contact.html")

@app.route("/send-message", methods=["POST"])
def sendMessage():
    name = request.form['name']
    email = request.form['email']
    msg = request.form['message']

    embed = DiscordEmbed(title="Message Recvd.", description="", color="03b2f8")
    embed.add_embed_field(name="Name", value=f"{name}")
    embed.add_embed_field(name="Email", value=f"{email}", inline=False)
    embed.add_embed_field(name="Message", value=f"{msg}", inline=False)

    webhook.add_embed(embed)
    response = webhook.execute()

    return redirect(url_for("contactus"))

if __name__ == "__main__":
    app.run()