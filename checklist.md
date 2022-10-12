## pre-requirements

- install pipenv `globally`

```
pip install pipenv
```

# F1ask Check1ist

- to create a directory
- go into that folder
- create virtual env

```
pipenv install flask pymysql
```

- `WARNING!` look for the files **pipfile** && **pipfile.lock**

  - if you do not see these than you need to figure it
    out right away.

- Activate it / go into the "world" aka: the shell

```
  pipenv shell
```

- set up the file structure

```
- main app folder
- flask_app
  - config
    - mysqlconnection.py
  - controllers
    - controller_routes.py
    - controller_table_name.py
  - models
    - model_table_name.py
  - templates
    - template.html
    - index.html
  - static
    - css
      - style.css
    - js
      - script.js
  - __init__.py
- pipfile
- pipfile.lock
- server.py
```

- input boilerplate code into files
- test to make sure your application works!
  ```
  python server.py
  ```

## server.py

```py
 from flask_app import app
 from flask_app.controllers import controller_burger, controller_routes

 #KEEP THIS AT THE BOTTOM
 if __name__=="__main__"":
    app.run(debug=True)
```

## \_\_init\_\_.py

```py
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "can be whatever you want"

bcrypt = Bcrypt(app)

DATABASE = "your_database"
```

## mysqlconnection.py

```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'root',
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close()
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

## model.py

```py
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

DATABASE = 'burgers_db'

class Burger:
  def __init__(self, data):
    # in the db table
    self.id = data['id']
    self.protein = data['protein']
    self.condiments = data['condiments']
    self.topping = data['topping']
    self.is_vegan = data['is_vegan']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def create(cls, data):
    query = "INSERT INTO burgers (protein, condiments, topping, is_vegan) VALUEs (%(protein)s, %(condiments)s, %(topping)s, %(is_vegan)s);"
    burger_id = MySQLConnection(DATABASE).query_db(query, data)
    return burger_id

  @classmethod
  def get_all(cls) :
    query = "SELECT * FROM burgers;"

    results = connectToMySQL(DATABASE) .query_db(query)# datatype return a list of dictionaries

    if not results :
      return []

    all_burgers = []
    for dict in results:
      all_burgers.append( cls(dict) )
    # returns a list of instances
    return a11 burgers

  @classmethod
  def update_one(cls):
    pass
  @classmethod
  def delete_one(cls):
    pass

```

## BASIC SQL QUERIES

```sql
###SELECT
    To read data from a table, we would use the Select statement where we define the columns that we want to fetch.

    The general syntax is:

        SELECT column1,column2,.. FROM table_name;

        If we wanted to select the name and phone number of a customer from our table, we would use:

        SELECT name, phone FROM customers;

        Also, to read all the columns from our table, we can replace the column names with * as follows:

        SELECT * FROM customers;

### INSERT

    To insert data into any table, we use the INSERT INTO statement.

      The general syntax for insert is:

        INSERT INTO table_name(column1,column2,...) VALUES (val1,val2,...);

        To insert data into our customer''s table, we would use the following statement:

        INSERT INTO customers(ID,name,phone,postalCode)

              VALUES(1,'Alice','+123456789',123456);

### UPDATE
    To update specific column(s) of specific row(s), we make use of the Update statement. The general syntax for an update statement is:

      UPDATE table_name

        SET column1=value1,column2=value2,...

        WHERE conditions...;

    For example, if we wanted to update the phone number of a customer that has an ID of 2, we would write our query as:

      UPDATE customers

        SET phone='+2223334445'

        WHERE ID=2;

    We can update multiple columns by adding them to the SET statement and we can target multiple rows by adding them to the WHERE statement. We will look at WHERE in detail in later sections of this SQL commands cheat sheet.

###DELETE
    If we wanted to remove some rows from a table, we would use the delete statement. The general syntax is:

        DELETE FROM table_name

            WHERE condition...;

    Let''s say we want to remove all the customers who live in a particular area. So, we simply delete those rows that have a specific area code:

        DELETE FROM customers

            WHERE postalCode=223344;

```
