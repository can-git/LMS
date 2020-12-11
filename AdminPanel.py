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

        print(bdb.list_books())
        menu_bar = Menu(self)
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Add", command=AddBookPage)
        file_menu.add_command(label="Edit", command=EditBookPage)

        order_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Order", menu=order_menu)
        order_menu.add_command(label="Take", command=TakeBookPage)
        order_menu.add_command(label="Give", command=GiveBookPage)

        exit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Exit", menu=exit_menu)
        exit_menu.add_command(label="Exit", command=self.onClose)

        self.config(menu=menu_bar)

        pub.subscribe(self.listener, "Open Admin Panel")

    # region Some Important Methods
    def onClose(self):
        self.destroy()
        pub.sendMessage("Open Main Panel", arg1="data")

    def listener(self, arg1, arg2=None):
        self.show()

    def hide(self):
        self.withdraw()

    def openFrame(self):
        self.hide()
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
# endregion
