import sqlite3
con = sqlite3.connect('example.db')

cursor = con.cursor()

cursor.execute("""
INSERT INTO person values ("john", 24, "abc@gmail.com")
""")


con.commit()
con.close()