import sqlite3 as lite
import sys

db = lite.connect('./db/todo.db')
print('Creating database and tables...')
with db:
    cur = db.cursor()
    cur.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, datetime TEXT)")

db.close()
print('Database and tables created successfully...')
