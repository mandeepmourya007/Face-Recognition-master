import sqlite3

conn = sqlite3.connect('attendance.db')


conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1542260,'Nikita Digra')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1542317,'Pankaj Bawa')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1542520,'Rabia Mahajan')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1543072,'Rasbihari Sharma')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1543091,'Rohan Khanna')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1543131,'Shivani Sharma')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1543136,'Simran Kanda')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1543141,'Aman Kumar')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1543157,'Tanu')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1543821,'Deepak Singh')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1544054,'Jyoti Sharma')");

conn.execute("INSERT INTO dat (Roll,NAME) \
                  VALUES (1544778,'Ramandeep Kaur')");


conn.commit()
print "Records created successfully";
conn.close()
