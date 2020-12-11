
PATH = "LMS.db"

# region Books
CHECKBOOKSTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Books'"""

SELECTBOOKS = "SELECT * FROM Books"

CREATEBOOKSTABLE = """CREATE TABLE Books(grid INTEGER PRIMARY KEY AUTOINCREMENT, bname TEXT, aname TEXT, 
cdate INT, dtype TEXT, state BOOL);"""

INSERTBOOKS = "INSERT INTO Books (bname, aname, cdate, dtype, state) VALUES(:bname, :aname, :cdate, :dtype, :state)"
# endregion

# region User
CHECKUSERSTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users'"""

SELECTUSERS = "SELECT * FROM Users"

CREATEUSERTABLE = """CREATE TABLE Users(grid INTEGER PRIMARY KEY AUTOINCREMENT, uname TEXT, usurname TEXT, 
cdate INT);"""

INSERTUSER = "INSERT INTO Users (uname, usurname, cdate) VALUES(:uname, :usurname, :cdate)"
# endregion

# region Order
CHECKORDERTABLE = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Orders'"""

SELECTORDERS = "SELECT * FROM Orders"

CREATEORDERTABLE = """CREATE TABLE Orders(grid INTEGER PRIMARY KEY AUTOINCREMENT, UID INT, BID INT, 
cdate INT, edate INT);"""

INSERTORDER = "INSERT INTO Orders (UID, BID, cdate, edate) VALUES(:UID, :BID, :cdate, :edate)"
# endregion
