import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg


def Page():
    winAdmin = tk.Tk()
    winAdmin.title("Admin Entry")
    winAdmin.resizable(False, False)
    winAdmin.geometry("250x150+650+300")
    winAdmin.grab_set()

    label_name = ttk.Label(winAdmin, text="Name: ")
    label_name.grid(column=0, row=0, padx=25, pady=5)

    name_entry = ttk.Entry(winAdmin, width=15)
    name_entry.grid(column=1, row=0, padx=25, pady=15)

    label_password = ttk.Label(winAdmin, text="Password: ")
    label_password.grid(column=0, row=1, padx=25, pady=5)

    password_entry = ttk.Entry(winAdmin, width=15)
    password_entry.grid(column=1, row=1, padx=25, pady=15)

    def admin_handler():
        if name_entry.get() == "Ati" and password_entry.get() == "123321":
            msg.showinfo("", "Admin entry successful")

        else:
             msg.showerror("Error", "Wrong name or password")

    def cancel_handler():
        winAdmin.destroy()

    ttk.Button(winAdmin, text="Cancel", command=cancel_handler).grid(column=0, row=3, padx=10, pady=10)
    ttk.Button(winAdmin, text="Login", command=admin_handler).grid(column=1, row=3)
