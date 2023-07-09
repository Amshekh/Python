# File handling helps in storing data from  temporary memory(RAM) to permanent memory such as hard disk
# There are 2 types of file in Python (i) Text files e.g. (.txt)   and  (ii) binary files (.jpg, .dat)
# Different modes in Python are (i) r  [read only]  (ii) w  [write mode]  (iii)  a  [append mode]   (iv)  x  [create mode] 

# Opening a file using open function
"""
f = open("File Test.txt","r")
myfile = f.read()
print(myfile)
f.close()

"""
# Reading only specified number of characters
f = open("File Test.txt", "r")
myfile = f.read(15)
print(myfile)  # Now only 15 characters from text content of File Test will be read and printed
f.close()
