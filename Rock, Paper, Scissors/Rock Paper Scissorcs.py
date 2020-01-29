#Rock Paper Sccisors Game
import random
from tkinter import *
from tkinter.ttk import *
def click2Rock():
    choices=['ROCK','PAPER','SCISSORS']
    computersChoice=random.choice(choices)
    if computersChoice=='SCISSORS':
        result=Label(window,text=f'YOU HAVE WON THE COMPUTER PICKED {computersChoice}',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60,pady=25,)
    elif  computersChoice=='ROCK':
        result=Label(window,text=f'IT IS A TIE THE COMPUTER PICKED {computersChoice} AS WELL',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60,pady=25,)
    elif computersChoice=='PAPER':
        result=Label(window,text=f'YOU HAVE LOST THE COMPUTER PICKED {computersChoice}',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60,pady=25,)
def click2Paper():
    choices=['ROCK','PAPER','SCISSORS']
    computersChoice=random.choice(choices)
    if computersChoice=='ROCK':
        result=Label(window,text=f'YOU HAVE WON THE COMPUTER PICKED {computersChoice}',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60, pady=25,)
    elif computersChoice=='PAPER':
        result=Label(window,text=f'IT IS A TIE THE COMPUTER PICKED {computersChoice} AS WELL',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60, pady=25,)
    elif computersChoice=='SCISSORS':
        result=Label(window,text=f'YOU HAVE LOST THE COMPUTER PICKED {computersChoice}',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60,pady=25,)
def click2Scissors():
    choices=['ROCK','PAPER','SCISSORS']
    computersChoice=random.choice(choices)
    if computersChoice=='SCISSORS':
        result=Label(window,text=f'IT IS A TIE THE COMPUTER PICKED {computersChoice} AS WELL',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60, pady=25,)
    elif  computersChoice=='PAPER':
        result=Label(window,text=f'YOU HAVE WON THE COMPUTER PICKED {computersChoice}',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60, pady=25,)
    elif computersChoice=='ROCK':
        result=Label(window,text=f'YOU HAVE LOST THE COMPUTER PICKED {computersChoice}',font=('Verdana',13))
        result.grid(row=3,column=1,padx=60,pady=25,)

window=Tk()
window.title('Rock vs Paper vs Scissors')
title=Label(window, text="Let's Play Rock, Papers, Scissors",font=('Verdana',20))
title.grid(row=0,sticky=W+E+N+S,column=1,columnspan=2,padx=115, pady=10,)

rockPhoto=PhotoImage(file="Rock2.png")
rockphoto=rockPhoto.subsample(5,5)
rockBtn=Button(window,text='ROCK',image=rockphoto,compound=TOP,command=click2Rock)
rockBtn.grid(row=1,sticky=W,column=0,padx=100, pady=50)

paperPhoto=PhotoImage(file='paper2.png')
paperphoto=paperPhoto.subsample(5,5)
paperBtn=Button(window, text='PAPER',image=paperphoto,compound=TOP,command=click2Paper)
paperBtn.grid(row=1,column=1,sticky=W,padx=220, pady=50)

scissorPhoto=PhotoImage(file='scissors2.png')
scissorphoto=scissorPhoto.subsample(5,5)
scissorBtn=Button(window,text='SCISSORS',image=scissorphoto,compound=TOP,command=click2Scissors)
scissorBtn.grid(row=1,column=2,sticky=W,padx=1, pady=50)
