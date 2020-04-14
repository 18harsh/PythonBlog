# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:04:27 2020

@author: Harsh
"""
from userdetail import log,update,forgot
from post_funct import fetch_post,post,update_post,search_title,search_name
from tkinter import*
from functions import send_email
import random
import sqlite3
from datetime import date
from tkinter import messagebox
global user_info
from PIL import ImageTk,Image
from tictactoe import play
from tkinter import filedialog
from credits import credit
import cv2

conn=sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF not EXISTS posts(id INTEGER PRIMARY KEY ,author text, title text, content text ,date_posted text)")
conn.commit()
conn.close()

conn=sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF not EXISTS mail(email_address text,password text)")
conn.commit()
conn.close()

conn=sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("INSERT INTO mail VALUES (?,?)",("YOUR_EMAIL_ADDRESS","EMAIL_PASSWORD"))
conn.commit()
conn.close()

conn=sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF not EXISTS register(user text,email text UNIQUE,password text)")
conn.commit()
conn.close()

user_info=()
def adjustwindow(window):
    
    w = 800  # width for the window size
    h = 650  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    
    window.geometry('%dx%d+%d+%d' % (ws, hs, 0, 0))  # set the dimensions of the screen and where it is placed
    window.resizable(True, True)    # disabling the resize option for the window
    window.configure(background='white')   
    
    
def layout(window):   
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    header = Canvas(window,bg="#5A7E91",width=window.winfo_screenwidth() ,height=75).pack()
   
    Label(window,text="Python Blog",font=("Lucida",20,'bold'),fg='white',bg="#5A7E91").place(x=120,y=30)
    big_frame = Frame(window)
    Button(big_frame,text="Home",font=("Lucida",15),fg='#9AA1A4',bg="#5A7E91",bd=0,activebackground="#5A7E91",anchor='w',command=lambda:home(window)).grid(row=0,column=0)
    Button(big_frame,text="About",font=("Lucida",15),fg='#9AA1A4',bg="#5A7E91",bd=0,activebackground="#5A7E91",anchor='e',command=lambda:about(window)).grid(row=0,column=1)
    big_frame.place(x=325,y=28)
    
    sidebar=Canvas(window,bg='white', highlightthickness=1, highlightbackground="#D7D9DA",height="350")
    Label(sidebar,text="Our Sidebar",font=("Lucida",25),width='10',bg='white').place(x=10,y=10)
    Label(sidebar,text="You can put any information here you'd  like.",font=("Lucida",15),width='32',bg='white',justify=LEFT,wraplength=350,fg='#9AA1A4').place(x=10,y=50)
    
    Latest_Post=Entry(sidebar,width="22",font=("Lucida",20),fg="gray",bg="white")
    Latest_Post.insert(0,"    Latest Posts")
    Latest_Post.configure(state="readonly")
    Latest_Post.place(x=20,y=120)
    
    Announcements=Entry(sidebar,width="22",font=("Lucida",20),fg="gray",bg="white")
    Announcements.insert(0,"    Announcements")
    Announcements.configure(state="readonly")
    Announcements.place(x=20,y=170)
    
    Calendars=Entry(sidebar,width="22",font=("Lucida",20),fg="gray",bg="white")
    Calendars.insert(0,"    Calendars")
    Calendars.configure(state="readonly")
    Calendars.place(x=20,y=220)
    
    etc=Entry(sidebar,width="22",font=("Lucida",20),fg="gray",bg="white")
    etc.insert(0,"    etc")
    etc.configure(state="readonly")
    etc.place(x=20,y=270)
    
    sidebar.place(x=ws-(1366-950),y=100)
    

        
def login_label(window):
    big_frame = Frame(window)
    Button(big_frame,text="Login",font=("Lucida",15),fg='#9AA1A4',bg="#5A7E91",bd=0,activebackground="#5A7E91",anchor='w',command=lambda:login(window)).grid(row=0,column=0)
    Button(big_frame,text="Register",font=("Lucida",15),fg='#9AA1A4',bg="#5A7E91",bd=0,activebackground="#5A7E91",anchor='e',command=lambda:register(window)).grid(row=0,column=1)
    big_frame.place(x=1025,y=28)

def account_label(window):
    big_frame = Frame(window)
    Button(big_frame,text="New Post",font=("Lucida",15),fg='#9AA1A4',bg="#5A7E91",bd=0,activebackground="#5A7E91",anchor='w',command=lambda:new_post(window)).grid(row=0,column=0)
    Button(big_frame,text="Account",font=("Lucida",15),fg='#9AA1A4',bg="#5A7E91",bd=0,activebackground="#5A7E91",anchor='e',command=lambda:account(window)).grid(row=0,column=1)
    Button(big_frame,text="Logout",font=("Lucida",15),fg='#9AA1A4',bg="#5A7E91",bd=0,activebackground="#5A7E91",anchor='e',command=lambda:logout(window)).grid(row=0,column=2)
    
    big_frame.place(x=1025,y=28)  
def update_post1(user_name,new_title,new_content,post,root): 
    if  update_post(user_name,new_title,new_content,post):
        home(root)
    
def edit(post,root1):
    global user_info
    root=Tk()
    print(user_info)
    adjustwindow(root)  
    layout(root)      
    if user_info == ():    
        login_label(root)
    else:
        account_label(root)
    login=Canvas(root,width=700,height=400,bg='white', highlightthickness=1, highlightbackground="#D7D9DA")
    Label(login,text="Edit Post",font=("Lucida",25),width='9',bg='white').place(x=10,y=20)
       
    Label(login,text="Title",font=("Lucida",15),width='6',bg='white',justify=LEFT,fg='black').place(x=13,y=100)
    title=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white")
    title.insert(0,post[2])
    title.place(x=30,y=130)
    
    Label(login,text="Content",font=("Lucida",15),width=8,bg='white',justify=LEFT,fg='black').place(x=13,y=170)
    content=Text(login,width="40",font=("Lucida",20),fg="gray",bg="white",height=3)
    content.insert(INSERT,post[3])
    content.place(x=30,y=200)
    
    
    Button(login,text="Update Post",font=("Lucida",15),fg="#0FBFF3",bg="white",bd=1,highlightbackground="#0FBFF3",command=lambda:update_post1(user_info[0][0],title.get(),content.get(1.0,END),post,root)).place(x=30,y=320)
    login.place(x=200,y=100)  
    root1.destroy()
    root.mainloop()
def delete(title,root):
    for i in title:
         if user_info[0][0] in i :  
            answer=messagebox.askyesno(title="Confirmation",message="Are you sure, you want to delete post?")
            if answer:
                print(i)
                conn = sqlite3.connect("lite.db")
                print("connection successful")
                cursor=conn.cursor()
                cursor.execute("DELETE FROM posts WHERE id=?",(i[0],))
                conn.commit()
                conn.close()
                home(root)
            
def title(x,root1):
    title = search_title(x)
    root=Tk()
    adjustwindow(root)  
    layout(root)      
    if user_info == ():    
        login_label(root)
    else:
        account_label(root)
    container = Frame(root)
    canvas = Canvas(container,width=550,height=root.winfo_screenheight()-300)
    
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    for i in title:     
        Post=Canvas(scrollable_frame,bg='white', highlightthickness=1, highlightbackground="#D7D9DA",width="500",height="800")
        Post_inside=Canvas(Post,bg='white', highlightthickness=1, highlightbackground="#D7D9DA",width="500",height="150")
        big_frame = Frame(root)
        Label(Post_inside,text=i[1],font=("Lucida",15),fg="#0FBFF3",bg="white",bd=0).grid(row=0,column=0)
        Label(Post_inside,text=" "+i[4],font=("Lucida",8),fg="#606768",bg="white",bd=0).grid(row=0,column=1)
        big_frame.pack()
        count=len(i[3].split())
        lines=int(count/8)
        print(lines)
        if user_info!=():        
            if user_info[0][0]==i[1]:
                Button(Post,text="Edit",font=("Lucida",10),fg="white",bg="green",bd=1,command=lambda:edit(i,root)).place(x=200,y=20)
                Button(Post,text="delete",font=("Lucida",10),fg="white",bg="red",bd=1,command=lambda:delete(title,root)).place(x=250,y=20)
        Label(Post,text=i[2],font=("Lucida",15),fg="Black",bg="white",bd=0).place(x=18,y=50)
        content=Label(Post,text=i[3],font=("Lucida",10),width='60',bg='white',justify=LEFT,wraplength=350+(lines*2),fg='black')
        content.place(x=18,y=80)
        Post_inside.place(x=10,y=10)
        Post.pack()
    container.place(x=330,y=100)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    root1.destroy()
    root.mainloop()  
    
def name(x,root1):
    print(user_info)
    authorname = search_name(x)
    root=Tk()
    adjustwindow(root)  
    layout(root)      
    if user_info == ():    
        login_label(root)
    else:
        account_label(root)
    container = Frame(root)
    canvas = Canvas(container,height=root.winfo_screenheight()-200,width=500)
    
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    for i in authorname:     
        Post=Canvas(scrollable_frame,bg='white', highlightthickness=1, highlightbackground="#D7D9DA",width="500",height="150")
        Post_inside=Canvas(Post,bg='white', highlightthickness=1, highlightbackground="#D7D9DA",width="500",height="150")
        big_frame = Frame(root)
        Label(Post_inside,text=i[1],font=("Lucida",15),fg="#0FBFF3",bg="white",bd=0).grid(row=0,column=0)
        Label(Post_inside,text=" "+i[4],font=("Lucida",8),fg="#606768",bg="white",bd=0).grid(row=0,column=1)
        big_frame.pack()
        title_name=i[2]
        Button(Post,text=title_name,font=("Lucida",15),fg="Black",bg="white",bd=0,command=lambda title_name=title_name: title(title_name,root)).place(x=18,y=40)
        content=Label(Post,text=i[3],font=("Lucida",15),width='32',bg='white',justify=LEFT,wraplength=350,fg='black')
        content.place(x=18,y=80)
        Post_inside.place(x=10,y=10)
        Post.pack()
    container.place(x=360,y=100)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    root1.destroy()
    root.mainloop()  
def home(root1):
    
    global user_info
    root=Tk()
    adjustwindow(root)  
    layout(root)     
    if user_info == ():    
        login_label(root)
    else:
        account_label(root)
    container = Frame(root)
    canvas = Canvas(container,height=root.winfo_screenheight()-200,width=500)
    
   # my_img = PhotoImage(file="game.png") 
    button_sample = Button(root,text="Game",bd=0,anchor="nw",command=play,fg="dark blue",font=("Lucida",20))
    button_sample.place(x=1200,y=600)

    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    posts=fetch_post()
    for i in reversed(posts):
        Post=Canvas(scrollable_frame,bg='white', highlightthickness=1, highlightbackground="#D7D9DA",width="500",height="150")
        Post_inside=Canvas(Post,bg='white', highlightthickness=1, highlightbackground="#D7D9DA",width="500",height="150")
        big_frame = Frame(root)
        user_name=i[1]
        Button(Post_inside,text=user_name,font=("Lucida",15),fg="#0FBFF3",bg="white",bd=0,command=lambda user_name=user_name: name(user_name,root)).grid(row=0,column=0)
        Label(Post_inside,text=" "+i[4],font=("Lucida",8),fg="#606768",bg="white",bd=0).grid(row=0,column=1)
        big_frame.pack()
        title_name=i[2]
        my_button=Button(Post,text=title_name,font=("Lucida",15),fg="Black",bg="white",bd=0,command=lambda title_name=title_name: title(title_name,root))
        my_button.place(x=18,y=50)
        
        content=Text(Post,height=3,width=55)
        content.insert(END,i[3])
        content.config(state="disable")
        content.place(x=18,y=80)
        Post_inside.place(x=10,y=10)
        Post.pack()
    
    container.place(x=360,y=100)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    root1.destroy()
    root.mainloop()  
    
def logout(root):
    global user_info
    print(user_info)
    user_info = ()
    print(user_info)
    login(root)

def update_acc(x,y,root):   
    global user_info
    print(user_info)
    print(x)
    print(y)
    user_info=update(x,y,user_info)
    print(user_info)
    account(root)

def upload_pic():
    # global small_frame
    # small_frame.filename = filedialog.askopenfilename(initialdir="/",title="Select A File",filetypes=(("jpg files", "*.jpg"),("png files","*.png"),("all files", "*.*")))
    # filename1=small_frame.filename
    # print(filename1)
    # img = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)
    # scale_percent = 4 
    # width=130
    # height=140
    # dim = (width, height)
    # # resize image
    # resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    # cv2.imwrite("ResizedImage.jpg", resized)
    # im=Image.open("ResizedImage.jpg")
    # ph=ImageTk.PhotoImage(im)
    # label=Label(small_frame,image=ph)
    # label.image=ph
    # label.place(x=0,y=0)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # Upload_p.insert(0,str(filename1))
    messagebox.showerror("Technical Error ","We Are Working ON It, Try Again later")
        
def account(root1):
    global user_info,small_frame
    root=Tk()
    print(user_info)
    adjustwindow(root)  
    layout(root)      
    if user_info == ():    
        login_label(root)
    else:
        account_label(root)
    login=Canvas(root,width=700,height=500,bg='white', highlightthickness=1, highlightbackground="#D7D9DA")

    small_frame=Frame(login,background='white')
    small_frame.place(x=20,y=5,width=130, height=140)

    Label(login,text=user_info[0][0],font=("Lucida",25),width='20',bg='white',anchor="w").place(x=200,y=20)
    Label(login,text=user_info[0][1],font=("Lucida",15),width='45',bg='white',fg="gray",anchor="w").place(x=200,y=60)
   
    Label(login,text="Account Info",font=("Lucida",20),width='11',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=150)
      
    Label(login,text="Username",font=("Lucida",15),width='10',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=190)
    username=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white")
    username.insert(0,user_info[0][0])
    username.place(x=30,y=220)
    
    Label(login,text="Email",font=("Lucida",15),width='7',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=280)
    email=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white")
    email.insert(0,user_info[0][1])
    email.place(x=30,y=310)
    
    Upload=Button(login,text="Upload Picture",command=lambda:upload_pic())
    Upload.place(x=30,y=400)
    
    Button(login,text="Update",font=("Lucida",15),fg="#0FBFF3",bg="white",bd=1,highlightbackground="#0FBFF3",command=lambda:update_acc(username.get(),email.get(),root)).place(x=30,y=450)
    login.place(x=200,y=100)  
    root1.destroy()
    root.mainloop()
    
def about(root1):
    root=Tk()
    adjustwindow(root)  
    layout(root)      
    if user_info == ():    
        login_label(root)
    else:
        account_label(root)
    Label(root,text=credit,font=("Lucida",11),width='100',bg='white',justify=LEFT,wraplength=600,fg='black').place(x=50,y=100)
    root1.destroy()
    root.mainloop()  
    
def SaveDetail(user,email,pwd,con_pwd,root):
    if user!="":
        if email!="":
            if pwd==con_pwd and pwd!="": 
                    details=[user,email,pwd]    
                    m=random.randint(1000,10000)        
                    subject = "OTP"
                    msg = str(m) 
                    if send_email(subject, msg,email,details):
                        login(root)
            else:
                 messagebox.showerror(' Failed',"Password doesn't match" ) 
        else:
             messagebox.showerror(' Failed',"Enter email Field" )
    else:
          messagebox.showerror(' Failed',"Enter User Name" )

def signin(x,y,root):
    global user_info
    user_info = log(x,y)
    if user_info!= ():
        home(root)
               
def forgot_password(root1):
    global user_info
    root=Tk()
    print(user_info)
    adjustwindow(root)  
    layout(root)      
    login_label(root)
  
    login=Canvas(root,width=700,height=400,bg='white', highlightthickness=1, highlightbackground="#D7D9DA")

    Label(login,text="Forgot Password?",font=("Lucida",20),width='15',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=40)
      
    Label(login,text="Username",font=("Lucida",15),width='10',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=100)
    username=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white")
    username.place(x=30,y=130)
    
    Label(login,text="Email",font=("Lucida",15),width='7',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=190)
    email=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white")
    email.place(x=30,y=220)
    
    
    Button(login,text="Get Password",font=("Lucida",15),fg="#0FBFF3",bg="white",bd=1,highlightbackground="#0FBFF3",command=lambda:forgot(username.get(),email.get())).place(x=30,y=280)
    login.place(x=200,y=100)  
    root1.destroy()
    root.mainloop()
          
def login(root1):
    root1.destroy()
    root=Tk()
    adjustwindow(root)  
    layout(root)      
    login_label(root)

    login=Canvas(root,width=700,height=350,bg='white', highlightthickness=1, highlightbackground="#D7D9DA")
    Label(login,text="Log In",font=("Lucida",25),width='10',bg='white').place(x=10,y=10)
    # Label(sidebar,text="You can put any information here you'd  like.",font=("Lucida",15),width='32',bg='white',justify=LEFT,wraplength=350,fg='#9AA1A4').place(x=10,y=50)
    login.create_line(15, 60, 670, 60,fill="#606768", width=2) 
    
    Label(login,text="Email",font=("Lucida",15),width='7',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=70)
    email=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white")
    email.place(x=30,y=100)
    
    Label(login,text="Password",font=("Lucida",15),width='10',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=150)
    password=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white",show="*")
    password.place(x=30,y=180)
    
    var1 = IntVar()
    Checkbutton(login, text="Remember Me", variable=var1,font=("Lucida",10)).place(x=30,y=230)
  
    Button(login,text="Login",font=("Lucida",15),fg="#0FBFF3",bg="white",bd=1,highlightbackground="#0FBFF3",command=lambda:signin(email.get(),password.get(),root)).place(x=30,y=280)
    Button(login,text="Forgot Password?",font=("Lucida",10),width='14',bg='white',justify=LEFT,fg='#0FBFF3',bd=0,command=lambda:forgot_password(root)).place(x=100,y=290)
    login.place(x=200,y=100)  
    
    Label(root,text="Need An Account?",font=("Lucida",10),width='20',bg='white',justify=LEFT,fg='black').place(x=200,y=460)
    Button(root,text="Sign Up Now",font=("Lucida",10),fg="#0FBFF3",bg="white",bd=0,highlightbackground="#0FBFF3",command=lambda :register(root)).place(x=340,y=460)

    root.mainloop()


def register(root1):
    root=Tk()
    adjustwindow(root)  
    layout(root)      
    login_label(root)
    
    register=Canvas(root,width=700,height=500,bg='white', highlightthickness=1, highlightbackground="#D7D9DA")
    Label(register,text="Join Today",font=("Lucida",25),width='10',bg='white').place(x=10,y=10)
    # Label(sidebar,text="You can put any information here you'd  like.",font=("Lucida",15),width='32',bg='white',justify=LEFT,wraplength=350,fg='#9AA1A4').place(x=10,y=50)
    register.create_line(15, 60, 670, 60,fill="#606768", width=2) 
    Label(register,text="Username",font=("Lucida",15),width='10',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=70)
    username=Entry(register,width="40",font=("Lucida",20),fg="gray",bg="white")
    username.place(x=30,y=100)
    
    Label(register,text="Email",font=("Lucida",15),width='7',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=150)
    email=Entry(register,width="40",font=("Lucida",20),fg="gray",bg="white")
    email.place(x=30,y=180)
    
    Label(register,text="Password",font=("Lucida",15),width='10',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=230)
    password=Entry(register,width="40",font=("Lucida",20),fg="gray",bg="white",show="*")
    password.place(x=30,y=260)
    
    Label(register,text="Confirm Password",font=("Lucida",15),width='17',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=13,y=310)
    confirm_password=Entry(register,width="40",font=("Lucida",20),fg="gray",bg="white",show="*")
    confirm_password.place(x=30,y=340)
    
    Button(register,text="Sign Up",font=("Lucida",15),fg="#0FBFF3",bg="white",bd=1,highlightbackground="#0FBFF3",command=lambda :SaveDetail(username.get(),email.get(),password.get(),confirm_password.get(),root)).place(x=30,y=400)
    Label(register,text="Already Have An Account?",font=("Lucida",10),width='20',bg='white',justify=LEFT,wraplength=350,fg='black').place(x=30,y=450)
    Button(register,text="Sign In",font=("Lucida",10),fg="#0FBFF3",bg="white",bd=0,highlightbackground="#0FBFF3",command=lambda:login(root)).place(x=200,y=450)
    register.place(x=200,y=100)    
    root1.destroy()
    root.mainloop()
    
def insert_post(author,title,content,date_posted,root):   
    if  post(author,title,content,date_posted):
        home(root)
def new_post(root1):
    global user_info
    root=Tk()
    print(user_info)
    adjustwindow(root)  
    layout(root)      
    if user_info == ():    
        login_label(root)
    else:
        account_label(root)
    login=Canvas(root,width=700,height=400,bg='white', highlightthickness=1, highlightbackground="#D7D9DA")
    Label(login,text="New Post",font=("Lucida",25),width='9',bg='white').place(x=10,y=20)
       
    Label(login,text="Title",font=("Lucida",15),width='6',bg='white',justify=LEFT,fg='black').place(x=13,y=100)
    title=Entry(login,width="40",font=("Lucida",20),fg="gray",bg="white")
    title.place(x=30,y=130)
    
    Label(login,text="Content",font=("Lucida",15),width=8,bg='white',justify=LEFT,fg='black').place(x=13,y=170)
    content=Text(login,width="40",font=("Lucida",20),fg="gray",bg="white",height=3)
    content.place(x=30,y=200)
    
    
    Button(login,text="Post",font=("Lucida",15),fg="#0FBFF3",bg="white",bd=1,highlightbackground="#0FBFF3",command=lambda:insert_post(user_info[0][0],title.get(),content.get(1.0,END),date.today().strftime("%B %d, %Y"),root)).place(x=30,y=320)
    login.place(x=200,y=100)  
    root1.destroy()
    root.mainloop()

    
root=Tk()
about(root) 
    
