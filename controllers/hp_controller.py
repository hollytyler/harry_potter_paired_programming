from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Student, Wand

hp_blueprint = Blueprint('students', __name__)

@hp_blueprint.route("/students")
def students():
    students= Student.query.all()
    return render_template("students/index.jinja", students=students)

@hp_blueprint.route("/students/<id>")
def show_student(id):
    student = Student.query.get(id)
    return render_template("students/show.jinja", student=student)

@hp_blueprint.route("/students/<id>/addwand")
def add_wand():
    wands = Wand.query.all()
    return render_template("students/<id>/addwand.jinja", wands=wands)
