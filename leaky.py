from email import message
from multiprocessing import connection
from sre_parse import State
import mysql.connector;
from tkinter import *
from tkinter import messagebox
def main_screeen():
    screen = Tk()
    screen.geometry("300x200")
    screen.title("off-shore 1.0")
    Button(screen,text="contractor",height = 1,width=9).place(x = 85 , y= 80)
def Ok():
    mydb = mysql.connector.connect(host = 'localhost', user='username',passwd='passwd',database="database")
    mycursor = mydb.cursor()
    uname = e1.get()
    password= e2.get()
    sql="select * from credentials where first_name=%s and passwd =%s"
    mycursor.execute(sql,[(uname),(password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("","login success")
        root.destroy()
        account = Tk()
        account.title("account")
        account.geometry("300x240")
        Button(account,text="CHECK FUNDS",height=1,width=19,bg="black",fg="white").place(x = 10,y = 10)
        Button(account,text="VIEW ACCOUNT DETAILS",height=1,width=19,bg="black",fg="white").place(x = 10,y = 40)
        Button(account,text="VIEW TRANSACTIONS",height=1,width=19,bg="black",fg ="white").place(x = 10,y = 70)
        Button(account,text="TRANSACT",height=1,width=19,bg="black",fg="white").place(x = 10,y = 100)
        Button(account,text="DEPOSIT",height=1,width=19,bg="black",fg="white").place(x = 10,y = 130)
        Button(account,text="LOG OUT",command=logout,height=1,width=9,bg="red",fg="white").place(x = 190,y = 190)
        return True

    else:
         #messagebox.showinfo("","Incorrect username and password")
         messagebox.showerror("error","Error!!2 attempts left")
         return False
def Insert():
    return
def logout():
    messagebox.showinfo("","logged out.Goodbye")
    exit()
    return
def done():
    messagebox.showinfo("Done","contract submittd for processing.Await confirmation")
    messagebox.showwarning("contract","This action cannot be undone untill contract is complete!")
    return
def reg():
    mydb = mysql.connector.connect(host ='localhost',user='username',passwd = 'passwd',database='database')
    cursor = mydb.cursor()
    def see():
        seeth=Tk()
        seeth.title("contract")
        seeth.geometry("300x200")
        Label(seeth,text ="Enter contract period(months) ").place(x = 70,y = 10)
        global cont
        cont=Entry(seeth)
        cont.place(x = 60, y = 40)
        Button(seeth,text ="start",command=done,height=1,width =9,bg="black",fg="white").place(x =92,y =64)
        return True    
    register = Tk()
    register.title("register")
    register.geometry("350x250")
    Label(register,text="First Name").place(x=10,y=8)
    Label(register,text="Last Name").place(x=10,y=40)
    Label(register,text="Password").place(x=10,y=70)
    Label(register,text="Valid Email").place(x=10,y=105)
    Label(register,text="Contact").place(x=10,y=130)
    Label(register,text="Deparetment").place(x=10,y=155)
    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    r1=Entry(register)
    r1.place(x=100,y=10)
    r2=Entry(register)
    r2.place(x=100,y=40)
    r3=Entry(register)
    r3.place(x=100,y=75)
    r3.config(show="*")
    r4=Entry(register)
    r4.place(x=100,y=100)
    r5=Entry(register)
    r5.place(x=100,y=125)
    r6=Entry(register)
    r6.place(x=100,y = 150)
    def insert():
        first_name =r1.get()
        last_name =r2.get()
        passwd= r3.get()
        email=r4.get()
        c_contact =r5.get()
        dept = r6.get()
        mydb = mysql.connector.connect(host = 'localhost', user='username',passwd='passwd',database="database")
        mycursor = mydb.cursor()
        try:
           sql = ("INSERT INTO credentials(first_name,last_name,passwd,email,c_contact,dept) VALUES(%s,%s,%s,%s,%s,%s)")
           record =(first_name,last_name,passwd,email,c_contact,dept)
           cursor.execute(sql,record)
           mydb.commit()
           messagebox.showinfo("","information updated succesfully..")
        except Exception as e:
            print(e)
            mydb.rollback()
            mydb.close()
    Button(register,text="contract",command=insert ,height=1,width=9,bg="black",fg="white").place(x=85,y=205)
    register.mainloop()
    return
root = Tk()
root.title("Off-shore")
root.geometry("300x200")
global e1
global e2
Label(root,text="username").place(x=10,y=10)
Label(root,text="password").place(x=10,y=40)
e1=Entry(root)
e1.place(x=100,y = 10)
e2 =Entry(root)
e2.place(x=100,y = 40)
e2.config(show="*")
Button(root,text="login",command=Ok ,height=1,width=9,bg="black",fg="white").place(x=85,y=80)
Button(root,text ="register",command= reg,height=1,width =9,bg="black",fg="white").place(x =85,y =120)
Button(root,text ="Home",command= main_screeen,height=1,width =9,bg="black",fg="white").place(x =85,y =160)

root.mainloop()
    