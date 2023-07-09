r = int(input("Enter number of rows : "))

for m in range(1, r+1):
    print(" " * (r-m) + "*" * m)