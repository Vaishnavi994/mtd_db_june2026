import pymysql
connection=pymysql.connect(user='root',password='root',port=3306,database='vaishu',charset='utf8',host='localhost')
print("DB Connected")
connection.close()
print("DB Disconnected")