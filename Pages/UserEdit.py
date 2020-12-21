import tkinter as tk
from tkinter import ttk

from CenterScreen import center_screen_geometry
import Database.UserDB.db_user as udb


def Page():
    winUser = tk.Toplevel()
    winUser.title("User Add/Edit/Remove")
    winUser.geometry(center_screen_geometry(screen_width=winUser.winfo_screenwidth() + 100,
                                            screen_height=winUser.winfo_screenheight(),
                                            window_width=400,
                                            window_height=230))
    winUser.resizable(False, False)
    winUser.grab_set()

    userlist=[]
    templist=[]
    userindex = 0

    container = tk.LabelFrame(winUser)
    container.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    lbl_user = ttk.Label(container, text="User: ")
    lbl_user.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    lbl_uname = ttk.Label(container, text="User Name: ")
    lbl_uname.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    lbl_usurname = ttk.Label(container, text="User Surname: ")
    lbl_usurname.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
    lbl_uphone = ttk.Label(container, text="Phone: ")
    lbl_uphone.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
    lbl_umail = ttk.Label(container, text="Mail: ")
    lbl_umail.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

    user = tk.StringVar()
    uname = tk.StringVar()
    usurname = tk.StringVar()
    phone = tk.IntVar()
    mail = tk.StringVar()

    cmb_users = ttk.Combobox(container, textvariable=user, width=27)
    cmb_users.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
    txt_uname = ttk.Entry(container, textvariable=uname, width=30)
    txt_uname.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)
    txt_usurname = ttk.Entry(container, textvariable=usurname, width=30)
    txt_usurname.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)
    txt_phone = ttk.Entry(container, textvariable=phone, width=30)
    txt_phone.grid(column=1, row=3, padx=5, pady=5, sticky=tk.E)
    txt_mail = ttk.Entry(container, textvariable=mail, width=30)
    txt_mail.grid(column=1, row=4, padx=5, pady=5, sticky=tk.E)

    def clear_text():
        txt_usurname.delete(0, tk.END)
        txt_uname.delete(0, tk.END)
        txt_mail.delete(0, tk.END)
        txt_phone.delete(0, tk.END)

    def clear_combo_text():
        nonlocal userlist, templist, cmb_users
        userlist = []
        templist = []
        cmb_users['values'] = ['']

    def fill_text(index):
        nonlocal userindex
        userindex = userlist[index][0]
        clear_text()
        txt_uname.insert(0, userlist[index][1])
        txt_usurname.insert(0, userlist[index][2])
        txt_phone.insert(0, userlist[index][3])
        txt_mail.insert(0, userlist[index][4])

    def search_handler():
        nonlocal userlist, templist, cmb_users
        clear_combo_text()
        for i in udb.search_users(user.get()):
            userlist.append(i)
            templist.append(i[1] + " " + i[2] + " " + str(i[3]))
        cmb_users['values'] = templist

    def cancel_handler():
        winUser.destroy()

    def delete_handler():
        nonlocal userindex
        udb.delete_user(userindex)
        clear_combo_text()
        clear_text()

    def save_handler():
        nonlocal userindex
        if udb.check_user(txt_uname.get(), txt_usurname.get()):
            udb.edit_user(txt_uname.get(), txt_usurname.get(), txt_phone.get(), txt_mail.get(), userindex)
        elif not udb.check_user(txt_uname.get(), txt_usurname.get()):
            udb.insert_user(txt_uname.get(), txt_usurname.get(), txt_phone.get(), txt_mail.get())

    ttk.Button(container, text="Search", command=search_handler).grid(column=2, row=0, padx=5, pady=5, sticky=tk.E)
    ttk.Button(container, text="Cancel", command=cancel_handler).grid(column=0, row=5, padx=5, pady=5, sticky=tk.E)
    ttk.Button(container, text="Delete", command=delete_handler).grid(column=1, row=5, padx=5, pady=5, sticky=tk.E)
    ttk.Button(container, text="Save", command=save_handler).grid(column=2, row=5, padx=5, pady=5, sticky=tk.E)

    cmb_users.focus()
    cmb_users.bind("<<ComboboxSelected>>", lambda _: fill_text(cmb_users.current()))
