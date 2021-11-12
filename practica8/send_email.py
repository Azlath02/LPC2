#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

usr = input('Escribe tu correo electronico: ')
pswrd = input('Escribe tu contraseña: ')
recep = input("A quien le deseas mandar el correo?: ")
asunto = input("Escribe el asunto: ")

# create and setup the parameters of the message
email_msg = MIMEMultipart()
email_msg["From"] = usr
receipents = [recep]
email_msg["To"] = ", ".join(receipents)
email_msg["Subject"] = asunto

# add in the message body
message = input("Escribe el mensaje que quieras enviar: ")
email_msg.attach(MIMEText(message, "plain"))

# create server
server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
# Login Credentials for sending the mail
server.login(usr, pswrd)


# send the message via the server.
server.sendmail(email_msg["From"], receipents, email_msg.as_string())
server.quit()
print("successfully sent email to %s:" % (email_msg["To"]))
