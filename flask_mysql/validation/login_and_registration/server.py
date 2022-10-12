from flask_app import app
from flask_app.models.user_model import User
from flask_app.controllers import users_controller
from flask_app.controllers import controller_routes

if __name__=="__main__":
  app.run(debug=True)