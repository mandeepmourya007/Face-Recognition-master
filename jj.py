import sqlite3

conn = sqlite3.connect('aTT.db')


conn.execute('''CREATE TABLE date
         (Roll INT      NOT NULL,
         NAME           TEXT    NOT NULL,
         D1 INT,
         D2 INT,
         D3 INT,
         D4 INT)
         ;''');
                  
