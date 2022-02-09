from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi" + str(request_form['name_input']) + ", nice to meet you.")
	return render_template("index.html")