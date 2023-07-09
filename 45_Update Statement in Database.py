# To update data in particular row  using  Update  statement.
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321", database = "python_db")
                    
my_cursor = conn.cursor()

my_cursor.execute("update empInfo set Emp_Name = 'Amber Watson' where Emp_ID = 98125475 ") # Updating name in row with Emp_ID

"""
# To delete a particular row in database (an employee leaves the company to join some other company)

my_cursor.execute("delete from empInfo where Emp_ID = 98125475 ")
print("Record Deleted!")

"""

conn.commit()  # To check whether row has been updated, run 43rd  program of Show Data in table.