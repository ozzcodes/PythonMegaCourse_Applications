from email.mime.text import MIMEText
import smtplib


def send_email(email, height):
    from_email = ''
    from_password = '!'
    to_email = email

    subject = "Height information"
    message = "Hello, your height is %s." % height
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail_acct = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_acct.ehlo()
    gmail_acct.starttls()
    gmail_acct.login(from_email, from_password)
    gmail_acct.send_message(msg)
