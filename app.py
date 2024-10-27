from flask import Flask, request, render_template, url_for, redirect, jsonify
from discord_webhook import DiscordWebhook, DiscordEmbed
from modules.supabase import SupabaseConn
from dotenv import load_dotenv
import json, sys, os
import logging

app = Flask(__name__)

load_dotenv()

with open('./static/config.json') as f:
    conf = json.load(f)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

supabase = None
webhook = DiscordWebhook(url=os.getenv("WEBHOOK_URL"))

try:
    supabase = SupabaseConn(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
    logging.info("Supabase connection successful.")
except Exception as ex:
    logging.error("Supabase connection failed. Exiting.")
    logging.error(ex)
    sys.exit()

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Accessed Home page.")
    return render_template('index.html')

@app.route("/register")
def registration():
    try:
        supabase.ping()
        logging.info("Supabase connection active.")
    except Exception as ex:
        logging.error("Failed to ping Supabase server.")
        return "Internal Server Error. Please try again later.", 500    
    logging.info("Accessed Registration page.")
    return render_template("regForm.html")

@app.route("/submitregn", methods=["POST"])
def submit():
    logging.info("Registration form submitted.")
    
    full_name = request.form["fullName"]
    dept = request.form["dept"]
    sem = request.form["sem"]
    exam_roll = request.form["examroll"]
    if len(exam_roll) < 12:
        exam_roll += " (Class)"
    email = request.form["email"]
    whatsapp = request.form["whatsapp"]
    team = request.form["team"]
    skill = request.form["skill"]
    about = request.form["about"]

    supabase.insert_app(full_name, dept, sem, exam_roll, email, whatsapp, team, skill, about)

    return redirect(url_for('registration', success='true'))

@app.route("/api/applications", methods=["GET", "OPTIONS"])
def get_applications():
    if request.method == "OPTIONS":
        response = jsonify() 
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "GET, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "API-Key")
        return response

    api_key = request.headers.get("API-Key")
    if api_key != os.getenv("API_KEY"):
        logging.warning("Unauthorized access attempt to /api/applications.")
        return {"error": "Unauthorized access"}, 401

    try:
        applications = supabase.select_all() 
        logging.info("Fetched all applications for authorized request.")
        
        response = jsonify({"applications": applications})
        response.headers.add("Access-Control-Allow-Origin", "*")
        
        return response, 200
    except Exception as ex:
        logging.error("Error fetching applications.")
        logging.error(ex)
        return {"error": "Internal Server Error"}, 500

@app.route("/patrons")
def patronsinfo():
    logging.info("Accessed Patrons Info page.")
    return render_template("patrons.html", patrons=conf['patrons'])

@app.route("/faqs")
def faq():
    logging.info("Accessed FAQs page.")
    return render_template("faqs.html")

@app.route("/tnc")
def terms():
    logging.info("Accessed Terms and Conditions page.")
    return render_template("tnc.html")

@app.route("/teams")
def teaminfo():
    logging.info("Accessed Teams Info page.")
    return render_template("teams.html", heads=conf['team-heads'], members=conf['team-members'])

@app.route("/contact")
def contactus():
    logging.info("Accessed Contact Us page.")
    return render_template("contact.html")

@app.route("/send-message", methods=["POST"])
def sendMessage():
    logging.info("Contact form submitted.")
    
    name = request.form['name']
    email = request.form['email']
    msg = request.form['message']

    embed = DiscordEmbed(title="Message Recvd.", description="", color="03b2f8")
    embed.add_embed_field(name="Name", value=f"{name}")
    embed.add_embed_field(name="Email", value=f"{email}", inline=False)
    embed.add_embed_field(name="Message", value=f"{msg}", inline=False)

    webhook.add_embed(embed)
    response = webhook.execute()

    return
