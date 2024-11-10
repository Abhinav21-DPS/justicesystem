import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Justice System")
window.geometry("400x400")
cases = []

def add_case():
    case_id = entry_case_id.get()
    offense = entry_offense.get()
    accused = entry_accused.get()
    status = entry_status.get()

    if case_id and offense and accused and status:
        case_details = {
            "Case ID": case_id,
            "Offense": offense,
            "Accused": accused,
            "Status": status
        }
        cases.append(case_details)
        update_case_list()
        clear_entries()
        messagebox.showinfo("Success", "Case added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")
def clear_entries():
    entry_case_id.delete(0, tk.END)
    entry_offense.delete(0, tk.END)
    entry_accused.delete(0, tk.END)
    entry_status.delete(0, tk.END)
def update_case_list():
    listbox_cases.delete(0, tk.END)
    for case in cases:
        case_text = f"ID: {case['Case ID']} | Offense: {case['Offense']} | Accused: {case['Accused']} | Status: {case['Status']}"
        listbox_cases.insert(tk.END, case_text)
tk.Label(window, text="Case ID:").pack()
entry_case_id = tk.Entry(window)
entry_case_id.pack()

tk.Label(window, text="Offense:").pack()
entry_offense = tk.Entry(window)
entry_offense.pack()

tk.Label(window, text="Accused:").pack()
entry_accused = tk.Entry(window)
entry_accused.pack()

tk.Label(window, text="Status:").pack()
entry_status = tk.Entry(window)
entry_status.pack()

button_add = tk.Button(window, text="Add Case", command=add_case)
button_add.pack(pady=10)

tk.Label(window, text="Case List:").pack()
listbox_cases = tk.Listbox(window, width=50, height=10)
listbox_cases.pack()

window.mainloop()
