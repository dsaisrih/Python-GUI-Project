import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "dsaisriharshit" and password == "12345":
        messagebox.showinfo("Login Success", "Welcome, Student!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Student Login")
root.geometry("300x200")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Login button
tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()