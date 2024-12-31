import  mysql.connector
from mysql.connector import connect

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='@Bob09099427146',
    database='ulearning'
)

mycursor = mydb.cursor()

# mycursor.execute('show databases')
mycursor.execute('select * from lessons')

for i in mycursor:
    print(i)