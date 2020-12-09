

BOOKPATH = "DatabaseClss/BookDB/LMS.db"

CHECK = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Books'"""

SELECT = "SELECT * FROM Books"

CREATE = """CREATE TABLE Books(grid INTEGER PRIMARY KEY AUTOINCREMENT, bname TEXT, aname TEXT, 
cdate INT, dtype TEXT, state BOOL);"""

INSERT = "INSERT INTO Books (bname, aname, cdate, dtype, state) VALUES(:bname, :aname, :cdate, :dtype, :state)"
