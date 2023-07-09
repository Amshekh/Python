r = int(input("Enter number of rows : "))

for m in range(r):
    for n in range(m):
        print(" ", end=" ")
    for o in range(m, r):
        print("*", end=" ")
    print()