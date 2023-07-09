# Here we will check usage of multiple opeators at once
a = 7
b = 5
c = 9
d = a > b and a > c  # Here a is greater than b, so in AND  second condition is checked but a less tha c
print(d)   # In AND if one condition is false, overall output is false  [ Logical AND gate concept]

x = a > b or a > c
print(x)  # In OR  even if one condition is true, output will be true

# Membership operators in Python -->  in   out

list = [1,2,3,4,5]
if (a in list):     # Here   in  is a membership operator in Python
    print("Yes it is in the list")
else:
    print("No it is not in the list")

# Usage of second membership operator  not in  
if (a not in list):     # Here  not in  is a membership operator in Python
    print("Yes it is in the list")
else:
    print("No it is not in the list")    
