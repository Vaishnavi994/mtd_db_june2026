import pymysql
import db_connect2 as dbc
def create_db():
      database_name=input("Enter the database name to create:")
      query=f"create database if not exists {database_name}"
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

def read_employee():
    name=input("Enter employee name:")
    designation=input("Enter employee designation:")
    salary=float(input("Enter employee salary:"))
    phone_number=int(input("Enter employee phone number:"))
    return (name,designation,salary,phone_number)

def insert_row():
      query="""insert into employees(name,designation,salary,phone_number) values(%s,%s,%s,%s)"""
      try:
          connection=dbc.db_connect()
          cursor=connection.cursor()
          employee=read_employee()
          result=cursor.execute(query,employee)
          connection.commit()
          cursor.close()
          dbc.db_disconnect(connection)
          if result==1:
              print("Row inserted")
          else:   
              print("Row insertion failed")
      except Exception as e:
          print("Error in inserting row")

def update_employee():
    id=int(input("Enter employee id whose salary to be updated:"))
    salary=float(input("Enter new salary:"))
    query='update employees set salary=%s where id=%s'
    try:
          connection=dbc.db_connect()
          cursor=connection.cursor()
          result=cursor.execute(query,(salary,id))
          connection.commit()
          cursor.close()
          dbc.db_disconnect(connection)
          if result==1:
              print("Row updated successfully")
          else:   
              print("Row update failed")
    except Exception as e:
          print("Error in updating row")

def delete_employee():
    id=int(input("Enter employee id to be deleted:"))
    query='delete from employees where id=%s'
    try:
          connection=dbc.db_connect()
          cursor=connection.cursor()
          result=cursor.execute(query,id)
          connection.commit()
          cursor.close()
          dbc.db_disconnect(connection)
          if result==1:
              print("Employee record deleted successfully")
          else:   
              print("Employee record deletion failed")
    except Exception as e:
          print("Error in deleting row")

def search_employee():
    id=int(input("Enter employee id to be searched:"))
    query='select * from employees where id=%s'
    try:
          connection=dbc.db_connect()
          cursor=connection.cursor()
          result=cursor.execute(query,id)
          row=cursor.fetchone()
          if row:
               print(row)
          else:
                print("Employee record not found")

          cursor.close()
          dbc.db_disconnect(connection)
    except Exception as e:
          print("Error in searching row")
def list_employees():
    query='select * from employees'
    try:
         connection=dbc.db_connect()
         cursor=connection.cursor()
         result=cursor.execute(query)
         rows=cursor.fetchall()
         if rows:
              print('-'*90)
              print('| %-5s | %-20s | %-20s | %-15s | %-15s |'%('ID','NAME','DESIGNATION','SALARY','PHONE NUMBER'))
              print('-'*90)
         for row in rows:
                print('| %-5s | %-20s | %-20s | %-15s | %-15s |'%row)
         print('-'*90)
         cursor.close()
         dbc.db_disconnect(connection)
    except Exception as e:
         print("Error in listing employees")

def drop_employees():
    query='drop table employees'
    try:
         connection=dbc.db_connect()
         cursor=connection.cursor()
         result=cursor.execute(query)
         connection.commit()
         cursor.close()
         dbc.db_disconnect(connection)
         if result==1:
              print("Employees table dropped successfully")
         else:   
              print("Failed to drop employees table")
    except Exception as e:
         print("Error in dropping employees table")

def exit_app():
        print("DB Connection closed")
        print("Exiting application")
        exit(0)
        
def menu(choice):
     match choice:
          case 1:
               insert_row()
          case 2:
               update_employee()
          case 3:
               delete_employee()
          case 4:
               search_employee()
          case 5:
               list_employees()
          case 6:
               drop_employees()
          case 7:
               exit_app()
          case _:
               print("Invalid choice")
        
def run_employee_app():
        while True:
            print("1. Insert employee record")
            print("2. Update employee salary")
            print("3. Delete employee record")
            print("4. Search employee record")
            print("5. List all employees")
            print("6. Drop employees table")
            print("7. Exit")
            choice=int(input("Enter your choice:"))
            menu(choice)

create_db()
create_table()
run_employee_app()



 # query='create table if not exists employee(id int primary key auto_increment,name varchar(200) not null,age int , department varchar(200),designation varchar(200),salary float,commision float default 0.0, years_of_experience tinyint,phone_number bigint unique)'zz