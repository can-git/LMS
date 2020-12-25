import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from CenterScreen import center_screen_geometry
from AdminPanel import Admin
from pubsub import pub


def Page():
    winAdmin = tk.Toplevel()
    winAdmin.title("Admin Log-In")
    winAdmin.resizable(False, False)
    winAdmin.geometry(center_screen_geometry(screen_width=winAdmin.winfo_screenwidth() + 100,
                                             screen_height=winAdmin.winfo_screenheight(),
                                             window_width=370,
                                             window_height=150))
    winAdmin.grab_set()

    label_name = ttk.Label(winAdmin, text="Name: ")
    label_name.grid(column=0, row=0, padx=15, pady=5)

    name_entry = ttk.Entry(winAdmin, width=30)
    name_entry.grid(column=1, row=0, padx=15, pady=15)

    label_password = ttk.Label(winAdmin, text="Password: ")
    label_password.grid(column=0, row=1, padx=15, pady=5)

    password_entry = ttk.Entry(winAdmin, width=30)
    password_entry.grid(column=1, row=1, padx=15, pady=15)

    def admin_handler():
        if name_entry.get() == "" and password_entry.get() == "":
            winAdmin.destroy()
            pub.sendMessage("Login", arg1="data")

        else:
            msg.showinfo("Failed", "Wrong name or password!")

    def cancel_handler():
        winAdmin.destroy()

    ttk.Button(winAdmin, text="Cancel", command=cancel_handler, width=15).grid(column=0, row=3, padx=5, sticky=tk.E)
    ttk.Button(winAdmin, text="Login", command=admin_handler, width=15).grid(column=1, row=3, sticky=tk.E)

    name_entry.focus()
