import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gowtham1209$',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!!")