from core.Api import Api
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import render_template

class Contact(Api):
    def __init__(self, db):
        super().__init__(db)

    def send(self, request):
        sender_email = "gofacturas.mail@gmail.com"
        receiver_email = ["emer.isau@gmail.com"]
        password = "spumnqawgiucbtck"
        message = MIMEMultipart("alternative")
        message["Subject"] = "CONTACTO WEB BEYRISFOOD"
        message["From"] = sender_email
        message["To"] = ",".join(receiver_email)
        html = render_template("email/contact.html",
        name=request.form['name'],
        email=request.form['email'],
        phone=request.form['phone'],
        message=request.form['message'])
        body = MIMEText(html, "html")
        message.attach(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
         server.login(sender_email, password)
         server.sendmail(
            sender_email, receiver_email, message.as_string()
         )
         return True
