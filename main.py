import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from centerscreen import center_screen_geometry


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

        for F in (AdminPanelPage, Frame1, Frame2):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AdminPanelPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class AdminPanelPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menu_bar = Menu(controller)
        controller.config(menu=menu_bar)

        # Creating a menu and add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Add", command=AddBookPage)
        file_menu.add_command(label="Edit", command=EditBookPage)

        order_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Order", menu=order_menu)
        # file_menu.add_command(label="Take the book", command=lambda: controller.show_frame(Frame1))
        # file_menu.add_command(label="Give a book", command=lambda: controller.show_frame(Frame2))
        order_menu.add_command(label="Take", command=TakeBookPage)
        order_menu.add_command(label="Give", command=GiveBookPage)


def TakeBookPage():
    winTake = tk.Toplevel()
    winTake.title("Take the book")
    winTake.geometry(center_screen_geometry(screen_width=winTake.winfo_screenwidth()+100,
                                            screen_height=winTake.winfo_screenheight(),
                                            window_width=800,
                                            window_height=600))
    winTake.resizable(False, False)
    winTake.grab_set()
    label = ttk.Label(winTake, text="Take the book")
    label.grid(row=0, column=4, padx=10, pady=10)


def GiveBookPage():
    winGive = tk.Toplevel()
    winGive.title("Give a book")
    winGive.geometry(center_screen_geometry(screen_width=winGive.winfo_screenwidth()+100,
                                            screen_height=winGive.winfo_screenheight(),
                                            window_width=800,
                                            window_height=600))
    winGive.resizable(False, False)
    winGive.grab_set()
    label = ttk.Label(winGive, text="Give a book")
    label.grid(row=0, column=4, padx=10, pady=10)


def AddBookPage():
    pass


def EditBookPage():
    pass


class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Take the book")
        label.grid(row=0, column=4, padx=10, pady=10)


class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Give a book")
        label.grid(row=0, column=4, padx=10, pady=10)


app = tkinterApp()
app.mainloop()
