from cgitb import text
from codecs import getencoder
from email.mime import application
import tkinter as TK
from tkinter import ttk
from tkinter import *

from mysqlx import Row

class ConnectorDB:

    def __init__(self,root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("800x800+300+0")
        self.root.resizable(width =False,height=False)
        #all frames go here
        MainFrame = Frame(self.root,bd=10,width=800,height=700,relief=RIDGE,bg="cadet blue")
        MainFrame.grid()

        #==================================functions=======================================
        def addrecord():
            return
        def delrecord():
            return
        def updateRecord():
            return
        def viewrecord():
            return
        # the title frame
        TittleFrame = Frame(MainFrame,bd=10,height=100,width=800,relief=RIDGE)
        TittleFrame.grid(row =0,column=0)
        myTitle = Label(TittleFrame,font=('arial',40,'bold'),text="MySQL Connector")
        myTitle.grid(row=0 ,column = 0,padx=143)

        topFrame=Frame(MainFrame,width=700,height=600,bd=5,relief=RIDGE)
        topFrame.grid(row =1,column=0)

        leftFrame = Frame(topFrame,width=600,height = 500,bd=5,relief=RIDGE,bg="cadet blue")
        leftFrame.pack(side=RIGHT)

        LeftFrame1=Frame(leftFrame,bd=5,width=600,height=480,padx=2,pady=4,relief=RIDGE)
        LeftFrame1.pack(side=LEFT,padx=0,pady=0)

        RightFrame1= Frame(topFrame,bd=5,width=100,height=400,padx=2,pady=4,bg="cadet blue",relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        #leftFrame1a=Frame(leftFrame,bd=5,width=500,height=180,padx=2,pady=2,relief=RIDGE)
        #leftFrame1a.grid(side=LEFT,padx=0,pady=0)

        lastFrame = Frame(MainFrame,bd=20,height=100,width=700,relief=RIDGE)
        lastFrame.grid(row =2,column=0,padx=10)


        #=========================creating entry boxes========================================
        self.std_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Student Name")
        self.std_label.grid(row=0,column=0)
        #student name entry box
        self.std_entry = Entry(LeftFrame1,bd=5,width=44)
        self.std_entry.grid(row=0,column=1)

        self.id_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Student ID")
        self.id_label.grid(row=1,column=0)
        #id entry box
        self.id_entry = Entry(LeftFrame1,bd=5,width=44)
        self.id_entry.grid(row=1,column=1)


        self.mail_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Email")
        self.mail_label.grid(row=2,column=0)

        self.mail_entry = Entry(LeftFrame1,bd=5,width=44)
        self.mail_entry.grid(row=2,column=1)


        self.mob_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Mobile")
        self.mob_label.grid(row=3,column=0)

        self.mobile_entry = Entry(LeftFrame1,bd=5,width=44)
        self.mobile_entry.grid(row=3,column=1)

        self.gender = Label(LeftFrame1,font=('Arial',12,'bold'),text="Gender")
        self.gender.grid(row=4,column=0)
        self.gender_label = ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=39,state='readonly')
        self.gender_label['values']=('','Female','Male')
        self.gender_label.current(0)
        self.gender_label.grid(row=4,column=1)
        #=====================================tables====================================
        #scroll_y = Scrollbar(leftFrame1a,orient=VERTICAL)
        
        #===============================================================================
        Button(lastFrame,state=ACTIVE,bd=5,text="Add Record",command=addrecord,width=18).grid(row=0,column=0)
        Button(lastFrame,state=ACTIVE,bd=5,text="Delete Record",command=delrecord,width=18).grid(row=0,column=1)
        Button(lastFrame,state=ACTIVE,bd=5,text="Update Record",command=updateRecord,width=18).grid(row=0,column=2)
        Button(lastFrame,state=ACTIVE,bd=5,text="View Record",command=viewrecord,width=18).grid(row=0,column=3)




if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()