from email.mime.text import MIMEText
from smtplib import SMTP


def push_email(email, height, average_height, count):
    from_email = 'ajwaldro@gmail.com'
    from_password = 'zexgdrhckghsmoaz'
    to_email = email

    subject = "Height information"
    message = "Hello, your height is <strong>%s</strong>. Average height of all entries is <strong>%s</strong> out " \
              "of <strong>%s</strong> entry('s)" % (
                  height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail_acct = SMTP('smtp.gmail.com', 587)
    gmail_acct.ehlo()
    gmail_acct.starttls()
    gmail_acct.login(from_email, from_password)
    gmail_acct.send_message(msg)
