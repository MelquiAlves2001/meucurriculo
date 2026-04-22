from flask import render_template, request, url_for, redirect, jsonify
from conect import app


@app.route("/")
def servicos():
    return render_template("servicos.html")
