import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb
import Database.OrderDB.db_orders as odb
from CenterScreen import center_screen_geometry
import DtypeDictionary as dtypeD


def Page():
    winAdd = tk.Toplevel()
    winAdd.title("Edit Book")
    winAdd.resizable(False, False)
    winAdd.grab_set()
    winAdd.geometry(center_screen_geometry(screen_width=winAdd.winfo_screenwidth() + 100,
                                           screen_height=winAdd.winfo_screenheight(),
                                           window_width=430,
                                           window_height=300))

    booklist = []
    templist = []
    bookindex = 0

    container = tk.LabelFrame(winAdd)
    container.pack(padx=5, pady=10, fill=tk.BOTH, expand=True)

    #Labels
    lbl_ename = ttk.Label(container, text="Book: ")
    lbl_ename.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    lbl_bname = ttk.Label(container, text="Title: ")
    lbl_bname.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    lbl_aname = ttk.Label(container, text="Author: ")
    lbl_aname.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
    lbl_cdate = ttk.Label(container, text="Published Date: ")
    lbl_cdate.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
    lbl_dtype = ttk.Label(container, text="Document Type: ")
    lbl_dtype.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

    bname = tk.StringVar()
    aname = tk.StringVar()
    cdate = tk.IntVar()
    dtype = tk.StringVar()
    ename = tk.StringVar()

    # Entry widgets and Combobox
    cmb_books = ttk.Combobox(container, textvariable=ename, width=27)
    cmb_books.grid(column=1, row=0, padx=10, pady=20, sticky=tk.W)
    txt_bname = ttk.Entry(container, textvariable=bname, width=30)
    txt_bname.grid(column=1, row=1, padx=10, pady=6, sticky=tk.W)
    txt_aname = ttk.Entry(container, textvariable=aname, width=30)
    txt_aname.grid(column=1, row=2, padx=10, pady=6, sticky=tk.E)
    txt_cdate = ttk.Entry(container, textvariable=cdate, width=30)
    txt_cdate.grid(column=1, row=3, padx=10, pady=6, sticky=tk.E)
    cmb_dtype = ttk.Combobox(container, textvariable=dtype, state='readonly', width=27)
    cmb_dtype.grid(column=1, row=4, padx=11, pady=6, sticky=tk.E)
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

    # For searching the database for the specified book.
    def clear_text():
        nonlocal cmb_dtype
        txt_bname.delete(0, tk.END)
        txt_aname.delete(0, tk.END)
        txt_cdate.delete(0, tk.END)
        cmb_dtype.delete(0, tk.END)

    def clear_combo_text():
        nonlocal booklist, templist, cmb_books
        booklist = []
        templist = []
        cmb_books['values'] = ['']

    def fill_text(index):
        nonlocal bookindex
        bookindex = booklist[index][0]
        clear_text()
        txt_bname.insert(0, booklist[index][1])
        txt_aname.insert(0, booklist[index][2])
        txt_cdate.insert(0, booklist[index][3])
        cmb_dtype.current(booklist[index][4])

    def search_handler():
        nonlocal booklist, templist, cmb_books
        clear_combo_text()
        for i in bdb.search_books(ename.get()):
            booklist.append(i)
            templist.append(i[1] + " / " + i[2])
        cmb_books['values'] = templist

    # For saving the changed properties.
    def save_handler():
        nonlocal bookindex
        bdb.edit_book(txt_bname.get(), txt_aname.get(), txt_cdate.get(), dtypeD.get_book.get(cmb_dtype.get()), bookindex)

    def delete_handler():
        nonlocal bookindex
        bdb.delete_book(bookindex)
        clear_combo_text()
        clear_text()

    def cancel_handler():
        winAdd.destroy()

    # Buttons
    ttk.Button(container, text="Cancel", command=cancel_handler).grid(column=0, row=6, padx=40, pady=25, columnspan=2, sticky=tk.W)
    ttk.Button(container, text="Save", command=save_handler).grid(column=2, row=6, padx=0, pady=25, sticky=tk.W)
    ttk.Button(container, text="Delete", command=delete_handler).grid(column=1, row=6, padx=5, pady=5, sticky=tk.W)
    ttk.Button(container, text="Search", command=search_handler).grid(column=2, row=0, padx=0, pady=20, sticky=tk.W)

    cmb_books.focus()
    cmb_books.bind("<<ComboboxSelected>>", lambda _: fill_text(cmb_books.current()))



