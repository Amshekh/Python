r = int(input("Enter number of rows : "))

for m in range(r):
    for n in range(m + 1):
        print("*", end=" ")
    print()    