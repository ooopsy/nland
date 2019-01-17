import smtplib

host = 'smtp.gmail.com'
username = 'jintian8899@gmail.com'
passwd = 'Shinimaa99@'
port = '465'

def send(toUser, message):
    server = smtplib.SMTP_SSL(host, 465)
    server.ehlo()
    server.login(username, passwd)
    server.sendmail(username, toUser, message)
