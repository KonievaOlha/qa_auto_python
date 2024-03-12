import sqlite3

connection = sqlite3.connect("C:\Works\Study_qa_auto\qa_auto_python\lesson_30_SQL\qqqqq.db")

cur = connection.cursor()
cur.execute("SELECT * FROM MyTable")

rows = cur.fetchall()

for row in rows:
    print(row)
