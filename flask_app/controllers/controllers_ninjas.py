from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html",dojos = Dojo.get_dojo())

@app.route("/ninjas/add_ninjas",methods=["POST"])
def add_ninjas():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    ninja.Ninja.add_ninja(data)
    return redirect('/dojos')

@app.route("/ninjas/edit/<int:id>/<int:dojo_id>")
def edit_ninja(id,dojo_id):
    data= {
        "id": id
        }
    dojo_data={
        "id": dojo_id
    }
    one_ninja =ninja.Ninja.show_ninja(data)
    return render_template("edit_ninja.html",ninja = one_ninja,dojo=Dojo.show_dojo(dojo_data))

@app.route("/ninjas/update/<int:id>/<int:dojo_id>",methods=["POST"])
def update(id,dojo_id):
    data={
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
    }
    data['dojo_id'] = dojo_id
    ninja.Ninja.update(data)
    return redirect(f"/dojos/{dojo_id}")

@app.route("/ninjas/delete/<int:id>/<int:dojo_id>")
def delete(id,dojo_id):
    data= {
        "id": id
    }
    ninja.Ninja.delete_ninja(data)
    return redirect(f"/dojos/{dojo_id}")