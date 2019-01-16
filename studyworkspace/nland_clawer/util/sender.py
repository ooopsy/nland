import smtplib

host = 'smtp.gmail.com'
username = 'jintian8899@gmail.com'
passwd = 'Shinimaa99@'
port = '587'


'''
smtpObj = smtplib.SMTP()
smtpObj.connect(host, port)    # 25 为 SMTP 端口号
smtpObj.login(username,passwd)
smtpObj.sendmail(username, 'li@jisan.com', 'a test mail')
'''

s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
s.ehlo()
s.login(username, passwd)
s.sendmail('jintian8899@gmail.com', 'li@jisan.com', 'a test mail')
