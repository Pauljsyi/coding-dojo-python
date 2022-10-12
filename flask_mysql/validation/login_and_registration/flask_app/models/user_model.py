from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM users;"
    results = connectToMySQL(DATABASE).query_db(query)
    # Create an empty list to append our instances of users
    users = []
    for user in results:
      users.append(cls(user))
    return users


  @classmethod
  def get_one(cls, data:dict):
    query = "SELECT * FROM users WHERE id=%(id)s;"
    results = connectToMySQL(DATABASE).query_db(query, data)

    if not results:
      return False
    return results[0]

  @classmethod
  def get_one_by_email(cls, data:dict):
    query = "SELECT * FROM users WHERE email=%(email)s;"
    results = connectToMySQL(DATABASE).query_db(query, data)

    if not results:
      return False
    return results[0]

  @classmethod
  def create(cls, data:dict):
    # print("class method CREATE:  ", data['first_name'])
    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
    user_id = connectToMySQL(DATABASE).query_db(query, data)
    return user_id
    
  @classmethod
  def update_one(cls, data:dict):
    print('update one data:  ', data)
    query = "UPDATE users SET first_name=(%(first_name)s), last_name=(%(last_name)s), email=(%(email)s), password=(%(password)s) WHERE id=%(id)s;"
    connectToMySQL(DATABASE).query_db(query, data)
  
  @classmethod
  def delete_one(cls, data:dict):
    query = "DELETE FROM users WHERE id=%(id)s"
    user_id = connectToMySQL(DATABASE).query_db(query, data)
    return user_id
  
  @staticmethod
  def validator(data:dict):
    is_valid = True

    if len(data['first_name']) < 1:
      is_valid = False
      flash("Field is required", 'err_user_first_name')

    if len(data['last_name']) < 1:
      is_valid = False
      flash("Field is required", 'err_user_last_name')

    if len(data['email']) < 1:
      is_valid = False
      flash("Field is required", 'err_user_email')
    elif not EMAIL_REGEX.match(data['email']): 
      flash("Invalid email address!", 'err_user_email')
      is_valid = False
    else:
      potential_user = User.get_one_by_email({'email': data['email']})
      if potential_user:
        flash("email address already in use!", 'err_user_email')
        is_valid = False

    if len(data['password']) < 1:
      is_valid = False
      flash("Field is required", 'err_user_password')

    if len(data['confirm_password']) < 1:
      is_valid = False
      flash("Field is required", 'err_user_confirm_password')

    if data['confirm_password'] != data['password']:
      is_valid = False
      flash("Passwords do not match", 'err_user_confirm_password')
    return is_valid

  @staticmethod
  def validate_login(data:dict):
    is_valid = True
    if len(data['email']) < 1:
      is_valid = False
      flash("Field is required", 'err_login_email')
    elif not EMAIL_REGEX.match(data['email']): 
      flash("Invalid email address!", 'err_login_email')
      is_valid = False

    if len(data['password']) == False:
      is_valid = False
      flash("Wrong Password", 'err_login_password')


    return is_valid
