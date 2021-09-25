#main flask file.

from flask import Flask, render_template, request, session
import helper as hp

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("layout.html")

if __name__ == "__main__":
	app.run(debug = True)
