import smtplib as smtp
import ssl as ssl
def send_emailo(msg):
    host="smtp.gmail.com"
    port=465
    password='pwho ilpo soie aumb'
    sender='mogilicharlaveerendrasai@gmail.com'
    receiver='mogilicharlaveerendrasai@gmail.com'
    context = ssl.create_default_context()


    with smtp.SMTP_SSL(host,port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,msg)
