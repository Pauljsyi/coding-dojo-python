from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User

@app.route('/')
@app.route('/user/new')
def user_new():
  if 'uuid' in session:
    redirect('/dashboard')
  users = User.get_all()
  return render_template("login.html", users = users)

@app.route('/user/create', methods=['POST'])
def user_create():
  #validate
  if not User.validator(request.form):
    return redirect('/user/new')
  # hash password

  hash_password = bcrypt.generate_password_hash(request.form['password'])
  
  data = {
    **request.form,
    'password': hash_password  
    }
  print(data)
  # add to db
  # print('request-form in CREATE:  ', request.form['confirm_password'])
  # if request.form['confirm_password'] != request.form['password']:
  #   return redirect('/')
  
  id = User.create(data)
  session['uuid'] = id
  return redirect('/dashboard')

# @app.route('/user_page')
# def user_page():
#   user = User.get_one()
#   # print('results users:  ', users[0].id)
#   return render_template("user_page.html", user = user)
@app.route('/user/login', methods=['post'])
def login():
    user = User.get_one_by_email(request.form)
    if not User.validate_login(request.form):
      return redirect('/user/new')
    # if not user:
    #   flash("Invalid Email", "err_login_email")
    #   return redirect('/')
    print(request.form)
    print('HELLO:   ', user)
    if user == False:
      flash('Email does not match our records', 'err_login_email')
      return redirect('/')
    if not bcrypt.check_password_hash(user['password'], request.form['password']):
      flash("Invalid Password", "err_login_password")
      return redirect('/')
    
    session['uuid'] = user['id']
    # user = User.get_one({'email': email, 'password': password})
    return redirect('/dashboard')

@app.route('/user/show/<int:id>')
def show_user(id):
  user = User.get_one({'id', id})
  return render_template("user_page.html", user = user)

@app.route('/user/<int:id>/')
# WHERE IS ID COMING FROM?  form action="/update/{{user.id}}"? or somewhere else?
def user_page(id):
  user = User.get_one({'id': id})
  return render_template('user_page.html', user = user )

@app.route('/<int:id>/update/', methods=['POST'])
# WHERE IS ID COMING FROM?  form action="/update/{{user.id}}"? or somewhere else?
def update(id):
  data = {
    **request.form,
    "id": id
  }
  
  User.update_one(data)
  return redirect('/')

@app.route('/<int:id>/delete')
def delete(id):
  User.delete_one({'id': id})
  return redirect('/')
