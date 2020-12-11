import sqlite3
from tkinter import messagebox as msg
from Database import Queries as q

PATH = q.PATH


def check_database():
    conn = None
    try:
        conn = sqlite3.connect(PATH)
        cur = conn.cursor()
        cur.execute(q.CHECKBOOKSTABLE)
        if cur.fetchone()[0] == 1:
            return True
        else:
            return False
    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
        return False
    finally:
        conn.commit()
        conn.close()


def create_database():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.CREATEBOOKSTABLE)
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", str(e))
    finally:
        conn.close()


def list_books():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SELECTBOOKS)
        list = cur.fetchall()
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
    finally:
        conn.close()
    return list


def insert_book(bname, aname, cdate, dtype):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.INSERTBOOKS,
                    {"bname": bname,
                     "aname": aname,
                     "cdate": cdate,
                     "dtype": dtype,
                     "state": True
                     })
        conn.commit()
        msg.showinfo("Done", "Books saved.")
    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
    finally:
        conn.close()
