"""
Flask: Form handling
"""

from flask import Flask, url_for, redirect, request

app = Flask(__name__)

HTML_FRAME_TOP = "<!DOCTYPE HTML>\n<html>\n<head>\n<title>Flask form example</title>\n</head>\n<body>\n"
HTML_FRAME_BOTTOM = "</body>\n</html>\n"

postcodes = {
    "0001": "Oslo",
    "4036": "Stavanger",
    "4041": "Hafrsfjord",
    "7491": "Trondheim",
    "9019": "Tromsø"
}

@app.route("/")
def index():
    # redirect to form
    return redirect(url_for("static", filename="exercise1.html"))


@app.route("/sendform", methods=["GET"])
def getEntry():
    number = request.args["number"]
    city = postcodes.get(number, None)
    html = HTML_FRAME_TOP.replace("{css}", url_for("static", filename="style.css"))

    if city != None:
        html += number + " : " + city + "<br>"
    else:
        html += "No city with postnumber " + number + " was found"

    html += "<br><a href='" + url_for("index") + "'> back </a>"
    html += HTML_FRAME_BOTTOM
    return html

@app.route("/sendform", methods=["POST"])
def addEntry():
    number = request.form["number"]
    city = request.form["city"]
    postcodes[number] = city

    html = HTML_FRAME_TOP
    html += "Added: " + city + " with Postnumber: " + number + "<br>"
    html += "<br><a href='" + url_for("index") + "'> back </a>"
    html += HTML_FRAME_BOTTOM

    return html


if __name__ == "__main__":
    app.run()
