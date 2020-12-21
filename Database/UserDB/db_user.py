import os
import sqlite3
from tkinter import messagebox as msg
from Database import Queries as q

PATH = q.PATH


def check_database():
    conn = sqlite3.connect(os.path.realpath(PATH))
    cur = conn.cursor()
    try:
        cur.execute(q.CHECKUSERSTABLE)
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
        cur.execute(q.CREATEUSERTABLE)
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", "Error while creating database:\n" + str(e))
    finally:
        conn.close()


def list_users():
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SELECTUSERS)
        list = cur.fetchall()
        conn.commit()

    except Exception as e:
        msg.showinfo("Error", "Error while selecting:\n" + str(e))
    finally:
        conn.close()
    return list


def check_user(name, surname):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.CHECKUSER, (name, surname,))
        c = cur.fetchone()
        if not c == (0,):  # if there is a value
            return True
        else:
            return False  # if there is no such value
    except Exception as e:
        msg.showinfo("Error", "Error while checking:\n" + str(e))
        return None
    finally:
        conn.commit()
        conn.close()


def delete_user(id):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.DELETEUSER, (id,))
        conn.commit()
        msg.showinfo("Done", "The user is deleted.")
    except Exception as e:
        msg.showinfo("Error", "Error while deleting:\n" + str(e))
        return None
    finally:
        conn.commit()
        conn.close()


def search_users(word):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    list = []
    try:
        cur.execute(q.SEARCHUSER, (word, word, word, word,))
        list = cur.fetchall()
    except Exception as e:
        msg.showinfo("Error", "Error while searching:\n" + str(e))
    finally:
        conn.commit()
        conn.close()
    return list


def insert_user(uname, usurname, phone, mail):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.INSERTUSER,
                    {"uname": uname,
                     "usurname": usurname,
                     "phone": phone,
                     "mail": mail,
                     "cdate": 0
                     })
        conn.commit()
        msg.showinfo("Done", "The user is added.")
    except Exception as e:
        msg.showinfo("Error", "Error while adding:\n" + str(e))
    finally:
        conn.close()


def edit_user(uname, usurname, phone, mail, id):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.EDITUSER,(uname, usurname, phone, mail, id))
        msg.showinfo("Done", "The user is changed.")

    except Exception as e:
        msg.showinfo("Error", "Error while editing:\n" + str(e))
    finally:
        conn.commit()
        conn.close()


def insert_user_silence(uname, usurname, phone, mail, cdate):
    conn = sqlite3.connect(PATH)
    cur = conn.cursor()
    try:
        cur.execute(q.INSERTUSER,
                    {"uname": uname,
                     "usurname": usurname,
                     "phone": phone,
                     "mail": mail,
                     "cdate": cdate
                     })
        conn.commit()
    except Exception as e:
        msg.showinfo("Error", "Error while adding:\n" + str(e))
    finally:
        conn.close()
