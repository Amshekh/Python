# To show all the data in table  empInfo
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321", database = "python_db")
                    
my_cursor = conn.cursor()

my_cursor.execute("select * from empInfo")

viewResult = my_cursor.fetchall()  # Here we have made a variable named viewResult which will store all values fetched by   fetchall() function in my_cursor

for row in viewResult:
    print(row)