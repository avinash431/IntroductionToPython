import sqlite3

with sqlite3.connect('example.db') as con:
    cursor = con.cursor()
    cursor.execute("select * from person where name = '%s'" % "kiran")
    print(cursor.fetchall())
