from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo



@app.route("/")
def index():
    return redirect('/showdojos')

@app.route("/adddojo", methods=["POST"])
def adddojo():
    data = {
        "name":request.form["name"],
    }
    Dojo.save_dojo(data)
    return redirect('/showdojos')


@app.route("/showdojos")
def dojo():
    dojos = Dojo.get_dojos()
    return render_template("index.html", dojos=dojos)



@app.route('/dojosninjas/<int:id>')
def dojosninjas(id):
    data = {
        "id":id,
    }
    return render_template("dojosninjas.html",dojo_ninjas=Dojo.get_all_ninjas(data))