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


def insert_book_silence(bname, aname, cdate, dtype):
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
    except Exception as e:
        msg.showinfo("Error", "Filling database is not complated:\n" + str(e))
    finally:
        conn.close()


def search_books(word):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SEARCHBOOK, (word, word, word, word,))
        list = cur.fetchall()
    except Exception as e:
        msg.showinfo("Error", "Error while searching:\n" + str(e))
    finally:
        conn.commit()
        conn.close()
    return list


def search_books2(word):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SEARCHBOOK2, (word, word, word, word,))
        list = cur.fetchall()
    except Exception as e:
        msg.showinfo("Error", "Error while searching:\n" + str(e))
    finally:
        conn.commit()
        conn.close()
    return list


def delete_book(id):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.DELETEBOOK, (id,))
        conn.commit()
        msg.showinfo("Done", "The book is deleted.")
    except Exception as e:
        msg.showinfo("Error", "Error while deleting:\n" + str(e))
        return None
    finally:
        conn.commit()
        conn.close()


def edit_book_state(state, bid):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.EDITBOOKSTATE, (state, bid))

    except Exception as e:
        msg.showinfo("Error", "Error while editing:\n" + str(e))
    finally:
        conn.commit()
        conn.close()


def edit_book(bname, aname, cdate, dtype, id):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.EDITBOOK, (bname, aname, cdate, dtype, id))
        msg.showinfo("Done", "The book is changed.")

    except Exception as e:
        msg.showinfo("Error", "Error while editing:\n" + str(e))
    finally:
        conn.commit()
        conn.close()
