# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:46:20 2020

@author: Harsh
"""
from tkinter import *
import sqlite3
import smtplib
global root1
from post_funct import fetch_post
from functions import verify_otp
from tkinter import messagebox




def forgot(x,y):
    try:
            conn = sqlite3.connect("lite.db")
            print("connection successful")
            cursor=conn.cursor()
            select_query =  "SELECT * FROM register where user = '" + x + "' AND email = '" + y + "';" # queries for retrieving values 
            cursor.execute(select_query) # executing the queries 
            user_info = cursor.fetchall() 
            conn.commit() # commiting the connection then closing it. 
            conn.close()
            print(user_info)
            if user_info:
               try:     
                    conn = sqlite3.connect("lite.db")
                    print("connection successful")
                    cursor=conn.cursor()
                    select_query =  "SELECT * FROM mail where email_address = '" + "brucewayne18112000@gmail.com" +"';" # queries for retrieving values 
                    cursor.execute(select_query) # executing the queries 
                    password= cursor.fetchall() 
                    conn.commit() # commiting the connection then closing it. 
                    conn.close()
                    if password:
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(password[0][0],password[0][1])
                        message = 'Subject: {}\nHi {} your password is {}.\nPlease do not share your password, even with your family '.format("Forgot Password?",user_info[0][0],user_info[0][2])
                        server.sendmail(password[0][0],y, message)
                        server.quit()
                    else: 
                        messagebox.showerror("technical error", "Check Your Connection")
               except:
                    messagebox.showerror("technical error", "Try again later")
                 
            else: 
                messagebox.showerror("Error", "Invalid Username or email") # displaying message for invalid details 
     
    except sqlite3.Error as error:
            messagebox.showerror(' error ',"techninal error {}".format(error))
        
def update(x,y,user_info):
    try:    
            name=user_info[0][0]
            conn = sqlite3.connect("lite.db")
            print("connection successful")
            cursor=conn.cursor() 
            select_query =  "UPDATE register SET user =?, email=? WHERE email= ?" 
            val=(x,y,user_info[0][1])
            cursor.execute(select_query,val) 
            cursor=conn.cursor()
            select_query =  "SELECT * FROM register where email = '" + y + "';" # queries for retrieving values 
            cursor.execute(select_query) # executing the queries 
            user_info = cursor.fetchall() 
            conn.commit() # commiting the connection then closing it. 
            conn.close()
            print(user_info)
            if user_info:
                try:
                    messagebox.showinfo("Congratulation", "Update Succesfull")
                    conn = sqlite3.connect("lite.db")
                    cursor=conn.cursor() 
                    select_query =  "UPDATE posts SET author =? WHERE author= ?" 
                    val=(x,name)
                    cursor.execute(select_query,val) 
                    conn.commit() # commiting the connection then closing it. 
                    conn.close()
                    return user_info
                except pymysql.Error as error:
                    messagebox.showerror(' Error ',"techninal error {}".format(error))
                 
            else: 
                messagebox.showerror("Error", "Try again later") # displaying message for invalid details 
     
    except pymysql.Error as error:
            messagebox.showerror(' Error ',"techninal error {}".format(error))
               
        
def log(x,y):
    
    try:
            conn = sqlite3.connect("lite.db")
            print("connection successful")
            cursor=conn.cursor()
            select_query =  "SELECT * FROM register where email = '" + x + "' AND password = '" + y + "';" # queries for retrieving values 
            cursor.execute(select_query) # executing the queries 
            user_info = cursor.fetchall() 
            conn.commit() # commiting the connection then closing it. 
            conn.close()
            print(user_info)
            if user_info:
                messagebox.showinfo("Congratulation", "Login Succesfull")
                return user_info
            else: 
                messagebox.showerror("Error", "Invalid Username or Password") # displaying message for invalid details 
                return ()                
    except sqlite3.Error as error:
            messagebox.showerror(' error ',"techninal error {}".format(error))
           
            

   



