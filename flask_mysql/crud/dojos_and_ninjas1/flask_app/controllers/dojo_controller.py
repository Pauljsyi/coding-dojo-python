from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo_model import Dojo

@app.route('/')
@app.route('/dojos/')
def dojos():
  dojos = Dojo.get_all_dojos()
  return render_template('dojos.html', dojos = dojos)

@app.route('/dojos/new', methods=['post'])
def new_dojo():
  Dojo.create_new_dojo(request.form)
  return redirect('/')

@app.route('/dojos/<int:id>')
def show_dojos(id):
  data ={
    'id': id
  }
  dojo_ninjas = Dojo.get_all_dojo_ninjas(data)
  dojo = Dojo.get_all_dojos()
  print('SHOW_DOJOS: >>>>', dojo_ninjas, "AND ID: >>>", id)
  return render_template('show_dojo.html', dojo_ninjas = dojo_ninjas, current_id = id)