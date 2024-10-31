from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text="View Student Result ", compound=LEFT,
                      font=("goudy old style", 20, "bold"), bg="#FFA500", fg="#262626")
        title.place(x=10, y=15, relwidth=1, height=50)
        
        # Search
        self.var_search = StringVar()
        self.var_id=StringVar()
        lbl_search = Label(self.root, text="Search By Roll No.", font=("goudy old style", 20, "bold"), bg="white")
        lbl_search.place(x=280, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20), bg="lightyellow")
        txt_search.place(x=520, y=100, width=150)
        
        # Search and Clear buttons
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"),
                            bg="#2196f3", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=680, y=100, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),
                           bg="gray", fg="white", cursor="hand2",command=self.clear)
        btn_clear.place(x=800, y=100, width=100, height=35)
        
        # Labels for student information
        lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_roll.place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_name.place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_course.place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_marks.place(x=600, y=230, width=150, height=50)
        lbl_full = Label(self.root, text="Total Marks", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_full.place(x=750, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="Percentage", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_per.place(x=900, y=230, width=150, height=50)
        
        # Dynamic Labels for displaying search results
        self.roll = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)
        self.full = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full.place(x=750, y=280, width=150, height=50)
        self.per = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)
        
        # Delete button
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2",command=self.delete)
        btn_delete.place(x=500, y=350, width=150, height=35)
    
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Please enter roll no.", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row is not None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")
        
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search Student result first", parent=self.root)
                return
            cur.execute("SELECT * FROM result WHERE rid=?", (self.var_id,))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                return  # Exit the function if the course does not exist
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)  # Use askyesno
                if op:  # op will be True if the user clicks 'Yes'
                    cur.execute("DELETE FROM result WHERE rid=?", (self.var_id,))
                    con.commit()
                    messagebox.showinfo("Delete", "result Deleted Successfully", parent=self.root)
                    self.clear()
                    #self.show()  # Optionally refresh the table to reflect the deletion
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
        

if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
