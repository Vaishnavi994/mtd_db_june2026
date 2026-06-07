import pymysql
import db_connect2 as dbc
def drop_table():
      table_name=input("Enter the table name to drop:")
      query = f'drop table if exists {table_name}'

      try:
          connection=dbc.db_connect()
          cursor=connection.cursor()
          result=cursor.execute(query)
          connection.commit()
          cursor.close()
          #connection.close()
          dbc.db_disconnect(connection)
          if result==0:
              print("Table dropped")
          else:   
              print("Table does not exist")
      except Exception as e:
          print("Error in dropping Table")
drop_table()