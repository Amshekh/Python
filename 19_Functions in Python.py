# There are 2 types of functions in Python  (i) Built in functions (ii) User defined functions
# Examples of built in function :  sum((x,y))  max((x,y))

# User defined function in Python involves 2 steps (i) defining function  and (ii)  calling that function
num = int(input("Enter any number:"))

def cube_function():   # Defining the function using def keyword followed by function name
    c = num * num * num
    print("The cube of",num,"is",c)

cube_function()  # Calling already defined function is importatnt