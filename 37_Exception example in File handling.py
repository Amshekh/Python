# Exception in File Handling
"""
try:
   fh = open("File_Exception_Test.txt", "w")
   fh.write("Hey! We are now filling some dummy content")
except IOError:
    print("Can't write data in file")
else:
    print("Content data has been added successfully")

"""

try:
   fh = open("File_Exception_Test.txt", "r")  # IOError because of read only mode
   fh.write("Hey! We are now filling some dummy content")  # You can't write something into file which is in read only mode
except IOError:
    print("Can't write data in file")
else:
    print("Content data has been added successfully")