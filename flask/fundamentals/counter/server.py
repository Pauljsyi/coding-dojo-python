from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '78d25bc4-840d-4794-990e-5ea4c97505e1'

@app.route('/', methods=['GET'])
def home():
  
  if session == {}:
    session['clicked'] = 0
    session['visited'] = 0
  else:
    session['clicked'] += 1 
    session['visited'] += 1
    print(session)
    
  # print(session)
  return render_template('index.html', clicked = session['clicked'], visited = session['visited'])
    


@app.route('/destroy_session')
def destroy_session():
  session.clear()
  return redirect('/')


# increments count by 2
@app.route('/increment_2')
def increment_2():
  # redirect will count as 1
  # we will add 1 more to session
  session['clicked'] += 1
  return redirect('/')

@app.route('/reset_count')
def reset_count():
  # on redirect default count will be 1 
  # will reset to 0 by subtracting by 1
  session['clicked'] = -1
  session['visited'] = -1
  return redirect('/')

@app.route('/user_count', methods=['POST'])
def user_count():
  print("got post info in user_count:  ",request.form['user-count'])
  user_count = int(request.form['user-count'])
  # print('user count type:  ',type(user_count))
  # user will define increment by num
  # increment current value by num
  session['clicked'] += user_count - 1
  return redirect('/')


if __name__=="__main__":
  app.run(debug=True)