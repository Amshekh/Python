# To find the length of a string
x = input("Enter any String: ")
l = len(x)  # len method is used to find length of a string in python
print("The length of entered string is: ",l)


#  .lower()  method is used to convert string in lower case and   .upper()  for  converting to upper case
y = x.lower()
print("Desired output in lower case is: ",y)
z = x.upper()
print("Desired output in upper case is: ",z)

#  to print the first and last letter of your entered string

print("The first letter of your entered string is: ",x[0])  # As indexing in Python starts from zero, this will print the first letter of your entered string

print("The last letter of your entered string is: ",x[-1]) # [-1] will yield last letter of your entered string
