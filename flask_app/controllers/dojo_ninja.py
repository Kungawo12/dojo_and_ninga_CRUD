from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_ninja import Dojo

@app.route('/')
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    return render_template("dojo.html", dojos = Dojo.get_dojo())

@app.route('/dojos/add_dojo',methods=['POST'])
def add_dojo():
    data ={
        'name' : request.form['name']
        }
    Dojo.add_dojo(data)
    return redirect('/dojos')