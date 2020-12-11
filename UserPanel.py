import tkinter as tk
from pubsub import pub
from tkinter import Menu
from CenterScreen import center_screen_geometry
from Pages import AddBook as AB, TakeBook as TB, GiveBook as GB


class User(tk.Toplevel):
    def __init__(self):

        tk.Toplevel.__init__(self)
        self.geometry(center_screen_geometry(screen_width=self.winfo_screenwidth(),
                                             screen_height=self.winfo_screenheight(),
                                             window_width=800,
                                             window_height=600))
        self.title("LMS -- User Panel")
        pub.subscribe(self.listener, "Open User Panel")

        btn = tk.Button(self, text="Exit", command=self.onClose)
        btn.pack()

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


