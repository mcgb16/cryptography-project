import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='pswdhere',
    database='bdcryptography'
)

cursor = conn.cursor()


cursor.close()
conn.close()
