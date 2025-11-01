import tkinter as tk
from tkinter import messagebox, Toplevel

# ---------- Core Logic ----------

def evaluate():
    name = entry_name.get().strip()
    marks = [e.get().strip() for e in entries]

    # Test Case 1: Check all filled
    if not name or any(m == "" for m in marks):
        messagebox.showwarning("Warning", "All fields must be filled!")
        return
    
    # Test Case 2: Validate numeric
    if not all(m.isdigit() for m in marks):
        messagebox.showerror("Error", "Marks must be numbers only!")
        return
    
    marks = [int(m) for m in marks]

    # Test Case 3: Check valid range
    if not all(0 <= m <= 100 for m in marks):
        messagebox.showerror("Error", "Marks must be between 0 and 100!")
        return

    # Test Case 4: Calculate total
    total = sum(marks)

    # Test Case 5: Calculate percentage and grade
    percentage = total / len(marks)
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B" 
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"

    # Test Case 6: Check Pass/Fail
    status = "PASS ✅" if all(m >= 35 for m in marks) else "FAIL ❌"

    # --- POPUP RESULT WINDOW ---
    result_window = Toplevel(root)
    result_window.title("Student Evaluation Result")
    result_window.geometry("400x320")
    result_window.config(bg="#121212")

    tk.Label(result_window, text="📊 Evaluation Result",
             font=("Arial", 15, "bold"), fg="#00FF99", bg="#121212").pack(pady=10)

    result_text = (
        f"Name: {name}\n"
        f"Subjects: {len(marks)}\n"
        f"Total Marks: {total}\n"
        f"Percentage: {percentage:.2f}%\n"
        f"Grade: {grade}\n"
        f"Status: {status}"
    )

    tk.Label(result_window, text=result_text, font=("Consolas", 12),
             fg="white", bg="#121212", justify="left").pack(pady=15)

    close_btn = tk.Button(result_window, text="Close", command=result_window.destroy,
                          font=("Arial", 11, "bold"), bg="#0078D7", fg="white",
                          activebackground="#005A9E", padx=15, pady=5, relief="raised", cursor="hand2")
    close_btn.pack(pady=10)

    # Keep popup on top
    result_window.grab_set()


# ---------- UI Design ----------

root = tk.Tk()
root.title("Student Performance Evaluator")
root.geometry("520x540")
root.config(bg="#1E1E1E")

title = tk.Label(root, text="🎓 Student Performance Evaluator",
                 font=("Arial", 16, "bold"), fg="#00FF99", bg="#1E1E1E")
title.pack(pady=15)

frame = tk.Frame(root, bg="#2D2D2D", bd=3, relief="ridge")
frame.pack(pady=10, padx=20, fill="x")

tk.Label(frame, text="Student Name:", font=("Arial", 12), bg="#2D2D2D", fg="white").pack(pady=5)
entry_name = tk.Entry(frame, font=("Arial", 13), width=30, justify="center")
entry_name.pack(pady=5)

subject_labels = ["Math", "Science", "English", "Computer", "History"]
entries = []

tk.Label(frame, text="Enter Marks (0–100):", font=("Arial", 12, "bold"), bg="#2D2D2D", fg="#00BFFF").pack(pady=5)
for sub in subject_labels:
    tk.Label(frame, text=f"{sub}:", font=("Arial", 11), bg="#2D2D2D", fg="white").pack()
    e = tk.Entry(frame, font=("Arial", 12), justify="center", width=20)
    e.pack(pady=3)
    entries.append(e)

tk.Button(root, text="Evaluate Result", font=("Arial", 12, "bold"),
          bg="#0078D7", fg="white", activebackground="#005A9E",
          command=evaluate, cursor="hand2", padx=10, pady=5).pack(pady=15)

footer = tk.Label(root, text="Tkinter Front-End with 6 Test Cases ",
                  font=("Arial", 9, "italic"), fg="gray", bg="#1E1E1E")
footer.pack(side="bottom", pady=5)

root.mainloop()
