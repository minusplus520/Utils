#!/u/chenc/.aliasscript/python
from datetime import datetime, timedelta
from email.mime.text import MIMEText
import os,sys
import smtplib
import argparse

def send_mail(mail_from, mail_to, subject, body):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = mail_from
    message['To'] = ', '.join(mail_to)
    print("From: " + message['From'])
    print("To: " + message['To'])
    print("Subject: " + message['Subject'])
    print("body:")
    print(body)
    check = input("Send? ")
    if check != 'Y':
        return
    s = smtplib.SMTP('mailhost.synopsys.com')
    s.sendmail(mail_from, mail_to, message.as_string())
    print("==========\nSent!!!\n==========")

def AddHi(body,list):
    body += "Hi "
    if len(list) == 0:
        assert(0)
    for name in list:
        body += name + ", "
    body += "\n\n"
    return body

# for Sign offs
T0 = "\n\nMany Thanks,\nChen"
T1 = "\nThanks.\n\nBest,\nChen"
T2 = "\n\nBest Regards,\nChen"
T3 = "\nThanks.\n\nBest Regards,\nChen"

def AddSignoffs(body, num):
    body += "\n"
    if num == 0:
        body += T0
    elif num == 1:
        body += T1
    elif num == 2:
        body += T2
    elif num == 3:
        body += T3
    else:
        assert(0)
    return body

if __name__ == "__main__":
    latter = ""
    latter = AddHi(latter, ["Jiachi"])

    latter += "<3"



    latter = AddSignoffs(latter,int(sys.argv[1]))
    #print(latter)

    #send_mail("chenc@synopsys.com", ["chenc@synopsys.com"], "HIHI", "Hi Jiachi,\n\n\nBest,\nChen")
    send_mail("chenc@synopsys.com", ["chiachh@synopsys.com"], "Reminder", latter)
