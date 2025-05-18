import smtplib as smtp
import ssl
import streamlit as st
from email.message import EmailMessage
#3rr4r4lkmrl4krm4
print("ji")

def send_emailo(user_message):
    host = "smtp.gmail.com"
    port = 465
    sender = 'mogilicharlaveerendrasai@gmail.com'
    receiver = 'mogilicharlaveerendrasai@gmail.com'
    password = st.secrets["email"]["password"]

    # Create the message
    msg = EmailMessage()
    msg["Subject"] = "New message from your portfolio website"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(user_message)

    context = ssl.create_default_context()

    try:
        with smtp.SMTP_SSL(host, port, context=context) as server:
            server.login(sender, password)
            server.send_message(msg)
        st.success("✅ Email sent successfully!")
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")
