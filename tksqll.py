from email.mime import application
import tkinter as TK
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import pymysql

class ConnectorDB:

    def __init__(self,root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("800x800+300+0")
        #self.root.resizable(width =False,height=False)
        #all frames go here
        MainFrame = Frame(self.root,bd=10,width=800,height=700,relief=RIDGE,bg="cadet blue")
        MainFrame.grid()

        #==================================functions=======================================
        def addrecord():
            conn = mysql.connector.connect(host = "localhost",user="root",passwd="Ghost@558**$",database="student")
            myCursor = conn.cursor();
            try:
               sql=("INSERT INTO About VALUES %d,%d,%d,%d,%d,%c")
               gen1 = 'M'     
               myCursor.execute(sql,[(f_name),(s_name),(mails),(address),(moby),(gen1)])
               conn.commit()
               messagebox.showinfo("Record added successfully")
            except Exception as e:
                print(e)
                messagebox.showerror("","Record failed to update")
                conn.rollback()
                conn.close()
                
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
        LeftFrame1.pack(side=TOP,padx=0,pady=0)

        #RightFrame= Frame(leftFrame,bd=5,width=100,height=400,padx=2,pady=4,bg="cadet blue",relief=RIDGE)
        #RightFrame.pack(side=RIGHT,padx=0,pady=0)
        #leftFrame1a=Frame(leftFrame,bd=5,width=500,height=180,padx=2,pady=2,relief=RIDGE)
        #leftFrame1a.grid(side=LEFT,padx=0,pady=0)

        lastFrame = Frame(MainFrame,bd=20,height=100,width=700,relief=RIDGE)
        lastFrame.grid(row =2,column=0,padx=10)


        #=========================creating entry boxes========================================
        self.std_label = Label(LeftFrame1,font=('arial',12,'bold'),text="First Name")
        self.std_label.grid(row=0,column=0)
        self.surname_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Surame")
        self.surname_label.grid(row=1,column=0)


        #student name entry box
        self.std_entry = Entry(LeftFrame1,bd=5,width=44)
        self.std_entry.grid(row=0,column=1)

        self.surname_entry = Entry(LeftFrame1,bd=5,width=44)
        self.surname_entry.grid(row=1,column=1)

        self.id_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Student ID")
        self.id_label.grid(row=2,column=0)
        #id entry box
        self.id_entry = Entry(LeftFrame1,bd=5,width=44)
        self.id_entry.grid(row=2,column=1)


        self.mail_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Email")
        self.mail_label.grid(row=3,column=0)

        self.mail_entry = Entry(LeftFrame1,bd=5,width=44)
        self.mail_entry.grid(row=3,column=1)

        self.address_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Adress")
        self.address_label.grid(row=4,column=0)

        self.address_entry = Entry(LeftFrame1,bd=5,width=44)
        self.address_entry.grid(row=4,column=1)



        self.mob_label = Label(LeftFrame1,font=('arial',12,'bold'),text="Mobile")
        self.mob_label.grid(row=5,column=0)

        self.mobile_entry = Entry(LeftFrame1,bd=5,width=44)
        self.mobile_entry.grid(row=5,column=1)

        self.gender = Label(LeftFrame1,font=('Arial',12,'bold'),text="Gender")
        self.gender.grid(row=6,column=0)
        self.gender_label = ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=39,state='readonly')
        self.gender_label['values']=('','Female','Male')
        self.gender_label.current(0)
        self.gender_label.grid(row=6,column=1)

        #=====================================tables====================================
        scroll_y = Scrollbar(leftFrame,orient=VERTICAL)
        self.student_records=ttk.Treeview(leftFrame,height=12,columns=("StudentID","FirstName","Surname","Address","Mobile","Gender"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side = RIGHT, fill=Y)

        self.student_records.heading("StudentID",text="studentID")
        self.student_records.heading("FirstName",text="Firstname")
        self.student_records.heading("Surname",text="Surname")
        self.student_records.heading("Address",text="Address")
        self.student_records.heading("Mobile",text="Mobile")
        self.student_records.heading("Gender",text="Gender")

        self.student_records['show']='headings'

        self.student_records.column("StudentID",width=120)
        self.student_records.column("FirstName",width=120)
        self.student_records.column("Surname",width=120)
        self.student_records.column("Address",width=120)
        self.student_records.column("Mobile",width=90)
        self.student_records.column("Gender",width=90)

        self.student_records.pack(fill=BOTH,expand=1)
        
        #===============================================================================
        Button(lastFrame,state=ACTIVE,bd=5,text="Add Record",command=addrecord,width=18).grid(row=0,column=0)
        Button(lastFrame,state=ACTIVE,bd=5,text="Delete Record",command=delrecord,width=18).grid(row=0,column=1)
        Button(lastFrame,state=ACTIVE,bd=5,text="Update Record",command=updateRecord,width=18).grid(row=0,column=2)
        Button(lastFrame,state=ACTIVE,bd=5,text="View Record",command=viewrecord,width=18).grid(row=0,column=3)

        global f_name
        f_name = self.std_entry.get()
        global s_name
        s_name = self.surname_entry.get()
        global stid
        stid = self.id_entry.get()
        global mails
        mails = self.mail_entry.get()
        global address
        address = self.address_entry
        global moby
        moby = self.mobile_entry.get()
        global gen
        gen = self.gender_label['values']


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()