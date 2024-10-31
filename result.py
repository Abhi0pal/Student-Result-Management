from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text=" Add Student Result ", compound=LEFT,
        font=("goudy old style", 20, "bold"), bg="#FFA500", fg="#262626")
        title.place(x=10, y=15,relwidth=1, height=50)
        #widgets
        ##### variable
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list=[]
        self.fetch_roll()
        
        
        lbl_select = Label(self.root, text="Select Student",font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=100) 
        lbl_name = Label(self.root, text="Name",font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=160) 
        lbl_course = Label(self.root, text="Course",font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=220) 
        lbl_marks = Label(self.root, text="Marks Obtained",font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=280) 
        lbl_full_marks = Label(self.root, text="Full Marks",font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=340) 
        
        
        self.txt_student = ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list, font=("goudy old style", 15, "bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=280, y=100,width=200)
        self.txt_student.set("Select")
        
        #btn search
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.search).place(x=500, y=100, width=100, height=28)
        #all Entry Feild
        txt_name = Entry(self.root, textvariable=self.var_name,font=("goudy old style", 20, "bold"), bg="lightyellow",state="readonly").place(x=280, y=160,width=320)
        txt_course = Entry(self.root, textvariable=self.var_course,font=("goudy old style", 20, "bold"), bg="lightyellow",state="readonly").place(x=280, y=220,width=320)
        txt_marks = Entry(self.root, textvariable=self.var_marks,font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=280,width=320)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks,font=("goudy old style",20, "bold"), bg="lightyellow").place(x=280, y=340,width=320)

        #button
        btn_add = Button(self.root, text="Submit", font=("times new roman",15),bg="lightgreen",activebackground="red",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear = Button(self.root, text="Clear", font=("times new roman",15),bg="lightgray",activebackground="yellow",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
        #image
        self.bg_img = Image.open("images/result1.png")
        original_width, original_height = self.bg_img.size
        target_width, target_height = 700, 350
        scale_factor = min(target_width / original_width, target_height / original_height)
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        self.bg_img = self.bg_img.resize((new_width, new_height), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=650 + (target_width - new_width) // 2, y=100 + (target_height - new_height) // 2, width=new_width, height=new_height)

    def fetch_roll(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            # v=[]
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
            # print(v)
            # self.course_list=v
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)  
    
    
    def search(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute(f"SELECT name,course FROM student WHERE roll=?",(self.var_roll.get(),))
            row = cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)  
            
        finally:
            con.close()
    
    
    
    def add(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
                return
            cur.execute("SELECT * FROM result WHERE roll=? and course=?", (self.var_roll.get(),self.var_course.get()))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Result already present", parent=self.root)
                return  # Exit the function if the course already exists
            per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
            cur.execute("INSERT INTO result (roll,name, course, marks_ob,full_marks,per) VALUES (?, ?, ?, ?,?,?)", (
                self.var_roll.get(),
                self.var_name.get(),
                self.var_course.get(),
                self.var_marks.get(),
                self.var_full_marks.get(),
                str(per)
            ))
            con.commit()
            messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)  
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)  
            
        finally:
            con.close()
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()