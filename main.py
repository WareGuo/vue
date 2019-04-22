from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route("/")
def index():
    places=request.cookies.get('places')
    return render_template("index.html",places=places)

@app.route("/add", methods=["POST"])
def add():
    temp = redirect(url_for("index"))
    response = make_response(temp)
    place = request.form.get("place")
    places = request.cookies.get('places')
    if(places):
        place += places
    response.set_cookie("places", place, expires=100000000)
    return response

if __name__ == "__main__":
    app.run()