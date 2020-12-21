import tkinter as tk
from tkinter import ttk

from CenterScreen import center_screen_geometry


def Page():
    winOrder = tk.Toplevel()
    winOrder.title("Taking / Giving")
    winOrder.geometry(center_screen_geometry(screen_width=winOrder.winfo_screenwidth() + 100,
                                             screen_height=winOrder.winfo_screenheight(),
                                             window_width=380,
                                             window_height=240))
    winOrder.resizable(False, False)
    winOrder.grab_set()

    container = tk.LabelFrame(winOrder)
    container.pack(padx=5, pady=10, fill=tk.BOTH, expand=True)

    lbl_book = ttk.Label(container, text="Book: ")
    lbl_book.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    lbl_title = ttk.Label(container, text="Title: ")
    lbl_title.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    lbl_author = ttk.Label(container, text="Author: ")
    lbl_author.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)

    var = tk.IntVar()
    rb_take = tk.Radiobutton(container, text="Taking", variable=var, value=1)
    rb_take.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
    rb_give = tk.Radiobutton(container, text="Giving", variable=var, value=2)
    rb_give.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W)

    lbl_user = ttk.Label(container, text="User: ")
    lbl_user.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

    book = tk.StringVar()
    title = tk.StringVar()
    author = tk.StringVar()
    user = tk.StringVar()

    txt_book = ttk.Entry(container, textvariable=book, width=30)
    txt_book.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
    txt_title = ttk.Entry(container, textvariable=title, width=30)
    txt_title.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)
    txt_author = ttk.Entry(container, textvariable=author, width=30)
    txt_author.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)
    txt_user = ttk.Entry(container, textvariable=user, width=30)
    txt_user.grid(column=1, row=4, padx=5, pady=5, sticky=tk.E)

    def searchB_handler():
        pass

    def searchU_handler():
        pass

    def save_handler():
        pass

    def cancel_handler():
        winOrder.destroy()

    ttk.Button(container, text="Search", command=searchB_handler).grid(column=2, row=0, padx=5, pady=5, sticky=tk.E)
    ttk.Button(container, text="Search", command=searchU_handler).grid(column=2, row=4, padx=5, pady=5, sticky=tk.E)
    ttk.Button(container, text="Save", command=save_handler).grid(column=2, row=6, padx=5, pady=5, sticky=tk.E)
    ttk.Button(container, text="Cancel", command=cancel_handler).grid(column=1, row=6, padx=5, pady=5, sticky=tk.E)

    txt_book.focus()
