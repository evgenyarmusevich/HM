import sqlite3

conn = sqlite3.connect('DB_pbook.db')
cur = conn.cursor()
result = cur.fetchall()
print(result)