# Identity Operators in Python
x = 2.1
if(type(x) is int):  # type can be used to check data type, in this case we are checking for int type
    print("Yes it's a integer")
else:
    print("No it's not a integer")

# Using   is not  identity operator

if(type(x) is not int):  # here    is not    will check if x is not a integer 
    print("Yes it's not a integer")
else:
    print("No it's a integer")    
