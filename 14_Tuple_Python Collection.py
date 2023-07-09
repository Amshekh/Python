# Tuple in Python is unchangeable and allow duplicate values, and are written using round brackets
computer_hardware = ("Monitor", "Motherboard", "SSD", "Cabinet", "RAM", "CPU", "Keyboard")
print(computer_hardware,"\n")

# to find the length of tuple
print(len(computer_hardware))
print("\n")

# to join two tuples
computer_hardware = ("Monitor", "Motherboard", "SSD", "Cabinet", "RAM", "CPU", "Keyboard")
computer_software = ("Operating System", "Pycharm IDE", "Web Browser", "Adobe", "Media player")
computer = computer_hardware + computer_software
print(computer, "\n")

# to count how many number of times an element appears in tuple
fitem = ("Burger", "Pizza", "Pasta", "Coffee", "Hamburger", "Pizza", "Tacos")
c = fitem.count("Pizza") #  it will count how many times Pizza comes in tuple food item
print(c,"\n")

# to use index() method to find index of an element in tuple
i = fitem.index("Coffee")  # index starts from 0 in Python
print(i)