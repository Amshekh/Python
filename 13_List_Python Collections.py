# Python Collections are of 4 types (i) list  (ii) tuple  (iii) set  (iv) dictionaries
# Here we will look for List

computer_hardware = ["Monitor", "Motherboard", "HDD", "Cabinet", "RAM", "CPU", "Keyboard"]
print(computer_hardware,"\n")

# list in python is changeable i.e. we can replace one element with some other
computer_hardware[2] = "SSD"  # now at index 2 HDD will now be replaced by SSD
print(computer_hardware,"\n")

# list in python allows addition of new elements as well as duplicate elements too
computer_hardware.append("Graphics Card") # adds new element
print(computer_hardware,"\n")

computer_hardware.append("RAM") # adding duplicate value which already exists in list
print(computer_hardware,"\n")

# removing an element from list
computer_hardware.remove("RAM")
print(computer_hardware,"\n")

# to print a particular element in list with given index
print(computer_hardware[5], "\n")  # index starts from 0 in python

# to delete the list
del(computer_hardware)
# print(computer_hardware)  print will not execute as list is now deleted

# to clear the list, i.e. clear the elements in the list, but list will exist
computer_hardware = ["Monitor", "Motherboard", "SSD", "Cabinet", "RAM", "CPU", "Keyboard"]
computer_hardware.clear()
print(computer_hardware)  # An empty list will be printed, as all elements are cleared
