import tkinter as tk
from tkinter import ttk

from tkinter import Menu
from CenterScreen import center_screen_geometry
import DatabaseClss.BookDB.db_books as bdb


def Page():
    winTake = tk.Toplevel()
    winTake.title("Take the book")
    winTake.geometry(center_screen_geometry(screen_width=winTake.winfo_screenwidth() + 100,
                                            screen_height=winTake.winfo_screenheight(),
                                            window_width=800,
                                            window_height=600))
    winTake.resizable(False, False)
    winTake.grab_set()
    label = ttk.Label(winTake, text="Take the book")
    label.grid(row=0, column=4, padx=10, pady=10)
