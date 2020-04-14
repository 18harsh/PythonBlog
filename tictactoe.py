# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:55:19 2020

@author: Harsh
"""
from tkinter import*
import os
import sys
import random 
game=[" "," "," "," "," "," "," "," "," "]
global player1
global player2
global c
global n
c=0
global X,O,a11,a12,a13,a21,a22,a23,a31,a32,a33,root
def adjustWindow(window):
    w = 800  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(True, True)    # disabling the resize option for the window
    window.configure(background='white')    # making the background white of the window
def isspacefree(board,index):
    return game[index]==" "  
def makemove(i,player2):
    game[i]=player2  
def playerisx():
    global player1
    global player2
    player1='x'
    player2='0'
    X.config(state='disable')
    O.config(state='disable')    
    a11.config(state='normal')
    a12.config(state='normal')
    a13.config(state='normal')
    
    a21.config(state='normal')
    a22.config(state='normal')
    a23.config(state='normal')
    
    a31.config(state='normal')
    a32.config(state='normal')
    a33.config(state='normal')
    print(player1)
    print(player2)
def playeris0():
    global player1
    global player2
    player1='0'
    player2='x'    
    X.config(state='disable')
    O.config(state='disable')    
    a11.config(state='normal')
    a12.config(state='normal')
    a13.config(state='normal')
    
    a21.config(state='normal')
    a22.config(state='normal')
    a23.config(state='normal')
    
    a31.config(state='normal')
    a32.config(state='normal')
    a33.config(state='normal')
    print(player1)    
    print(player2)
def checkresult(bo,p):
    global c
    solution1=list(set((bo[0],bo[4],bo[8])))
    solution2=list(set((bo[0],bo[3],bo[6])))
    solution3=list(set((bo[1],bo[4],bo[7])))
    solution4=list(set((bo[3],bo[4],bo[5])))
    solution5=list(set((bo[2],bo[5],bo[8])))
    solution6=list(set((bo[2],bo[4],bo[6])))
    solution7=list(set((bo[6],bo[7],bo[8])))
    solution8=list(set((bo[0],bo[1],bo[2])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
#    print(result)
#    print(c)
    if n==0:
        if c==5:
            playres=Frame(root)
            playres.pack()
            Label(playres,text="Draw",bg="white").pack() 
    for i in range(8):
        if len(result[i])==1 and result[i][0]!=" ":
            if result[i][0]==p:                
                return True
            else:
                return False    
def print_game(pos):
    global play
    global n
    global c
#    print(pos)
    if pos==0:
        a11=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a11.grid(row=0, column=0 ,padx=5,pady=5)
        a11.config(state='disable')
    elif pos==1:
        a12=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a12.grid(row=0, column=1 ,padx=5,pady=5)
        a12.config(state='disable')
    elif pos==2:
        a13=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a13.grid(row=0, column=2,padx=5,pady=5)
        a13.config(state='disable')
    elif pos==3:
        a21=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a21.grid(row=1, column=0,padx=5,pady=5)
        a21.config(state='disable')
    elif pos==4:
        a22=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a22.grid(row=1, column=1,padx=5,pady=5)
        a22.config(state='disable')
    elif pos==5:
        a23=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a23.grid(row=1, column=2,padx=5,pady=5)
        a23.config(state='disable')
    elif pos==6:
        a31=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a31.grid(row=2, column=0,padx=5,pady=5)
        a31.config(state='disable')
    elif pos==7:
        a32=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a32.grid(row=2, column=1,padx=5,pady=5)
        a32.config(state='disable')
    elif pos==8:
        a33=Button(play,text=player2,width=12,anchor=CENTER,height=3)
        a33.grid(row=2, column=2,padx=5,pady=5)
        a33.config(state='disable')
def randomchoice(board,a):
      possibleMoves = []
      for i in a:
          if isspacefree(board, i):
            possibleMoves.append(i)
      if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
      else:
        return None        
def computer(player1,player2):
    for i in range(0,9):  
        copy=[]
        for j in range(0,9):
            copy.append(game[j])
        if isspacefree(copy,i):
            copy[i]=player2
            if checkresult(copy,player2):
                print("position",i)
                return i    
    for i in range(0,9):  
        copy=[]
        for j in range(0,9):
            copy.append(game[j])    
        if isspacefree(copy,i):
            copy[i]=player1
            if checkresult(copy,player1):
                return i  
    if isspacefree(game,4):
         return 4
    move=randomchoice(game,[1,3,5,7]) 
    if move!=None: 
        return move
    else:
         return randomchoice(game,[0,2,6,8])  

def dis(p):
    playres=Frame(root)
    playres.pack()
    Label(playres,text="Winner "+p,bg="white").pack()
           
def b11():
        global n
        global c
        c=c+1
        n=0
        a11=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a11.grid(row=0, column=0 ,padx=5,pady=5)
        game[0]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a11.config(state='disable')
def b12():
        global c
        c=c+1
        global n
        n=0
        a12=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a12.grid(row=0, column=1 ,padx=5,pady=5)
        game[1]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a12.config(state='disable')
def b13():
        global c
        c=c+1
        global n
        n=0
        a13=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a13.grid(row=0, column=2 ,padx=5,pady=5)
        game[2]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a13.config(state='disable')
def b21():
        global c
        c=c+1
        global n
        n=0
        a21=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a21.grid(row=1, column=0 ,padx=5,pady=5)
        game[3]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a21.config(state='disable')
def b22():
        global c
        c=c+1
        global n
        n=0
        a22=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a22.grid(row=1, column=1 ,padx=5,pady=5)
        game[4]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a22.config(state='disable')
def b23():
        global c
        c=c+1
        global n
        n=0
        a23=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a23.grid(row=1, column=2 ,padx=5,pady=5)
        game[5]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a23.config(state='disable')
def b31():
        global c
        c=c+1
        global n
        n=0
        a31=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a31.grid(row=2, column=0 ,padx=5,pady=5)
        game[6]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a31.config(state='disable')
def b32():
        global c
        c=c+1
        global n
        n=0
        a32=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a32.grid(row=2, column=1 ,padx=5,pady=5)
        game[7]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a32.config(state='disable')        
def b33():  
        global c
        c=c+1
        global n
        n=0
        a33=Button(play,text=player1,width=12,anchor=CENTER,height=3)
        a33.grid(row=2, column=2 ,padx=5,pady=5)
        game[8]=player1
#        print(game)
        if checkresult(game,player1):
            dis(player1)
            n=1 
        pos=computer(player1,player2)
        makemove(pos,player2)
#        print(pos)
        print_game(pos)
        if n==0:
            if checkresult(game,player2):
                dis(player2)
             
        a33.config(state='disable')
def play():        
	global X,O,a11,a12,a13,a21,a22,a23,a31,a32,a33,root
	root=Tk()
	root.title("Tic Tac Toe")
	adjustWindow(root)
	Label(root,text="",bg="white").pack()
	Label(root, text='Tic Tac Toe',font=("Lucida",25,'bold'),fg='#ffffff',bg='black',).pack()
	Label(root,text="",bg="white").pack()
	Label(root,text="",bg="white").pack()
	big_frame = Frame(root)
	big_frame.pack()
	X=Button(big_frame,text='Player-1 is X',width=12,anchor=CENTER,command=playerisx)
	X.grid(row=0, column=0 ,padx=5,pady=5)
	O=Button(big_frame,text='Player-1 is 0',width=12,anchor=CENTER,command=playeris0)
	O.grid(row=0, column=1 ,padx=5,pady=5)
	Label(root,text="",bg="white").pack()
	Label(root,text="",bg="white").pack()
	Label(root,text="",bg="white").pack()
	global play
	play=Frame(root)
	play.pack()
	a11=Button(play,text='1',width=12,anchor=CENTER,height=3,command=b11)
	a11.grid(row=0, column=0 ,padx=5,pady=5)
	a12=Button(play,text='2',width=12,anchor=CENTER,height=3,command=b12)
	a12.grid(row=0, column=1 ,padx=5,pady=5)
	a13=Button(play,text='3',width=12,anchor=CENTER,height=3,command=b13)
	a13.grid(row=0, column=2 ,padx=5,pady=5)

	a21=Button(play,text='4',width=12,anchor=CENTER,height=3,command=b21)
	a21.grid(row=1, column=0 ,padx=5,pady=5)
	a22=Button(play,text='5',width=12,anchor=CENTER,height=3,command=b22)
	a22.grid(row=1, column=1 ,padx=5,pady=5)
	a23=Button(play,text='6',width=12,anchor=CENTER,height=3,command=b23)
	a23.grid(row=1, column=2 ,padx=5,pady=5)

	a31=Button(play,text='7',width=12,anchor=CENTER,height=3,command=b31)
	a31.grid(row=2, column=0 ,padx=5,pady=5)
	a32=Button(play,text='8',width=12,anchor=CENTER,height=3,command=b32)
	a32.grid(row=2, column=1 ,padx=5,pady=5)
	a33=Button(play,text='9',width=12,anchor=CENTER,height=3,command=b33)
	a33.grid(row=2, column=2 ,padx=5,pady=5)
	Label(root,text="",bg="white").pack()
	Label(root,text="",bg="white").pack()
	Label(root,text="",bg="white").pack()
	Label(root,text="",bg="white").pack()

	a11.config(state='disable')
	a12.config(state='disable')
	a13.config(state='disable')

	a21.config(state='disable')
	a22.config(state='disable')
	a23.config(state='disable')

	a31.config(state='disable')
	a32.config(state='disable')
	a33.config(state='disable')


	root.mainloop()
