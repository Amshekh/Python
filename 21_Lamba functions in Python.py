# Lambda in Python are  anonymous function   or   one line function

# lambda function to print sum of three numbers
"""
sum = lambda a,b,c : a+b+c  # Syntax :  variable name assigning to lambda followed by variables on which operation is to be performed  followed by colon then the operation
print(sum(2,3,7))  # Here sum = 2+3+7 = 12 

"""

# lambda function to print cube of a number
n = int(input("Enter the number: "))

cube = lambda n : n * n * n   # one line function
print("Cube of",n,"is",cube(n))