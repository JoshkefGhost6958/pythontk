from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
screen = Tk()
screen.geometry("300x250")
screen.title("notes 1.0")
#create login function
def login():


    conn =mysql.connector.connect(host='localhost',user='username',passwd='passwd',database='database')
    c_cursor = conn.cursor()
    sql =""
    conn.commit()
    conn.close()
    return

#update function
def update():
    update = Tk()
    update.title("record update")
    update.geometry("400x300")
    update.configure(bg='blue')

    upd_username_label = Label(update,text="Update username",bg='blue').grid(row=0,column=0)
    upd_username = Entry(update,width=29).grid(row=0,column=1)

    upd_email_label = Label(update,text="Update email",bg='blue').grid(row=1,column=0)
    upd_email = Entry(update,width=29).grid(row=1,column=1)

    upd_passwd_label = Label(update,text="Update password",bg='blue').grid(row=2,column=0)
    upd_passwd = Entry(update,width=29).grid(row=2,column=1)
    
    Button(update,text= "Update",height=1,width=14,command=update,state=ACTIVE).grid(row=3,column=1,columnspan=2)

    #connection to my database
    conn =mysql.connector.connect(host='localhost',user='username',passwd='passwd',database='database')
    c_cursor = conn.cursor()
    sql =""
    conn.commit()
    conn.close()
    update.mainloop()
    return

#delete from database function
def delete():
    conn =mysql.connector.connect(host='localhost',user='username',passwd='passwd',database='database')
    c_cursor = conn.cursor()
    sql =""
    conn.commit()
    conn.close()
    return

#insert into database
def register():
    conn =mysql.connector.connect(host='localhost',user='username',passwd='passwd',database='database')
    c_cursor = conn.cursor()
    sql =""
    conn.commit()
    conn.close()
    return
#create text names

u_name_label = Label(screen,text="username").grid(row=0,column=0)
mail_label = Label(screen,text="Email").grid(row=1,column=0)
passwd_label = Label(screen,text="password").grid(row=2,column=0)
#create text boxes

u_name = Entry(screen,width=20).grid(row=0,column=1)
email = Entry(screen,width=20).grid(row=1,column=1)
passwd = Entry(screen,width=20).grid(row=2,column=1)

Button(text="Login",height=1,width=14,command=login,state=ACTIVE,bg="gray",fg="black").grid(row=4,columnspan=2)
Button(screen,text= "update credentials",height=1,width=14,command=update,state=ACTIVE).grid(row=5,columnspan=2)
Button(screen,text="Create account",height=1,width=14,state=ACTIVE,command=register).grid(row=6,columnspan=2)
screen.mainloop()