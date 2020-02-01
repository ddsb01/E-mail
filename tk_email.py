#!/usr/bin/python3

# used tkinter to create application for the email sender program.
# this is the graphical version of the 'single user, email without attachment' program.
# other similar ones can be modified accordingly.



from tkinter import *
import smtplib



# the main window object "master"
master = Tk(className = "ddsb E-MAILZ")

master.geometry('620x250')



# F U N C T I O N S :
# to make sure all the mandatory entries are filled.
def check_entry() :
    if sender.get() and receiver.get() and pswrd.get() :
        send()
    else :
        print("Required field(s) not filled !")

# entry.get() method : to extract user input in the entry field


def send() :
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender.get(), pswrd.get())
    s.sendmail(sender.get(), receiver.get(), message.get())
    s.quit()





# L A B E L S       (for entry fields) :
Label(master, text = "Sender's e-mail Address : ", padx = 20, pady = 10, font = 'Arial').grid(row = 0, column = 0, sticky = W)

Label(master, text = "Receiver's e-mail Address : ", padx = 20, pady = 10, font = 'Arial').grid(row = 1, column = 0, sticky = W)

Label(master, text = "Message : ", padx = 20, pady = 20, font = 'Arial').grid(row = 2,column = 0, sticky = W)

p = Label(master, text = "Password : ", padx = 20, pady = 20, font = 'Arial').grid(row = 3,column = 0, sticky = W)



# E N T R Y     F I E L D S:
sender = Entry(master, width = 45, foreground = 'blue')
sender.grid(row = 0, column = 1)

receiver = Entry(master, width = 45, foreground = 'blue')
receiver.grid(row = 1, column = 1)

message = Entry(master, width = 45, foreground = 'green')
message.grid(row = 2, column = 1)

pswrd = Entry(master, width = 45, foreground = 'blue', show = "*")
pswrd.grid(row = 3, column = 1)
# show = "*" attribute of label is to ensure that password is hidden (or only asterisk is shown)



# B U T T O N : 
btn = Button(master, text = "S E N D !", padx = 5, pady = 5, font = 'Arial 16 bold underline', foreground = 'red', width = 15, activebackground = 'green', highlightbackground = 'black', command = check_entry)
btn.grid(row = 4, columnspan = 2)





# to  E X E C U T E :
master.mainloop()
