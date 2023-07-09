# conditional statements in Python:  if  elif  else
tuple = ("111", "222", "333", "444", "555", "666", "777", "888", "999")
index = 0
item = 0

index = int(input('Enter index (0-8): '))  # Taking input from user

if index < 0:
    print('Bad index!')
elif index > 8:
    print('Bad Index!')
else:
    item = tuple[index]
    print(item,'found at index',index)
