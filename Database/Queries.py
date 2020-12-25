
PATH = "LMS.db"

# region Books
CHECKBOOKSTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Books'"""

SELECTBOOKS = "SELECT * FROM Books"

CREATEBOOKSTABLE = """CREATE TABLE Books(bid INTEGER PRIMARY KEY AUTOINCREMENT, bname TEXT, aname TEXT, 
cdate INT, dtype INT, state BOOL);"""

INSERTBOOKS = "INSERT INTO Books (bname, aname, cdate, dtype, state) VALUES(:bname, :aname, :cdate, :dtype, :state)"

SEARCHBOOK = "SELECT * FROM Books WHERE (bname LIKE '%'||?||'%' " \
             "OR aname LIKE '%'||?||'%' OR cdate LIKE '%'||?||'%' OR dtype LIKE '%'||?||'%') AND state = TRUE"

SEARCHBOOK2 = "SELECT * FROM Books WHERE (bname LIKE '%'||?||'%' " \
             "OR aname LIKE '%'||?||'%' OR cdate LIKE '%'||?||'%' OR dtype LIKE '%'||?||'%') AND state = FALSE"

EDITBOOK = "UPDATE Books SET bname = ?, aname = ?, cdate = ?, dtype = ? WHERE bid = ?"

EDITBOOKSTATE = "UPDATE Books SET state = ? WHERE bid = ?"

DELETEBOOK = "DELETE FROM Books WHERE bid = ?"
# endregion

# region User
CHECKUSERSTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users'"""

SELECTUSERS = "SELECT * FROM Users"

CREATEUSERTABLE = """CREATE TABLE Users(uid INTEGER PRIMARY KEY AUTOINCREMENT, uname TEXT, usurname TEXT, 
phone INT, mail TEXT, cdate INT);"""

INSERTUSER = "INSERT INTO Users (uname, usurname, phone, mail, cdate) VALUES(:uname, :usurname, :phone, :mail, :cdate)"

SEARCHUSERS = "SELECT * FROM Users WHERE uname LIKE '%'||?||'%' " \
             "OR usurname LIKE '%'||?||'%' OR phone LIKE '%'||?||'%' OR mail LIKE '%'||?||'%'"

SEARCHUSER = "SELECT * FROM Users WHERE uid = ?"

CHECKUSER = "SELECT count(*) FROM Users WHERE uname = ? AND usurname = ?"

EDITUSER = "UPDATE Users SET uname = ?, usurname = ?, phone = ?, mail = ? WHERE uid = ?"

DELETEUSER = "DELETE FROM Users WHERE uid = ?"
# endregion

# region Order
CHECKORDERTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Orders'"""

SELECTORDERS = "SELECT * FROM Orders"

CREATEORDERTABLE = """CREATE TABLE Orders(oid INTEGER PRIMARY KEY AUTOINCREMENT, uid INT, bid INT, 
cdate INT, edate INT);"""

INSERTORDER = "INSERT INTO Orders (uid, bid, cdate, edate) VALUES(:uid, :bid, :cdate, :edate)"

SEARCHORDER = "SELECT o.oid, u.uname, u.usurname, b.bname, b.aname, o.cdate, o.edate FROM Orders o INNER JOIN Users u USING(uid) INNER JOIN Books b USING(bid)"

DELETEORDER = "DELETE FROM Orders WHERE bid = ?"

GETORDERUSERIDBYBOOKID = "SELECT uid FROM Orders WHERE bid = ?"
# endregion
