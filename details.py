import tkinter as tk
from tkinter import ttk
from subprocess import call

t=tk.Tk()

t.minsize(1500,1500)


n=tk.Label(t,text='BELL EVENT MANAGEMENT',fg='red',font='none 40 bold')
n.place(x=0,y=0)

def wed():
    t.destroy()
    call(['python','wedding.py'])
        
a=tk.Button(t,text='WEDDING',bg='black',fg='white',font='none 30 bold',command=wed)
a.place(x=100,y=100)

def eng():
    t.destroy()
    call(['python','engagmnt.py'])
    
b=tk.Button(t,text='ENGAGEMENT',bg='black',fg='white',font='none 30 bold',command=eng)
b.place(x=100,y=200)

def bir():
    t.destroy()
    call(['python','birthday.py'])
    
c=tk.Button(t,text='BIRTHDAY',bg='black',fg='white',font='none 30 bold',command=bir)
c.place(x=100,y=300)

def ann():
    t.destroy()
    call(['python','anniversery.py'])
    
d=tk.Button(t,text='ANNIVERSERIES',bg='black',fg='white',font='none 30 bold',command=ann)
d.place(x=100,y=400)

def death():
    t.destroy()
    call(['python','death.py'])
    
e=tk.Button(t,text='DEATH',bg='black',fg='white',font='none 30 bold',command=death)
e.place(x=100,y=500)

def back():
    t.destroy()
    call(['python','front_page.py'])
    
x=tk.Button(t,text='Back',bg='black',fg='white',font='none 20 bold',command=back)
x.place(x=100,y=600)

def exit():
    t.destroy()

y=tk.Button(t,text='Exit',bg='black',fg='white',font='none 20 bold',command=exit)
y.place(x=250,y=600)


t.mainloop()
