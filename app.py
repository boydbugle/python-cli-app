from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///cli.db'
db=SQLAlchemy(app)
class user(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	firstName=db.Column(db.String(100))
	surName=db.Column(db.String(100))
	email=db.Column(db.String(100))
	password=db.Column(db.String(100))
	timeStamp=db.Column(db.String(100))
	def __init__(self,firstName,surName,email,password,timeStamp):
		self.firstName=firstName
		self.surName=surName
		self.email=email
		self.password=password
		self.timeStamp=timeStamp


def add(fname,sname,email,password,timeStamp):
	add=user(fname,sname,email,password,timeStamp)
	db.session.add(add)
	db.session.commit()
	return "record added"
add("kwame","asiago","emai@","password","time")
print "added"

