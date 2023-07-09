# To use where clause in database   python_db
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321", database = "python_db")
                    
my_cursor = conn.cursor()

my_cursor.execute("select * from empInfo where Emp_Post = 'Python Programmer'")

viewResult = my_cursor.fetchall()  # Here fetchall() function based on where condition of Emp_Post = Python Programmer will get stored in variable  viewResult.

for row in viewResult:
    print(row)