# To show all databases that exists

import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321")
                    # connect function requires three parameters and if we have passed all three correctly,then connection will be established correctly.
                    # Now this connect function will return an object which we have assigned to a variable named  conn

my_cursor = conn.cursor()  # the conn  variable has connection object, and object has the property to call the function
 # the object in conn variable will now call a function named cursor.When function  cursor  will run, it will return an cursor object which we will store in  my_cursor

# my_cursor.execute("")   #  object in my_cursor can call   execute   function  and in double inverted comma  we  can pass any  SQL Query

# my_cursor.execute("create database python_db") # we have passed SQL Command  to create a database named Python_DB

# Now we will run SQL Command to show all databases
my_cursor.execute("show databases")
for db in my_cursor:
    print(db)