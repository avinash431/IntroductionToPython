import sqlite3
con = sqlite3.connect('example.db')

cursor = con.cursor()

persons = [("kiran", 21, "kiran@gmail.com"),
           ("anu", 29, "anu@yahoo.com"),
           ("sathis", 65, "satish@rediff.com")]

cursor.executemany("INSERT INTO person values (?, ?, ?)", persons)
print(cursor.rowcount)
con.commit()
con.close()
