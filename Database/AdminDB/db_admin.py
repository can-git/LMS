import sqlite3
from tkinter import messagebox as msg
from Database import Queries as q

PATH = q.PATH


def check_database():
    conn = None
    try:
        conn = sqlite3.connect(PATH)
        cur = conn.cursor()
        cur.execute(q.CHECKADMINTABLE)
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
        cur.execute(q.CREATEADMINTABLE)
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", str(e))
    finally:
        conn.close()


def insert_admin(aname, apassword):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.INSERTADMIN,
                    {"aname": aname,
                     "apassword": apassword
                     })
        conn.commit()
    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
    finally:
        conn.close()


def search_admin(aname, apassword):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SEARCHADMIN, (aname, apassword,))
        list = cur.fetchall()
    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
    finally:
        conn.commit()
        conn.close()
    return list
