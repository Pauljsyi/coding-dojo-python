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
    results = MySQLConnection(DATABASE).query_db(query)
    # Create an empty list to append our instances of users
    users = []

    for user in results:
      users.append(cls(user))
    return users

  @classmethod
  def create(cls, data:dict):
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
    

    user_id = MySQLConnection(DATABASE).query_db(query, data)
    return user_id