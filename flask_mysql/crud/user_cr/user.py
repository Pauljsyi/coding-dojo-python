from mysqlconnection import connectToMySQL, MySQLConnection

DATABASE = 'users'

class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
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
    query = "SELECT * FROM users WHERE id = %(id)s;"
    results = connectToMySQL(DATABASE).query_db(query, data)
    print(query)
    if not results:
      return False

    # print('get one!', results[0])
    return results[0]

  @classmethod
  def create(cls, data:dict):
    print("class method CREATE:  ", data['first_name'])
    
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
    # query = "INSERT INTO users (first_name, last_name, email) VALUES ('pablo', 'escobar', 'pe@gmail.com')"
    user_id = connectToMySQL(DATABASE).query_db(query, data)
    return user_id
    
  @classmethod
  def update_one(cls, data:dict):
    # print('update one id:  ', data.id)
    print('update one data:  ', data)
    query = "UPDATE users SET first_name=(%(first_name)s), last_name=(%(last_name)s), email=(%(email)s) WHERE id=%(id)s;"

    connectToMySQL(DATABASE).query_db(query, data)
  
  @classmethod
  def delete_one(cls, data:dict):
    print('DELETEEEDD', data)
    query = "DELETE FROM users WHERE id=%(id)s"

    user_id = connectToMySQL(DATABASE).query_db(query, data)
    return user_id