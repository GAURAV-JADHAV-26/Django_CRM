import mysql.connector

dataBase = mysql.connector.connect(

    host='localhost',
    user = 'root',
    passwd = 'SqL_root@123',
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE JRM_DB')
print("DB Created !")

# admin : Admin