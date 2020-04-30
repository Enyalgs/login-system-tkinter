#SQLite3
import sqlite3

connection = sqlite3.connect('UsersData.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print("Database Connected")
'''
cursor.execute("""
    INSERT INTO Users VALUE
""") 
'''