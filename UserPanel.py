import tkinter as tk
from tkinter import ttk
from pubsub import pub
from CenterScreen import center_screen_geometry
from AdminPanel import Admin
import Database.BookDB.db_books as bdb
import Database.UserDB.db_user as udb
import Database.OrderDB.db_orders as odb
from Pages import AdminEntry as AE
import DtypeDictionary as dtype


class MyApp(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("LMS")
        self.root.resizable(False,False)
        self.frame = tk.Frame(parent, bg="peach puff", highlightbackground="peach puff")
        self.frame.place(x=110, y=60)

        lbl_book = ttk.Label(self.frame, text="Book: ")
        lbl_book.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.sname = tk.StringVar()

        self.ent = tk.Entry(self.frame, textvariable=self.sname, width=60)
        self.ent.grid(column=1, row=0, padx=1, pady=5, sticky=tk.W)

        self.btn_search = tk.Button(self.frame, text="Search", width=20, command=self.fill_table_rows)
        self.btn_search.grid(column=2, row=0, padx=5, pady=5, sticky=tk.W)

        self.btn_admin = tk.Button(self.frame, text="Admin Login", highlightthickness=0, bg="white", command=self.openAdminPanel)
        self.btn_admin.grid(column=2, row=5, padx=5, pady=5, sticky=tk.E)

        # Table
        self.tree = ttk.Treeview(self.frame, height=20, selectmode='browse')
        self.tree.grid(column=0, row=1, padx=5, pady=5, columnspan=3, rowspan=3, sticky=tk.W)
        # Scrollbar of Table
        self.vsb = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.vsb.grid(column=3, row=1, rowspan=3, sticky=tk.S + tk.E + tk.N)
        self.tree.configure(yscrollcommand=self.vsb.set)

        pub.subscribe(self.listener, "Open Main Panel")  # Listens if this text calls from another page
        pub.subscribe(self.openAdminPanel, "Login")

        self.verifyDatabases()
        self.fill_table_columns()
        self.fill_table_rows()

    # region Some Important Methods
    def fill_table_rows(self):
        list = bdb.list_books()
        self.remove_tree(self.tree)
        for i in list:
            if self.sname.get() == "" or self.sname.get() == " ":
                self.tree.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], dtype.set_book.get(i[4]), self.change_status(i[5])))
                continue
            for ch in i:
                if self.sname.get() in str(ch):
                    self.tree.insert("", 'end', text=i[0], values=(i[1], i[2], i[3], dtype.set_book.get(i[4]), self.change_status(i[5])))
                    break

    def change_status(self, num):
        if num == 0:
            return "NOT OKEY"
        else:
            return "OKEY"

    def fill_table_columns(self):
        self.tree['columns'] = ("one", "two", "three", "four", "five")
        self.tree.column('#0', width=40, stretch=tk.NO)
        self.tree.column('one', width=120, stretch=tk.NO)
        self.tree.column('two', width=120, stretch=tk.NO)
        self.tree.column('three', width=90, stretch=tk.NO)
        self.tree.column('four', width=125, stretch=tk.NO)
        self.tree.column('five', width=125, stretch=tk.NO)
        self.tree.heading('#0', text="ID", anchor=tk.W)
        self.tree.heading('one', text="Title", anchor=tk.W)
        self.tree.heading('two', text="Author Name", anchor=tk.W)
        self.tree.heading('three', text="Created Date", anchor=tk.W)
        self.tree.heading('four', text="Category", anchor=tk.W)
        self.tree.heading('five', text="Status", anchor=tk.W)

        self.fill_table_rows()

    def remove_tree(self, tree):
        x = tree.get_children()
        if x != '()':
            for child in x:
                tree.delete(child)

    def listener(self, arg1, arg2=None):
        self.show()

    def openAdminPanel(self,):
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
        bdb.insert_book_silence("uygarligin ayak izleri", "celil sadik", 1940, 1)
        bdb.insert_book_silence("türklerle beraber", "emre sarıl", 2018, 1)
        bdb.insert_book_silence("sevgili wanda", "gephart hauptman", 1999, 1)
        bdb.insert_book_silence("kuyucakli yusuf", "sabahattin ali", 1999, 1)
        bdb.insert_book_silence("beyaz geceler", "fyodor dostoyevski", 1999, 1)
        bdb.insert_book_silence("palto", "nikolay gogol", 1999, 1)
        bdb.insert_book_silence("dokuzuncu harbiye kogusu", "peyafi safa", 1999, 1)
        bdb.insert_book_silence("vurun kahpeye", "halide edip adivar", 1999, 1)
        bdb.insert_book_silence("yilanlarin ocu", "fakir baykurt", 1999, 1)
        bdb.insert_book_silence("gulyabani", "huseyin rahmi gunpinar", 1999, 1)
        bdb.insert_book_silence("esir sehrin insanlari", "kemal tahir", 1999, 1)
        bdb.insert_book_silence("maviye boyanmis sular", "cemil kavukcu", 1999, 1)
        bdb.insert_book_silence("insanciklar", "fyodor dostoyevski", 1999, 1)
        bdb.insert_book_silence("mai ve siyah", "halit ziya usakligil", 1999, 1)
        bdb.insert_book_silence("istanbul hatirasi", "ahmet umit", 1999, 1)
        bdb.insert_book_silence("devlet ana", "kemal tahir", 1999, 1)
        bdb.insert_book_silence("fosforlu cevriye", "suat dervis", 1999, 1)
        bdb.insert_book_silence("fatih harbiye", "peyami safa", 1999, 1)

    def fillUsers(self):
        udb.insert_user_silence("can", "yilmaz", 5073022302, "canyil97@hotmail.com", 21)
        udb.insert_user_silence("ozlem", "acar", 5453022301, "safsafsa@hotmail.com", 12)
        udb.insert_user_silence("ozde", "acarkan", 5073024533, "asdsadsa@gmail.com", 10)
        udb.insert_user_silence("atahan", "adanir", 5073524533, "dfsf@gmail.com", 10)
        udb.insert_user_silence("mehmet", "adiguzel", 5073064533, "asdsafsdag@gmail.com", 10)
        udb.insert_user_silence("bestami", "agnar", 5074024533, "xcvxcvxc@gmail.com", 10)
        udb.insert_user_silence("aslan", "ahmet", 5073124533, "nghnhg@gmail.com", 10)
        udb.insert_user_silence("sennur", "agca", 5043024533, "asdsadsa@htyh.com", 10)
        udb.insert_user_silence("tutkum", "akarcali", 5173024533, "yhthty@gmail.com", 10)
        udb.insert_user_silence("nuhaydar", "akay", 5873024533, "utyuty@gmail.com", 10)
        udb.insert_user_silence("servet", "akca", 5073624533, "dfgdfhdf@gmail.com", 10)

    def AdminEntryPage(self):
        AE.Page()
    # endregion


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(center_screen_geometry(screen_width=root.winfo_screenwidth(),
                                         screen_height=root.winfo_screenheight(),
                                         window_width=800,
                                         window_height=600))
    bgImage = tk.PhotoImage(file="bg.png")
    bg = tk.Label(image=bgImage)
    bg.pack()
    app = MyApp(root)
    root.mainloop()
