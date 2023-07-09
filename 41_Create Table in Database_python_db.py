# To create table in Database    python_db

import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321", database = "python_db")
                    # connect function requires three parameters and if we have passed all three correctly,then connection will be established correctly.
                    # Now this connect function will return an object which we have assigned to a variable named  conn

my_cursor = conn.cursor()

my_cursor.execute("create table empInfo(Emp_ID int, Emp_Name varchar(100), Emp_Post varchar(50), Emp_CTC dec(15, 2))")