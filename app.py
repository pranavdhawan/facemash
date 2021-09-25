#main flask file.
from urllib.request import urlopen

from flask import Flask, render_template, request, session
import helper as hp

app = Flask(__name__)

@app.route("/")
def home():
    with urlopen('https://api.instagram.com/v1/users/pranavdhawan4/?accesstoken=ACCESS-TOKEN') as r:
        img = r.read()
    return render_template("layout.html")

if __name__ == "__main__":
	app.run(debug = True)
