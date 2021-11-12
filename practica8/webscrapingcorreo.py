import requests
from bs4 import BeautifulSoup 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def uni():
    soup = get_soup("https://www.uanl.mx")
    nota = soup.find_all('span', class_="hidden share_title")
    a = [ele.text.strip('<') for ele in nota]
    print('Notacias UANL: ')
    msg = ''
    for z in a:
        print(z)
        msg = msg + '\n' + z
    correo(msg)
        

def correo(msg):
    usr = input('Escribe tu correo electronico: ')
    pswrd = input('Escribe tu contraseña: ')
    recep = input("A quien le deseas mandar el correo?: ")
    asunto = input("Escribe el asunto: ")

    email_msg = MIMEMultipart()
    email_msg["From"] = usr
    receipents = [recep]
    email_msg["To"] = ", ".join(receipents)
    email_msg["Subject"] = asunto

    message = msg 
    email_msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP("smtp.office365.com:587")
    server.starttls()

    server.login(usr, pswrd)
    server.sendmail(email_msg["From"], receipents, email_msg.as_string())
    server.quit()

    print("successfully sent email to %s:" % (email_msg["To"]))






if __name__ == "__main__": 
    uni()