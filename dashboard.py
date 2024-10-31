from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Load the image for the icon
        self.logo_dash = ImageTk.PhotoImage(file="images/logo.png")

        # Title
        title = Label(self.root, text="Student Result Management System", compound=LEFT,
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # MenuBar
         # MenuBar
        M_Frame = LabelFrame(self.root, text="Menu", font=("times new roman", 15), bg="white")
        M_Frame.place(x=5, y=70, width=1340, height=80)
        
        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_course.place(x=20, y=5, width=200, height=40)
        
        btn_Student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_student)
        btn_Student.place(x=230, y=5, width=200, height=40)
        
        btn_Result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_result)
        btn_Result.place(x=440, y=5, width=200, height=40)
        
        btn_View = Button(M_Frame, text="View", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_report)
        btn_View.place(x=650, y=5, width=200, height=40)
        
        btn_Logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_Logout.place(x=860, y=5, width=200, height=40)
        
        btn_Exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2")
        btn_Exit.place(x=1070, y=5, width=200, height=40)

        # Buttons
        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=5, width=200, height=40)
        
        # Add remaining buttons similarly...

        # Content window background image
        self.bg_img = Image.open("images/bg.jpg")
        original_width, original_height = self.bg_img.size
        target_width, target_height = 920, 350
        scale_factor = min(target_width / original_width, target_height / original_height)
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        self.bg_img = self.bg_img.resize((new_width, new_height), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400 + (target_width - new_width) // 2, y=180 + (target_height - new_height) // 2, width=new_width, height=new_height)

        # Details section
        self.lbl_course = Label(self.root, text="Total Courses\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#E6E6FA", fg="#4B0082")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Student\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#87CEFA", fg="#191970")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Result\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#FFDAB9", fg="#8B4513")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # Footer
        footer = Label(self.root, text="SRMS - Student Result Management System\nContact Us for any Technical Issue: 730XXX3049",
                       font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill="x")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)
        
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
