from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
  User.create(request.form)
  return redirect('/results')

@app.route('/results')
def results():
  users = User.get_all()
  return render_template("results.html", users = users)

@app.route('/edit')
def edit():
  return render_template('edit.html')

if __name__ == "__main__":
  app.run(debug=True)