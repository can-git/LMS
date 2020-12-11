import tkinter as tk
from pubsub import pub
from CenterScreen import center_screen_geometry
from AdminPanel import Admin
from UserPanel import User
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb
import Database.OrderDB.db_orders as odb


class MyApp(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("LMS")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        verifyDatabases()

        btn = tk.Button(self.frame, text="Admin Panel", command=openAdminPanel)
        btn.pack()
        btn2 = tk.Button(self.frame, text="User Panel", command=openUserPanel)
        btn2.pack()
        pub.subscribe(listener, "Open Main Panel")


# region Some Important Methods
def listener(arg1, arg2=None):
    show()


def hide():
    root.withdraw()


def openAdminPanel():
    hide()
    subFrame = Admin()


def openUserPanel():
    hide()
    subFrame2 = User()


def show():
    root.update()
    root.deiconify()


def verifyDatabases():
    if not bdb.check_database():
        bdb.create_database()
    if not odb.check_database():
        odb.create_database()
    if not udb.check_database():
        udb.create_database()
# endregion


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(center_screen_geometry(screen_width=root.winfo_screenwidth(),
                                         screen_height=root.winfo_screenheight(),
                                         window_width=800,
                                         window_height=600))
    app = MyApp(root)
    root.mainloop()
