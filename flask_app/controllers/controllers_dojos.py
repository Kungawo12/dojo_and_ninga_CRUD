from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/')

@app.route('/dojos')
def dojos():
    return render_template("dojo.html", dojos = Dojo.get_dojo())

@app.route('/dojos/add_dojo',methods=['POST'])
def add_dojo():
    data ={
        'name' : request.form['name']
        }
    Dojo.add_dojo(data)
    return redirect('/')

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "id" : id
    }
    return render_template("dojo_ninja.html", dojo = Dojo.get_one_with_ninjas(data))

    