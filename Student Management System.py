import tkinter as tk
import sqlite3 as lite
from tkinter import messagebox as msgbox




master = tk.Tk() 
master.title("Student Management")

master.geometry("700x250") 


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)

def connection():
        con = lite.connect('students.db')
        with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS student(Name TEXT,Batch TEXT,Roll TEXT,Mark1 INT,Mark2 INT,Mark3 INT)")
                con.commit()

def insert_data():
        conn = lite.connect('students.db')
        with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO student(Name,Batch,Roll,Mark1,Mark2,Mark3) VALUES(?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()))
                conn.commit()
        msgbox.showinfo("SUCCESS","Data Successfully Inserted")
def update_data():
        conn = lite.connect('students.db')
        with conn:
                cur = conn.cursor()
                cur.execute("UPDATE student SET Name=?,Batch=?,Roll=?,Mark1=?,Mark2=?,Mark3=? WHERE Name=?",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e1.get()))
                conn.commit()
                msgbox.showinfo("SUCCESS", "Data Successfully Updated")
def delete_data():
        fname = e1.get()
        conn = lite.connect('students.db')
        with conn:
                cur = conn.cursor()
                cur.execute("delete from student WHERE Name = '" + fname + "';")
                conn.commit()
                msgbox.showinfo("SUCCESS", "Data Successfully Deleted")
def clear():
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')
        e4.delete(0, 'end')
        e5.delete(0, 'end')
        e6.delete(0, 'end')
        tk.Label(master, text ="").grid(row=7, column=4)



    
def display():
        avg=(int(e4.get())+int(e5.get())+int(e6.get()))/3
        if(avg>=90.0):
                tk.Label(master, text ="A").grid(row=7, column=4)
        elif(avg>=75.0 and avg<90.0):
                tk.Label(master, text ="B").grid(row=7, column=4)
        elif(avg>=60.0 and avg<75.0):
                tk.Label(master, text ="C").grid(row=7, column=4)
        elif(avg>=45.0 and avg<60.0):
                tk.Label(master, text ="D").grid(row=7, column=4)
        else:
                tk.Label(master, text ="F").grid(row=7, column=4)
    
connection()
tk.Label(master, text="Name").grid(row=0, column=0)
tk.Label(master, text="Roll.No").grid(row=0, column=3)
tk.Label(master, text="Batch").grid(row=1, column=0) 

tk.Label(master, text="Sr.No").grid(row=2, column=0) 
tk.Label(master, text="1").grid(row=3, column=0)
tk.Label(master, text="2").grid(row=4, column=0)
tk.Label(master, text="3").grid(row=5, column=0)

tk.Label(master, text="Subject").grid(row=2, column=1) 
tk.Label(master, text="Maths").grid(row=3, column=1)
tk.Label(master, text="Science").grid(row=4, column=1)
tk.Label(master, text="Computer").grid(row=5, column=1)

tk.Label(master, text="Marks").grid(row=2, column=2) 
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)

tk.Label(master, text="Grade").grid(row=7, column=3)

e1=tk.Entry(master) 
e2=tk.Entry(master)
e3=tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)

def search():
        fname = e1.get()
        conn = lite.connect('students.db')
        cursor = conn.execute("SELECT * from student WHERE Name = '" + fname + "';")
        conn.commit()
        for row in cursor:
                e2.insert(0, row[1])
                e3.insert(0, row[2])
                e4.insert(0, row[3])
                e5.insert(0, row[4])
                e6.insert(0, row[5])
        conn.close()

tk.Button(master, text="Insert", height=2, width=13, command=lambda:[display(),insert_data(),clear()]).grid(row=8, column=1)
tk.Button(master, text="Update", height=2, width=13, command=lambda:[update_data(),clear()]).grid(row=8, column=2)
tk.Button(master, text="Delete", height=2, width=13, command=lambda:[delete_data(),clear()]).grid(row=8, column=3)
tk.Button(master, text="Search", height=2, width=13, command=lambda:[search(),display()]).grid(row=8, column=4)


 
master.mainloop()


