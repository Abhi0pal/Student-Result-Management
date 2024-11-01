from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text="Manage Course Details", compound=LEFT,
        font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15,relwidth=1, height=35)
        
        # Variable
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
     
        # Widgets
        lbl_courseName = Label(self.root, text="Course Name",font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_courseDuration = Label(self.root, text="Duration",font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_courseCharges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_courseDescription = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        #Entry Fields
        self.txt_courseName = Entry(self.root, textvariable=self.var_course,font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_courseName.place(x=150, y=60,width=200)
        
        txt_courseDuration = Entry(self.root,textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100,width=200)
        
        txt_courseCharges = Entry(self.root,textvariable=self.var_charges, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140,width=200)
        
        self.txt_courseDescription = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_courseDescription.place(x=150, y=180,width=500,height=130)
        # Button
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add).place(x=150, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update).place(x=270, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete).place(x=390, y=400, width=110, height=40)
        self.btn_add = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear).place(x=510, y=400, width=110, height=40)
        #Search Panel
        self.var_search=StringVar()
        lbl_search_courseName = Label(self.root, text="Course Name",font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search,font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60,width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)
        #content
        self.C_Frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        
        # Set Scroll Bar
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        # Treeview widget with scroll commands linked
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "decription"),
        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        # Pack scrollbars after linking them
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("decription",text="Decription")
        #this is help to remove Extra spance int the starting 
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=60)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("decription",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #self.CourseTable.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
         ##########################################3
    def search(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute(f"SELECT * FROM course WHERE name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row) 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)  
            
        finally:
            con.close()
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_courseDescription.delete(1.0,END)
        self.txt_courseName.config(state=NORMAL)
    
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
                return
            cur.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Select Course From List", parent=self.root)
                return  # Exit the function if the course does not exist
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)  # Use askyesno
                if op:  # op will be True if the user clicks 'Yes'
                    cur.execute("DELETE FROM course WHERE name=?", (self.var_course.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Course Deleted Successfully", parent=self.root)
                    self.clear()
                    self.show()  # Optionally refresh the table to reflect the deletion
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

            
        
        
        
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        # print(row) 
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_courseDescription.delete(1.0,END)
        self.txt_courseDescription.insert(END,row[4])
    def add(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
                return
            cur.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Course Name already present", parent=self.root)
                return  # Exit the function if the course already exists
            cur.execute("INSERT INTO COURSE (name, duration, charges, description) VALUES (?, ?, ?, ?)", (
                self.var_course.get(),
                self.var_duration.get(),
                self.var_charges.get(),
                self.txt_courseDescription.get("1.0", END)
            ))
            con.commit()
            messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)  
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)  
            
        finally:
            con.close()
    def update(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
                return
            cur.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Select Course From List", parent=self.root)
                return  # Exit the function if the course already exists
            cur.execute("UPDATE COURSE SET duration=?, charges=?, description=? WHERE name=?", (
                self.var_duration.get(),
                self.var_charges.get(),
                self.txt_courseDescription.get("1.0", END),
                self.var_course.get()
            ))

            con.commit()
            messagebox.showinfo("Success", "Course Update Successfully", parent=self.root)  
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)  
            
        finally:
            con.close()
            
            
            
    def show(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row) 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)  
            
        finally:
            con.close()

    
    
    
    
    
    


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()