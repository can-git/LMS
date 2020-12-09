import tkinter as tk
from tkinter import ttk

from tkinter import Menu
from CenterScreen import center_screen_geometry
import DatabaseClss.BookDB.db_books as bdb


def Page():
    winAdd = tk.Toplevel()
    winAdd.title("Add a book")
    winAdd.resizable(False, False)
    winAdd.grab_set()

    container = tk.LabelFrame(winAdd)
    container.pack(padx=30, pady=60, fill=tk.BOTH, expand=True)

    lbl_bname = ttk.Label(container, text="Title: ")
    lbl_bname.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    lbl_aname = ttk.Label(container, text="Author: ")
    lbl_aname.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    lbl_cdate = ttk.Label(container, text="Published Date: ")
    lbl_cdate.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
    lbl_dtype = ttk.Label(container, text="Document Type: ")
    lbl_dtype.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)

    bname = tk.StringVar()
    aname = tk.StringVar()
    cdate = tk.IntVar()
    dtype = tk.StringVar()

    txt_bname = ttk.Entry(container, textvariable=bname, width=30)
    txt_bname.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
    txt_aname = ttk.Entry(container, textvariable=aname, width=30)
    txt_aname.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)
    txt_cdate = ttk.Entry(container, textvariable=cdate, width=30)
    txt_cdate.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)
    cmb_dtype = ttk.Combobox(container, textvariable=dtype, state='readonly', width=27)
    cmb_dtype.grid(column=1, row=3, padx=5, pady=5, sticky=tk.E)
    cmb_dtype['values'] = ('Action and Adventure',
                           'Classics',
                           'Comic Book',
                           'Detective and Mystery',
                           'Fantasy',
                           'Historical Fiction',
                           'Horror',
                           'Literary Fiction',
                           'Romance',
                           'Science Fiction',
                           'Short Stories',
                           'Suspense and Thrillers',
                           '''Women's Fiction''',
                           'Biographies and Autobiographies',
                           'Cookbooks',
                           'Essays',
                           'History',
                           'Memoir',
                           'Poetry',
                           'Self-Help',
                           'True Crime')

    def save_handler():
        bdb.insert_book(txt_bname.get(), txt_aname.get(), txt_cdate.get(), cmb_dtype.get())

    def cancel_handler():
        pass

    ttk.Button(container, text="Cancel", command=cancel_handler).grid(column=0, row=4, padx=5, pady=5, sticky=tk.E)
    ttk.Button(container, text="Save", command=save_handler).grid(column=1, row=4, padx=5, pady=5, sticky=tk.E)

    txt_bname.focus()


