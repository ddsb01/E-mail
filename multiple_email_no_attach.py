#!/usr/bin/python3
# This program can be used to send a 'any message' (with attachments) to 'multiple user' at a time.

import smtplib 

# list of receivers' email addresses.
receivers = ["cpandey.apj@gmail.com", "damandeepddsb01@gmail.com"]


for i in range (len(receivers)) :
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("damandeepddsb@gmail.com", "9997321707")
    msg = "Hi there! This is testing."
    s.sendmail("damandeepddsb@gmail.com", receivers[i], msg)
    s.quit()
