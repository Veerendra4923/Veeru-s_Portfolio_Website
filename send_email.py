import smtplib as smtp
import ssl as ssl

from dotenv import load_dotenv
import os

load_dotenv()  # This loads .env from current working directory


def send_emailo(msg):
    host="smtp.gmail.com"
    port=465
    password=os.getenv("PASSWORD")
    sender='mogilicharlaveerendrasai@gmail.com'
    receiver='mogilicharlaveerendrasai@gmail.com'
    context = ssl.create_default_context()


    with smtp.SMTP_SSL(host,port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,msg)
