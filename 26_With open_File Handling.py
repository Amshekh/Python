# Using   with open   to read, write in a file etc
# The main advantage is that you don't have to close the file everytime and it get's closed automatically.

"""
with open('File Test 2.txt','r') as f:  # Notice the Syntax
    x = f.read()
    print(x)

"""

# To rename and delete Python files using built-in Python module "os"  
import os
old_file_name = "Demo_file_01.txt"
new_file_name = "Demo_file_02.txt"

with open(old_file_name) as f:
    data = f.read()

with open(new_file_name, 'w') as f:   # here we could have also pass actual new file name 'Demo_file_02.txt'
    f.write(data)   # we have used  w   mode because we want to create and write content data into it at the same time

# We have copy/transfer/written  old file data to new file.
# Now we are going to delete that old file 'Demo_file_01.txt'

os.remove(old_file_name)  # Syntax:  module name i.e  os followed by  .  and then old file name. This will remove Demo_file_01.txt
print("New file has been created and content is also tansfered from old file. Also, old file has been removed","\n","You may check in folder where you have written program")
