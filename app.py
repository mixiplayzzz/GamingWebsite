from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hud")
def hud():
    return render_template("hud.html")

@app.route("/hud/<finger>")
def hud_gallery(finger):
    return render_template("hud_gallery.html", finger=finger)

@app.route("/sensitivity")
def sensitivity():
    return render_template("sensitivity.html")

@app.route("/sensitivity/<level>")
def sensitivity_gallery(level):
    return render_template("sensitivity_gallery.html", level=level.capitalize())
