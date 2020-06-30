import tkinter as tk
import tkinter.messagebox as mg
from subprocess import call
import pymysql
from datetime import datetime
        
t=tk.Tk()

tk.Label(t,text='BELL EVENT MANAGEMENT',fg='maroon',font='none 40 bold').place(x=30,y=30)
tk.Label(t,text='REGISTRATION FORM',bg='light yellow',fg='black',font='none 30 bold').place(x=100,y=100)

tk.Label(t,text='NAME    :',bg='light yellow', fg='black',font='none 20 bold').place(x=100,y=200)
tk.Label(t,text='DISTRICT   :',bg='light yellow', fg='black',font='none 20 bold').place(x=100,y=250)
tk.Label(t,text='AREA  :', bg='light yellow',fg='black',font='none 20 bold').place(x=100,y=300)
tk.Label(t,text='PIN :', bg='light yellow',fg='black',font='none 20 bold').place(x=100,y=350)
tk.Label(t,text='MOBILE :', bg='light yellow',fg='black',font='none 20 bold').place(x=100,y=400)
tk.Label(t,text='MAIL_ID:', bg='light yellow',fg='black',font='none 20 bold').place(x=100,y=450)
tk.Label(t,text='DATE OF THE EVENT:', bg='light yellow',fg='black',font='none 20 bold').place(x=100,y=500)
tk.Label(t,text='TYPE OF THE EVENT:', bg='light yellow',fg='black',font='none 20 bold').place(x=100,y=550)
tk.Label(t,text='PACKAGE :', bg='light yellow',fg='black',font='none 20 bold').place(x=100,y=600)

name=tk.StringVar()
cn=tk.Entry(t,width=50,textvariable=name)
name.set('type your full name here!!!')
cn.place(x=400,y=210)
cd=tk.Entry(t,width=50)
cd.place(x=400,y=260)
ca=tk.Entry(t,width=50)
ca.place(x=400,y=310)
cp=tk.Entry(t,width=50)
cp.place(x=400,y=360)
cmo=tk.Entry(t,width=50)
cmo.place(x=400,y=410)
cmb=tk.Entry(t,width=50)
cmb.place(x=400,y=460)

date= tk.IntVar()
cde = tk.Entry( t, textvariable=date,width=50)
date.set( "YYYY/MM/DD" )


cde.place(x=400,y=510)
cte=tk.Entry(t,width=50)
cte.place(x=400,y=560)
cpe=tk.Entry(t,width=50)
cpe.place(x=400,y=610)

def register():
    name=cn.get()
    district=cd.get()
    area=ca.get()
    pin=cp.get()
    mobile=cmo.get()
    mail=cmb.get()
    event_date=cde.get()
    event_type=cte.get()
    event_package=cpe.get()
    n=datetime.now()

    if(name=="" or mobile=="" or pin==""):
        mg.showinfo('complt fields!!!')
    else:
        x=pymysql.connect('localhost','root','root1','event_mn')
        cursor=x.cursor()
        cursor.execute("insert into events values('"+name+"','"+district+"','"+area+"','"+pin+"','"+mobile+"','"+mail+"','"+event_date+"','"+event_type+"','"+event_package+"',now())")
        cursor.execute('commit')
        x.close()
        mg.showinfo('we will contact you soon :)')
        t.destroy()

    global y
    y=[name,district,area,mail,pin,mobile,event_date,event_type,event_package]

g=tk.Button(t,text='APPLY',bg='VIOLET',fg='white',command=register,font='none 28 bold').place(x=250,y=670)

def back():
    t.destroy()
    call(['python','details.py'])
bk=tk.Button(t,text='BACK',bg='VIOLET',fg='white',command=back,font='none 28 bold').place(x=55,y=670)


def exit():
    mg.showinfo('visit again')
    t.destroy()
ex=tk.Button(t,text='EXIT',bg='VIOLET',fg='white',command=exit,font='none 28 bold').place(x=450,y=670)

t.mainloop()

