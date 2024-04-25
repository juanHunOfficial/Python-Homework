import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mateo2023!!"
)

print(mydb)