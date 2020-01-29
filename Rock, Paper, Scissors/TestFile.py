import random
from tkinter import *
from tkinter.ttk import *
def click2Rock():
    choices=['rock','paper','scissors']
    computersChoice=random.choice(choices)
    if computersChoice=='rock':
        Game='rockTie'
        print('it is a tie the computer {computersChoice} as well')
    elif  computersChoice=='scissors':
        Game='rockWin'
        print('You have won the computer picked {computersChoice}')
    elif computersChoice=='paper':
        Game='rockLose'
        print('You have lost the computer picked {computersChoice}')

def click2Paper():
    choices=['rock','paper','scissors']
    computersChoice=random.choice(choices)
    if computersChoice=='paper':
        result='it is a tie the computer {computersChoice} as well'
    elif  computersChoice=='rock':
       result='You have won the computer picked {computersChoice}'
    elif computersChoice=='scissors':
       result='You have lost the computer picked {computersChoice}'

def click2Scissors():
    choices=['rock','paper','scissors']
    computersChoice=random.choice(choices)
    if computersChoice=='scissors':
        result=(f'it is a tie the computer {computersChoice} as well')
    elif  computersChoice=='paper':
        result=(f'You have won the computer picked {computersChoice}')
    elif computersChoice=='rock':
        result==(f'You have lost the computer picked {computersChoice}')
def gameResults():
    if Game=="rockTie":
        Game.set('You Tied')
    elif Game=="rockWin":
        Game.set('You Won')
    elif Game=='rockLose':
        Game.set('You Lose')
window=Tk()
window.title('Rock vs Paper vs Scissors')
title=Label(window, text="Let's Play Rock, Papers, Scissors",font=('Verdana',18))
title.grid(row=0,sticky=W+E+N+S,column=1,columnspan=2,padx=130, pady=10,)

rockPhoto=PhotoImage(file="Rock2.png")
rockphoto=rockPhoto.subsample(5,5)
rockBtn=Button(window,text='ROCK',image=rockphoto,compound=TOP,command=click2Rock)
rockBtn.grid(row=1,sticky=W,column=0,padx=75, pady=50)

paperPhoto=PhotoImage(file='paper2.png')
paperphoto=paperPhoto.subsample(5,5)
paperBtn=Button(window, text='PAPER',image=paperphoto,compound=TOP,command=click2Paper)
paperBtn.grid(row=1,column=1,sticky=W,padx=220, pady=50)

scissorPhoto=PhotoImage(file='scissors2.png')
scissorphoto=scissorPhoto.subsample(5,5)
scissorBtn=Button(window,text='SCISSORS',image=scissorphoto,compound=TOP,command=click2Scissors)
scissorBtn.grid(row=1,column=2,sticky=W,padx=1, pady=50)

resultDis=Entry(window,text=gameResults,state='readonly')
resultDis.configure(width=100)
resultDis.grid(row=3,sticky=W+E+N+S, column=1,columnspan=1,padx=30, pady=75)
resultDis.bind(rockBtn,)
window.mainloop()
