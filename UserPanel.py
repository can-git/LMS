import tkinter as tk
from pubsub import pub
from CenterScreen import center_screen_geometry
from AdminPanel import Admin
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb
import Database.OrderDB.db_orders as odb
from Pages import AdminEntry as AE
from tkinter import messagebox as msg


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
            self.fillBooks()
        if not odb.check_database():
            odb.create_database()
        if not udb.check_database():
            udb.create_database()
            self.fillUsers()

    def fillBooks(self):
        bdb.insert_book_silence("Uygarligin Ayak Izleri", "Celil Sadik", 1940, "History")

    def fillUsers(self):
        udb.insert_user_silence("can", "yilmaz", 5073022302, "canyil97@hotmail.com", 21)
        udb.insert_user_silence("tugce", "can", 5453022301, "safsafsa@hotmail.com", 12)
        udb.insert_user_silence("atakan", "alperen", 5073024533, "asdsadsa@gmail.com", 10)

    def AdminEntryPage(self):
        AE.Page()

    # def admin_handler(self):
    #     if self.name_entry.get() == "Ati" and self.password_entry.get() == "123321":
    #         msg.showinfo("", "Admin entry successful")
    #
    #     else:
    #          msg.showerror("Error", "Wrong name or password")

    # endregion


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(center_screen_geometry(screen_width=root.winfo_screenwidth(),
                                         screen_height=root.winfo_screenheight(),
                                         window_width=800,
                                         window_height=600))
    app = MyApp(root)
    root.mainloop()
