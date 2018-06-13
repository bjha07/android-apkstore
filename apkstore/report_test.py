import os
import sys
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = "django_project.settings"
sys.path.append('/home/django/django_project/apkstore/')

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
#import settings
#import django_project.settings
#from django.core.mail import EmailMultiAlternatives
'''
def simple_send():
    from django.core.mail import send_mail

    send_mail('Subject here','Here is the message.','from@example.com',['bjha07@gmail.com'],fail_silently=False,)
simple_send()
'''
'''
def email_send():
    import smtplib
    sender = 'bjha07@gmail.com'
    receivers = ['bjha07@gmail.com']

    message = "From: From Person <from@fromdomain.com> To: To Person <to@todomain.com>Subject: SMTP e-mail test This is a test e-mail message"

  #  try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"

#    except SMTPException:
 #       print "Error: unable to send email"
email_send()
'''

def test():
    #for i in range(1000,100000):
#	print i
    from django.core.mail import send_mail
    body = "Hi User \r\nPlease click in URL\r\n  Code : "
    #s1 = smtplib.SMTP("smtp.gmail.com", 465)
  #  s1 = smtplib.SMTP('i.prtouch.com', 26)
    s1 = smtplib.SMTP_SSL('smtp.zoho.com',465)
    s1.login("support@android-apkstore.com","androidapkstore")
    subject = "Test Mail"
    content = "Welcome Androied-apkstore"
    to_mail_ids = ['bjha07@gmail.com']
    for mail in to_mail_ids:
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = "Android-apkstore <support@android-apkstore.com>"
        plain_test_part = MIMEText(content, 'plain')
        msg.attach(plain_test_part)
        msg['To']=mail
        s1.sendmail(msg['From'] , msg['To'], msg.as_string())
        #s1.quit()
    print "send"
    s1.quit()
    #x = send_mail_content("test mail",body,['bjha07@@gmail.com'])
    #send_mail('Password Reset', body , 'noreply@gmail.com', ['bjha07@gmail.com'])
test()

'''
def send_mail_content(subject, content, to_mail_ids):
    s1 = smtplib.SMTP('i.prtouch.com', 26)
    for mail in to_mail_ids:
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = "Support <support@prtouch.in>"
        plain_test_part = MIMEText(content, 'plain')
        msg.attach(plain_test_part)
        msg['To']=mail
        s1.sendmail(msg['From'] , msg['To'], msg.as_string())
    s1.quit()
    return True
'''
