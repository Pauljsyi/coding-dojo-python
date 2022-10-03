from flask import Flask, session, redirect, render_template
app = Flask(__name__)
app.secret_key = 'hahaxmonkey'

@app.route('/')
def home():

  return render_template('index.html')

if __name__ =="__main__":
  app.run(debug=True)