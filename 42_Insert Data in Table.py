# To insert data in table  empInfo
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "Amit_Shekhar", passwd = "$_shekh321", database = "python_db")
                    

my_cursor = conn.cursor()

# Inserting values in table empInfo using  method 1
# my_cursor.execute("insert into empInfo(Emp_ID, Emp_Name, Emp_Post, Emp_CTC) values (99988007, 'Amit Shekhar', 'Data Engineer/Data Scientist', 185000)")

# However we can also insert values in table using Tuple in Python |  Method 2

insertData = "insert into empInfo(Emp_ID, Emp_Name, Emp_Post, Emp_CTC) values (%s, %s, %s, %s)"  # here inserData is a variable. | Understand the syntax

# Now we will create a tuple named records to insert some dummy data in the table
records = [
    (99988007, 'Amit Shekhar', 'Data Engineer/Data Scientist', 185000),
    (11100555, 'Kim Zhao', 'Data Analyst', 185000),
    (15784398, 'Tulika Kumari', 'DevOps Engineer', 185000),
    (82697417, 'Andrea Sharapova', 'Graphic Designer', 185000),
    (81379452, 'Siddhi Arora', 'Graphic Designer', 185000),
    (94782569, 'Emma Bezos', 'Web Developer', 185000),
    (32985476, 'Michelle Stone', 'PL/SQL Developer', 185000),
    (65278413, 'Zandaya Olsen', 'Front-End Developer', 185000),
    (73215824, 'Chandrika Singh', 'Software Tester', 185000),
    (98125475, 'Amber Watson', 'Java Programmer', 185000),
    (37591549, 'Emily White', 'Python Programmer', 185000),
    (29475369, 'Niharica Srivastava', 'DevOps Engineer', 185000),
    (83547121, 'Elizabeth Upton', 'Software Engineer', 185000),
    (37981456, 'Beyonce Brown', 'Game Developer', 185000),
    (37914565, 'Lipika Gupta', 'Front-End Developer', 185000),
    (85247194, 'Greta Kerber', 'Python Programmer', 185000),
    (96335885, 'Meike Niemeier', 'Java Programmer', 185000),
    (49873254, 'Kumkum Mishra', 'Software Engineer', 185000),
    (88224561, 'Clara Hesse', 'Game Developer', 185000),
    (80003792, 'Amandine Parry', 'Web Developer', 185000),
    (54336778, 'Samridhi Sharma', 'Software Tester', 185000),
    (11154457, 'Iga Bielawaska', 'Graphic Designer', 185000),
    (86622159, 'Karolina Kreglicka', 'Python Programmer', 185000),
    (35578419, 'Swarnika Kapoor', 'Data Analyst', 185000),
    (77993256, 'Lisa Lalaguna', 'Web Developer', 185000),
    (56258525, 'Jennifer Skliva', 'Game Developer', 185000),

]
my_cursor.executemany(insertData, records) # as there are multiple entries, so we will give executeMany

conn.commit() # commit function will save the last query that we executed