import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5:
    with open('quotes.txt', 'r') as wish:
        lines = wish.readlines()
        if lines:
            message_body = random.choice(lines)

    subject = "Email Subject"
    body = message_body
    sender = "sender_mail@gmail.com"
    recipients = ["recivermail1@gmail.com", "recivermail2@gmail.com"]
    password = "your_app_password"


    def send_email(subject, body, sender, recipients, password):

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent!")

    send_email(subject, body, sender, recipients, password)


