from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = '78d25bc4-840d-4794-990e-5ea4c97505e2'


@app.route('/')
def home():
  print(session)
  return render_template('index.html')

@app.route('/guess', methods=['post'])
def guess():
  # persist session data
  # keep random_num from changing session[random-num]'s value
  if session == {}:
    random_num = random.randint(1, 100)
    session['random_num'] = random_num
    session['attempt'] = 0
  
  user_guess = int(request.form['num']) 
  if session['attempt'] == 5 and user_guess != session['random_num']:
    session['attempt'] = 0
    return render_template('you_lose.html')
  elif user_guess == session['random_num'] and session['attempt'] < 5:
    print(session)
  else:
    session['attempt'] +=1
    print(session)
    # print('this is attempt', session['attempt'])
  
  # print(session)
  # print('session:  ', session)

   
  print("user's guess type: ",type(user_guess), user_guess, "\nrandom number type:  ", type(session['random_num']), session['random_num'])
  print(session)
  # print(type(session['random_num']))
  if  user_guess == session['random_num']:
    # print('user guess matches session number!!!')
    correct = f'{user_guess} is the answer!'
    # PRINT STATEMENTS TO CHECK USERS GUESS AND CURRENT SESSION VALUE
    # print("user's guess and type: ",type(user_guess), user_guess, "\nrandom number and type:  ", type(session['random_num']), session['random_num'])
    # print("is same? :  ",user_guess == session['random_num'])
    # print('correct!')
    # uncommenting the line below will reassign session to a diff #
    # store current session value to temp
    # print('current session random num: ', session['random_num'])
    temp = session['random_num']
    # print('temp: ', temp)
    # and run the line below to reassign session
    session['random_num'] = random.randint(1, 100)
    # print('next session random num: ', session['random_num'])
    container_color = 'background-color: green'
    return render_template('index.html', guess=user_guess, rand_num=temp, correct = correct, container_color = container_color, go = '/')
  elif user_guess > session['random_num']:
    print(session)

    print('too high')
    too_high = 'too high!'
    container_color = 'background-color: red'
    return render_template('index.html', too_high = too_high, guess = user_guess, rand_num = session['random_num'], container_color = container_color)
  elif user_guess < session['random_num']:
    print(session)
    print('too low')
    too_low = 'too low!'
    container_color = 'background-color: red'
    return render_template('index.html', too_low = too_low, guess = user_guess, rand_num = session['random_num'] ,container_color = container_color, go = '/guess')
  # print('random number: ', random_num)
  # return redirect('/')
  


if __name__=="__main__":
  app.run(debug=True)