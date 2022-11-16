import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE User_Details (FirstName TEXT, MiddleName TEXT, LastName TEXT, PhoneNumber INTEGER,Address VARCHAR, Email VARCHAR, Password VARCHAR)')
print("Table created successfully");
conn.close()
