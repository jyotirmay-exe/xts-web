from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/register")
def registration():
    return(render_template("regForm.html"))

@app.route("/submitregn", methods=["POST"])
def submit():
    return(request.form)

@app.route("/teams")
def teaminfo():
    files = os.walk("./static/assets/heads")
    data = list(files)[0][2]
    dic = {"tech":[],
           "pr":[],
           "exec":[]}
    for ele in data:
        team, name = ele.split('-')
        dic[team].append({"name":name.split('.')[0].upper(),
                          "src": f"/static/assets/heads/{ele}"})
    return render_template("teams.html",heads = dic)

if __name__ == "__main__":
    app.run()