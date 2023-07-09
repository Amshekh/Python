# Dictionary in Python is unordered, but it is changeable and indexed.It is created with curly brackets
# Dictionary have key and value pair

mobile = {
          "Product": "IPhone",
          "Company": "Apple",
          "Model": "IPhone 14 Pro Max",
          "Year": "2022"
}
print(mobile,"\n")

# Now we wil access value using key
o = mobile["Product"] # Syntax : dictionary name and then in square brackets the key you want to access and assign it to a new variable
print(o,"\n")

# To change a given value from key value pair
mobile["Model"] = "Iphone 14 Pro" # Syntax :  Dictionary name then in square bracket the key you want to change, followed by assingnment operator andd then new value
print(mobile,"\n")

# To find length of dictionary
print(len(mobile))  # length will be 4 because we have four key and value pair
print("\n")

# To add new key value pair to dictionary
mobile["Color"] = "Space Black"
print(mobile,"\n")

# To remove a key value pair from dictionary
mobile.pop("Year")  # alternatively you can also use      del mobile[Year]
print(mobile,"\n")

# To delete entire dictionary
# del(mobile)
# print(mobile,"\n")  # error will be shown as now dictionary is deleted

# To clear dictionary
# mobile.clear()  # Syntax : dictionary name followed by dot and then clear()  method
# print(mobile) # {} will be output as dictionary data is cleared now

# To copy a dictionary
phone = mobile.copy() # Syntax : new dictionary then assignment to old dictionary name followed by dot and then copy() 
print(phone,"\n")


