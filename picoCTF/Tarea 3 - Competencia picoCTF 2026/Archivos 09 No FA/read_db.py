import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

for row in cursor.execute("SELECT username, password, two_fa FROM users;"):
    print(row)

conn.close()