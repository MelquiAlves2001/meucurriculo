from flask import render_template, request, url_for, redirect
from melqui import app

@app.route("/")
def quemsoueu():
    return render_template("quemsoueu.html")

@app.route("/sql")
def sql():
    par_next = request.args.get('next')
    if par_next:
        return redirect(par_next)
    else:
        return render_template("sql.html")

@app.route("/powerbi")
def powerbi():
    return render_template("powerbi.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/excel")
def excel():
    return render_template("excel.html")

@app.route("/word")
def word():
    return render_template("word.html")

@app.route("/powerpoint")
def powerpoint():
    return render_template("powerpoint.html")

@app.route("/administracao")
def administracao():
    return render_template("administracao.html")

@app.route("/gastronomia")
def gastronomia():
    return render_template("gastronomia.html")

@app.route("/html&css")
def htmlecss():
    return render_template("htmlecss.html")