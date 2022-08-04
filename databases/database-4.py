import sqlite3
con = sqlite3.connect('example.db')

cursor = con.cursor()

cursor.execute("select * from person")

one_row = cursor.fetchone()
many_row = cursor.fetchmany(2)
all_row = cursor.fetchall()

print(one_row)
print(many_row)
print(all_row)

con.close()
