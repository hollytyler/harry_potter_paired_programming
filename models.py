from app import db

class Student(db.Model):
  __tablename__ = "students"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  house = db.Column(db.String(64))
  age = db.Column(db.Integer)
  good = db.Column(db.Boolean, default=False)
  wands = db.relationship('Wand', backref='student')


class Wand(db.Model):
  __tablename__ = "wands"
  id = db.Column(db.Integer, primary_key=True)
  wood_type = db.Column(db.String(64))
  core_type = db.Column(db.String(64))
  plyable = db.Column(db.Boolean, default=False)
  student_id = db.Column(db.Integer, db.ForeignKey('students.id'))