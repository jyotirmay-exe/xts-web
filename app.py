from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    # return("HOMEPAGE")
    return render_template('index.html')

@app.route("/register")
def registration():
    return(render_template("index.html"))

@app.route("/submitregn", methods=["POST"])
def submit():
    return(request.form)

@app.route("/teams")
def teaminfo():
    return("TEAMS")

if __name__ == "__main__":
    app.run()