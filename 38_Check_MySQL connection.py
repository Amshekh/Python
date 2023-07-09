# To establish MySQL connection

import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321")
                    # connect function requires three parameters and if we have passed all three correctly,then connection will be established correctly.
                    # Now this connect function will return an object which we have assigned to a variable named  conn
print(conn)

if(conn):
    print("\n Bingo! MySQL connected successfully!")
else:
    print("MySQL connection unsuccessful!")