import tkinter as tk
from pubsub import pub
from tkinter import Menu
from CenterScreen import center_screen_geometry
from Pages import AddBook as AB, TakeBook as TB, GiveBook as GB
import Database.BookDB.db_books as bdb


class Admin(tk.Toplevel):
    def __init__(self):

        tk.Toplevel.__init__(self)
        self.geometry(center_screen_geometry(screen_width=self.winfo_screenwidth(),
                                             screen_height=self.winfo_screenheight(),
                                             window_width=800,
                                             window_height=600))
        self.title("LMS -- Admin Panel")

        # MENUBAR
        self.menu_bar = Menu(self)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Add Book", command=AddBookPage)
        self.file_menu.add_command(label="Edit Book", command=EditBookPage)
        self.file_menu.add_command(label="Add/Edit User", command=UserPage)
        self.order_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Order", menu=self.order_menu)
        self.order_menu.add_command(label="Taking", command=TakeBookPage)
        self.order_menu.add_command(label="Giving", command=GiveBookPage)
        self.exit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Exit", menu=self.exit_menu)
        self.exit_menu.add_command(label="Exit", command=self.onClose)
        self.config(menu=self.menu_bar)

        print(bdb.list_books())
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
def TakeBookPage():
    TB.Page()


def GiveBookPage():
    GB.Page()


def AddBookPage():
    AB.Page()


def EditBookPage():
    pass


def UserPage():
    pass
# endregion
