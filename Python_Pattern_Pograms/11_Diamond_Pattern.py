r = int(input("Enter number of rows : "))

for m in range(r):
    for n in range(r - m - 1):
        print(" ", end=" ")
    for n in range(2 * m + 1):
        print("*", end=" ")
    print()    

for m in range(r - 1):
    for n in range(m + 1):
        print(" ", end=" ")
    for n in range(2 * (r - m - 1) - 1):
        print("*", end=" ")
    print()
