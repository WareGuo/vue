from flask import Flask, render_template, request, redirect, url_for, make_response, session
import os
from datetime import timedelta
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = b"\x86\xfc'\x95q\xee@a\xeb\x19T \xbb\x0e\x05\xb6H\xa1\x16\x85\x80\x17Fb"
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)

@app.route("/")
def index():
    placesList = None
    if(session.get('places')):
        placesList=session.get('places').split("@")
    return render_template("index.html",places=placesList)

@app.route("/add", methods=["POST"])
def add():
    place = request.form.get("place")
    places = session.get('places')
    if(places):
        session['places'] = places + "@" +place
    else:
        session['places'] = place
    return redirect(url_for("index"))

@app.route("/output")
def output():
    places = session.get('places')
    if(places):
        placesList = places.split("@")
        a = random.sample(placesList, 1)
        return str(a)
    else:
        return "暂无数据"

if __name__ == "__main__":
    app.run()
