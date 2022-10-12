from flask_app.config.mysqlconnection import connectToMySQL, DATABASE
from flask_app.models.ninja_model import Ninja

class Dojo:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.location = data['location']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.ninjas = []

  @classmethod
  def get_all_dojos(cls):
    query = "SELECT * FROM dojos;"
    results = connectToMySQL(DATABASE).query_db(query)
    # Create an empty list to append our instances of users
    dojos = []
    for dojo in results:
      dojos.append(Dojo(dojo))
    return dojos

  @classmethod
  def get_all_dojo_ninjas(cls, data):
    print("get_all_dojo_ninjas:  >>>  ", data)
    # SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = 1;
    query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
    results = connectToMySQL(DATABASE).query_db(query, data)
    # Create an empty list to append our instances of users
    # print("get all dojo ninjas func output:  >>>> ", results[0]['location'])

    # dojo = cls(results[0])
    # print('what is dojo!!!!!    >>>>>>>>>>>> ', dojo)
    # for ninja in results:
    #   ninja_obj = {
    #     'id': ninja['ninjas.id'],
    #     'first_name': ninja['first_name'],
    #     'last_name': ninja['last_name'],
    #     'age': ninja['age'],
    #     'created_at': ninja['ninjas.created_at'],
    #     'updated_at': ninja['ninjas.updated_at'],
    #   }
    #   dojo.ninjas.append(Ninja(ninja_obj))
    # return dojo
    return results


# query = "SELECT * FROM dojos JOIN ninjas ON dojo_id = dojos.id;"
  @classmethod
  def create_new_dojo(cls, data):
    print(data)
    query = "INSERT INTO dojos (name, location) VALUES (%(name)s, %(location)s);"
    new_dojo_id = connectToMySQL(DATABASE).query_db(query, data)
    return new_dojo_id