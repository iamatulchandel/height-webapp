import smtplib
from email.mime.text import MIMEText
def send_email(email,height):
	from_email="iamatulchandel@gmail.com"
	from_password="atul1206"
	to_email= email

	subject="Height Data"
	message="Your height is : %s. Average height of all : . Total height entries here till now :."%height
	msg=MIMEText(message,"html")
	msg['Subject']=subject
	msg['From']=from_email
	msg['To']=to_email

	gmail=smtplib.SMTP("smtp.gmail.com",587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email,from_password)
	gmail.send_message(msg)