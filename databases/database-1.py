import sqlite3
con = sqlite3.connect('example.db')

cursor = con.cursor()

cursor.execute("""
CREATE TABLE person (name TEXT, age INT, email_id TEXT)
""")

con.commit()
con.close()
