""" views.py """

from flask import render_template

from app import app

@app.route('/')

def index():
    return render_template("index.html")

@app.route("/leaderboards")

def leaderboards():
    return render_template("leaderboards.html")

@app.route("/challenges")

def challenges():
    return render_template("challenges.html")

@app.route("/about")

def about():
    return render_template("about.html")