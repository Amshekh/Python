# While loop in Python
"""
i = 1
print("Even numbers upto 50 are as follows :")
while i <= 50:
    if i%2 == 0:
     print(i) 
    i += 1
"""

# break in while loop  (simple explanation)
"""
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break   # As there is break statement, output will be 1,2,3,4,5  only
    i += 1

"""

# continue statement in while loop (simple explanation)

"""
i = 1
while i <= 10:
    i += 1     # Here i value will be increment from 1 to 2, so printing starts from 2
    if i == 5:
        continue  # continue will jump the loop by 1 iteration, i.e  when i will be 5 it will jump to 6 in this case.
    print(i)  #  as there is continue statement at i = 5, output will be from 2 to 4 and then 6 to 11

"""

# For loop in Python
"""
computer_hardware = ["Monitor", "Motherboard", "HDD", "Cabinet", "RAM", "CPU", "Keyboard"]
for x in computer_hardware:  # Syntax: for  then variable name   in   list
    print(x)

"""

# range() function in for loop in Python  (range function returns a sequence of numbers starting from zero and increments by 1
"""
for x in range(10):
    print(x)  # output will be 0,1,2,3.....9  as range starts from 0 till 10th number i.e. 9  in this case

"""

# range() function usage between two values in for loop
"""
for x in range(1,10):
    print(x)  # output will be 1,2,3,4......9   (excluding 10)

"""
# to print a multiplication table of any entered number using range function in for loop
num = int(input("Enter the number fo multiplication table: "))
for i in range(1,11):
    res = num * i
    print(num,"*",i,"=",res)
