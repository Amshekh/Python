# To use drop table to delete table
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321", database = "python_db")
                    
my_cursor = conn.cursor()

my_cursor.execute("drop table empInfo")  # To delete a table named empInfo

