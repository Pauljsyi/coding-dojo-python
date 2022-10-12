from flask_app.config.mysqlconnection import connectToMySQL, DATABASE



class Ninja():
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM ninjas JOIN dojos ON dojo_id = dojos.id;"
    ninjas = connectToMySQL(DATABASE).query_db(query)
    # Create an empty list to append our instances of users
    ninjas = []
    for ninja in ninjas:
      ninjas.append(cls(ninja))
    return ninjas

  @classmethod
  def create_new_ninja(cls, data):
    query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
    new_ninja_id = connectToMySQL(DATABASE).query_db(query, data)
    print(new_ninja_id)
    return new_ninja_id