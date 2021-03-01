import os
import sys
import sqlite3

DATABASE = "comments.db"
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE)

if os.path.exists(DATABASE_PATH):
    print("File already exists")
    sys.exit(0)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

sql = """CREATE TABLE comments(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      comment TEXT);"""
cursor.execute(sql)

sql = "INSERT INTO comments (name, comment) VALUES('Paul', 'Ich mag diese Seite sehr gerne!');"
cursor.execute(sql)

sql = "INSERT INTO comments (name, comment) VALUES('Kim', 'Ich mag diese Seite überhaupt nicht!');"
cursor.execute(sql)

sql = "INSERT INTO comments (name, comment) VALUES('Teddy', 'Ich kenne diese Seite.');"
cursor.execute(sql)

connection.commit()
connection.close()
