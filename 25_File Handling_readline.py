# To read and print text content linewise
"""

f = open("File Test 2.txt", "r")
print(f.readline())
# print(f.readline())   # if you again give readline, it will print 2nd line and so on
f.close()

"""

# to print the whole content data of file using for loop
"""
f = open("File Test 2.txt", "r")
for x in f:   
    print(x)

"""

# Now we will create a file and write data into it using python code


f = open("Demo_file_01.txt","x")  # Here we use "x" mode to create a new file Demo_file_01.txt
# Remember if you run code again, it will show error as file can be created only once, however if you delete this file from folder and run again you eill not get error

f = open("Demo_file_01.txt","w") # After creating file we are going to write into file using "w" mode. However if there was no such file, "w" mode can create and write file simultaneously
f.write("Hey! We created new file using Python code, and now we are writing this content in it.")
print("File has been created and content is also written.You may check in folder where you have written program")
f.close()



# We use append mode to write additional data in existing file

"""
f = open("Demo_file_01.txt","a")
f.write("This is additional data we are adding to file using append mode")
f.close()

"""
