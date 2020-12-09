import tkinter as tk
from tkinter import ttk

from tkinter import Menu
from CenterScreen import center_screen_geometry
import DatabaseClss.BookDB.db_books as bdb


def Page():
    winGive = tk.Toplevel()
    winGive.title("Give a book")
    winGive.geometry(center_screen_geometry(screen_width=winGive.winfo_screenwidth() + 100,
                                            screen_height=winGive.winfo_screenheight(),
                                            window_width=800,
                                            window_height=600))
    winGive.resizable(False, False)
    winGive.grab_set()
    label = ttk.Label(winGive, text="Give a book")
    label.grid(row=0, column=4, padx=10, pady=10)
