import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
from datetime import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import email

motion_pin = 16
gmail_user = "sender@gmail.com"  # Sender email address

gmail_pwd = "password"  # Sender email password

to = "receiver@gmail.com"  # Receiver email address

subject = "Home Security Alert"   #Subject of the mail

#body of the mail
text = "WARNING!! There is some activity occuring in your house.Please see the attached picture. Take necessary actions!!"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motion_pin, GPIO.IN)

#get the picname as the input parameter and attach the text. Check the server, 
# login using the credentials and send the mail.

def  sendEmail(picname):
    attach = picname
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    email.encoders.encode_base64(part)
    part.add_header('Content-Disposition',

                    'attachment; filename="%s"' % os.path.basename(attach))

    try:
        msg.attach(part)
        mailServer = smtplib.SMTP("smtp.googlemail.com")
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        mailServer.close()
    except:
        print("Authentication error")

    print("Mail Sent to the owner")

    os.remove(picname)

#continouosly checking if there is any motion detected
while True:
    if(GPIO.input(motion_pin) == 0):
        print("Motion detected")
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        print("Capturing Photo")
        picname = datetime.now().strftime("%y-%m-%d-%H-%M")
        picname = picname+'.jpg'
        cv2.imwrite(picname, frame)
        print("Sending mail")
        sendEmail(picname)
    elif(GPIO.input(motion_pin) == 1):
        print ("No motion detected")
    time.sleep(1)

