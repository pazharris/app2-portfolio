import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "pazthreed@gmail.com"
    password = "wyqpgbclngeyuute"
    receiver = "pazharris222@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, 465, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
