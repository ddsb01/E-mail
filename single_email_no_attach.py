#!/usr/bin/python3
# This program can be used to send a 'textual message' (no attachments) to 'single user' at a time. 

# don't name this pyscript 'email.py' cuz it prevents 'smtplib' form importing the built-in 'email' module.

import smtplib
# The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.


# To create SMTP (Simple Mail Transfer Protocol) session.
s = smtplib.SMTP('smtp.gmail.com', 587)     # 587 is the port number


# starting TLS (Transfer Layer Security) for security
s.starttls()


s.login("damandeepddsb@gmail.com", "9997321707")


message = "Hi there! This is testing."


s.sendmail("damandeepddsb@gmail.com", "damandeepddsb01@gmail.com", message)


# To terminate the session
s.quit()

