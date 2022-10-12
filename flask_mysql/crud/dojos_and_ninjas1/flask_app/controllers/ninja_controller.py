from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/ninja/')
def ninja_form():
  dojos = Dojo.get_all_dojos()
  ninjas = Ninja.get_all()
  print("ninjas: ", ninjas)
  print("dojos:  ", dojos)
  return render_template('new_ninja.html', dojos = dojos)

@app.route('/new_ninja', methods=['post'])
def new_ninja():
  print(request.form)
  Ninja.create_new_ninja(request.form)
  return redirect('/')