import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database="sys",
   
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES") #muestra las tabas de la base de datos

for x in mycursor:
    print(x)





