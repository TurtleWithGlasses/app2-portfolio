import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "mhmtsoylu1928@gmail.com"
    pw = "yfvcacavjfbiwpjd"

    receiver = "mhmtsoylu1928@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, pw)
        server.sendmail(username, receiver, message)