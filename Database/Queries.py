
PATH = "LMS.db"

# region Books
CHECKBOOKSTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Books'"""

SELECTBOOKS = "SELECT * FROM Books"

CREATEBOOKSTABLE = """CREATE TABLE Books(bid INTEGER PRIMARY KEY AUTOINCREMENT, bname TEXT, aname TEXT, 
cdate INT, dtype TEXT, state BOOL);"""

INSERTBOOKS = "INSERT INTO Books (bname, aname, cdate, dtype, state) VALUES(:bname, :aname, :cdate, :dtype, :state)"
# endregion

# region User
CHECKUSERSTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users'"""

SELECTUSERS = "SELECT * FROM Users"

CREATEUSERTABLE = """CREATE TABLE Users(uid INTEGER PRIMARY KEY AUTOINCREMENT, uname TEXT, usurname TEXT, 
phone INT, mail TEXT, cdate INT);"""

INSERTUSER = "INSERT INTO Users (uname, usurname, phone, mail, cdate) VALUES(:uname, :usurname, :phone, :mail, :cdate)"

SEARCHUSER = "SELECT * FROM Users WHERE uname LIKE '%'||?||'%' " \
             "OR usurname LIKE '%'||?||'%' OR phone LIKE '%'||?||'%' OR mail LIKE '%'||?||'%'"

CHECKUSER = "SELECT count(*) FROM Users WHERE uname = ? AND usurname = ?"

EDITUSER = "UPDATE Users SET uname = ?, usurname = ?, phone = ?, mail = ? WHERE uid = ?"

DELETEUSER = "DELETE FROM Users WHERE uid = ?"
# endregion

# region Order
CHECKORDERTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Orders'"""

SELECTORDERS = "SELECT * FROM Orders"

CREATEORDERTABLE = """CREATE TABLE Orders(oid INTEGER PRIMARY KEY AUTOINCREMENT, UID INT, BID INT, 
cdate INT, edate INT);"""

INSERTORDER = "INSERT INTO Orders (UID, BID, cdate, edate) VALUES(:UID, :BID, :cdate, :edate)"
# endregion
