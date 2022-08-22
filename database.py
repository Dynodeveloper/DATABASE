import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database="base1",
   
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES") #muestra las bases de datos existentes

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #se cambia la tabla "costumers", delegandola como llave primaria

mycursor.execute("SHOW TABLES") #muestra las tabas de la base de datos

for x in mycursor:
    print(x)





