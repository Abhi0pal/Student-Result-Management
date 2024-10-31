from tkinter import *
from tkinter import messagebox
import sqlite3



class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("500x450")
        self.root.configure(bg="#E8F6EF")
        
        # Initialize Database
        # init_db()
        
        # Aesthetic Frame for login
        login_frame = Frame(self.root, bg="#C1E1C1", bd=5, relief=RIDGE)
        login_frame.place(x=80, y=50, width=340, height=320)
        
        # Title Label
        title = Label(login_frame, text="Login", font=("Helvetica", 20, "bold"), bg="#C1E1C1", fg="#34495E")
        title.place(x=130, y=20)
        
        # Username Label and Entry
        lbl_user = Label(login_frame, text="Username", font=("Arial", 12, "bold"), bg="#C1E1C1", fg="#34495E")
        lbl_user.place(x=50, y=80)
        self.txt_user = Entry(login_frame, font=("Arial", 12), bg="#F7F9F9")
        self.txt_user.place(x=50, y=110, width=220)
        
        # Password Label and Entry
        lbl_pass = Label(login_frame, text="Password", font=("Arial", 12, "bold"), bg="#C1E1C1", fg="#34495E")
        lbl_pass.place(x=50, y=150)
        self.txt_pass = Entry(login_frame, font=("Arial", 12), bg="#F7F9F9", show="*")
        self.txt_pass.place(x=50, y=180, width=220)
        
        # Login Button
        btn_login = Button(login_frame, text="Login", command=self.login_function, font=("Arial", 12, "bold"),
                           bg="#34495E", fg="white", cursor="hand2")
        btn_login.place(x=50, y=230, width=220)
        
        # Forgot Password Button
        btn_forgot = Button(login_frame, text="Forgot Password?", command=self.forgot_password_window,
                            font=("Arial", 10), bg="#C1E1C1", fg="#2980B9", bd=0, cursor="hand2")
        btn_forgot.place(x=100, y=270)
    
    def login_function(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        
        # Check login credentials with SQLite
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            messagebox.showinfo("Success", "Login Successful")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
    
    def forgot_password_window(self):
        # Window for Forgot Password
        self.new_win = Toplevel(self.root)
        self.new_win.title("Forgot Password")
        self.new_win.geometry("400x200")
        self.new_win.configure(bg="#E8F6EF")
        
        # Label and Entry for email
        lbl_email = Label(self.new_win, text="Enter your Email", font=("Arial", 12, "bold"), bg="#E8F6EF", fg="#34495E")
        lbl_email.pack(pady=20)
        self.txt_email = Entry(self.new_win, font=("Arial", 12), bg="#F7F9F9")
        self.txt_email.pack(pady=5, fill=X, padx=50)
        
        # Reset Password Button
        btn_reset = Button(self.new_win, text="Reset Password", command=self.reset_password_function, font=("Arial", 12, "bold"),
                           bg="#34495E", fg="white", cursor="hand2")
        btn_reset.pack(pady=20)
    
    def reset_password_function(self):
        email = self.txt_email.get()
        
        # Check if email exists in database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            messagebox.showinfo("Reset Password", "Password reset link sent to your email")
            self.new_win.destroy()
        else:
            messagebox.showerror("Error", "Email not found")

# Main Function
root = Tk()
obj = login(root)
root.mainloop()
