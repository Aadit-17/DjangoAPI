import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='21bds0203'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE dcrmdb")
print("Success")
