from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/addninja", methods=["POST"])
def addninja():
    Ninja.save_ninja(request.form)
    return redirect('/')
    

@app.route("/newninja")
def newninja():
    return render_template("newninja.html",dojos=Dojo.get_dojos())



