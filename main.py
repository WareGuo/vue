from flask import Flask, render_template, request, redirect, url_for, make_response, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)

@app.route("/")
def index():
    places=session.get('places')
    return render_template("index.html",places=places)

@app.route("/add", methods=["POST"])
def add():
    place = request.form.get("place")
    places = session.get('places')
    if(places):
        session['places'] = places + place
    else:
        session['places'] = place
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()