import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE mydatabase")

print('All done')