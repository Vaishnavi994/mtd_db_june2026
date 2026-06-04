import pymysql
import db_connect2 as db2

def insert_row():
      query="""insert into employees(name,designation,salary,phone_number) values('vaishnavi','software engineer',1000000.00,9876543210)"""
      try:
          connection=db2.db_connect()
          cursor=connection.cursor()
          result=cursor.execute(query)
          connection.commit()
          cursor.close()
          db2.db_disconnect(connection)
          if result==1:
              print("Row inserted")
          else:   
              print("Row insertion failed")
      except Exception as e:
          print("Error in inserting row")

insert_row()