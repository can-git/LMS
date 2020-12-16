import tkinter as tk
from pubsub import pub
from CenterScreen import center_screen_geometry
from AdminPanel import Admin
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb
import Database.OrderDB.db_orders as odb


class MyApp(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("LMS")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.btn = tk.Button(self.frame, text="Admin Panel", highlightthickness=0, command=self.openAdminPanel)
        self.btn.pack()

        pub.subscribe(self.listener, "Open Main Panel")  # Listens if this text calls from another page
        self.verifyDatabases()

    # region Some Important Methods
    def listener(self, arg1, arg2=None):
        self.show()

    def openAdminPanel(self):
        root.withdraw()
        subFrame = Admin()

    def show(self):
        root.update()
        root.deiconify()

    def verifyDatabases(self):
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
