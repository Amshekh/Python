r = int(input("Enter number of rows : "))
for m in range(r):
    for n in range(r-m-1):
        print(" ", end=" ")
    for o in range(2 * m+1):
        print("*", end=" ")
    print()