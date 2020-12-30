import tkinter as tk
from tkinter import ttk
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb
import Database.OrderDB.db_orders as odb
from CenterScreen import center_screen_geometry
from tkinter import messagebox as msg
import DtypeDictionary as dtype
from pubsub import pub


def Page():
    winOrder = tk.Toplevel()
    winOrder.title("Order")
    winOrder.geometry(center_screen_geometry(screen_width=winOrder.winfo_screenwidth() + 100,
                                             screen_height=winOrder.winfo_screenheight(),
                                             window_width=400,
                                             window_height=250))
    winOrder.resizable(False, False)
    winOrder.grab_set()

    tab_parent = ttk.Notebook(winOrder)
    tabGive = ttk.Frame(tab_parent)
    tabTake = ttk.Frame(tab_parent)
    tab_parent.add(tabGive, text="Giving")
    tab_parent.add(tabTake, text="Taking")
    tab_parent.pack(expand=1, fill='both')

    # region TabGiving
    # region Initials
    Gbooklist = []
    Gtemplist = []
    Gbookindex = 0
    Guserlist = []
    Gtemplist2 = []
    Guserindex = 0
    # endregion

    contGive = tk.LabelFrame(tabGive)
    contGive.pack(padx=5, pady=10, fill=tk.BOTH, expand=True)

    lbl_bookG = ttk.Label(contGive, text="Book: ")
    lbl_bookG.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    lbl_titleG = ttk.Label(contGive, text="Title: ")
    lbl_titleG.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    lbl_authorG = ttk.Label(contGive, text="Author: ")
    lbl_authorG.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
    lbl_givenmonthG = ttk.Label(contGive, text="Given Month: ")
    lbl_givenmonthG.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
    lbl_userG = ttk.Label(contGive, text="User: ")
    lbl_userG.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

    def callback1(index, value, op):
        nonlocal Guserindex
        if not userG.get():
            Guserindex = 0

    bookG = tk.StringVar()
    titleG = tk.StringVar()
    authorG = tk.StringVar()
    givenmonthG = tk.StringVar()
    untilmonthG = tk.StringVar()
    userG = tk.StringVar()
    userG.trace_add('write', callback1)

    cmb_bookG = ttk.Combobox(contGive, textvariable=bookG, width=28)
    cmb_bookG.grid(column=1, row=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
    txt_titleG = ttk.Entry(contGive, textvariable=titleG, width=30, state=tk.DISABLED)
    txt_titleG.grid(column=1, row=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
    txt_authorG = ttk.Entry(contGive, textvariable=authorG, width=30, state=tk.DISABLED)
    txt_authorG.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky=tk.W)
    cmb_given_monthG = ttk.Combobox(contGive, textvariable=givenmonthG, width=12)
    cmb_given_monthG.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W)
    cmb_given_monthG['values'] = list(dtype.get_month_by_id.values())
    cmb_given_monthG.current(0)
    txt_untilmonthG = tk.Entry(contGive, textvariable=untilmonthG, width=13, state=tk.DISABLED)
    txt_untilmonthG.grid(column=2, row=3, padx=0, pady=5, sticky=tk.W)
    cmb_userG = ttk.Combobox(contGive, textvariable=userG, width=28)
    cmb_userG.grid(column=1, row=4, columnspan=2, padx=5, pady=5, sticky=tk.W)

    def clear_combo_textG():
        nonlocal Gbooklist, Gtemplist
        Gbooklist = []
        Gtemplist = []
        userG.set("")

    def clear_combo_textG2():
        nonlocal Guserlist, Gtemplist2
        Guserlist = []
        Gtemplist2 = []

    def clear_text_bookG():
        titleG.set("")
        authorG.set("")

    def fill_month_taken(index):
        if not index == 11:
            untilmonthG.set(dtype.get_month_by_id.get(index + 1))
        else:
            untilmonthG.set(dtype.get_month_by_id.get(0))

    def fill_textG(index):
        nonlocal Gbookindex
        Gbookindex = Gbooklist[index][0]
        clear_text_bookG()
        titleG.set(Gbooklist[index][1])
        authorG.set(Gbooklist[index][2])

    def fill_textG2(index):
        nonlocal Guserindex
        Guserindex = Guserlist[index][0]

    def searchB_handlerG():
        nonlocal Gbooklist, Gtemplist, cmb_bookG
        clear_combo_textG()
        for i in bdb.search_books(bookG.get()):
            Gbooklist.append(i)
            Gtemplist.append(i[1] + " / " + i[2])
        cmb_bookG['values'] = Gtemplist

    def searchU_handlerG():
        nonlocal Guserlist, Gtemplist2, cmb_userG, userG
        clear_combo_textG2()

        for i in udb.search_users(userG.get()):
            Guserlist.append(i)
            Gtemplist2.append(i[1] + " / " + i[2])
        cmb_userG['values'] = Gtemplist2

    def save_handlerG():
        nonlocal Gbookindex, Guserindex
        if Gbookindex == 0 or Guserindex == 0:
            msg.showinfo("Error", "Unknown book or user")
        else:
            if odb.insert_order(Guserindex, Gbookindex, cmb_given_monthG.current(), dtype.get_month_by_name[txt_untilmonthG.get()]):
                bdb.edit_book_state(False, Gbookindex)
                clear_text_bookG()
                clear_combo_textG()
                bookG.set("")
                Gbookindex = 0
                Guserindex = 0
                pub.sendMessage("reload_data", arg1="data")
                searchB_handlerG()
                searchU_handlerG()


    def cancel_handler():
        winOrder.destroy()
    # endregion

    # region TabTaking
    # region Initials
    Tbooklist = []
    Ttemplist = []
    Tbookindex = 0
    Tuserlist = []
    Ttemplist2 = []
    Tuserindex = 0
    # endregion
    contTake = tk.LabelFrame(tabTake)
    contTake.pack(padx=5, pady=10, fill=tk.BOTH, expand=True)

    lbl_bookT = ttk.Label(contTake, text="Book: ")
    lbl_bookT.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    lbl_titleT = ttk.Label(contTake, text="Title: ")
    lbl_titleT.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    lbl_authorT = ttk.Label(contTake, text="Author: ")
    lbl_authorT.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)

    lbl_userT = ttk.Label(contTake, text="User: ")
    lbl_userT.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

    bookT = tk.StringVar()
    titleT = tk.StringVar()
    authorT = tk.StringVar()
    userT = tk.StringVar()

    cmb_bookT = ttk.Combobox(contTake, textvariable=bookT, width=30)
    cmb_bookT.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
    txt_titleT = ttk.Entry(contTake, textvariable=titleT, width=30, state=tk.DISABLED)
    txt_titleT.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)
    txt_authorT = ttk.Entry(contTake, textvariable=authorT, width=30, state=tk.DISABLED)
    txt_authorT.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)
    txt_userT = ttk.Entry(contTake, textvariable=userT, width=30, state=tk.DISABLED)
    txt_userT.grid(column=1, row=4, padx=5, pady=5, sticky=tk.E)


    def clear_combo_textT():
        nonlocal Tbooklist, Ttemplist, cmb_bookT
        Tbooklist.clear()
        Ttemplist.clear()
        cmb_bookT.delete(0, tk.END)
        cmb_bookT['values'] = ['']
        bookT.set("")

    def clear_text_bookT():
        titleT.set("")
        authorT.set("")
        userT.set("")

    def fill_textT(index):
        nonlocal Tbookindex
        Tbookindex = Tbooklist[index][0]
        clear_text_bookT()
        titleT.set(Tbooklist[index][1])
        authorT.set(Tbooklist[index][2])
        searchU_T(Tbookindex)

    def searchB_handlerT():
        nonlocal Tbooklist, Ttemplist, cmb_bookT
        clear_combo_textT()
        for i in bdb.search_books2(bookT.get()):
            Tbooklist.append(i)
            Ttemplist.append(i[1] + " / " + i[2])
        cmb_bookT['values'] = Ttemplist

    def searchU_T(bookID):
        txt_userT.delete(0, tk.END)
        if odb.get_userid_by_bookid(bookID):
            userID = odb.get_userid_by_bookid(bookID)
            btnSave.config(state=tk.NORMAL)
            word = udb.search_user(userID)
            userT.set(word[1] + " " + word[2])
        else:
            btnSave.config(state=tk.DISABLED)
            userT.set("")

    def save_handlerT():
        nonlocal Tbookindex, Tuserindex
        if Tbookindex == 0:
            msg.showinfo("Error", "Unknown book")
        else:
            if odb.delete_order(Tbookindex):
                bdb.edit_book_state(True, Tbookindex)
                clear_text_bookT()
                Tbookindex = 0
                Tuserindex = 0
                clear_combo_textT()
                pub.sendMessage("reload_data", arg1="data")
                searchB_handlerT()

    def cancel_handler2():
        winOrder.destroy()
    # endregion

    ttk.Button(contGive, text="Search", command=searchB_handlerG).grid(column=3, row=0, padx=0, pady=5, sticky=tk.E)
    ttk.Button(contGive, text="Search", command=searchU_handlerG).grid(column=3, row=4, padx=0, pady=5, sticky=tk.E)
    ttk.Button(contGive, text="Save", command=save_handlerG).grid(column=3, row=6, padx=5, pady=5, sticky=tk.E)
    ttk.Button(contGive, text="Cancel", command=cancel_handler).grid(column=2, row=6, padx=5, pady=5, sticky=tk.E)

    ttk.Button(contTake, text="Search", command=searchB_handlerT).grid(column=2, row=0, padx=5, pady=5, sticky=tk.E)
    btnSave = ttk.Button(contTake, text="Save", command=save_handlerT)
    btnSave.grid(column=2, row=6, padx=5, pady=5, sticky=tk.E)
    ttk.Button(contTake, text="Cancel", command=cancel_handler2).grid(column=1, row=6, padx=5, pady=5, sticky=tk.E)

    cmb_bookG.focus()
    cmb_bookG.bind("<<ComboboxSelected>>", lambda _: fill_textG(cmb_bookG.current()))
    cmb_userG.bind("<<ComboboxSelected>>", lambda _: fill_textG2(cmb_userG.current()))
    cmb_given_monthG.bind("<<ComboboxSelected>>", lambda _: fill_month_taken(cmb_given_monthG.current()))
    cmb_bookT.focus()
    cmb_bookT.bind("<<ComboboxSelected>>", lambda _: fill_textT(cmb_bookT.current()))

    searchU_handlerG()
    searchB_handlerG()
    searchB_handlerT()
