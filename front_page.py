from tkinter import *
from subprocess import call
import tkinter.messagebox as mg
from PIL import Image
from PIL import ImageTk

t=Tk()

t.minsize(750,750)

t.title('BELL EVENT MANAGEMENT')

t.configure(background='green')


width=750
height=750
photo=Image.open("C:\\Users\\User\\Desktop\\22.png")
photo = photo.resize((width,height), Image.ANTIALIAS)
p=ImageTk.PhotoImage(photo)

q=Label(t,image=p)
q.place(x=0,y=0)

a=Label(t,text='BELL EVENT MANAGEMENT',fg='black',font='none 40 bold').place(x=5,y=0)
b=Label(t,text='...OUR SERVICES...',fg='yellow',font='none 30 bold',bg='maroon').place(x=25,y=100)
c=Label(t,text='WEDDING',fg='WHITE',font='none 25 bold',bg='maroon').place(x=25,y=200)
d=Label(t,text='ENGAGEMENT',fg='WHITE',font='none 25 bold',bg='black').place(x=25,y=250)
e=Label(t,text='BIRTHDAY',fg='WHITE',font='none 25 bold',bg='maroon').place(x=25,y=300)
f=Label(t,text='ANNIVERSARIES',fg='WHITE',font='none 25 bold',bg='maroon').place(x=25,y=350)
g=Label(t,text='DEATH',fg='WHITE',font='none 25 bold',bg='maroon').place(x=25,y=400)



def n():
    t.destroy()
    call(['python','details.py'])

y=Button(text='OUR PROGRAMMES',fg='white',font='none 25 bold',bg='brown',command=n)
y.place(x=25,y=500)

def z():
    mg.showinfo('visit again')
    t.destroy()
    
m=Button(text='EXIT',fg='white',font='none 20 bold',bg='brown',command=z)
m.place(x=100,y=600)    

t.mainloop()
