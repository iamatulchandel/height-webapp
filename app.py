from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:atul1206@localhost/height_collector'

db=SQLAlchemy(app)

class Data(db.Model):
	__tablename__= 'height_table'
	id= db.Column(db.Integer,primary_key=True)
	email_=db.Column(db.String(120),unique=True)
	height_=db.Column(db.Integer)

	def __init__(self,email_,height_):
		self.email_=email_
		self.height_=height_

db.create_all()
@app.route("/")
def index():
	return render_template('index.html')
@app.route("/success",methods=['POST'])
def success():
	if request.method=='POST':
		email=request.form["email_name"]
		height=request.form["height_name"]
		data=Data(email,height)
		
		if db.session.query(Data).filter(Data.email_==email).count()==0:
			db.session.add(data)
			db.session.commit()
			avg_height= db.session.query(func.avg(Data.height_)).scalar()
			avg_height= round(avg_height)
			count= db.session.query(Data.height_).count()
			send_email(email,height)
			return render_template('success.html')
		else :
			
			return render_template("index.html",text='Email already exists with height %s.'%data.height_)




if __name__ == "__main__":
	app.debug=True
	app.run()