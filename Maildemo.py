import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('pruthvikrishna97@gmail.com','ganesh@999')
server.sendmail('pruthvikrishna97@gmail.com','udevi96@gmail.com','Hi, This is Python mail')
print("Mail sent")