import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from pubsub import pub
from tkinter import Menu
from CenterScreen import center_screen_geometry
from Pages import AddBook as AB, OrderBook as OB, UserEdit as US
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb


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
        self.button4 = tk.Button(self, text="Ordering", command=OrderPage)
        self.button4.grid(column=0, row=4, padx=15, pady=15)

        self.label_ctg = tk.Label(self, text="Categories:")
        self.label_ctg.grid(column=1, row=0, padx=2, pady=15)

        self.BookTitle = ttk.Combobox(self, width=12)
        self.BookTitle.grid(column=2, row=0, padx=2, pady=15)

        self.BookSearch = tk.Entry(self, width=50)
        self.BookSearch.grid(column=3, row=0, padx=5, pady=15)

        self.btn_Search = tk.Button(self, text="Search")
        self.btn_Search.grid(column=4, row=0, padx=5, pady=15)

        self.BookList = scrolledtext.ScrolledText(self, width=70, height=20, wrap=tk.WORD)
        self.BookList.grid(column=1, row=1, columnspan=5, rowspan=7)

        print(bdb.list_books())
        print(udb.list_users())
        pub.subscribe(self.listener, "Open Admin Panel")

    # region Some Important Methods
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
    pass


def UserPage():
    US.Page()


def OrderPage():
    OB.Page()
# endregion
