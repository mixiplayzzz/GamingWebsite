from flask import Flask, render_template
import os

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# Sensitivity main page
@app.route("/sensitivity")
def sensitivity():
    return render_template("sensitivity.html")


# Sensitivity images page
@app.route("/sensitivity/<level>")
def sensitivity_gallery(level):
    return render_template("sensitivity_gallery.html", level=level.capitalize())


