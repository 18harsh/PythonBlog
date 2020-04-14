# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:10:36 2020

@author: Harsh
"""
import sqlite3
from tkinter import *
import smtplib
from tkinter import messagebox

  
def post(author,title,content,date_posted):
    args=[author,title,content,date_posted]
    try:
        conn = sqlite3.connect("lite.db")
        cursor=conn.cursor()
        add_user = ("INSERT INTO posts "
                        "(author,title,content,date_posted) "
                        "VALUES (?,?,?,?)")
        cursor.execute(add_user,args) # executing the 
        conn.commit() # commiting the connection then closing it.
        conn.close() # closing the connection of the database
        messagebox.showwarning(' Success ',' Your blog has been posted')
        return True
    except pymysql.Error as error:
         messagebox.showerror(' error ',"Failed inserting BLOB data into MySQL table {}".format(error))
      
def fetch_post():
    try:
        conn = sqlite3.connect("lite.db")
        print("connection successful")
        cursor=conn.cursor()
        select_query =  "SELECT * FROM posts"
        cursor.execute(select_query) # executing the queries 
        posts= cursor.fetchall() 
        conn.commit() # commiting the connection then closing it. 
        conn.close()
        if posts:
            return(posts)
        else: 
            messagebox.showerror("Error", "technical error")
    except :
        messagebox.showerror( "technical error","Try again later")        
        
def update_post(user_name,new_title,new_content,post):   
      try:      
            conn = sqlite3.connect("lite.db")
            print("connection successful")
            cursor=conn.cursor() 
            select_query =  "UPDATE posts SET title =?, content=?  WHERE id=?" 
            val=(new_title,new_content,post[0])
            cursor.execute(select_query,val) 
            conn.commit() # commiting the connection then closing it. 
            conn.close()
            messagebox.showinfo(' success ',"post updated")
            return True
      except pymysql.Error as error:
                    messagebox.showerror(' Error ',"techninal error {}".format(error))        
        
def search_name(x):
    posts=fetch_post()
    post=[]
    for i in posts:
        if i[1]==x:
            post.append(i)
    return post        


def search_title(x):
    posts=fetch_post()
    print(x)
    post=[]
    for i in posts:
        print (i)
        if i[2]==x:
            post.append(i)
    return (post)





    
