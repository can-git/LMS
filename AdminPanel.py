import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from pubsub import pub
from tkinter import Menu
from CenterScreen import center_screen_geometry
from Pages import AddBook as AB, OrderBook as OB, UserEdit as US, EditBook as EB
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb
import Database.OrderDB.db_orders as odb


class Admin(tk.Toplevel):
    def __init__(self):

        tk.Toplevel.__init__(self)
        self.geometry(center_screen_geometry(screen_width=self.winfo_screenwidth(),
                                             screen_height=self.winfo_screenheight(),
                                             window_width=750,
                                             window_height=400))
        self.title("LMS -- Admin Panel")

        self.button1 = tk.Button(self, text="Add Book", command=AddBookPage)
        self.button1.grid(column=0, row=1, padx=15, pady=15)
        self.button2 = tk.Button(self, text="Edit Book", command=EditBookPage)
        self.button2.grid(column=0, row=2, padx=15, pady=15)
        self.button3 = tk.Button(self, text="User Add Edit", command=UserPage)
        self.button3.grid(column=0, row=3, padx=15, pady=15)
        self.button4 = tk.Button(self, text="Order", command=OrderPage)
        self.button4.grid(column=0, row=4, padx=15, pady=15)
        self.button5 = tk.Button(self, text="Main Screen", command=self.onClose)
        self.button5.grid(column=0, row=5, padx=15, pady=15)

        self.label_ctg = tk.Label(self, text="Categories:")
        self.label_ctg.grid(column=1, row=0, padx=2, pady=15)

        self.Title = ttk.Combobox(self, width=12)
        self.Title.grid(column=2, row=0, padx=2, pady=15)
        self.Title['values'] = (
            "Users", "Books", "Orders"
        )

        self.BookSearch = tk.Entry(self, width=50)
        self.BookSearch.grid(column=3, row=0, padx=5, pady=15)

        self.btn_Search = tk.Button(self, text="Search", command=self.search)
        self.btn_Search.grid(column=4, row=0, padx=5, pady=15)

        container = tk.LabelFrame(self, width=640, height=400)
        container.grid(column=1, row=1, columnspan=7, rowspan=7, sticky=tk.W)

        self.treeU = ttk.Treeview(container, selectmode='browse')
        self.treeU.grid(column=1, row=1, columnspan=7, rowspan=7, sticky=tk.W)
        self.treeB = ttk.Treeview(container, selectmode='browse')
        self.treeB.grid(column=1, row=1, columnspan=7, rowspan=7, sticky=tk.W)
        self.treeO = ttk.Treeview(container, selectmode='browse')
        self.treeO.grid(column=1, row=1, columnspan=7, rowspan=7, sticky=tk.W)

        self.vsb = ttk.Scrollbar(container, orient="vertical", command=self.treeU.yview)
        self.vsb.grid(column=7, row=1, rowspan=7, sticky=tk.S + tk.E + tk.N)
        self.treeU.configure(yscrollcommand=self.vsb.set)

        self.vsb2 = ttk.Scrollbar(container, orient="vertical", command=self.treeB.yview)
        self.vsb2.grid(column=7, row=1, rowspan=7, sticky=tk.S + tk.E + tk.N)
        self.treeB.configure(yscrollcommand=self.vsb2.set)

        self.vsb3 = ttk.Scrollbar(container, orient="vertical", command=self.treeO.yview)
        self.vsb3.grid(column=7, row=1, rowspan=7, sticky=tk.S + tk.E + tk.N)
        self.treeO.configure(yscrollcommand=self.vsb3.set)

        pub.subscribe(self.listener, "Open Admin Panel")
        self.Title.bind("<<ComboboxSelected>>", lambda _: self.change_table(self.Title.get()))

        self.change_table("Books")
        self.Title.current(1)
        self.search()

    # region Some Important Methods
    def search(self):
        if self.Title.get() == "Users":
            self.searchbyU(self.BookSearch.get())
        elif self.Title.get() == "Books":
            self.searchbyB(self.BookSearch.get())
        elif self.Title.get() == "Orders":
            self.searchbyO(self.BookSearch.get())

    def searchbyU(self, word):
        list = udb.list_users()
        self.remove_tree(self.treeU)
        for i in list:
            if word == "" or word == " ":
                self.treeU.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
                continue
            for ch in i:
                if word in str(ch):
                    self.treeU.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
                    break

    def searchbyB(self, word):
        list = bdb.list_books()
        self.remove_tree(self.treeB)
        for i in list:
            if word == "" or word == " ":
                self.treeB.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
                continue
            for ch in i:
                if word in str(ch):
                    self.treeB.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
                    break

    def searchbyO(self, word):
        list = odb.search_orders()
        self.remove_tree(self.treeO)
        for i in list:
            if word == "" or word == " ":
                self.treeO.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6]))
                continue
            for ch in i:
                if word in str(ch):
                    self.treeO.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6]))
                    break

    def remove_tree(self, tree):
        x = tree.get_children()
        if x != '()':
            for child in x:
                tree.delete(child)

    def change_table(self, c):
        self.treeO.grid_forget()
        self.treeU.grid_forget()
        self.treeB.grid_forget()
        self.vsb.grid_forget()
        self.vsb2.grid_forget()
        self.vsb3.grid_forget()
        self.remove_tree(self.treeB)
        self.remove_tree(self.treeU)
        self.remove_tree(self.treeO)

        if c == "Users":
            self.treeU.grid(column=1, row=1, columnspan=7, rowspan=7, sticky=tk.W)
            self.vsb.grid(column=7, row=1, rowspan=7, sticky=tk.S + tk.E + tk.N)
            self.treeU['columns'] = ("one", "two", "three", "four", "five")
            self.treeU.column('#0', width=40, stretch=tk.NO)
            self.treeU.column('one', width=100, stretch=tk.NO)
            self.treeU.column('two', width=100, stretch=tk.NO)
            self.treeU.column('three', width=90, stretch=tk.NO)
            self.treeU.column('four', width=145, stretch=tk.NO)
            self.treeU.column('five', width=145, stretch=tk.NO)
            self.treeU.heading('#0', text="ID", anchor=tk.W)
            self.treeU.heading('one', text="Name", anchor=tk.W)
            self.treeU.heading('two', text="Surname", anchor=tk.W)
            self.treeU.heading('three', text="Phone", anchor=tk.W)
            self.treeU.heading('four', text="Mail", anchor=tk.W)
            self.treeU.heading('five', text="Created Date", anchor=tk.W)
        elif c == "Books":
            self.treeB.grid(column=1, row=1, columnspan=7, rowspan=7, sticky=tk.W)
            self.vsb2.grid(column=7, row=1, rowspan=7, sticky=tk.S + tk.E + tk.N)
            self.treeB['columns'] = ("one", "two", "three", "four", "five")
            self.treeB.column('#0', width=40, stretch=tk.NO)
            self.treeB.column('one', width=130, stretch=tk.NO)
            self.treeB.column('two', width=130, stretch=tk.NO)
            self.treeB.column('three', width=120, stretch=tk.NO)
            self.treeB.column('four', width=100, stretch=tk.NO)
            self.treeB.column('five', width=100, stretch=tk.NO)
            self.treeB.heading('#0', text="ID", anchor=tk.W)
            self.treeB.heading('one', text="Title", anchor=tk.W)
            self.treeB.heading('two', text="Author Name", anchor=tk.W)
            self.treeB.heading('three', text="Created Date", anchor=tk.W)
            self.treeB.heading('four', text="Type", anchor=tk.W)
            self.treeB.heading('five', text="State", anchor=tk.W)
        elif c == "Orders":
            self.treeO.grid(column=1, row=1, columnspan=7, rowspan=7, sticky=tk.W)
            self.vsb3.grid(column=7, row=1, rowspan=7, sticky=tk.S + tk.E + tk.N)
            self.treeO['columns'] = ("one", "two", "three", "four", "five", "six")
            self.treeO.column('#0', width=40, stretch=tk.NO)
            self.treeO.column('one', width=100, stretch=tk.NO)
            self.treeO.column('two', width=100, stretch=tk.NO)
            self.treeO.column('three', width=100, stretch=tk.NO)
            self.treeO.column('four', width=120, stretch=tk.NO)
            self.treeO.column('five', width=80, stretch=tk.NO)
            self.treeO.column('six', width=80, stretch=tk.NO)
            self.treeO.heading('#0', text="ID", anchor=tk.W)
            self.treeO.heading('one', text="User Name", anchor=tk.W)
            self.treeO.heading('two', text="User Surname", anchor=tk.W)
            self.treeO.heading('three', text="Book Title", anchor=tk.W)
            self.treeO.heading('four', text="Author Name", anchor=tk.W)
            self.treeO.heading('five', text="Created Date", anchor=tk.W)
            self.treeO.heading('six', text="End Date", anchor=tk.W)
        self.search()

    def onClose(self):
        self.destroy()
        pub.sendMessage("Open Main Panel", arg1="data")

    def listener(self, arg1, arg2=None):
        self.show()

    def openFrame(self):
        self.withdraw()
        # subFrame = OtherFrame2()

    def show(self):
        self.update()
        self.deiconify()
    # endregion


# region Pages
def AddBookPage():
    AB.Page()


def EditBookPage():
    EB.Page()


def UserPage():
    US.Page()


def OrderPage():
    OB.Page()
# endregion
