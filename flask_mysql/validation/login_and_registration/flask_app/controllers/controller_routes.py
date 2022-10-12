from flask import render_template, redirect, request, session
from flask_app import app

@app.route('/dashboard')
def dashboard():
  if 'uuid' not in session:
    return redirect('/user/new')
  return render_template('dashboard.html')