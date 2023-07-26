from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://holly@localhost:5432/db_hp"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Wand, Student
from controllers.hp_controller import hp_blueprint

@app.route("/")
def home():
  return "DONT LOOK AT THIS, GO BACK TO STUDENTS!!! CLICK A NAME!"

app.register_blueprint(hp_blueprint)