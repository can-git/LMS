import sqlite3
from tkinter import messagebox as msg
from Database import Queries as q

PATH = q.PATH


def check_database():
    conn = None
    try:
        conn = sqlite3.connect(PATH)
        cur = conn.cursor()
        cur.execute(q.CHECKORDERTABLE)
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
        cur.execute(q.CREATEORDERTABLE)
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", str(e))
    finally:
        conn.close()


def list_orders():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SELECTORDERS)
        list = cur.fetchall()
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
    finally:
        conn.close()
    return list


def insert_order(uid, bid, cdate, edate):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.INSERTORDER,
                    {"uid": uid,
                     "bid": bid,
                     "cdate": cdate,
                     "edate": edate})
        conn.commit()
        msg.showinfo("Done", "Order is created.")
        return True
    except Exception as e:
        msg.showinfo("Error", "Error:\n" + str(e))
        return False
    finally:
        conn.close()


def search_orders():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SEARCHORDER)
        list = cur.fetchall()
    except Exception as e:
        msg.showinfo("Error", "Error while searching:\n" + str(e))
    finally:
        conn.commit()
        conn.close()
    return list


def get_userid_by_bookid(bid):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.GETORDERUSERIDBYBOOKID, (bid,))
        word = cur.fetchone()
        if word:
            return word[0]
        else:
            return ""
    except Exception as e:
        msg.showinfo("Error", "Error while searching:\n" + str(e))
    finally:
        conn.commit()
        conn.close()


def delete_order(bid):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.DELETEORDER, (bid,))
        conn.commit()
        msg.showinfo("Done", "The order is deleted.")
        return True
    except Exception as e:
        msg.showinfo("Error", "Error while deleting:\n" + str(e))
        return False
    finally:
        conn.commit()
        conn.close()
