#!/usr/bin/python3 

# This program can be used to send 'any message' (with attachments) to 'single user' at a time.

# The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib

# to enable attachments
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# the required email addresses
sender = "damandeepddsb@gmail.com"
receiver = "damandeepddsb01@gmail.com"





# PREPARING THE MESSAGE STRUCTURE :
# an instance of MIMEMultipart
msg = MIMEMultipart()

msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "Testing."


# body of the mail :
body = "This is an email with an attachment."


# to attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))  #(msg, its_type)


# opening the file to be sent 
file = "name.py"
attchmnt = open("/home/ddsb01/Documents/PythonPrac/name.py", "rb")
# rb : open the file in binary format for reading.


# an instance of MIMEBase 
b = MIMEBase('application', 'octet-stream')


# changing the attachment into encoded form
b.set_payload((attchmnt).read())
 
encoders.encode_base64(b)

b.add_header('Example', "attchmnt; filename = %s" % file)

# finally attach the instance 'b' to the instance 'msg'
msg.attach(b)







# SENDING THE STRUCTURED MESSAGE NOW :
# old school stuff now
s = smtplib.SMTP('smtp.gmail.com', 587)
s. starttls()
s.login(sender, "9997321707")

# to convert the multipart message into string.
text = msg.as_string()

s.sendmail(sender, receiver, text)

# terminate the SMTP session.
s.quit()