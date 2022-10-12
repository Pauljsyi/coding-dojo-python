from flask_app import app

from flask import Flask
from flask_app.models.user import User
app = Flask(__name__)


if __name__ == "__main__":
  app.run(debug=True)