import tkinter as tk
from tkinter import ttk
from subprocess import call

t=tk.Tk()

f=tk.Label(t,text='BELL EVENT MANAGEMENT',fg='red',font='none 40 bold')
f.place(x=0,y=0)
p=tk.Label(t,text='BIRTHDAY',fg='green',font='none 30 bold')
p.place(x=50,y=70)
q=tk.Label(t,text='We provide our best to make your day beautiful...',fg='white',font='none 20 italic',bg='black')
q.place(x=50,y=120)
r=tk.Label(t,text='Our service includes food, stage decorations,etc etc....',fg='WHITE',font='none 20 italic',bg='black')
r.place(x=50,y=180)
s=tk.Label(t,text='Our range: \n 1. Diamond pack: 50000 per 1000 head. \n :FOOD LIST: \n +3 types of juices \n +Mutton majboos and chicken chilly \n +Veg fried rice and Mushroom butter masala. \n (Other programs depends upon your ideas :) )\n  \n 2. Golden pack: 25000 per 1000 head \nFOOD LIST: \n+Mint lime and Water melon squash \n +Beef biriyani and chicken roast \n +Sadhya \n (others depends upon your ideas :) ) \n  \n 3.Silver pack: 10000 per 1000 head \n FOOD LIST: \n +Mint lime \n +Chicken biriyani \n +Veg biriyani /n  ',fg='WHITE',font='none 15 italic',bg='black')
s.place(x=50,y=230)

def login():
    t.destroy()
    call(['python','login.py'])

a=tk.Button(t,text='Register',bg='violet',fg='white',font='none 20 bold',command=login)
a.place(x=150,y=720)

import tkinter.messagebox as mg

def ext():
    mg.showinfo('visit again')
    t.destroy()
    
ex=tk.Button(t,text='EXIT',bg='VIOLET',fg='white',command=ext,font='none 20 bold').place(x=400,y=720)
          
t.mainloop()
