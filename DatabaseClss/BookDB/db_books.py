import sqlite3
from tkinter import messagebox as msg
import DatabaseClss.Queries as q


def check_database():
    conn = sqlite3.connect(q.BOOKPATH)
    cur = conn.cursor()
    try:
        cur.execute(q.CHECK)
        if cur.fetchone()[0] == 1:
            return True
    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
        return False
    finally:
        conn.commit()
        conn.close()


def create_database():
    conn = sqlite3.connect(q.BOOKPATH)
    cur = conn.cursor()
    try:
        cur.execute(q.CREATE)
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", str(e))
    finally:
        conn.close()


def list_books():
    conn = sqlite3.connect(q.BOOKPATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SELECT)
        list = cur.fetchall()
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
    finally:
        conn.close()
    return list


def insert_book(bname, aname, cdate, dtype):
    conn = sqlite3.connect(q.BOOKPATH)
    cur = conn.cursor()
    try:
        cur.execute(q.INSERT,
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
