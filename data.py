import sqlite3

conn = sqlite3.connect('attendance.db')


conn.execute('''CREATE TABLE dat
         (Roll INT      NOT NULL,
         NAME           TEXT    NOT NULL,
                D1 INT,
                  D2 INT ,
         D3 INT ,
         D4 INT ,
         D5 INT ,
         D6 INT ,
         D7 INT ,
         D8 INT ,
         D9 INT ,
         D10 INT ,
         D11 INT ,
         D12 INT ,
         D13 INT ,
         D14 INT ,
         D15 INT ,
         D16 INT ,
         D17 INT ,
         D18 INT ,
         D19 INT ,
         D20 INT ,
         D21 INT ,
         D22 INT ,
         D23 INT ,
         D24 INT ,
         D25 INT ,
         D26 INT ,
         D27 INT ,
         D28 INT ,
         D29 INT ,
         D30 INT ,
         D31 INT )
         ;''')

