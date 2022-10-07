from flask import Flask, session, redirect, render_template, request
app = Flask(__name__)
app.secret_key = 'hahaxmonkey'

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  session['form_data'] = request.form
  form_results = session['form_data']
  print('form results for dojo-location:  >>> ',form_results)

  for key in session['form_data']:
    print(session['form_data'][key])

  print('process!!!!')
  return redirect('/results')


@app.route('/results', methods=['GET'])
def results():
  print('results!!!!!')
  return render_template('results.html')



if __name__ =="__main__":
  app.run(debug=True)