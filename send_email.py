import email
from email.mime.text import MIMEText
import smtplib

def send_email(email,height):
    from_email="ngdai6789@gmail.com"
    from_password="G118topcliff"
    to_email=email
    subject="Height Data"
    message="Hello here is the data %s" %height

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
