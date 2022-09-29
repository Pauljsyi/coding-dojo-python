from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by_eight(x=8, y=8):
  render_template('index.html', x=x, y=y)