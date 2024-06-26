import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'wildan',
    passwd = 'wildan123',
)

cursor_object = db.cursor()

cursor_object.execute('CREATE DATABASE chatwebdb')

print('Create database successfully!')