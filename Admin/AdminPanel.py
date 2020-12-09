import tkinter as tk
from tkinter import ttk

from tkinter import Menu
from CenterScreen import center_screen_geometry
import DatabaseClss.BookDB.db_books as bdb
from Admin import AddBook as AB, GiveBook as GB, TakeBook as TB


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(center_screen_geometry(screen_width=self.winfo_screenwidth(),
                                             screen_height=self.winfo_screenheight(),
                                             window_width=800,
                                             window_height=600))
        self.resizable(False, False)
        self.title("Admin Panel")

        # creating a container
        container = tk.Frame(self)
        container.pack(side="left", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (AdminPanelFrame, Frame1, Frame2):  # THE FRAME NAME SHOULD BE ADDED IN THIS LINE /1
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AdminPanelFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# region Frames section
# Frames let you to change the frame and this does not open a new window
class AdminPanelFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menu_bar = Menu(controller)
        controller.config(menu=menu_bar)

        # CREATING A MENU
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Add", command=AddBookPage)
        file_menu.add_command(label="Edit", command=EditBookPage)
        # FRAMES WILL BE PLACED LIKE THE EXAMPLES, THE OTHERS ARE PAGES /2
        # file_menu.add_command(label="Take the book", command=lambda: controller.show_frame(Frame1)) #EXAMPLE FRAME
        # file_menu.add_command(label="Give a book", command=lambda: controller.show_frame(Frame2)) #EXAMPLE FRAME

        order_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Order", menu=order_menu)
        order_menu.add_command(label="Take", command=TakeBookPage)
        order_menu.add_command(label="Give", command=GiveBookPage)

        # CHECKS IF THERE IS A DATABASE FILE
        if not bdb.check_database():
            bdb.create_database()

        refresh_list()


class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Take the book") # example kodes
        label.grid(row=0, column=4, padx=10, pady=10)


class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Give a book") # example kodes
        label.grid(row=0, column=4, padx=10, pady=10)


# endregion


# region Pages section
# Pages let you to start a new window
def TakeBookPage():
    TB.Page()


def GiveBookPage():
    GB.Page()


def AddBookPage():
    AB.Page()


def EditBookPage():
    pass


# endregion


def refresh_list():
    print(bdb.list_books())


app = tkinterApp()
app.mainloop()
