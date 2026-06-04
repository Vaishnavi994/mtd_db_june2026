import pymysql

def db_connect():
      connection=None
      try:
          connection=pymysql.connect(user='root',password='root',port=3306,database='vaishu',charset='utf8',host='localhost')
          print("DB Connected")
      except Exception as e:
          print("DB Connection failed")
      return connection

def db_disconnect(connection):
     try:
          connection.close()
          print("DB Disconnected")
     except Exception as e:
          print("DB disconnection failed")

connection=db_connect()
db_disconnect(connection)