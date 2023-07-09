# Exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions

# In short, Exception is an abnormal condition  # we put the code intry block  and if an exception occurs,  it reaches to except block where we handle the error

try:
    x = int(input("Enter the dividend :"))
    y = int(input("Enter the divisor :"))

    z = x / y
    print("The result is: ", z)
except ValueError: 
    print("Error! enter number only")  # if user enters alphabetical value instead of numerical value
# except ZeroDivisionError:  # This  also works fine, instead of ArithmeticError used below
except ArithmeticError:
    print("Error! Divisor can't be Zero")  # if user enters the dividend value as zero [Denominator in divison can't be zero, as something divided by zer is infinite]
else:
    print("Goodbye!")


