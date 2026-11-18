from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
from datetime import datetime

t=Tk()
t.geometry("700x700")
t.title("Login page")
l=Label(t,text="USER NAME: ")
l.place(x=100,y=180)
l1=Label(t,text="PASSWORD")
l1.place(x=100,y=230)
e=Entry(t,width="20",bd=3)
e.place(x=180,y=180)
e1=Entry(t,width="20",bd=3)
e1.place(x=180,y=230)
def reg():
    t1=Tk()
    t1.geometry("700x700")
    l1=Label(t1,text="DATE")
    l1.place(x=150,y=200)
    l2=Label(t1,text="TIME")
    l2.place(x=150,y=240)
    e1=Entry(t1,width="20",bd=3)
    e1.place(x=230,y=200)
    e2=Entry(t1,width="20",bd=3)
    e2.place(x=230,y=240)
    def checkin():
        name=e1.get()
        date=e2.get()
        chin=e3.get()
        chout=e4.get()
        
    b1=Button(t1,text="CHECK IN")
    b1.place(x=150,y=360)
    b2=Button(t1,text="CHECK OUT")
    b2.place(x=230,y=360)
    

def login():
    user=e.get()
    pwd=e1.get()
    if user=="" and pwd=="":
        messagebox.showerror("Error","Please fill all the fields")
    else:
        con=mysql.connect(host="localhost",user="root",password="vasv2001",database="userlogin")
        cur=con.cursor()
        sql="select * from input where username='"+user+"' and password='"+pwd+"'"
        cur.execute(sql)
        row=cur.fetchone()

        if row==None:
            messagebox.showinfo("Information","Invalid username/password")
        else:
            messagebox.showinfo("Information","Login Successful")
            reg()
            
        con.close()
        
def cancel():
    t.destroy()

    
b1=Button(t,text="LOGIN",command=login)
b1.place(x=230,y=280)
b2=Button(t,text="CANCEL",command=cancel)
b2.place(x=150,y=280)

