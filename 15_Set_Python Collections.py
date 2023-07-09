# Set in Python is unordered, unindexed and we cannot add duplicate items to a set.We use curly brackets for set

computer_hardware = {"Monitor", "Motherboard", "HDD", "Cabinet", "RAM", "CPU", "Keyboard"}
print(computer_hardware,"\n") # It's not necessary that in set the output comes in same order, as set is unordered

# We can add new item in set
computer_hardware.add("SSD")
print(computer_hardware,"\n")

# we can add multiple items at once in a set
computer_hardware.update(["Graphics Card","Printer","Speaker","Webcam","Pendrive"]) # notice syntax to add
print(computer_hardware,"\n")



