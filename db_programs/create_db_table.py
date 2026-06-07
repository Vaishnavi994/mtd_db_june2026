import pymysql

import db_connect2 as dbc
def create_db():
      query='create database if not exists vaishu_db'
      try:
          connection=dbc.db_connect()
          cursor=connection.cursor()
          result=cursor.execute(query)
          connection.commit()
          cursor.close()
          #connection.close()
          dbc.db_disconnect(connection)
          if result==1:
              print("DB created")
          else:   
              print("DB already exists")
      except Exception as e:
          print("Error in creating DB")


def create_table():
      query = 'create table if not exists employees(id int primary key auto_increment, name varchar(255) not null, designation varchar(255), salary float, phone_number bigint unique)'

      try:
          connection=dbc.db_connect()
          cursor=connection.cursor()
          result=cursor.execute(query)
          connection.commit()
          cursor.close()
          #connection.close()
          dbc.db_disconnect(connection)
          if result==1:
              print("Table created")
          else:   
              print("Table already exists")
      except Exception as e:
          print("Error in creating Table")

create_db()
create_table()
          












 # query='create table if not exists employee(id int primary key auto_increment,name varchar(200) not null,age int , department varchar(200),designation varchar(200),salary float,commision float default 0.0, years_of_experience tinyint,phone_number bigint unique)'