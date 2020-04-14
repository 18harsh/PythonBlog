# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:43:38 2020

@author: Harsh
"""

from tkinter import *
import sqlite3
import smtplib
from tkinter import messagebox




def connection(args):
    try:
        conn=sqlite3.connect("lite.db")
        print("connection successful")
        cursor=conn.cursor()
        add_user = ("INSERT INTO register "
                        "(user,email,password) "
                        "VALUES (?, ?,?)")
        cursor.execute(add_user,args) # executing the 
        conn.commit() # commiting the connection then closing it.
        conn.close() # closing the connection of the database
        messagebox.showwarning(' Success ',' Data Inserted Successful ')
        
    except pymysql.Error as error:
         messagebox.showerror(' error ',"Failed inserting BLOB data into MySQL table {}".format(error))

def verify_otp(msg,otp,details,root1):
    print(msg,otp)
    if otp!="":
        if int(msg)==int(otp):
                
             messagebox.showinfo(' Verified','Your email has been verified')
             connection(details)
             return root1.destroy()
        else:
            messagebox.showwarning(' Verification Failed','OTP is invalid')
    else:
        messagebox.showwarning(' Verification Failed','Enter OTP ')   

def send_email(subject,msg,email,details):
    global root1
    try:
        conn = sqlite3.connect("lite.db")
        print("connection successful")
        cursor=conn.cursor()
        select_query =  "SELECT * FROM mail where email_address = '" + "brucewayne18112000@gmail.com" +"';" # queries for retrieving values 
        cursor.execute(select_query) # executing the queries 
        password1= cursor.fetchall() 
        conn.commit() # commiting the connection then closing it. 
        conn.close()
        if password1:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(password1[0][0],password1[0][1])
            message = 'Subject: {}\nHi {}\n{}\n'.format(subject,details[0],msg)
            server.sendmail(password1[0][0],email, message)
            server.quit()
            answer=messagebox.askyesno(title="verification",message="have you recieved mail?")
            print(message)
            print(msg)
            print(answer)
            if answer:
                # messagebox.showinfo(' success','enter otp')
                root1 = Tk()
                otp = Entry(root1)
                otp.pack()
                Button(root1, text="Verify", command=lambda:verify_otp(msg,otp.get(),details,root1)).pack()
                root1.geometry("300x300")
                root1.mainloop()
            else:
                messagebox.showerror(' failed','check your connection')
                
            
        else: 
            messagebox.showerror("Error", "technical error")
    except pymysql.Error as error:
                    messagebox.showerror(' Error ',"techninal error {}".format(error))        
        
        