from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
  print('create route:  ', request.form['first_name'])
  User.create(request.form)
  return redirect('/results')

@app.route('/results')
def results():
  users = User.get_all()
  # print('results users:  ', users[0].id)
  return render_template("results.html", users = users)

@app.route('/<int:id>/show_one')
def show_one(id):
  user = User.get_one({'id': id})
  return render_template("show_one.html", user = user)

@app.route('/<int:id>/edit/')
# WHERE IS ID COMING FROM?  form action="/update/{{user.id}}"? or somewhere else?
def edit(id):
  user = User.get_one({'id': id})
  print('edit:  ', user)
  return render_template('edit.html', user = user )

@app.route('/<int:id>/update/', methods=['POST'])
# WHERE IS ID COMING FROM?  form action="/update/{{user.id}}"? or somewhere else?
def update(id):
  data = {
    **request.form,
    "id": id
  }
  
  User.update_one(data)
  return redirect('/results')

@app.route('/<int:id>/delete')
def delete(id):
  User.delete_one({'id': id})
  return redirect('/results')

if __name__ == "__main__":
  app.run(debug=True)