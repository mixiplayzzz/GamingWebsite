from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# HUD main page
@app.route("/hud")
def hud():
    return render_template("hud.html")


# HUD images page
@app.route("/hud/<finger>")
def hud_gallery(finger):
    return render_template("hud_gallery.html", finger=finger)


# Sensitivity main page
@app.route("/sensitivity")
def sensitivity():
    return render_template("sensitivity.html")


# Sensitivity images page
@app.route("/sensitivity/<level>")
def sensitivity_gallery(level):
    return render_template("sensitivity_gallery.html", level=level.capitalize())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
