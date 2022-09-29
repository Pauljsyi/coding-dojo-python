from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/dojo')
def func_2():
  return 'Dojo!'

@app.route('/say/<name>')
def func_3(name):
  # print(type(name))
  if (type(name) == str):
    return f'Hi {name}'


@app.route('/repeat/<int:num>/<salute>')
def salute(num,salute):
  print('checking type of num: ', type(num))

  if (type(num) == int and type(salute) == str):
    say_x_times = num * salute
    return f'{say_x_times} '
  # print(say_x_times)
  

app.errorhandler(404)
def page_not_found(error):
  return f'sorry! page not found teeheehaa'


# KEEP ON BOTTOM
if __name__=="__main__":
  app.run(debug=True)